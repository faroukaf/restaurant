LOGO='''      ____    ____     _______
     / __/   /    \\   |__   __|
    / /__   /  /\\  \\     | |
   /  __/  /  /__\\  \\    | |
  / /___  /  /____\\  \\   | |
 /_____/ /__/      \\__\\  |_|

 	\t\t\t@byFarouk'''

try:
	import re
	mainofr=open('maino.txt','r')
	tempd=mainofr.readlines()
	mainodic={}
	i=0

	#the mine idea of the following peace of code is but first then but other i well deleted so be free to use it by time
	while i <len(tempd):
		if re.search(r',[\w]+,',tempd[i]):
			keyt=tempd[i].replace("\n",'').replace(',','')
			mainodic[keyt]=[]
			i+=1
			while i<len(tempd) and not(re.search(r',[\w]+,',tempd[i])):
				mainodic[keyt].append(tempd[i])
				i+=1
	del i,tempd
except FileExistsError:
	open('maino.txt','x').close()
	print("maino.txt wasn`t exist and now we creat one")
finally:
	mainofr.close()
def printMaino():
	'''this function to print manio '''
	firstLines=[]#have the keys of mainodic
	submaino=[]#have values seprated
	length=[] #to get lengt and get the bigger
	for i in list(mainodic.values()):
		length.append(len(i))
	for n in range(len(mainodic)//3):
		submaino.append([])
		for nn in range(max(length)):
			submaino[n].append('')
	kjumb=0
	sv=len('vegetables          ')
	l=0
	while kjumb<len(mainodic)//3:
		firstLines.append('')
		for k in list(mainodic.keys())[kjumb*3:kjumb*3+3]:
			line=k.replace(',','').replace('\n','')
			line=line+' '*(sv-len(line))
			firstLines[l]+=line
			for nn in range(max(length)):
				try:
					string=mainodic[k][nn].split()
					string=(':'.join(string[0:2])+'->'+string[2]).replace('\n','').replace('_'," ")
					string=string+' '*(sv-len(string))
					submaino[l][nn]+=string
				except IndexError:
					submaino[l][nn]+=' '*sv
		kjumb+=1
		l+=1
	if len(mainodic)%3!=0:
		firstLines.append('')
		submaino.append([])
		for nn in range(max(length)):
			submaino[l].append('')
		for k in list(mainodic.keys())[kjumb*3:kjumb*3+len(mainodic)%3]:
			line=k.replace(',','').replace('\n','')
			line=line+' '*(sv-len(line))
			firstLines[l]+=line
			for nn in range(max(length)):
				try:
					string=mainodic[k][nn].split()
					string=(':'.join(string[0:2])+'->'+string[2]).replace('\n','').replace('_'," ")
					string=string+' '*(sv-len(string))
					submaino[l][nn]+=string
				except IndexError:
					submaino[l][nn]+=' '*sv

	del l,kjumb,sv
	#this to print
	if len(submaino)==len(firstLines):
		for itemn in range(len(firstLines)):
			print(firstLines[itemn])
			for sn in submaino[itemn]:
				print(sn)
def print_poth(st,fi):
	history=open('history.txt','a')
	history.write(st+'\n')
	fi.write(st+'\n')
	print(st)
	history.close()
def edit():
	'''nc new_catogre_name
	ec old_catogre,new
	ec number,new
	ni cNum,new
	ei cNum,iNum,new
	q : is to end
	b : is to back what we had made
	r : is to back one move
	p : is to print maino
	h : is to get help
	rp cNum,iNum,newp
	'''
	helps='''nc new_catogre_name
	ec old_catogre,new
	ec number,new
	ni cNum,new
	ei cNum,iNum,new
	q : is to end
	b : is to back what we had made
	r : is to back one move
	p : is to print maino
	h : is to get help
	rp cNum,iNum,newp
	'''
	global mainodic
	spare=mainodic.copy()
	lastMove={} 
	while 1:
		command=input('>>>').split()
		if command==[] or command==['']:
			continue
		if command[0].lower()=='r':
			if lastMove!={}:
				mainodic=lastMove
				continue
		if command[0].lower()=='nc':#add new catogre
			if re.search(r'[\w]+',command[1]):
				mainodic[command[1]]=[]
			else:
				print("Invalid syntax")
		elif command[0].lower()=='ec':#edit old catogry
			co=command[1].split(',')
			try:
				mainodic[co[1]]=mainodic.pop(co[0])
			except KeyError:
				try:
					mainodic[co[0]]=mainodic.pop(co[1])
				except (KeyError,IndexError):
					try:
						cNum=int(co[0])
						mainodic[co[1]]=mainodic.pop(list(mainodic.keys())[cNum])
					except IndexError:
						print("no such catograie")
					except:
						print("Invalid syntax")
			except:
				print("Invalid syntax")

		elif command[0].lower()=='q':
			break
		elif command[0].lower()=='ni':
			try:
				co=command[1].split(',')
				if len(co)!=2:
					print('Invalid syntax')
				float(co[1].split('_')[-1])
				coo=co[1].split('_')
				coos='_'.join(coo[:len(coo)-1])+' '+coo[-1]
				mainodic[list(mainodic.keys())[int(co[0])-1]].append(str(len(mainodic[list(mainodic.keys())[int(co[0])]]))+' '+coos+'\n')
			except IndexError:
				print("no item")
			except (ValueError,TypeError):
				print('Invalid syntax')
		elif command[0].lower()=='ei':
			try:
				co=command[1].split(',')
				if len(co)!=3:
					print('Invalid syntax')
				float(co[1].split('_')[-1])
				coo=co[1].split('_')
				coos='_'.join(coo[:len(coo)-1])+' '+coo[-1]
				tmpl=mainodic[list(mainodic.keys())[int(co[0])-1]]
				tmpl[int(co[1])-1]=co[1]+' '+coos
			except IndexError:
				print("no item")
			except (ValueError,TypeError):
				print('Invalid syntax')
		elif command[0].lower()=='rp':
			co=command[1].split(',')

			if len(co)==3:
				try:
					mas=0
					cNum=int(co[0])
					if cNum>=len(mainodic):raise IndexError
					mas=1
					iNum=int(co[1])
					mas=2
					newp=int(co[2])
					tempi=mainodic[list(mainodic.keys())[cNum-1]][iNum-1].split()
					mas=3
					tempi[-1]=str(newp)
					mainodic[list(mainodic.keys())[cNum-1]][iNum-1]=' '.join(tempi)
				except TypeError:
					if mas==0:
						try:
							mas=1
							iNum=int(co[1])
							mas=2
							newp=int(co[2])
							tempi=mainodic[co[0]][iNum-1].split()
							mas=3
							tempi[-1]=str(newp)
							mainodic[co[0]][iNum-1]=' '.join(tempi)
						except KeyError:print("no such catogre")
						except TypeError:
							if mas==1:print("no such item")
							elif mas==2:print("this isn`t price")
							else:print("Invalid syntax")
					
						except IndexError:
							if mas==0:print("no such catogre")
							elif mas==1:print("no such item")
							else:print("bs")
						except:
							print("Invalid syntax")
					elif mas==1:print("no such item")
					elif mas==2:print("this isn`t price")
					else:print("Invalid syntax")
					
				except IndexError:
					if mas==0:print("no such catogre")
					elif mas==1:print("no such item")
					else:print("bs")
				except:
					print("Invalid syntax")
			else:print("Invalid syntax")
		elif command[0].lower()=='b':
			mainodic=spare
			del spare
			break
		elif command[0].lower()=='h':
			print(helps)
		elif command[0].lower()=='p':
			printMaino()
		else:
			print('Invalid syntax')
			continue
		lastMove=mainodic.copy()
	printMaino()
	with open('test.txt','w') as f:
		for k in mainodic.keys():
			f.write(','+k+',\n')
			for v in mainodic[k]:
				f.write(v)
def cach():
	history=open('history.txt','a')
	history.write(">"*16+'\n')
	history.close()
	f=open('temp.txt','w')
	pall=0
	while 1:
		s=input("cach:>>")
		if s=='':continue
		if s.lower()=='q':
			#rember ther change here
			print_poth("your meal cost: {}".format(pall),f)
			print_poth("service cost 20",f)
			print_poth("sales tax cost: {}".format(pall*(100/15)),f)
			print_poth("\tTotal is: {}".format(20+pall*(1+100/15)),f)
			break
		elif s.lower()=='n':
			print_poth("you cancel operation",f)
			#f.close()
			cach()
		elif s.lower()=='p':
			printMaino()
		elif re.match(r'[\d]+,[\w\s]+',s):
			command=s.split(',')
			try:
				tpall=pall
				msg=0
				mush=int(command[0])
				msg=1
				command[1]=command[1].replace(' ','_')
				for v in mainodic.values():
					msg=2
					for vs in v:
						if re.search(command[1],vs):
							print_poth(vs,f)
							msg=3
							pall+=mush*float(vs.split()[-1])
							break
					if pall!=tpall:break
					msg=1
				if pall==tpall and msg==1:
					print("not such item")
			except ValueError:
				if msg==0:print("No part of meal")
				elif msg==3:print('manio have problem')
			except IndexError:
				print('manio have problem')
		elif re.search(r'^[\d]+,[\d]+,[\d]+',s):
			command=s.split(',')
			if len(command)==3:
				try:
					msg=0
					much=int(command[0])
					msg=1
					item=mainodic[list(mainodic.keys())[int(command[1])-1]][int(command[2])-1]
					print_poth(item.replace('_',' '),f)
					msg=2
					pall+=much*float(item.split()[-1])
				except ValueError:
					if msg==0:print('much must be integer')
					elif msg==2:print('maino have problem')
					else:print('Invalid syntax')
				except IndexError:
					try:
						list(mainodic.keys())[int(command[1])-1]
						print('no such item')
					except IndexError:print('no such catogre')
			elif len(command)==4:
				try:
					msg=0
					much=int(command[0])
					msg=4
					precent=float(command[3])/100
					msg=1
					item=mainodic[list(mainodic.keys())[int(command[1])-1]][int(command[2])-1]
					print_poth(item.replace('_',' '),f)
					msg=2
					pall+=much*float(item.split()[-1])*precent
				except ValueError:
					if msg==0:print('much must be integer')
					elif msg==2:print('maino have problem')
					elif msg==4:print('chek your precent')
					else:print('Invalid syntax')
				except IndexError:
					try:
						list(mainodic.keys())[int(command[1])-1]
						print('no such item')
					except IndexError:print('no such catogre')
			else:print('Invalid syntax')
			del item
		else:print('Invalid sntax')

	f.close()

if __name__ == '__main__':
	print("pice be upon you")
	print(LOGO)
	printMaino()
	while 1:
		say=input("*>>")
		if say.lower()=="edit":edit()
		elif say.lower()=='cach':cach()
		elif say.lower()=="q":
			print("pice be upon you")
			break
		elif say.lower()=='p':printMaino()
		elif say=="":continue
		else:
			print("Invalid syntax")
			continue
'''to be fix
re in cach
name of cacher
times and helps'''