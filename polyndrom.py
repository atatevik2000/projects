def polyndrom(slovo):
	if slovo[::1] == slovo[::-1]:
		return True
	else: 
	    return False
sl = input()
s = polyndrom(sl)
if s ==True :
	print("polyndrom")
else:
	print("Not polyndrom")