
#print ime
STRING="MARKO"
print(STRING)


#print račun
x=1
y=2

x+y

print(x+y)


#if pogoj

mele_name = ("Marko")
female_name = ("Tjasa")


if mele_name == "Marko":  
  print ("Ti si car") 
else:
   print ("")  
 



#input 

male_name = input("Insert male name\n")
female_name = input("Insert female name\n")

print("Pozdravljena, " + male_name + " in " + female_name + "!")


if not male_name ==...:
    print("Čaw, " + male_name + " ti si super")
else:
    print("Podravljen neznani uporabnik")


#input naloga 1

user_mood = input("In what mood are you today?\n")

if user_mood == "happy":
   print("It is great to see you happy")
elif user_mood == "nervous":
   print("Take a deep breath 3 times")
elif user_mood == "sad":
   print("Take a deep breath 3 times") 
elif user_mood == "exited":
   print("Good for you!")    
elif user_mood == "exited":
   print("Good for you!")  
elif user_mood == "exited":
   print("Good for you!")
else: print("I don't recognize this mood")        


#guess the number - naloga 2


secret_num = 1

guess = int(input("Guess secret number\n"))

if guess == secret_num:
   print("Yes, you are correct!!!") 
else: print("No, you are wrong. Try again!")



#guess the number - naloga 2.1 loop, dokler ni vpisana pravilna numerična vrednost.
secret_num = 1
while True:
    try:
      guess = int(input("Guess secret number from 1-10.\n"))
    except ValueError:
      print("Please sign in a value.")
      continue
    if guess == secret_num:
         print("Yes, you are correct!!!") 
         break
    else:
         print("No, you are wrong. Try again!")
   


#naloga 3 - kalkulator

q1 = input("Do you want to calculate two numbers? yes/no\n").lower()

if q1 ==  "yes":
   q2 = input("Which aritmetic opreation do you want to do? addition (+),subtraction (-), multiplication (*), division (/)\n")     
   if q2 ==  "+" or q2 ==  "addition" or q2 ==  "addition (+)": 
         first_num = int(input("First number to add:\n"))
         second_num = int(input("Second number to add:\n"))
         result= first_num + second_num
         print("Result is" , result)

   elif q2 == "subtraction (-)" or q2 == "subtraction" or q2 == "-":
         first_num = int(input("First number to subtract:\n"))
         second_num = int(input("Second number to subtract:\n"))
         result= first_num - second_num
         print("Result is" , result)
         
   elif q2 == "multiplication (*)" or q2 == "multiplication" or q2 == "*":
         first_num = int(input("First number to multiply:\n"))
         second_num = int(input("Second number to multiply:\n"))
         result= first_num * second_num
         print("Result is" , result) 

   elif q2 == "division (/)"  or q2 == "/" or q2 == "division" or q2 == ":":
         first_num = int(input("First number to divide:\n"))
         second_num = int(input("Second number to devide:\n"))
         result= first_num / second_num
         print("Result is" , result)

   else:
      print("Wrong operation.") 

else: print("Bye then!")    

        
        

    



