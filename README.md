# Python as a Programming Language

1.High-Level Language: Easy to read and write like English.
2.General Purpose: Suitable for Web Development, AI, ML, Automation, Data Science, etc.
3.Interpreted: Executes code line-by-line without prior compilation.
4.Dynamically Typed: No need to specify veriable types.
5.Object-Oriented: Supports concepts like classes and objects.
6.Extensible and Embeddable: Integrates with C,C++, easily.

# Features of Python

1.Simple and Easy to Learn: Beginner-friendly syntax.
2.Free and Open Source: Available at no cost with a huge community.
3.Portable: Runs on Windows,MacOS, and Linux without modification.
4.Extensive Libraries: Access to NumPy,Pandas,TensorFlow,Scikit-learn,etc.
5.Robust community Support:Millions of developers contribute worldwide.
6.Automatic Memory Management: Garbage collection handled internally.

# History Of Python

1.Creator: Guido van Rossum
2.Start Year: 1989
3.First release: 1991
4.Developed at: Centrum Wiskunde & Informatica(CWI),Netherlands
5.Motivation: To address issues found in ABC language and make programming easy.

# Versions of Python

1.Python 1.x: Initial release(1991)
2.Python 2.x: Improved features(2000),not fully compatible with 3.x
3.Python 3.x: Major changes(2008),modern standard
4.Latest Stable Version(2025): Python 3.12+
Note: Python 2.x support officially ended on January 1, 2020.

# Implementations of Python

1.CPython: Default,written in C language.
2.PyPy: Faster execution using Just-In-Time(JIT) compiler.
3.Jython: Python code exceution on Java Virtual Machine(JVM)
4.IronPython: Python integrated with .NET Framework.
5.MicroPython: Designed for microcontrollers(IoT applications).

##====================================================================##
                     Build Process of Python
##===================================================================##

# PVM (Python Virtual Machine)

1.PVM is the runtime engine of Python.
2.It reads .pyc(compiled bytecode) files and executes them.
3.Provides platform independence.
4.Handle memory allocation,garbage collection, and exception handling.

# Build Process of Python Code

1.Source Code(.pyc):
    Developer writes Python code in a .py file.

2.Lexical Analysis:
    The Python interpreter scans the code and breaks it into tokens.

3.Parsing & AST Generation:
    Tokens are parsed and transformed into an Abstract Syntax Tree(AST).
    Checks for syntax errors during this step.

4.Compilation to Bytecode:
    AST is compiled into Python bytecode(.pyc files).
    Bytecode is platform-independence stored in __pycache__ folder.

5.Execution by PVM:
    The Python Virtual Machine reads the bytecode and executes it line-by-line.
    Handles runtime actions such as memory management,method calls,and control flow.

# Complete Python Toolchain(Execution Flow)

1.Editor/IDE:
    Tools like VS Code,PyCharm,Jupyter Notebooks.
    Used to write and edit .py files.

2.Tokenizer/Lexer:
    Converts code into smaller tokens(identifiers,keywords,literals).

3.Parser:
    Validates the syntax and forms the AST.

4.Bytecode Compiler:
    Converts AST into bytecode.
    Bytecode is a low-level set of instructions understandable by the PVM.

5.Bytecode Storage:
    Stored as .py files in the ___pycache__ directory.

6.Python Virtual Machine(PVM):
    Executes bytecode line-by-line.
    Manages memory,exceptions,object references,and more.

7.Standard Libraries:
    Build-in modules like OS,math,random,etc.are loaded if used.

8.Thired-Party Libraries:
    Installed using pip. Stored in site-packages directory.
    Imported and linked at runtime if present in the script.


##=======================================================================================##
                              Data Types in Python
##======================================================================================##

A data type defines the type of a value and the set of oprations that can be performed on that value.
In simple words, it tells what kind of data a variable can hold,like numbers,text,boolean values,collections,etc.

In Python,everthing is an object,and every object belongs to some class or data type.

# Python is a Dynamically Typed Language
    In Python,you don't need to declare the type of variable while creating it.
    The type is automatically assigned during runtime based on the value assigned.
    You can even change the type of a variable by assigning a new value of different type.

# Dynamic Typing Means:
    Variable type can change any time.
    Type safety is ensured during execution,not while writing code.

# Advantages:
    Easier and faster to write code.
    No need for lengthy type declarations.

# Important Behavior:
    Python checks types at runetime,not at compile-time.
    Variable are just labels pointing to objects, and the object carries the type information, not the variable itself.

# Example:
    x = 10          # x is an integer
    x = "Python"    # Now x is a string

# Variable creation in Python:
    A variable is a name that refers to a location in memory where data is stored.
    It acts as a container to store values.

# Data Types in Python:
    Type                           Name                                Example

    int                            Integer                             x = 11
    float                          Floating number                     pi = 3.14
    bool                           Boolean                       is_active = True
    str                            String                          name = "Python"
    list                           List                         Batches = ["PPA","LB"]
    tuple                          Tuple                         Fees  = (21000,22000)
    dict                           Directonary                   person = {"name":"Vishal", "age":34}
    set                            Set                           numbers = {1,2,3,4,5}
    complex                        Complex number                      z = 5 + 6j
    NoneType                       None value                       value = None

# Variable creation in Python:
    # creating variables
    a = 10
    b = 3.14
    c = "Jay Ganesh"
    d = True

    # Multiple assignments
    x,y,z = 1,2,3

# Functions to Check Data Type of a Variable

    type() Function:

    Used to find the data type of any variable.

    x = 101
    print(type(x))          # <class 'int'>

    y = "Marvellous"
    print(type(y))          # <class  'str'>

# Function to Check Size of Variable in Memory:

    sys.getsizeof() function:

    Syntax:

    import sys
    sys.getsizeof(variable_name)

    Example:
    import sys

    x = 11
    print(sys.getsizeof(x)          # 28 bytes

# Size of Different Data Types:

    Data Type                      Example                       Size(Bytes)
    
    


