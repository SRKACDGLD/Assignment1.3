# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:00:43 2018

@author: srk

Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
""" 
Fname = input("Enter First Name: ")
Lname = input("Enter Last Name: ")

myname = Fname + " " + Lname
#printing default order as per given input sequence
print("Fullname in actual given order of Firstname and Lastname is: ", myname) 
Lnameindex = myname.index(" ")+1
Mynamelength = myname.__len__()
# print("Index of space is: ", Lnameindex)
# print("Length of name is: ", Mynamelength)

Lnameindextemp = Lnameindex
print("Fullname in reverse order of Firstname and Lastname is: ",end="")
while Lnameindextemp < Mynamelength:  # This loop prints last name first
    print(myname[Lnameindextemp],end="")
    Lnameindextemp = Lnameindextemp + 1

print(" ",end="")
Mynameindex=0
while Mynameindex < Lnameindex-1:    #This loop prints First name at last
    print(myname[Mynameindex],end="")
    Mynameindex = Mynameindex + 1
