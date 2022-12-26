# QnA : [Python Interview Questions](https://www.edureka.co/blog/interview-questions/python-interview-questions/)

---------------------------

    What is JWT token?
    
    JSON Web Token is an open industry standard used to share information between 
    two entities, usually a client (like your app's frontend) and a server 
    (your app's backend). 
    They contain JSON objects which have the information that needs to be shared.

-----------------------------------

    Quotes API
    
    An API is a pre-arranged template of coding instructions that a third-party 
    app can use to perform some sort of function. 
    In particular, a quote API is a massive database of quotes.
    
---------------------

    What is pep 8?

    PEP stands for Python Enhancement Proposal. 
    It is a set of rules that specify how to format Python code for maximum readability.
    
----------------------------

    What are Python namespaces?

    A namespace in python refers to the name which is assigned to each object in python. 
    The objects are variables and functions. 
    As each object is created, its name along with space (the address of the outer 
    function in which the object is), gets created. 
    The namespaces are maintained in python like a dictionary where the 
    key is the namespace and value is the address of the object. 
    
    There 4 types of namespace in python:

    - Built-in namespace– These namespaces contain all the built-in objects in 
      python and are available whenever python is running.
    - Global namespace– These are namespaces for all the objects created at the level of the main program.
    - Enclosing namespaces– These namespaces are at the higher level or outer function.
    - Local namespaces– These namespaces are at the local or inner function.

-------------------------------

    What is the difference between .py and .pyc files?

    The .py files are the python source code files. 
    While the .pyc files contain the bytecode of the python files. 
    .pyc files are created when the code is imported from some other source. 
    The interpreter converts the source .py files to .pyc files which helps by saving time.

-----------------------------

    What are Literals in Python and explain about different Literals

    A literal in python source code represents a fixed value for primitive data types. 
    There are 5 types of literals in python-

        String literals–
        A string literal is created by assigning some text enclosed in single or double quotes to a variable. 
        To create multiline literals, assign the multiline text enclosed in triple quotes. Eg.name=”Tanya”

        A character literal– 
        It is created by assigning a single character enclosed in double quotes. Eg. a=’t’

        Numeric literals- 
        It include numeric values that can be either integer, floating point value, or a complex number. Eg. a=50

        Boolean literals– 
        These can be 2 values- either True or False.

        Literal Collections– 
            These are of 4 types-

            a) List collections-Eg. a=[1,2,3,’Amit’]
            b) Tuple literals- Eg. a=(5,6,7,8)
            c) Dictionary literals- Eg. dict={1: ’apple’, 2: ’mango, 3: ’banana’}
            d) Set literals- Eg. {“Tanya”, “Rohit”, “Mohan”}

    Special literal- Python has 1 special literal None which is used to return a null variable.

------------------------------------

    How is memory managed in Python?

    Memory is managed in Python in the following ways:

        Memory management in python is managed by Python private heap space. 
        All Python objects and data structures are located in a private heap. 

        The programmer does not have access to this private heap. 
        The python interpreter takes care of this instead.

        The allocation of heap space for Python objects is done by Python’s memory manager. 
        The core API gives access to some tools for the programmer to code.

        Python also has an inbuilt garbage collector, which recycles all the 
        unused memory and so that it can be made available to the heap space.

----------------------------------

    What is the property decorator in Python?

    The @property is a built-in decorator for the property() function in Python. 
    It is used to give "special" functionality to certain methods to make them act as 
    getters, setters, or deleters when we define properties in a class.
