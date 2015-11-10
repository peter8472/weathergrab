#! /usr/bin/python
"""radargrab
Get the images and backgrounds associated with a storm event and save them to
a directory or something
"""
import urllib2
import httplib
import time
from xml.dom import minidom
from HTMLParser import HTMLParser
_n0r = "http://radar.weather.gov/ridge/RadarImg/N0R/%s/"
_overlay  = "http://radar.weather.gov/ridge/Overlays/"
class Urlgen(object):
    def __init__(self, site):
        self.n0r = _n0r % (site)

class my_parser(HTMLParser):
    def ready(self):
        self.linkray = []
        
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for i in attrs:
                if i[0] == "href":
                    if i[1].startswith("DAX"):
                        self.linkray.append(i[1])

    def nextlink(self):
        for i in self.linkray:
            yield i
if __name__ == "__main__":
    a =  Urlgen("DAX")
    #blah = urllib2.urlopen(a.n0r)
    g = blah.read()
    myht = my_parser()
    myht.ready()
    myht.feed(g)
    for i in myht.nextlink():
        time.sleep(1)
        pic = urllib2.urlopen(a.n0r+i)
        # with open(i,'w') as f:   CLOBBERS FILES.  FIX THIS BEFORE USING
          #  f.write(pic.read())
    
    
