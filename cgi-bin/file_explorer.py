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
            <title>File Explorer</title>	
            <link rel="stylesheet" href="../style.css">

        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')


def get_cookies():
    if 'HTTP_COOKIE' in environ:
        cookies = environ['HTTP_COOKIE'].split("; ")
        if cookies[0] == '' or cookies[0].split("=")[1] == 'deleted':
            return False
        d = {}
        for i in cookies:
            s = i.split("=")
            d[s[0]] = s[1]
        return d

def display_files(userdata):
    if userdata == False:
        print('''
              <div class="loginbox">
                    <h2>Not Logged In!</h2>
                    <h3><a href="../pages/login.html">login</a> | <a href="../index.html">home</a></h3>
              </div>
              '''
              )
    else:
        print('''
              <div class="filebox">
                    <form method="post" action="remove.py">
                    <div class="filelist">
                    <h3>Your Files:</h3>
              '''
              )
        userpath = datapath + userdata["UserID"] + "/files/"
        filepath = "../" + datapath + str(userdata["UserID"]) + "/files/"
        for file in os.listdir(userpath):
            print('''
                  <input type="checkbox" name="{0}" value="on"/> <a href="{1}{0}" download>{0}</a>
                  </br>
                  '''.format(file, filepath)
                  )
        print('''
              </div>
              <div class="buttonbox">
              <h3>Actions:</h3>
              <input type="submit" class="deletebutton" value="delete selected" name="delete"/>
              </form>
              <form enctype="multipart/form-data" action="upload_file.py" method="post">
              <h3>Select Files:</h3>
              <input type="file" id="files" name="files" class="selectbutton" multiple>
              <input type="submit" class="uploadbutton">
              </br>
              <h3><a href="../index.html">return home</a> | <a href="logout.py">logout</a></h3>
              </div>
              </div>
              '''
              )


    

if __name__ == "__main__":
    htmlTop()
    display_files(get_cookies())
    htmlTail()



