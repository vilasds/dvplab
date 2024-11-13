from difflib import SequenceMatcher
s1=input("enter the first string:")
s2=input("enter the second string:")
print(SequenceMatcher(None,s1,s2).ratio())