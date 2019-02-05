string="malayalam"
revstr=''.join(reversed(string))
print(revstr)
if list(string)==list(revstr):
	print("palindrome")
else:
	print("not a palindrome")
