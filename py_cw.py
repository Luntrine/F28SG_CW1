# Lucca Anthony Marcondes Browning   <--- so we know who you are
# H00369673                          <--- so we know who you are
# Edinburgh Campus                   <--- Edinburgh, Dubai, or Malaysia 
# F28PL Coursework 1, Python         <--- leave this line unchanged 

# Deadline is Wednesday 26 October 2022 at 15:30, local time for your campus (Edinburgh / Dubai / Malaysia).

# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 

# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

# Before submitting this coursework please complete the Student authorship declaration here:
#   https://canvas.hw.ac.uk/courses/20804/assignments/102574 

################################################################################
# Question 1   

"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""

#####################################
# Question 1a

"""
The following method takes two tuples as inputs that represent two complex numbers.
It then adds the real parts of the two numbers together and appends it to be the 
first element of the result list. Afterwards, it adds the imaginary parts of the 
two numbers together and appends it to be the second element of the results list.

This final number returned by the results list is the sum of adding together
the numbers in the parameter.
"""
def cadd(c1, c2):
    result = []
    result.append(c1[0] + c2[0]) #The real numbers added together.
    result.append(c1[1] + c2[1]) #The imaingary numbers added together.
    return result
 
"""
The following method takes two tuples as inputs that represent two complex numbers.
It then multiplies the real parts of the two numbers together and appends it to be the 
first element of the result list. Afterwards, it multiplies the imaginary parts of the 
two numbers together and appends it to be the second element of the results list. It
does this using the FOIL method.

This final number returned by the results list is the product of adding together
the numbers in the parameter.
"""
def cmult(c1, c2):
    result = []
    #Both real numbers multiplied together - both imaginary numbers multiplied together.
    #The reason they are subtracted is because i^2 = -1.
    result.append(c1[0] * c2[0] - c1[1] * c2[1])
    #Real part of complex c1 multiplied by imaginary part of c2 + imaginary part of c1 
    #multiplied by real part of c2. Real numbers multiplied by imaginary ones result
    #in imaginary numbers.
    result.append(c1[0] * c2[1] + c1[1] * c2[0])
    return result


#####################################
# Question 1b

"""
The following method takes two numbers, which represent a complex number with a real part
and an imaginary part. It then multiplies the imaginary part of the number with 1j,
turning it imaginary for real. It then returns the the real part of the number + the imaginary part
of the number, turning it into a fully fledged imaginary number.
"""
def tocomplex(x1, y1):
    return (x1 + y1 * 1j)

"""
The following method takes an imaginary number and returns a tuple with the first element being
the real part of the complex number and the second element being the imaginary part of the complex
number.
"""
def fromcomplex(c):
    return (c.real, c.imag)


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2

"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""

#####################################
# Question 2a


"""
The following method takes two lists. It iterates through them using a for loop with 
a zip function which appends the "and" result of the current elements to a third list 
by multiplying them together. It does this for every element in lists l1 and l2.
"""
def seqandi(l1, l2):
    l3 = []
    for a, b in zip(l1, l2):
        l3.append(a and b)
    return l3

"""
The following method takes two lists. It iterates through them using for loop with 
a zip function which appends the "xor" result of the current elements to a third list.
It does this for every element in lists l1 and l2.
"""
def seqxori(l1, l2):
    l3 = []
    for a, b in zip(l1, l2):
        l3.append((a and not b) or (not a and b)) #This calculation is equivalent to xor.
    return l3


#####################################
# Question 2b

"""
The following method takes two lists. It iterates through them recursively, appending
the "and" result of the current elements to a third list by multiplying them together. 
It does this for every element in lists l1 and l2. To be able to do this, it uses a
helper method written below.
"""
def seqandr(l1, l2):
    l3 = []
    n = 0
    seqandrhelper(l1, l2, l3, n)
        
def seqandrhelper(l1, l2, l3, n):
    l1Element = l1[n]
    l2Element = l2[n]
    n+=1
    l3.append(l1Element and l2Element)
    #returns the result only if the final elements of both lists have been calculated
    #and appended to the third list.
    if len(l1) == n:
        print(l3)
        return
    seqandrhelper(l1, l2, l3, n)
        
"""
The following method takes two lists. It iterates through them recursively, appending
the "xor" result of the current elements to a third list. It does this for every element 
in lists l1 and l2. To be able to do this, it uses a helper method written below.
"""
def seqxorr(l1, l2):
    l3 = []
    n = 0
    seqxorrhelper(l1, l2, l3, n)

