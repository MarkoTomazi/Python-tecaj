
#ctrtl+' zakomentiraš

#while zanka

secret = 22


while guess == secret:

   guess = int(input("Guess the secret number between 1 and 25: "))

   if guess == secret:
      print("Yes")
   else:
      print("noup, the secret numbe ris not " )   


# #for zanka

import time
x = range(3,6)

for n in x: 
 print(n)

 time.sleep(2)

# če označiš element + ctrl+D ti označi vse elemente i njih lahko popravljaš

secret = 22
for x in range(5):
      guess = int(input("Guess the secret number between 1 and 25: "))
      if guess == secret:
         print("Yes")
         break
      else:
        print("noup, the secret numbe ris not " )  


#rendom modul
import random     

secret  = random.randint(1,30) #zbira št med 1-30rand

while True:
   guess = int(input("Guess the secret number between 1 and 25: "))
   
   if guess == secret:
         print("Yes")
         break
   elif guess > secret:
       print("sorr")
   else:
        print("noup, the secret numbe ris not " ) 


 #naloga 2.1 --pretvornik km v milje
mile = float(0.621371192) 
     
while True:

    km = int(input("Pozdravljeni, to je pretvornik km v milje. Prosim vnesite km: "))
    Result = km*mile
    print(km*mile)

    ask = (input("Želiš ponovni izračun?: "))

    if ask.upper() == "DA" or ask == "YES" or ask == "yes":
        continue
    else: 
     print("Goodbye") 
     break
    
 #naloga 2.2. Fizzbuzz

  
guess_num = int(input("Enter number between 1 - 100: "))
x = range(guess_num,101)
for n in range(guess_num,101): 
   if n%3 == 0 and n%5 == 0: 
     print("fizzbuzz")
   elif n%3 == 0:
    print("fizz")
   elif n%5 == 0:
    print("buzz") 
   else:  
    print(n) 


#naloga 2.3.
str_one = "Happy"
str_two = "Day"


print("%s %s" % (str_one, str_two))

print("{first} {second_str}".format(first=str_one, second_str=str_two))

print(f"{str_one} {str_two}")















  



        

            











    
        

