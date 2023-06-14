"""
in python there is a more straight forward way of "using"
another code inside your owns. this is done by using "imports"

using the syntax below you can bring in the definitions (functions,
classes, variables, etc.) from another python file/library to your
own code, as if they were defined here:
|
|   import <name of file/library>
|
note that in case of importing a file, the ".py" filename extension
must NOT be included. 

any python file/library is called a module; which is essentially 
a collection of definitions and statements that are grouped together 
under a name. this name is either the file name(for single-file modules)
or the containing folder name (for multi-file modules)

with that knowlege, do the previous task again. but this time, use 
import instead of copying the code by hand.

also it is worth mentioning the use of these lines of code that you
may have noticed in the previoud tasks:
|
|   if __name__ == "__main__":
|       main()
|
as you already know, the python interpretter reads the code line by
line and from the top to bottom, saving every definition and 
executing every statement. in all of the previous codes examples,
these lines were the first ever statements to be executed. this is
useful for when you want to write a python module that is both a 
PROGRAM and a LIBRARY. in this case p5.py is one such module. 
you can either run the module directly, or import it into another
one. the __name__ variable is evaluated at run-time by the 
interpretter (and as a rule of thumb, the rest of the variables/functions 
that are of the form __******__ ). __name__ specifically, is the name of 
the current module. but, for the module that has been called directly
(for example in this case its p7.py), __name__ is evaluated to
"__main__", for the moudles that are imported, it valuates to the 
module name(in this case that would be p5.py, so __name__ variable 
evaluates to "p5"). so the two lines above make sure that the main
function for every module, is called only when we are calling it
directly.
"""

# < fill in here
