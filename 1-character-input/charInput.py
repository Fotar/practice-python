#I feel like I'm committing some form of fuckery by not having a main.
#This just needed to be said.
#Marion, 27/2/17
import datetime

name = input("What is your name? ")
print("Confirmation: " + name)

age = int(input("What is your age? "))
print("Confirmation: %d" % age)

#hahaha, I'm actually having to delete semicolons that I'm instinctively putting at the end of every line
now = datetime.datetime.now()
gap = (100 - age)
print("You will turn 100 years old in the year %d" %(now.year + gap))