def seqxorrhelper(l1, l2, l3, n):
    l1Element = l1[n]
    l2Element = l2[n]
    n+=1
    l3.append((l1Element and not l2Element) or (not l1Element and l2Element)) #This calculation is equivalent to xor.
    #returns the result only if the final elements of both lists have been calculated
    #and appended to the third list.
    if len(l1) == n:
        print(l3)
        return
    seqxorrhelper(l1, l2, l3, n)

#####################################
# Question 2c

"""
The following method takes two lists. It zips them into a third list. Then, it iterates through
that third list using a list comprehension which appends the "and" result of both elements
inside of the current element (a tuple) to a fourth list by multiplying them together. 
It does this for every element in list l3.
"""
def seqandlc(l1,l2):
    l3 = list(zip(l1, l2))
    l4 = [a and b for a,b in l3] 
    return l4

"""
The following method takes two lists. It zips them into a third list. Then, it iterates through
that third list using a list comprehension which appends the "xor" result of both elements
inside of the current element (a tuple) to a fourth list. It does this for every element in list l3.
"""
def seqxorlc(l1,l2):
    l3 = list(zip(l1, l2))
    l4 = [(a and not b) or (not a and b) for a,b in l3]
    return l4


# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

"""
a. The difference between mutable and immutable types is that after creation, mutable types can be modified
internally (as in added to or removed from) and immutable types cannot have this done to them. Examples of
mutable types are Lists, Sets, and Dictionaries. Examples of immuatable types are Tuples, and Frozen Sets.
What sets there types apart is that Lists, Sets and Dictionaries have mutability methods such as append(), 
remove() and delete().

The following would compute.
"""
def testQ3ai():
    list = []
    list.append(1)

"""
The following would not compute.
"""
def testQ3aii():
    tuple = ()
    tuple.append(1)
"""
b. The difference between integer and float types put simply, is that integers do not have decimals and floating
point numbers do. However, there are differences in their capabilities and use cases. As floating point numbers are
64 bit double precision values, they are used for extremely large numbers. Integers are only 32 bits, so they take up
less space in memory and are better used in day to day programs. However, both can be used in whichever program they
are required in.

Below are an example of an integer and a float type.
"""
def testQ3b():
    exInteger = 1
    exFloat = 1.0

"""
c. The difference between "=", "==", and "is" is that "=" is used for assigning a value to a variable. "==" is used to
check whether the values in two potentially different points in memory are equal to each other. "is" is used to check
whether two values are pointing to the same exact place in memory, not just if they are equal to each other.

Below are examples of this.For the sake of demonstration, the numbers cannot be between -5 and 256 since they are 
stored in an array by python and will always point to the same location in memory.
"""
def testQ3c():
    
    #Assignment (Pointing to different places in memory)
    a = 1000
    b = 1000

    #Equality but NOT Identity
    assert (a==b) == True
    assert (a is b) == False

    #Assignment (Pointing to same place in memory)
    a = b

    #Equality AND Identity
    assert (a==b) == True
    assert (a is b) == True

"""
d. The range will always be an object in memory, and you can call and print it. However, if you try to print it, you will only get
the idea of the range (in the example below, it being a range from 0 to 5). To be able to actually see the numbers in the range, 
one would need to turn the range into a list with the list() function in Python3. It would also allow you to perform list functions 
on the range in the future.

An example of printing the idea of the range vs the actual "listed" range is down below.
"""

def testQ3d():
    exRange = range(5)
    print(exRange)
    
    exRangeList = list(range(5))
    print(exRangeList)

"""
e. In Python3, a slice can either come in two forms: slice(start, end, step) and [start:end] where the starting index
is included and the ending index is not. What slices do is return elements (between start and end) of a list, string, 
tuple, byte, bytearray, or range. 
The reason why list(range(10**10)[10:10]) prints an empty list is because it is returning a sub-list
between 10 and 10, not inclusive of 10 in a list with a range of 10**10. Since it's not inclusive of its starting index,
it will not return anything aside from an empty list. It will not crash your PC, despite the size of the original range,
because it will not create the original list before applying the slice to it, and, hence, won't fully load the memory.
Therefore, the reason why list(range(10**10))[10:10] doesn't return everything before my terminal hoards 75 gigabytes 
of RAM (including virtual memory on my machine) and crashes is because it creates the list before applying the slice
to it. Obviously, no modern machine can take a list 10000000000 elements long without suffering.
In short, the difference between list(range(10**10)[10:10]) and list(range(10**10))[10:10] is that the former applies
the slice to the range before the list has been created, and the latter applies the slice to the list after it has
been created.

"""


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a *datum* something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""

