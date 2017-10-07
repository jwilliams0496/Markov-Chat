#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:18:31 2017

@author: MarbleCake
"""

def main():
    x = input("Say something!: ")

    while(x != "quit"):
        markov(x)
        x = input("Say something!: ")
        

def markov(str):
    usrStr = str.split()
    
    for word in range(len(usrStr)):
        print(usrStr[word], end = " ")
        
        # Create a set
        
    print("")
        
        
main()