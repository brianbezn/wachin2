import random
n=0
y=50
z11=8
z12=2
z21=5
z22=5
#z escenario jugador
j=2
#j: significatividad del ultimo pago en el aprendizaje
c=5
#c:castigo
while n<5:
	x=random.randint(1,101)
	if x>y:
	#si x>y escenario 2
		print "pagos jugador 1:"
		print z21
		print "pagos jugador 2:"
		print z22
		a=raw_input("y/n")
		if a=="y":
			p=z21
			y=y-(p*j)*y/100
		else:
			p=0
			y=y+(c*j)*(100-y)/100
	else:
		print "pagos jugador 1:"
		print z11
		print "pagos jugador 2:"
		print z12
		a=raw_input("y/n")
		if a=="y":
			p=z11
			y=y+(p*j)*(100-y)/100
		else:
			p=0
			y=y-(c*j)*y/100
	
	print y
	if y>100:
		y=100
	elif y<1:
		y=1
	print y
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	n+=1

		
