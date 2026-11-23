#_________________#
#-----part 1-------
#_________________#


# print("Hello world!")
# print("Mikail Munshi", "is a gandu")
""" 
variable naming -> 
"""
# name = "Name1"
# age = 23
# # name, age print korle majhe automatic space ashbe
# print(name,age)
# print(type(name))   # class str mane string type
# print(type(age))  # class int mane integer type


# name = input("Enter name: ")
# print(name)
# print("Wlcome, ", name) # anoter way is
# print("Welcome, " + name,"!") # this is called concatenation 



#_________________#
#-----part 2-------
#_________________#


# age = input("Enter your age : ")
# age = int(age)
# print(age)
# print(age, type(age))
# print(age+1) # this is error. different type

# new_age = int(age) # string theke int e convert hoye jabe input 23
# print(new_age+1) # age increment 24
# print(float(new_age)) # 23.0


# type castig vs type conversion
# type casting-> amra jei gula kori. jemon age = int(age)

#type conversion
# print(1+2.5) # implicit-> automatic -> type conversion
# print( 1 + int(2.999)) # explicit -> amra kori -> type casting

# a = input("enter a: ")
# b = input("enter b: ")
# sum = a+b
# print(sum)

# 2,3 input dile output 23 ashbe. fact-> string. int er jonno type casting korte hobe

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# print(a+b) # akhon output thik ashbe


# name= "Mikail Gandu"
# grade = "A+"

#string operation
# print(name.upper())
# print(name)

#find
# print(name.find("il")) # returns the index no -> 0 based indexing 
# print(name.find("Df")) # khuje na paile -1 return kore

#replace
# name = "Mikail Munshi"
# name.replace("Munshi", "Goru") # replaec kore kuthao store kora hocche na
# print(name) # tai Mikail Munshi print korbe. mane replace hobe na
# print(name.replace("Munshi", "Goru")) #Eibar thik vabe print korbe - > Mikail Goru

#check presence
# name = "Mikail Munshi"
# print('x' in name) # if exists return True else False
# print("Munshi"in name)

#reserved keywords -> in, true, while, break, for

#practice excercise 2
# p1 = float(input("Enter price 1 : "))
# p2 = float(input("Enter price 2 : "))
# p3 = float(input("Enter price 3 : "))
# print("Total bill=", p1+p2+p3)
# print("Avg bill=", (p1+p2+p3)/3)

# superhero = input("Enter Hero Name : ")
# if(superhero[0] == "s" or superhero[0] == "S"): print("Starts with s") 
# else : print("Doesn't start with s") 


#_________________#
#-----part 3-------
#_________________#

#arithmetic operator

# print(5+3)
# print(5-3)
# print(5*3)
# print(5/3)
# print(5//3) # removes the decimal part . shows only integer part
# print(5%3) # 5/3 korar pore vagshesh koto
# print(5**3) # 5 to the power 3

#assignment operator
# x= 5
# x+=5 # x = x+5
# x*=5 # x = x*5
# x/=5 # x = x/5

# i = 1 
# i+=1

#operator presedence like BODMAS om math
# ans = 2 + 5*3
# print(ans) # ans = 17

# presedance -> 
'''
1. ()
2. * , /
3. + , -

'''

# ans = (2 + 5) *3
# print(ans) # ans = 21

# comparison < , > , == , !=  returns true or false
# print(5<3) # falase

#Logical operator -> and or not
# stat1 = 4>2
# stat2 = 4<3

# print(stat1 or stat2) # True
# print(stat1 and stat2) # False
# print(not True) # not means opposite.so, it prints False
# print(not 3>5) # Prints True 

#Conditional Statment
# age = int(input("Enter age : "))

# if age>=24 :
#     print("He can vote")
#     print("He can drive")

# else :
#     print("He cannot vote")


    


