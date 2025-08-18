#!/bin/bash

ls -1  Cosmosdb/entityMapping > conf_files.txt
insertdate=`date "+%Y-%m-%d-%H-%M.%S"`

# Insert Values at runtime for id and it's uuid
for i in $( cat conf_files.txt); do
partitionKeyName=`grep -oP '(?<="entity": ")[^"]*' Cosmosdb/entityMapping/$i`
uuid=`echo -n  "${partitionKeyName}" | md5sum |awk '{print $1}'`
#uuid=${uui% *}
sed -i '/"entity":/i "id":"'"$uuid"'",' Cosmosdb/entityMapping/$i
done



# Assign the values to the as per the received parameters/branch/environment
if [[ "$1" == "rgrp-msfnex20-10-CentralNode-GLB-dev" ]]; then
    resourceGroup="$1"
    comsosDbInstanceName="$2"
elif [[ "$1" == "rgrp-msfnex20-10-CentralNode-GLB-QA" ]]; then
    resourceGroup="$1"
    comsosDbInstanceName="$2"
elif [[ "$1" == "rgrp-msfnex20-10-CentralNode-GLB-prd" ]]; then
    resourceGroup="$1"
    comsosDbInstanceName="$2"
else
    echo "Improper resourcegroup provided"
    exit 0;
fi
dbName="metadata"
containerName1="entityMapping"
containerName2="environment"
isUpsert=true

# Construct Urls
baseUrl="https://$2.documents.azure.com/"
verb="post"
resourceType="docs"
resourceLink1="dbs/$dbName/colls/$containerName1/docs"
resourceId1="dbs/$dbName/colls/$containerName1"

resourceLink2="dbs/$dbName/colls/$containerName2/docs"
resourceId2="dbs/$dbName/colls/$containerName2"

# Get the Master key from CosmosDB
masterKey=$(az cosmosdb keys list --name $comsosDbInstanceName --resource-group "$resourceGroup"  --subscription "MSFAZX20 Data Lake DEV" --type keys --query primaryMasterKey --output tsv)
now=$(env LANG=en_US TZ=GMT date '+%a, %d %b %Y %T %Z')

echo $masterKey

signature1="$(printf "%s" "$verb\n$resourceType\n$resourceId1\n$now" | tr '[A-Z]' '[a-z]')\n\n"
signature2="$(printf "%s" "$verb\n$resourceType\n$resourceId2\n$now" | tr '[A-Z]' '[a-z]')\n\n"

hexKey=$(printf "$masterKey" | base64 --decode | hexdump -v -e '/1 "%02x"')
echo "Hex key: " $hexKey
hashedSignature1=$(printf "$signature1" | openssl dgst -sha256 -mac hmac -macopt hexkey:$hexKey -binary | base64)
hashedSignature2=$(printf "$signature2" | openssl dgst -sha256 -mac hmac -macopt hexkey:$hexKey -binary | base64)


authString1="type=master&ver=1.0&sig=$hashedSignature1"
authString2="type=master&ver=1.0&sig=$hashedSignature2"

urlEncodedAuthString1=$(printf "$authString1" | sed 's/=/%3d/g' | sed 's/&/%26/g' | sed 's/+/%2b/g' | sed 's/\//%2f/g')
urlEncodedAuthString2=$(printf "$authString2" | sed 's/=/%3d/g' | sed 's/&/%26/g' | sed 's/+/%2b/g' | sed 's/\//%2f/g')

url1="$baseUrl$resourceLink1"
url2="$baseUrl$resourceLink2"

# Import the files to CosmosDB
# for i in $( cat conf_files.txt); do
# partitionKeyName=`grep -oP '(?<="domain": ")[^"]*' Cosmosdb/entityMapping/$i`
# az rest --verbose -m $verb -b "@Cosmosdb/entityMapping/$i" -u $url1 --headers x-ms-date="$now" x-ms-documentdb-partitionkey=[\"$partitionKeyName\"] x-ms-documentdb-is-upsert=$isUpsert x-ms-version=2018-12-31 x-ms-documentdb-isquery=true Content-Type=application/json Authorization=$urlEncodedAuthString1
# done
partitionKeyName=`grep -oP '(?<="entity": ")[^"]*' Cosmosdb/entityMapping/Account-Enriched-CA.json`
az rest --verbose -m $verb -b "@Cosmosdb/entityMapping/Account-Enriched-CA.json" -u $url1 --headers x-ms-date="$now" x-ms-documentdb-partitionkey=[\"$partitionKeyName\"] x-ms-documentdb-is-upsert=$isUpsert x-ms-version=2018-12-31 x-ms-documentdb-isquery=true Content-Type=application/json Authorization=$urlEncodedAuthString1