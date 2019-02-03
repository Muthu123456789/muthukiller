g=['a','e','i','o','u']
s=raw_input()
if s in g:
    print ("Vowel")
elif(s.isalpha()):
    print("Consonant")
else:
        print("Invalid")
