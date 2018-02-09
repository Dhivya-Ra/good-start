d ={'chennaimadurai':{'1':['pandiyan','9:00',50],'2':['GURUVAYUR','3:00',50]},'chennaicoimbatore':{'1':['cheran','11:00',25],'2':['SENGOTTAI','2:00',50]}}
a=input('from')
b=input('to')
a=a+b
print('\ns.no  train name  time  seats\n')
for m in d[a]:
	print('\n')
	print (m,end="   ")
	for n in d[a][m]:
		print (n,end="   ")
n=input('train no:')
s=int(input("seats"))
if d[a][n][2] >= s:
	print('\nyour ticket booked in '+d[a][n][0]+' seat number is')
	b=d[a][n][2]+1
	for i in range(s):
		b=b-1
		print(b)
	d[a][n][2]=b-1
