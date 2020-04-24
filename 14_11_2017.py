def print_triangle(num_of_lines, number):

	for i in range(0, num_of_lines):
		to_print=" "
		for j in range(1,num_of_lines-i):
			print to_print,
		
		to_print=number
		for k in range(1,i*2):
			print to_print,

		print("\n")
		#print("{}{}".format(space_to_print,number_to_print))


print_triangle(10,5)