"""
The following method takes a piece of data, whether it be an integer, or a list of either lists or integers, and
applies a function to every single integer in that list recursively by calling itself on every sub-list until every
element has been accounted for. For every element, in the end, it will either return an empty list, a single value
with the result of the function, or a list filled with one or both of the aforementioned results.
"""
def supermap(func, data):
    if isinstance(data, int): #Does this if the data is an integer.
        return func(data)
    elif isinstance(data, list) and len(data) == 0: #Does this if the data is an empty list.
        return []
    else: #Does this if the data is a list with elements inside of it.
        for i in range(len(data)):
            #Recursively calls the function for every element in data, and then for every element in data[i].
            #So on and so forth.
            data[i] = supermap(func, data[i]) 
        return data
    

# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""

"""
The following method returns either an empty list if n is 0 or it returns a list
of [x-1, [x-1]], where x is how many times the aforementioned list will be
printed inside of both elements of the list recursively.
"""
def fenc(n):   
    if n == 0: #Base Case
        return '[]'
    else: #Recursive Case
        return '[{N}, [{N}]]'.format(N=fenc(n-1))

"""
The following method returns 1 if the base case condition is met. If not, it returns
n where n is how many of the "Base cases" are inside of the primary array.
"""
def fdec(l): #Base Case
    if l == [[],[[]]]:
        return 1
    else: #Recursive Case
        return 1 + fdec(l[0])


# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""

"""
The following method yields an ever increasing string for every next() call that is made to it.
"""
def love():
    loveString = ""
    while 1==1: #This will *always* be true.
        if loveString == "": #Does this if the string is still empty.
            loveString = "I love you "
        elif loveString[0] == "I": #Does this if previous string added was "I love you" or "I love that"
            loveString = "You love that " + loveString
        else: #Does this if previous string added was "You love that"
            loveString = "I love that " + loveString
        yield loveString
        #Only goes to the next iteration of the while loop if next() is called.

# END ANSWER TO Question 6
################################################################################


#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""

"""
The following method takes a number and a list of numbers and removes all instances of the number by iterating
through the list using a while loop.
"""
def removeall_oo(i, l):
    j = 0
    while j < len(l):
        if i == l[j]: #Checks if the element is equal to the number that is supposed to be removed from list.
            #If a number is removed, the list shortens, meaning the next element becomes the current element.
            #This removes the need to iterate to the next element.
            l.remove(i)
        else: #If an element is not removed, it iterates to the next element and checks that.
            j+=1
    return l

"""
The following method takes a number and a list of numbers and removes all instances of the number by using the
filter method and then returning a list of the results.
"""
def removeall_ft(i, l):
    import functools
    return list(filter(lambda x: x != i, l))

"""
The following method takes a number and a list of numbers and removes all instances of the number by using an
anonymous function that makes each element in the list empty unless it's not equal to i.
The parameters of reduce hold the function that will be applied, the list it will be writing from, and the
list it will be writing to in that order. The latter doesn't need to be declared since the function is 
anonymous and the result is returned in the same line.
"""
def removeall_rd(i, l):
    from functools import reduce #Imports only the reduce part of functools, as the question specifies.
    return reduce(lambda x, y: x + ([y] if y != i else []), l, [])
    
    

# END ANSWER TO Question 7
################################################################################


##########################################################
# Question 8

"""
The *Sudan* function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

"""
From the definiton of Sudan's function, I extrapolated the following.
"""
def sudan(n, x, y):
  if n==0:
    return x + y
  elif y==0:
    return x
  else: #Called if n or y are both greater than 0.
    return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)


# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""

"""
    High level languages are those in which there is a strong abstraction from the details of the computer (BBC). 
This means the code itself is closer to human language than it is to binary (at least more so than a language such as 
assembly, which is a low level language). 

    Python is a very high level language. This high abstraction from binary is what makes it so appealing to write in. 
Because of this, It's not a verbose language, meaning it's fast and efficient to write code in (Pulumi). It's also
more straightforward than a language like Haskell, despite being a lower level language than it. It's also much 
easier to learn than a low level language, or even a high level language like Java because of its closeness to English.

    These factors make it a fantastic language for those in industries such as Web Development, Data Science, and
