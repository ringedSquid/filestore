#!/usr/bin/python3

import cgi 
import os
from os import environ

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


def get_cookies():
    if 'HTTP_COOKIE' in environ:
        cookies = environ['HTTP_COOKIE'].split("; ")
        if cookies[0] == '':
            return False
        d = {}
        for i in cookies:
            s = i.split("=")
            d[s[0]] = s[1]
        return d

def delete_files(userdata, files):
    filepath = datapath + userdata["UserID"] + "/files/"
    for i in files:
        os.remove(filepath + i)

def process_input(userdata):
    formData = list(cgi.FieldStorage())
    formData.pop(formData.index("delete"))
    delete_files(userdata, formData)
    print('''
              <div class="loginbox">
                    <h2>Deletion Successful!</h2>
                    <h3><a href="../index.html">home</a> | <a href="file_explorer.py">files</a></h3>

              </div>
              '''
              )

if __name__ == "__main__":
    htmlTop()
    delete_files(get_cookies(), process_input(get_cookies()))
    htmlTail()
    

