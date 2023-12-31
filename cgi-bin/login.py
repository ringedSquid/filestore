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
            <title>Login status</title>	
            <link rel="stylesheet" href="../style.css">

        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def getData():
    formData = cgi.FieldStorage()
    username = formData.getvalue("username")
    password = formData.getvalue("password")
    print(username, password)
    if (username == None) or (password == None):
        return False 
    credentials = (
            username,
            sha256(password.encode('utf-8')).hexdigest()
            )
    return credentials

#0 = login success
#1 = password incorrect
#2 = username invalid
def verifyLogin(credentials):
    if credentials == False:
        return 3
    if os.path.exists(datapath + credentials[0]):
        file = open(datapath + credentials[0] + "/password_SHA256").read()
        if (file == credentials[1]):
            print("Set-Cookie:UserID = " + credentials[0])
            print("Set-Cookie:Pass = " + credentials[1])
            return 0
        else:
            return 1
    else:
        return 2

def feedBack(status):
    if (status == 0):
        print('''
              <div class="loginbox">
                    <h2>Login Successful!</h2>
                    <h3><a href="file_explorer.py">Continue</a></h3>
              </div>
              '''
              )
    elif (status == 1):
        print('''
              <div class="loginbox">
                    <h2>Incorrect Password!</h2>
                    <h3><a href="../pages/login.html">Back to login</a></h3>
              </div>
              '''
              )
    elif (status == 2):
        print('''
              <div class="loginbox">
                    <h2>Incorrect Username!</h2>
                    <h3><a href="../pages/login.html">Back to login</a></h3>
              </div>
              '''
              )
    elif (status == 3):
        print('''
              <div class="loginbox">
                    <h2>Blank Field Submitted!</h2>
                    <h3><a href="../pages/login.html">Back to login</a></h3>
              </div>
              '''
              )
                
if __name__ == "__main__":
    status = verifyLogin(getData())
    htmlTop()
    feedBack(status)
    htmlTail()



            