Education to use. Because of the large number of people interested in writing in Python, there is a huge supportive
and active community that creates modules that anyone can use (Great Learning). These modules make it easier to write in 
Python, leading even more people to want to write in it. This, in turn, makes it very popular for the educational industry 
to use it. It's a positive feedback loop. Those in Web Development, Data Science and more love access to these modules as
well.

    Python does have its issues, though. Due to having high abstraction from binary, it has less control over the actual
processes of the computer. This means it takes up more resources to run a program with the same function in Python over
a lower level language. 

    In the future, Python has nowhere to go but up. Because of how easy it is for beginners to learn, and hence its
popularity in the education industry, 40% of Python developers are between the ages of 21 and 29 (Finextra). This generation
of Python developers are just entering university and having Python grilled into them just as hard if not harder than
the previous ones(Finextra). Because of the simplicity of Python as well as the massive assortment of modules that the 
general public have access to, many of these students will become developers with Python as their primary language. 
In short, Python is big and it's not going anywhere any time soon.

Sources:

BBC. “Types of Programming Language - AQA - Revision 1 - GCSE Computer Science - BBC Bitesize.” BBC Bitesize, 2020, 
www.bbc.co.uk/bitesize/guides/z4cck2p/revision/1.

Finextra, “Python: The Programming and Development Language of the Future.” Finextra Research, 14 Dec. 2021, 
www.finextra.com/blogposting/21401/python-the-programming-and-development-language-of-the-future. Accessed 24 Oct. 2022.

Pulumi, “Why Is Python so Popular?” Pulumi, 
www.pulumi.com/why-is-python-so-popular/#:~:text=Python%20is%20easy%20to%20learn&text=It%20uses%20a%20simplified%20syntax. 
Accessed 24 Oct. 2022.

Team, Great Learning. “Top 10 Uses of Python in Real World with Examples.” GreatLearning Blog: Free Resources What Matters
to Shape Your Career!, 17 Feb. 2021, www.mygreatlearning.com/blog/top-uses-of-python-in-real-world-with-examples/.
"""


# END ANSWER TO Question 9 
###############################################################################


###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""

"""
a. The difference between ([],[],[]) and [[]]*3 is that although both have the same output, the objects
they contain are very different in nature. In the former, if you were to change, say, the first list in
in the tuple by appending an element to it, only the first element (list) in the tuple would change. 
That is because each list in the tuple holds a different space in memory.
In the second example, if you were to modify the first element in the list the same way you would have
in the first example, it would change every single element in the list. This is because all of the nested
lists point to the exact point of data because all "[[]]*3" does is return three pointers to the exact same
object.
"""

"""
b. All that happens here is that x points to itself. The only change in memory when append() is called is that it points to
itself instead of an empty list. The reason why it doesn't eat more and more memory, filling with a functionally
infinite amount of nested lists is because it doesn't actually create a list for every list inside of x. It only points
back to itself.
"""

# END ANSWER TO Question 10
###############################################################################

###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
"""
This function takes a number, turns it into a string, and then takes each element of said string, 
maps them to a list, and then turns all elements of the list and turns them into an integer.
It then takes that list and reverses it. If that list contains one zero and nothing else,
it is turned into an empty list.
"""
def iint(n):
    intList = list(map(int, str(n)))
    revIntList = list(reversed(intList))
    if revIntList == [0]:
        revIntList = []
    return revIntList

# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
"""
This function takes a list of digits, reverses it, and for each element in the list, adds it to a string. 
It has to be reversed because the infinite precision lists are reversed versions of their matching numbers.
The string is then converted to an int and then returned.
"""
def pint(list):
    stringNumber = ""
    i = 0
    if len(list) == 0: #returns 0 if the list is empty.
        return 0;
    for i in reversed(range(len(list))):
        stringNumber += str(list[i])
    return int(stringNumber)

# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
"""
The following method takes 2 lists of integers and adds one of them to the other, and puts all sums on an element
by element basis into a third list, which it then returns.
"""
def iadd(I,J):
    
    
    sum = []
    carry = False #No need to carry over before checks have been made so it's set to 0 by default.
    
    #The loop will run for as many iterations as the largest number it is adding otherwise half the number
    #could be truncated if it was done with the length of I or J. Remember, both numbers don't have to be
    #the same length to be added.
    for i in range(max(len(I), len(J))):
        Ival = 0
        Jval = 0
        
        #If an empty list is calculated on, it will break the program. This code sets all empty lists to
        #Holding a single element: integer 0.
        if I[i] == []: I[i] = [0]
        if J[i] == []: J[i] = [0]
        
        #This needs to be specified because as the loop is going over whichever list is longest. If I made
        #Ival or Jval equal to the current element of I or J, that element could not exist and crash the program.
        #Thus, if that element does not exist, Ival or Jval would be set to 0 if all of I's or J's numbers have
        #already been added to each other.
        if i < len(I):
            Ival = I[i]
        else:
            Ival = 0
            
        if i < len(J):
            Jval = J[i]
        else:
            Jval = 0  
        
        #If there was a carry from the previous iteration, it's added to the current element,
        #and then the carry value is set to False to show that there is no longer a value to carry.
        if carry == True:
            Ival += 1
            carry = False
        
        #If the sum of the current values is greater than 9, they will need more than one element in
        #the list to represent. Thus, carry is set to true. Ival also has 10 taken away from it so the sum's
        #current element represents the number after a carryover has been applied to it.
        if Ival + Jval > 9:
            carry = True
            Ival -= 10
            
        sum.append(Ival + Jval)
        
    #If the final iteration of the while loop set carry to be true, the sum list is made one element
    #longer to represent the number becoming one digit longer.
    if carry == True:
        sum.append(1)
        
    return sum

# multiply two infinite integers
# e.g. imult([], [5])= []
"""
As multiplication is repeated addition, iadd is called on one list for the number of times that the second list
(converted into a number) specifies. For example, if I was [4,2] and J was [9,2] it would add I's elements to itself
[9,2] --> 29 times.
"""
def imult(I,J):
    
    #This (product) is fed into the iadd so that I does not overwrite itself and has somewhere external to write
    #The repeated addition.
    product = [0] #Product is 0 and not an empty list so that adding to it does not crash the program.
    
    for i in range(pint(J)):
        product = iadd(product, I)
    
    return product

# raise I to the power of J
"""
As exponents are repeated multiplication, imult is called on one list for the number of times that the second list
(converted into a number) specifies. For example, if I was [4,2] and J was [9,2] it would multiply I's elements to itself
[9,2] --> 29 times.
"""
def ipow(I,J):
    
    #This (exponent) is fed into the imult so that I does not overwrite itself and has somewhere external to write
    #The repeated multiplication.
    exponent = [1] #Exponent is 1 because if you multiply by 0, you will *always* get 0. The reason it is not an empty list is specified in imult.
    
    for i in range(pint(J)):
        exponent = imult(exponent, I)
    
    return exponent

# END ANSWER TO Question 11 
###############################################################################


###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a *datum*.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this will depend on implementation and on the size of the integer payload!) 
b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the issues involved. 
"""

