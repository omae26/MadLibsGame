print("Let's play Mad Libs!\nFill in the blanks below: ")

#Collect user inputs.
name = input("Enter a name: ")
planet = input("Enter the name of a planet: ")
vehicle = input("Enter a type of vehicle: ")
alien_creature = input("Enter a type of alien creature: ")
emotion = input("Enter an emotion: ")
verb = input("Enter a verb: ") 

#story template
print("Captain " + name + " boarded the " + vehicle + " and set course for planet " + planet + "."
      " \nUpon landing, they were greeted by a group of " + alien_creature + "s." " \nFeeling very " + emotion + 
      "." "Captain " + name + " decided to " + verb + " into the unknown jungle." "\nIt was a space adventure"
      " like no other!")
