#!/usr/bin/python

from ntlm import HTTPNtlmAuthHandler # pip install python-ntlm
import urllib2
import re

# use full url to sharepoint document library
url = "https://mysharepointsite.com/sites/jdoe/Shared%20Documents/Forms/AllItems.aspx"
username = 'corp\\jdoe' # domain\\user
password = 'mypassword'
localdir = "~\\" # add escape characters where needed

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, username, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# create and install the opener
opener = urllib2.build_opener(auth_NTLM)
urllib2.install_opener(opener)

# retrieve the result
data = (urllib2.urlopen(url)).read()
#f = open('html.txt', 'w')
#f.write(data.read())
#f.close()
#print(data.read())

# Create required string variables
site = "/".join((url.split('/'))[0:3])
pattern = "/".join((url.split('/'))[3:]).replace("%20", ' ')
data = data.replace(pattern, "") 
pattern = "href=\"/" + pattern.replace("Forms/AllItems.aspx", '') + "[\w\s\-.]+"

# Parse html source for SP documents
match = re.findall(pattern, data)

# Downloading all files from SharePoint
for line in match:
    downloadurl = site + line.replace("href=\"", "")
    localfile = localdir + (line.split("/"))[-1]
    print localfile
#    print(site + line)
#    curl -k --ntlm -u domain\\username:password -o filename  downloadurl

myfile.close()
