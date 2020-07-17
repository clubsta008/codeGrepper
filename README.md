codeGrepper.py - Automates the greping of a source code project.
Uses the code base items to scan for potential issues within the code. Each item within this file should be in the format <category>:<scan value>. If the grep returns a result, the output will be saved under each category.
        -h = prints this usage
        -s = Directory to source code. [required]
        -d = Destination directory [optional]. Default is the current working directory
        -c = Item list to load. (PHP, .NET, Java) Default is PHP. [optional]
