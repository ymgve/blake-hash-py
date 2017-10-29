
----------------------------------
Python C module for Decred hashing 
----------------------------------

Notes for Decred:
----------------

Module: blake_hash

Please see the "test.py" for a testcase

Requirements:
-------------
In order to run P2Pool and other Python based pools with the Decred network, you need to build and install the
'blake_hash' module for Python that includes the Blake-256 proof of work code that Decred uses for hashes.

Linux:

    sudo python setup.py install


Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In cmd type this:

    C:\Python27\python.exe setup.py build --compile=mingw32 install

    - untested

	
Windows (microsoft visual c/c++)
* Open visual studio console for VS 2015

In cmd type this:

    SET VS90COMNTOOLS=%VS140COMNTOOLS%	           # For visual c++ 2015
    C:\Python27\python.exe setup.py install

	Test the install:
	
	C:\Python27\python.exe
	...
	>>>import blake_hash
	>>>help('blake_hash')
	>>>quit()
	
    - tested ok

	
	Test hashing:

	C:\python test.py
	bba2bd849f3f562a11fec065dad26adae8aab3b7a668bb8d39cbca7114cf7177

	- tested ok

