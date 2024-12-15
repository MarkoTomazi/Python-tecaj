#zapisi filov, različne končnice

#odpiranje filov,ko jih odpreš jih probaš tudi zapret za sabo.

moj_file = open("ninja3.txt", "r")

vsebina = moj_file.read()

print(vsebina)

moj_file.close()


#odpre in na koncu zapre file, pristop 1: prebere vse na enkrat
with open("ninja.txt", "r") as moj_file:
    vsebina = moj_file.read()
print(vsebina)

#opdre in na koncu zapre file, pristop 1: prebere line by line
with open("ninja.txt", "r") as moj_file:
    ninja_lines = moj_file.readlines()

    for line in ninja_lines:
     print(ninja_lines)


#delaš zapise v novem filu
with open("ninja2.txt", "w") as moj_file:
   moj_file.write("Ninja\n")
   moj_file.write("Samurai\n")

   open()


#v txt smo zapisal številke od 1 do 100

with open("ninja3.txt", "w") as moj_file:
 for n in range(1,100): 
    moj_file.write(f"number : {n}")


    for x in range(1, 101):
      print(x)

with open("ninja4.txt", "w") as test:
   for n in range(1,21):
    test.write(f"Number: {n}\n")


# simple open txt    
moj_file = open("ninja4.txt", "r")

vsebina = moj_file.read()

print(vsebina)

moj_file.close() 

    
    
# 1 2 3 4 5 6 7 8 9 10 ... 100

# a b c d e f g h i j ... z

# # create a list of alphabetci characters and chars should be with double quotes

# [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]



for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    print(f"tole je pa crka: {i}")


    #curl klic za api

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

#guess the secret number counter of attempts + save best score 
import random

secret = random.randint(1,10)
attempts = 0

while True:
   guess = int(input("Guess the secret number (between 1 and 10): "))
   attempts +=1

   if guess == secret:
        with open("score.txt", "a") as score_file:
         score_file.write(f"Attempts needed: {attempts}\n")
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
   elif guess > secret:
        print ("Your geuss is not correct.. try something smaller")
   elif guess < secret:
        print ("Your geuss is not correct.. try something bigger")   

#read txt
file = open("score.txt", "r")
vsebina = file.read()
print(vsebina)

#write csv
with open("test.csv", "w") as moj_file:
     moj_file.write("Name;")
     moj_file.write("Age;")
     moj_file.write("Gender\n")
     moj_file.write("Marko;")
     moj_file.write("30;")
     moj_file.write("male")


#read csv
import csv
with open("test.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file)
  for line in csv_reader:
   print(line[2])    



#pandas
import pandas as pd
df = pd.read_csv("test.csv") 
df.head
print(df.to_string())


#Naloga 3.1. -->read csv + create new output
import csv
with open("test.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter= ';') #sets delimiter
  next(csv_reader) # skip fisrst line
  for line in csv_reader:
   print(line[0] + " is " + line[1] + " years old"   + " and " + line[2] + ".") 

     


   









     


    


    


   




    
