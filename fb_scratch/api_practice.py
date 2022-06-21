#%%
'''This is to serve as a tutorial to help you to think about
working with APIs. This tutorial is geared to people who work in 
VSCode but the same principles apply to any other IDE or project.
'''

#%%
'''
First, we need to get some packages to access the variables that
will be made. 
'''
import requests
import json
from dotenv import load_dotenv
import os
'''
These packages will usually be used when working with APIs. 
The main package that will be used to access our API keys will be
the os package. 

If you don't have these packages already downloaded, I would 
recommed doing a pip install to install these packages. 
'''
#%%
'''
The second thing is to store the API key(s) itself. In your file
system, go ahead and make a .env file. It is important to not 
name it anything. You can either make this file outside of the 
folder that is in git or add the name of the file to the .gitignore
file. 

Inside the .env file write the following:

myapi=copy_and_paste_your_API_key_here

You don't need quotes to indicate that it is a string. 
'''
#%%
'''
The last step is to actually refer to the variable. 
You do this by doing the following.
'''
load_dotenv()
lt_token = os.getenv('myapi')
'''
Line 43 goes and looks for the .env file that you just made. 
Line 44 saves the name that you gave to the key to a variable 
in your code.  
'''