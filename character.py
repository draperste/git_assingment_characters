#!/usr/bin/env python3

def character():
 character = x

print ("Character lister")

cont = "y"
while (cont.lower() == "y"):
 print ("Enter a character name")
 x = input()
 print("The character you picked is " + x)

 if x == "Sauron":
  print("The Dark lord of Mordor.")

 if x == "Gandalf":
  print ("A wizard is never late, Frodo Baggins. Nor is he early. He arrives precisely when he means to.")

 if x == "Darth Vader":
  print ("You don't know the power of the dark side!")

 if x == "Spider-Man":
  print ("With great power there must also come great responsibility.")


 cont = input ("Do you want anther character? [y/n] ")
