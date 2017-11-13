'''
Created on Nov 13, 2017

@author: ymarwah001
'''
from google.appengine.ext import ndb


class Model1(ndb.Model):
    '''
    classdocs
    '''
    
    col1 = ndb.IntegerProperty()
    col2 = ndb.StringProperty()
        