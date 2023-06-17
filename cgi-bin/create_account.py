#!/usr/bin/python3

import cgi
import os
from hashlib import sha256

datapath = "userdata/"

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

#0 = success
#1 = user exists
#2 = passwords do not match
def createAccount(credentials):
    if os.path.exists(datapath + credentials[0]):
        return 1
    if credentials[1] != credentials[2]:
        return 2
    os.mkdir(datapath + credentials[0], 0o777)
    os.chmod(datapath + credentials[0], 0o777)
    os.mkdir(datapath + credentials[0] + "/files", 0o777)
    os.chmod(datapath + credentials[0] + "/files", 0o777)
    with open(datapath + credentials[0] + "/password_SHA256", "w") as wpath:
        wpath.write(sha256(credentials[1].encode('utf-8')).hexdigest())
        wpath.close()
    return 0

def feedBack(status):
    if (status == 0):
        print('''
            <div class="loginbox">
                <h2>Account Creation Successful!</h2>
                <h3><a href="../pages/login.html">return to login</a> | <a href="../index.html">return home</a><h3>
            </div>
            '''
            )
    elif (status == 1):
         print('''
            <div class="loginbox">
                <h2>User Already Exists!</h2>
                <h3><a href="../pages/create_account.html">return to account creation</a> | <a href="../index.html">return home</a><h3>
            </div>
            '''
            )

    else:
         print('''
            <div class="loginbox">
                <h2>Passwords do not match!</h2>
                <h3><a href="../pages/create_account.html">account creation</a> | <a href="../index.html">return home</a><h3>
            </div>
            '''
            )

if __name__ == "__main__":
    htmlTop()
    feedBack(createAccount(getData()))
    htmlTail()
    


