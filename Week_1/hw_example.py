print "1. Square"
print "2. Rectangle"
selection = raw_input("Enter a choice: ")

selection = int(selection)

if selection == 1:
	side = raw_input("Enter the length of the sides: ")
	side = int(side)
	perimeter = side * 4
	area = side * side
	print "The perimeter is: " + str(perimeter)
	print "The area is: " + str(area)

elif selection == 2:
	sideOne = raw_input("Enter the length of a side: ")
	sideOne = int(sideOne)
	sideTwo = raw_input("Enter the length of the other side: ")
	sideTwo = int(sideTwo)
	perimeter = sideOne * 2 + sideTwo * 2
	area = sideOne * sideTwo
	print "The perimeter is: " + str(perimeter)
	print "The area is: " + str(area)
