def cach():
	try:
		history=open('history.txt','a')
		history.write(">"*16)
		history.close()
		f=open('temp.txt','w')
		pall=0
		s=''
		while 1:
			igiven=input(">>>")
			given=igiven.split(',')
			s=mainodic[list(mainodic.keys())[int(given[0])-1]][int(given[1])-1]
			f.write(s);print(s)
			pall+=int(s.split()[-1])
	except (TypeError,ValueError,IndexError):
		if igiven.lower()=='q':
			print_poth("your meal cost: {}".format(pall),f)
			print_poth("service cost 20",f)
			print_poth("sales tax cost: {}".format(pall*(100/15)),f)
			print_poth("\tTotal is: {}".format(20+pall*(1+100/15)),f)
		elif igiven.lower=='n':print("you cancel the order");cach()
		try:
			n1=float(given[0])
			n2=float(given[1])
			if n1>len(mainodic):
				print("no catogre by this index")
			elif n2!=int(n2) or n1!=int(n1):
				print("this is float")
			elif n2>len(mainodic[list(mainodic.keys())[int(given[0])-1]][int(given[1])-1]):
				print("no such item")
		except (TypeError,IndexError,ValueError):
			print("Invalid syntax")