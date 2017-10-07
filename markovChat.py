#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:18:31 2017

@author: MarbleCake
"""

class MarkovWord:
    
    # takes a word, its frequency, and the next 4 MarkovWords that follow it
    def __init__(self, word, freq, next4):
        self.word = word
        self.freq = freq
        self.next4 = next4
        
    def getWord(self):
        return self.word
    
    def getFreq(self):
        return self.freq
    
    def getNext4(self):
        return self.next4
    
    def setWord(self, word):
        self.word = word
        
    def setFreq(self, freq):
        self.freq = freq
        
    def setNext4(self, next4):
        self.next4 = next4
    
    def printMarkovWord(self):
        print("[" + str(self.word) + ", " + str(self.freq) + ", " + str(self.next4) + "]")

def main():
    response = input("Say something!: ")

    while(response != "quit"):
        markov(response)
        response = input("Say something!: ")
        

def markov(response):
    usrStr = response.split()
    freqTable = []
    
    for word in range(len(usrStr)):
        
        freq = 0
        # loop through all words in sentence to find matches
        for word2 in range(len(usrStr)):
            if usrStr[word] == usrStr[word2]:
                freq += 1

        markovWord = MarkovWord(usrStr[word], freq, [])
        freqTable.append(markovWord)
        
    for mword in range(len(freqTable)):
        for word in range(len(usrStr)):
            #todo

        
main()