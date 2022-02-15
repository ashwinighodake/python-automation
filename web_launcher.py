from sys import *
import webbrowser
import re
from urllib.request import urlopen

def is_connected():
    try:
        urlopen("http://www.google.com/")
        return True
    except:
        return False

    url=re.findall('http[s]?://([a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
def Find(string):
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url=Find(line)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("Application name:"+argv[0])

    if(len(argv)!=2):
        print("ERROR:Invalid number arguments")
        exit()
    
    if(argv[1]=="-h") or (argv[1]=="-H"):
        print()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage: Application_name Name_of_file")
        exit()
    
    try:
        connected=is_connected()
        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect internet...")

    except ValueError:
        print("ERROR:Invalid datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)

if __name__=="__main__":
    main()
        