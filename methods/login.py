#!/usr/bin/python3

import cgi
import os
from hashlib import sha256

datapath = "../userdata/"

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title>My first server-side script. </title>	
            <link rel="stylesheet" href="../style.css">

        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def getData():
    formData = cgi.FieldStorage()
    credentials = (
            formData.getvalue("username"),
            sha256((formData.getvalue("password")).encode('utf-8')).hexdigest()
            )
    return credentials

#0 = login success
#1 = password incorrect
#2 = username invalid
def verifyLogin(credentials):
    if os.path.exists(datapath + credentials[0]):
        file = open(datapath + credentials[0] + "/password_SHA256").read()
        if (file == credentials[1]):
            print("<h1>Login successful, welcome " + credentials[0] + "!</h1>")
        else:
            print("<h1>Incorrect password!</h1>")
    else:
        print("<h1>Invalid username!</h1>")

if __name__ == "__main__":
    htmlTop()
    verifyLogin(getData())
    htmlTail()



            


