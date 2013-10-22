
import json

import os

from datetime import datetime

from PIL import Image


class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self, title, subtitle, creator, publication_date):

        self.title = title
        
        self.subtitle = subtitle
        
        self.creator =creator
        
        self.publication_date = publication_date

    def show():

        print '{0}:{1}\n{2}'.format(self.title,self.subtitle, self.content)


    def matches_url(url):

        pattern = r'http://thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/([\w-]+)/'

        return re.search(pattern, url)


class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''

    def __init__(self, title, subtitle, creator, publication_date, related_image= None):

        super(Article,self).__init__(self, title, subtitle, creator, publication_date)

        self.related_image = related_image

    def show():

        super(Article,self).show()

        if self.related_image:

            self.related_image.show()

  

class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''

    def __init__(self,title, subtitle, creator, publication_date, image_file):

        super(Picture, self).__init__()

        self.image_file = image_file
    def show():

        if self.image_file:

            Img.open(self.image_file).show()




'''
Question 1e
'''
def from_url(c_lst, url):


    pattern = r'http://thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/([\w-]+)/'

    Type = None

    year = None

    month = None

    year = None

    slug = None

    match = re.search(pattern, url)

    if match:

        Type = match.groups()[0]

        year = int(match.groups()[1])

        month = int(match.groups()[2])

        day = int(match.groups()[3])

        slug = match.groups()[4]

        sl = Slug.split('-')

        Slug = ''

        for (s in sl):

            slug = slug + s + ' '
        slug = slug[:a.__len__()-1]  #here the slug is equal to a title


    for (c in c_list):

        Date = c.publication_date

        if type(c) == Type && year == Date.year && month = Date.month && day = Date.day:

            return c

        return None
        
 
'''
Question 1e
'''
def posted_after(c_lst, dt):

    return {c for c in c_list if c > dt}
