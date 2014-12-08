
# Getting started with Python

Python is an interpreted, high level language that emphasises on the code
readability and its functions rather than the syntax. It also has a lot of
built-in methods and tools that allow programmers to express their code in very
less lines of code. For this reason, it has been widely used for various
purposes. It is also supported by the open source community and because of this,
you will find modules for everything right from email fetching to complex tasks
like image recognition.

Raspberry Pi can be programmed using the Python language as well as the new,
feature rich Wolfram language.

#### Basics of Python

The customary starting point of learning any programming language: Printing
'hello world!'


    print 'hello world!'

    hello world!


In Python, you don't have to worry about memory allocation or specifying the
data type of variables unlike commonly used languages like C, C++ and Java. This
makes it easy for beginners and experts to concentrate on their code
functionality. Also, Python uses indentation to specify blocks(instead of
semicolons and brackets).



    a = 10


    print type(a) #type() returns the type of the variable.

    <type 'int'>



    b = 10.01


    print type(b)

    <type 'float'>



    c = 'python'


    print type(c)

    <type 'str'>



    d = 'p'


    print type(d)

    <type 'str'>


Note that, in Python, string and character are not different data types.


    listExample = [1, 2, 3] #list is the Python equivalent of arrays in C, C++, etc.

The only difference is that, in Python, lists can be heterogeneous in nature.
That is, a list's can have elements of different data types.


    listExample = [1, 'a', 1.9]

The variable's data type can also be changed when necessary.


    integer = 5


    print type(integer)

    <type 'int'>



    integer = 'changing the type'


    print type(integer)

    <type 'str'>


#### Getting input from the user


    variable =  raw_input() 

    8



    print type(variable)

    <type 'str'>


Note that the raw_input() function stores values as strings by default.

To change this, use the following built in methods.


    variable = int(raw_input())

    6



    print type(variable)

    <type 'int'>



    variable = float(raw_input())

    8



    print variable, type(variable)

    8.0 <type 'float'>


Note that, the print function can be used to print multiple values by separating
them with a comma.

To display a prompt to the user while getting input, specifying the prompt
string like:


    a = raw_input("Enter your name")

    Enter your nameEnsemble Tech



    a




    'Ensemble Tech'



#### Some commonly used built-in methods


    list = [1, 3, 5, 2, 4, 1]


    list.count(1) #the count of the element 1 in the list

    2



    list.sort() #sorts the list


    list #the list has been sorted




    [1, 1, 2, 3, 4, 5]




    list.append(6) #add an element to the end of the list.

In Python, a string is basically a list of characters. For this reason, list
methods can also be used for strings. There are also some extra methods.


    string = "this is an example"


    string.capitalize() #capitalizes the first letter of the string




    'This is an example'




    string = 'single quotes can also be used'

But make sure that you don't use ' and " together. For example,


    dontDoThis = 'look at the error"


      File "<ipython-input-23-1868471ea474>", line 1
        dontDoThis = 'look at the error"
                                       ^
    SyntaxError: EOL while scanning string literal



#### Loops and conditions

If, if..else, nested if:


    if True:
        print 'this'

    this



    if False:
        print 'hello'
    else:
        print 'hello world'

    hello world



    a = 5


    if a > 5:
        print 'this computer is very poor at Math'
    else:
        print 'Come on! Even a kid can say this'

    Come on! Even a kid can say this


Nested if is achieved by using elif statements.


    #this example uses whatever we have learnt till now
    #can you guess the output without scrolling down?
    userInput = int(raw_input("Enter something"))
    inType = type(userInput)
    if inType == str: #== is used for checking equality. Use = only for assignment
        print "you entered a string" #or maybe you forgot to cast it to the required type. Use int() or float()
    elif inType == float:
        print "you entered a float value"
    elif inType == list:
        print "that is a list"
    else:
        print "This is an integer." #properly typed because this is the right output.

    Enter somethingsomething



    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-31-2d0aa59e6b53> in <module>()
          1 #this example uses whatever we have learnt till now
          2 #can you guess the output without scrolling down?
    ----> 3 userInput = int(raw_input("Enter something"))
          4 inType = type(userInput)
          5 if inType == str: #== is used for checking equality. Use = only for assignment


    ValueError: invalid literal for int() with base 10: 'something'


