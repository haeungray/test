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