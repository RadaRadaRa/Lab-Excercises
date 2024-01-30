
def uniqueChar(word):
    dict1={}
    for letter in word:
        if letter in dict1:
            dict1[letter]+=1
        else:
            dict1.update({letter:1})
    print(dict1)

uniqueChar("mammogram")

list_one=[1,1,3,4,9,11,22,33,45,56,98,101,200]
list_two=[1,5,7,9,15,20,33,40,41,45,75,88,99,101]
list_three=[]
for number in list_one:
    if number in list_two and number not in list_three:
        list_three.append(number)
list_three

dict.fromkeys(keys,values)

def practice(a):
    if a.isalpha():
        return(a[:5].upper())
    else:
        print("Needs to contains only alphabetical characters")
practice("yourmom")
practice("y0ur m0m")