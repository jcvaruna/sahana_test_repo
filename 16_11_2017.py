# Find if a given number is a power of 3

test_num = raw_input("Enter number under test: ")
test_num = int(test_num)
test_num1 = test_num
rem=100

if test_num < 0:
    print "The number is less than 0, so it is not power of 3"
elif test_num == 0:
    print "The given number is 0. Please provide a number other than 0"
elif (test_num%3) != 0:
    print "Number",test_num1,"is NOT a power of 3"
else:
    rem = test_num%3
    while test_num>=3 and rem==0:
        rem = test_num%3
        test_num = test_num/3
        print "test_num: "+str(test_num)+"\nrem: "+str(rem)

if rem == 0:
    print "Number",test_num1,"is a power of 3"
else:
    print "Number",test_num1,"is NOT a power of 3"
