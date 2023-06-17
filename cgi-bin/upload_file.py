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

def save_files(userdata, files): 
    filepath = datapath + userdata["UserID"] + "/files/" 
    if (isinstance(files, list)):
        for i in files: 
            name = os.path.basename(i.filename) 
            with open(filepath + name, 'wb') as wpath:
                wpath.write(i.file.read())
                wpath.close()
    else:
        name = os.path.basename(files.filename)
        with open(filepath + name, 'wb') as wpath:
            wpath.write(files.file.read())
            wpath.close()


def process_input(userdata):
    formData = cgi.FieldStorage()['files']
    save_files(userdata, formData)
    print('''
              <div class="loginbox">
                    <h2>Upload Successful!</h2>
                    <h3><a href="../index.html">home</a> | <a href="file_explorer.py">files</a></h3>

              </div>
              '''
              )


if __name__ == "__main__":
    htmlTop()
    process_input(get_cookies())
    htmlTail()
 
