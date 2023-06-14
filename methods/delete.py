import cgi
import os
import shutil

datapath = "../userdata/"

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>Create Account</title>	
            <link rel="stylesheet" href="../style.css">

        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def main():
    deletelist = ["deletetest", "pooptest", "wadawd"]
    for f in deletelist:
        os.chmod(datapath + f, 0o777)
        os.chmod(datapath + f + "/files", 0o777)
    print("KEK")


if __name__ == "__main__":
    htmlTop()
    main()
    htmlTail()


