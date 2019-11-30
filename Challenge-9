# Preston Hudson 11/30/19 Challenge 9 Written in Python

#1. Find a file on computer and print its contents.

with open("Read-File.txt", "r") as f:
    print(f.read())

#2. Write a program that asks the user a question and writes the anwser to a file.

user_color = input("Whats your favorite color? ")

with open("Read-File.txt","w") as f:
    f.write(user_color)

#3. Write stuff from list to file.

import csv

watches = [["Top Gun", "Riskey Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Flight"]]

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(watches[0])
    w.writerow(watches[1])
    w.writerow(watches[2])


#Completed
