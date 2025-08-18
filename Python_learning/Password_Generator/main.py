# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

let = random.sample(letters, nr_letters)
ran_letter = let[0]
for i in let:
  ran_letter+=i
####
num = random.sample(numbers, nr_numbers)
ran_num = num[0]
for i in num:
  ran_num +=i
####
ran_sym =""
# for i in range(1,nr_symbols):
#   sym = random.choice(symbols)
#   ran_sym +=sym
sym = random.sample(symbols,nr_symbols)
ran_sym = sym[0]
for i in sym:
 ran_sym +=i

add = ran_letter + ran_num + ran_sym
# new_random_pass = ''.join(random.sample(add,len(add)))
ad = list(add)
random.shuffle(ad)
new = ''.join(ad)
print(f"{new}")

#str_var = list("shuffle_this_string")
#random.shuffle(str_var)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P