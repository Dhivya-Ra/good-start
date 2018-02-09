n=int(input(''))
l=[]
for i in range(n):
	l.append(int(input('')))
l=sorted(l)
print(l)
for i in range(n-1):
	m=0
	for j in range(i+1,n):
		if l[i]==l[j]:
			m=m+1
	if m==1:
		l[n]=1
		print(l[i])
if l[n]!=1:
	print("unique")
		

	
