#!/usr/bin/python

#========================================================================
#      Copyright 2010 asciimoo <asciimoo@gmail.com> 
#       Licensed under the GNU Affero General Public License v3
#========================================================================

#========================================================================
#  Modified from code originally written by
#    Raja <rajajs@gmail.com> - Copyright 2007 
#      This program is free software; you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation; either version 2 of the License, or
#      (at your option) any later version.
#==========================================================================
## ======================================================================
## Modified from code originally written by Baishampayan Ghose
## Copyright (C) 2006 Baishampayan Ghose <b.ghose@ubuntu.com>
## ======================================================================
 
import urllib2, base64
import feedparser
 
##################   Edit here      #######################

# !! use HTTP|S! !!
URL = "https://mail.google.com/gmail/feed/atom"

LEDD_PIPE='/var/run/ledd-pipe'

ANIMATION='anim NCS 200 nCS 200 NcS 200 NCs 200 NcS 200 nCS 200 NCS 200 NCS 400 nCS 200 NcS 200 NCs 200 NcS 200 nCS 200 NCS 200 NCS 400 ncs\n' # see man ledd
 
 
USERNAME = ''
PASSWORD = ''                            # pwd stored in script
 
###########################################################
 
def GmailRSSOpener(username, password):
    '''Logs on with stored password and username
       Password is stored in a hidden file in the home folder'''
    base64string = base64.encodestring('%s:%s' % (username,password)).strip()
    req = urllib2.Request( URL )
    req.add_header("Authorization", "Basic %s" % base64string)
    try:
        resp = urllib2.urlopen( req )
        #print '-=: Successfull login to %s :=-\n\t\tuser: %s\n\t\tpassword: %s\n' % (url, username, password)
    except:
        pass

    return resp.read()
 
 
def showmail(feed):
    '''Parse the Atom feed and send signal to leds'''
    atom = feedparser.parse(feed)
    newmails = len(atom.entries)
    if newmails > 0:
        p = open(LEDD_PIPE, 'w')
        p.write(ANIMATION)
        p.close()

    # print the title with formatting
 
if __name__ == "__main__":
    showmail(GmailRSSOpener(USERNAME, PASSWORD))
