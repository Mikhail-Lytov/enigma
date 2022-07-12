#enigma
def the_first_rotor(op,rot_1): # это первый ротор или самый правый
	i = 0
	rotor_1 = [ ]
	while i < 33:
		rotor_1[i] = rotor_1[(i + rot_1)%32]

	return (op)# вернуть что-то
def open_txt():
	open_file = open('open.txt','r')
	try:
		f.read(1)
		
	finally:
		open_file.close()

print("введите значения для правого(1 ротора), среднего(2 ротора), левого (3 ротора")
rot_1 = input("введите первый ротор:")
rot_1_int = ord(rot_1) - 96  подставить под таблицу аски 
rot_2 = input("введите второй роутер:")
rot_3 = input("введите третий роутер:")
open_file = open('open.txt','r')
close_file = open('close.txt','a')
op = str()
for line in open_file:
	op = open_file.read(1)
	if (op >= 'а' and op <= 'я') or (op >= 'А' and  op <= 'Я'):
		the_first_rotor (op,rot_1)
	close_file.write(op)

	print (op,'прочитал')
	