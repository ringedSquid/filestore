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
            <title>Login status</title>	
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
            return 0
        else:
            return 1
    else:
        return 2

def feedBack(status):
    if (status == 0):
        print('''
              <div class="loginsuccessbox">
                    <h2>Login Successful!</h2>
                    <a href="">Continue</a>
              </div>
              '''
              )
    elif (status == 1):
        print('''
              <div class="loginfailbox">
                    <h2>Incorrect Password!</h2>
                    <a href="../index.html">Back to login</a>
              </div>
              '''
              )
    else:
        print('''
              <div class="loginfailbox">
                    <h2>Incorrect Username!</h2>
                    <a href="../index.html">Back to login</a>
              </div>
              '''
              )
                
if __name__ == "__main__":
    htmlTop()
    feedBack(verifyLogin(getData()))
    htmlTail()



            


