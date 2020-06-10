'''
5 key differences to know between Python 2.7.x vs 3.x, plus one important backward compatibility
    1) The print keyword in python2 must be now converted into function print()
    2) The division operator  "/"  does not cast the quotient into INT (7/2 = 3), but instead it returns a float (7/2 = 3.5)
    3) The functionality of xrange() in V2 is now implemented by range() in V3
    4) Error Handling. the keyword "as" is instead of "," in the except (catch) syntax.
    5) Default/Implicit string type from ASCII to Unicode

    6) _future_module may be used in python 2 as backward compatibility to help use modules from python 3

'''
from __future__ import division
import sys
'''
 1) print keyword in python2 must be now converted into function print()
'''

# Will work in both versions 2 and 3
print("I am using the version", sys.version)

# Will only work in version 2.
#print "I am using the version", sys.version


'''
2) The division operator  "/"  does not cast the quotient into INT (7/2 = 3), 
  but instead it returns a float (7/2 = 3.5)
'''
x = 7/2

print("division integer or float", x)


'''
 3) The functionality of xrange() in V2 is now implemented by range() in V3
 Let's print the first 10 square numbers
'''

# will work in both v2 and v3. the function range() exist in
lists = [i*i for i in range(10)]
print(lists)

# will work in v2 only. xrange does not exist in v3
#lists = [i*i for i in xrange(10)]
#print(lists)


'''
 4) Error Handling. the keyword "as" is instead of "," in the except (catch) clause.
 Let's handle the exception for the  undefined function "not_defined_funct"
'''

# Will only work in both V2 and V3  using the "as" instead "," in the except clause
try:
    x = not_defined_funct(y)
except Exception as ex:
    print(ex.__str__())

# Will only work in V2 using the "," instead "as"  in the except clause


'''
5) Default/Implicit string type from ASCII to Unicode
printing the type of the variable my_name: will be string in V2 as there is no difference between byte and string. 
in the other hand, the type will be byte in V3.
'''
my_name = b'Pierre Mathieu'
print(type(my_name))





'''
6) _future_module may be used in python 2 as backward compatibility to help use modules from python 3
This will let us use the division that will return a float instead of the integer part, using V2.
'''

x = 7/2
print("division integer or float", x)  # This will return 3.5 in V2