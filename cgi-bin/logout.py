#!/usr/bin/python3

import cgi 
import os
from os import environ

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


def del_cookies():
    if 'HTTP_COOKIE' in environ:
        cookies = environ['HTTP_COOKIE'].split("; ")
        if cookies[0] == '':
            return False
        for i in cookies:
            print("Set-Cookie:" + i.split("=")[0] + "= deleted")
        return True

def process_output(state):
    if state == False:
        print('''
              <div class="loginbox">
                    <h2>Logout Unsuccessful!</h2>
                    <h3><a href="../index.html">home</a> | <a href="../pages/login.html">login</a></h3>

              </div>
              '''
              )
    if state == True:
        print('''
              <div class="loginbox">
                    <h2>Logout Successful!</h2>
                    <h3><a href="../index.html">home</a> | <a href="../pages/login.html">login</a></h3>

              </div>
              '''
              )
 

 

if __name__ == "__main__":
    state = del_cookies()
    htmlTop()
    process_output(state)
    htmlTail()


