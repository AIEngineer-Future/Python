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
    


