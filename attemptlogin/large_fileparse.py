#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
posts=0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            z=line.split()
            print(z[-1])
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif " - - - - -] POST" in line:
            posts+=1

print("The number of failed log in attempts is", loginfail)
print("the number of posts requests are", posts)
