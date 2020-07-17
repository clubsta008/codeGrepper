#!/usr/bin/python
import os
import sys
import getopt
import subprocess

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def usage():
    print('codeGrepper.py - Automates the greping of a source code project. '\
        '\nUses the code base items to scan for potential issues within the code.'\
        ' Each item within this file should be in the format <category>:<scan value>.'\
        ' If the grep returns a result, the output will be saved under each category.'\
        '\n\t-h = prints this usage\n\t-s = Directory to source code. [required]\n\t'\
        '-d = Destination directory [optional]. Default is the current working directory'\
        '\n\t-c = Item list to load. (PHP, .NET, Java) Default is PHP. [optional]')

def main(argv):
    dstBase = os.getcwd()
    sourceDir = ''
    codeBase = 'PHP'
    itemsName = 'phpItems.txt'

    try:
        opts, args = getopt.getopt(argv,"hd::s:c:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-d':
            dstBase = arg
        elif opt == '-s':
            sourceDir = arg
        elif opt == '-c':
            codeBase = arg
    
    if codeBase.lower() == '.net': 
        itemsName = 'dotnetItems.txt'
    elif codeBase.lower() == 'java':
        itemsName = 'javaItems.txt'

    if sourceDir == '':
        print(bcolours.FAIL + 'Source code directory is required' + bcolours.ENDC)
        usage()
        sys.exit(2)
    
    if not os.path.isdir(sourceDir):
        print(bcolours.FAIL + 'Invalid source code directory' + bcolours.ENDC)
        usage()
        sys.exit(2)

    if not os.path.exists(dstBase):
        os.mkdir(dstBase)
    elif not os.path.isdir(dstBase):
        print(bcolours.FAIL + 'Invalid destination directory specified. Must be a directory' + bcolors.ENDC)
        usage()
        sys.exit(2)
    
    if dstBase[len(dstBase)-1:] != '/':
        dstBase += '/'
    
    with open(itemsName, 'r') as scanItems:
        for scan in scanItems:
            try:
                category, item = scan[:-1].split(':')
            except ValueError as e:
                print(bcolours.FAIL + 'Error reading line: "%s". Error message: %s. Check formatting.' % (scan[:-1], e) + bcolours.ENDC)
                continue
            if not os.path.exists(dstBase + category):
                os.mkdir(dstBase + category)
            
            print('Grepping for %s under %s category' % (item, category))
            command = ['grep', '-rnsi', item, sourceDir]
            proc = subprocess.Popen(command, stdout=subprocess.PIPE)
            res = proc.stdout.readlines()
            if len(res) > 0:
                print(bcolours.OKGREEN + '\tResults found. Writing to file' + bcolours.ENDC)
                with open(dstBase + category + '/' + item.replace('*,',''), 'wb') as out:
                    for i in res:
                        out.write(i)
            else:
                print(bcolours.OKBLUE + '\tNo results found' + bcolours.ENDC)

if __name__ == "__main__":
    main(sys.argv[1:])