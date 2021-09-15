doc = input("")
jon = input("")

if doc.count("a")>=0 and doc.count("a")<=999 and jon.count("h")==1 and doc.islower()==True and jon.islower()==True:
    if jon.count("a")<=doc.count("a"):
        print("go")
    elif jon.count("a")>doc.count("a"):
        print("no")
