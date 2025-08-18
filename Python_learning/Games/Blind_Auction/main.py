from replit import clear
#HINT: You can call clear() to clear the output in the console.

#from art import logo

#print(logo)
aution = True
bid_data={}

while aution == True:
	name = input("Enter the person name for a bid:  ")
	bid = int(input("Enter the bid $"))
	bid_data[name]=bid
	clear()
	another_auction = input("Any other auction Yes / No ? ").lower()
	if another_auction == "no":
		aution = False

temp  = 0
for bidder in bid_data:
	bid_amount =  bid_data[bidder]
	if bid_amount > temp :
		highest_bid = bid_amount
		winner = bidder

print(f"Highest bid is of ${highest_bid} and is of {winner}")