"""
This method takes either an integer or a list as data. It returns 1 if it's either an integer or an empty list
as the question specifies. If it's a list with one or more elements, it calls the abstractsize method for each element 
in the list recursively, and adds 1 to the abstract memory size of the list for every list and integer inside of the 
original list or sub-lists.
"""
def abstractsize(data):
    if isinstance(data, list) and len(data) > 0: #Does this if given a list with 1 or more elements.
        count = 1
        for i in range(len(data)):
            if isinstance(data[i], list):
                count = count + abstractsize(data[i]) #Adds the number of abstract units in data[i] to the total number of abstract units.
            else:
                count+=1
        return count
    else: #Does this if given an integer or an empty list.
        return 1

"""
This method takes either an integer or a list as data. If the data is an integer, it remains untouched. If it's an empty list,
it is deleted (and removed from its parent list if it is in one). If it is a list with one element, it is taken out of that list.
If it is still in a list, it is taken out of that one too (recursively). If it is a list with 2 or more elements, it shall not be 
deleted but the elements inside of it will still be subject to change.
"""
def compress(data):
    if isinstance(data, list): #Does this if the data is a list.
        i = 0;
        while i < len(data): #I used a while loop because it allowed me to choose whether I wanted to iterate to the next I or not.
            if isinstance(data[i], list) and len(data[i]) == 0:
                del(data[i])
            elif isinstance(data[i], list) and len(data[i]) == 1: #Does this if the element is a list and has an element that is a list.
                data[i] = data[i][0] #Assigns the element inside of the list to be the element itself.
                compress(data[i]) #After the element has been taken out of its list "shell" it is checked again to see if it is an empty list or an integer.
            else:
                i+=1
    #Does this if data is either an integer or the while loop and all the recursion inside of it has been completed.
    return data
            

# END ANSWER TO Question 12 
###############################################################################

###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""
"""
This code assigns the anonymous function that returns true if x = 23 to the variable equals23.
"""
equals23 = lambda x: x == 23

# END ANSWER TO Question 13 
###############################################################################