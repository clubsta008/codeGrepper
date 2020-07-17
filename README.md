# codeGrepper.py
This project is designed to automate the greping of a source code project during a manual source code review.

codeGrepper uses the code base items to scan for potential issues within the code. 
Each item within the code base items file should be in the format <category>:<scan value>. 

If the grep returns a result, the output will be saved under each category.

Usage:

        python codeGrepper.py -h
        -s = Directory to source code. [required]
        -d = Destination directory. Default is the current working directory. [optional]
        -c = Item list to load. (PHP, .NET, Java) Default is PHP. [optional]
