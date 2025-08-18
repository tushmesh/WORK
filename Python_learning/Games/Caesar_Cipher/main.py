

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
def caesar(pass_text, pass_shift, pass_direction):
    #direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        cipher_text = ""
        for letter in pass_text:
            if letter.isalpha():
                if not letter == " ":
                    position = alphabet.index(letter)
                    new_position = position + pass_shift
                    new_letter = alphabet[new_position]
                    cipher_text +=new_letter
                else:
                    cipher_text +=letter
            else:
                cipher_text +=letter
        print(cipher_text)
    decode = input("Do you want to decrypt the code ? Then type decode \n").lower()
    if decode == "decode":
        pass_text = input("Type your message:\n").lower()
        pass_shift = int(input("Type the shift number:\n"))
        pass_shift = pass_shift % 26
        cipher_text=""
        for letter in pass_text:
            if letter.isalpha():
                if not letter == " ":
                    position = alphabet.index(letter)
                    new_position = position -pass_shift
                    new_letter = alphabet[new_position]
                    cipher_text+=new_letter
                else:
                    cipher_text +=letter
            else:
                cipher_text +=letter
        print(cipher_text)

caesar(pass_text=text, pass_shift=shift, pass_direction=direction)
# def encrypt(text,shift):
#     #new_alphabet = alphabet[shift:]
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text +=new_letter
#     print(cipher_text)

# def decrypt():
#     input("Type decode' to decrypt:\n")
#     dtext = input("Type your message:\n").lower()
#     dshift = int(input("Type the shift number:\n"))

#     cipher_text=""
#     for letter in dtext:
#         position = alphabet.index(letter)
#         new_position = position -dshift
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(cipher_text)
# encrypt(text,shift)
# decrypt()

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.