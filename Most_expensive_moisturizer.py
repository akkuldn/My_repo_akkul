"""
 Program to add most expensive item from moisturizer page into the cart
"""
from slenium import webdriver
driver.get("https://weathershoppers.pythonanywhere.com")
#go and change the program
#You have to install the mergetool
#Refer the below options to do the mergetool
#Here is the updated steps to follow to setup with kdiff3 on Windows
"""- Download the kdiff3 file --
https://sourceforge.net/projects/kdiff3/files/kdiff3/
- Copy the followinf Block to .gitconfig file
``
[merge]
tool = kdiff3
[mergetool "kdiff3"]
path = C:/Program Files/KDiff3/kdiff3.exe
trustExitCode = false
[diff]
guitool = kdiff3
[difftool "kdiff3"]
path = C:/Program Files/KDiff3/kdiff3.exe
trustExitCode = false

``
- Use git mergetool to launch kdiff3 when there is merge conflict"""

"""
Download kdiff3: http://sourceforge.net/projects/kdiff3/files/latest/download?source=files
Copy the path where you installed kdiff
Add these lines to your .gitconfig (usually in your home directory)
[merge]
     tool = kdiff3
[mergetool "kdiff3"]
     path = PATH_TO_KDiff3/kdiff3.exe
[diff]
     tool = kdiff3
     guitool = kdiff3
[difftool "kdiff3"]
     path = PATH_TO_KDiff3/kdiff3.exe
     """