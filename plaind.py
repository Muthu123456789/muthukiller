string="malayalam"
revstr=''.join(reversed(string))
print(revstr)
if list(string)==list(revstr):
	print("yes")
else:
	print("no")
