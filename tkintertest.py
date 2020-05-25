from sys import argv
from os import makedirs, unlink
from os.path import isdir, exists, dirname, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO


class Retriever:

    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
    
    def filename(self url, deffile = "index.htm"):
        # url path parsing
        parsedurl = urlparse(url, "http:", 0)
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '':
            if newpath[-1] == '/':
                path  = path+deffile
            else :
                path = path + "/" + deffile
        dir = dirname(path)
        if not isdir(dir):
            if exists(dir): unlink(dir)
            makedirs(dir)
        return path