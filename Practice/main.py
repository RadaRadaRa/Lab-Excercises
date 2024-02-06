from function import AddTwo, AddThree

print(AddTwo(1,3))
print(AddThree(1,3,5))

#user name generator
import random

def gen_username():

  try:
    name = input("Please input your first name: ")
    number = int(input("Please input a random number: "))
  except ValueError:
    print("That was not a valid number! Please insert a number")
    gen_username()
  else:
    x = random.randint(1, number)
    user = (name[:5] + (str(x))).lower()
    print(f"Your new username is {user}")
    return user
  finally:
    print("thanks for using this generator!")

gen_username()

'''I think one of the interesting things that I learned today is syntactical sugar and salt. I didn't know we could just change 
code works. I wonder when anyone would want use syntactical salt. The two more important stuff that I learn is coding etiquette and 
importing files. I agree that its easier to work with code thats less than 75 lines and glad that I can use multiple files and importing
to make coding easier.  '''