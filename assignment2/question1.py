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


    def matches_url():

        pass



class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''

    def __init__(self, title, subtitle, creator, publication_date, related_image= NONE):

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


    pass

'''
Question 1e
'''
def from_url(c_lst, url):
    pass

'''
Question 1e
'''
def posted_after(c_lst, dt):
    return {c for c in c_list if c > dt}
