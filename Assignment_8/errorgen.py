import sys  #This module is used to know the type of the exception

check_list = [0,'c',5]

for entry in check_list:
	try:
	   print("The entry is ",entry)
	   r = 1/int(entry)
	   break
	except:
	   print("Sorry ",sys.exc_info()[0],"occurred")
	   print("Next entry.")
	   print()
print("The reciprocal of" ,entry,"is",r )
