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
            <title>Create Account</title>	
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
            formData.getvalue("password"),
            formData.getvalue("conpassword")
            )
    return credentials

def createAccount(credentials):
    if os.path.exists(datapath + credentials[0]):
        print("<h1>User already exists!</h1>")
        return
    if credentials[1] != credentials[2]:
        print("<h1>Passwords do not match!</h1>")
        return
    os.mkdir(datapath + credentials[0], 0o777)
    os.chmod(datapath + credentials[0], 0o777)
    os.mkdir(datapath + credentials[0] + "/files", 0o777)
    os.chmod(datapath + credentials[0] + "/files", 0o777)
    with open(datapath + credentials[0] + "/password_SHA256", "w") as wpath:
        wpath.write(sha256(credentials[1].encode('utf-8')).hexdigest())
        wpath.close()
    print("<h1>Account creation successful!</h1>")

if __name__ == "__main__":
    htmlTop()
    createAccount(getData())
    htmlTail()
    