No, I was cheating. You can't convert a string to an integer unless it has only
numbers. For example, you can change '9898' to a string but changing 'asdasdsad'
to a number is not possible.


    #this example uses whatever we have learnt till now
    #can you guess the output without scrolling down?
    userInput = int(raw_input("Enter something: "))
    inType = type(userInput)
    if inType == str: #== is used for checking equality. Use = only for assignment
        print "you entered a string" #or maybe you forgot to cast it to the required type. Use int() or float()
    elif inType == float:
        print "you entered a float value"
    elif inType == list:
        print "that is a list"
    else:
        print "This is an integer." #properly typed because this is the right output.

    Enter something: 123
    This is an integer.


#### Loops:

For loop: Uses range() and xrange() to iterate through a series of values.


    range(1, 10) #series of values from 1 upto 10(excluding 10)




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




    xrange(1, 10)




    xrange(1, 10)



The difference between range() and xrange() is beyond the scope of Python
application in RPi. However, in brief, use range() in situations where you need
the values in the series(like printing numbers from 1 to 100). Use xrange() when
you don't need the values(like printing hello world 100 times). You can use any
of the two but using them according to the above guidelines will result in an
optimised code.


    for number in range(2):
        print number

    0
    1


Note that the arguments of both range() and xrange() is of the form
(x)range(start, stop[, step]). Here the stop parameter is mandatory. The start
parameter is 0 by default. step parameter allows you to go through the list in
increments. For example,


    range(0, 10, 2) #note that the start parameter is needed if a step is provided.




    [0, 2, 4, 6, 8]




    a = 5
    while a < 10:
        print a
        a += 1 #the increment and decrement operators are not present in Python

    5
    6
    7
    8
    9


Python doesn't provide a switch case construct. Use nested if(with elif) when
necessary.

#### User defined methods

The basic syntax is :

def functionName(optional, parameters, if, needed):
    the function
    does this


    def evenCheck(number):
        if (number % 2) == 0:
            return True
        else:
            return False
    
    def anotherImplementation(number):
        if (number % 2) == 0:
            return "even"
        else:
            return "odd"
    
    for testCase in xrange(2): 
        n = int(raw_input())
        if evenCheck(n):
            print "the number is even"
        else:
            print "the number is odd"
            
        result = anotherImplementation(n)
        print "The number is " + result #string concatenation can be done with the + operator
        print "The number %d is %s" %(n, result)

    3
    the number is odd
    The number is odd
    The number 3 is odd
    4
    the number is even
    The number is even
    The number 4 is even


### Raspberry Pi with Python

In combination with the above mentioned Python basics, you can use the RPi.GPIO
module to program the GPIO pins of the Raspberry Pi. This module is already
available in RPi so you don't have to install it. If you need any additional
modules, launch the terminal in the RPi and use the command sudo pip install
moduleName


    import RPi.GPIO as GPIO #imports the module. using the 'as GPIO' makes it possible to use all the 
                            #module components as GPIO.something instead of RPi.GPIO.something

The following are some basics. An extensive documentation can be found here:
http://pythonhosted.org/RPIO/


    GPIO.setmode(GPIO.BOARD) #sets the numbering scheme according to the board
    GPIO.setwarnings(False)  #sets warnings to false. cleaner ouput.
    GPIO.setup(7, GPIO.OUT)  #set pin 7 as output
    GPIO.output(7, True)     #Set the output as true. In simple terms, light on
    GPIO.output(7, False)    #sets the output to false. In simple terms, light off
    GPIO.cleanup()           #reset every channel that has been set up by this program,
                             # and unexport interrupt gpio interfaces

Make sure you don't use the wrong pins. This image from http://www.raspberrypi-
spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/ should give you
an idea of what to use and what not to use.

<img src = "gpio.png">

Here is a simple program to turn on an LED.


    import RPi.GPIO as GPIO
    import time
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    
    GPIO.output(7, True)
    time.sleep(3)
    GPIO.output(7, False)

This program turns on the LED, keeps it on for 3 seconds and then turns it off.

The pin connections are to be given as follows:

<img src = "ledSingle.png">

To make the LED blink at specific time intervals(say blink thrice. once in every
two seconds)


    import RPi.GPIO as GPIO
    import time
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    
    for blink in xrange(3):
        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        time.sleep(2)

To do the same with multiple LEDS,


    #one led blinks, then the next..waits 
    #for two seconds and then repeats it.
    
    import RPi.GPIO as GPIO
    import time
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    
    for blink in xrange(3):
        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        GPIO.output(3, True)
        time.sleep(0.5)
        GPIO.output(3, False)
        time.sleep(2)
