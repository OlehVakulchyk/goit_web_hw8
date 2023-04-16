from mongoengine import *

import connect

# connect(host="mongodb+srv://goit-web10:131065@goitlearn-10.m8bniak.mongodb.net/test?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()

class Quote(Document):  
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    content = StringField()
    # meta = {'allow_inheritance': True}



# class User(Document):
#     email = StringField(required=True)
#     first_name = StringField(max_length=50)
#     last_name = StringField(max_length=50)


# class Post(Document):
#     title = StringField(max_length=120, required=True)
#     author = ReferenceField(User, reverse_delete_rule=CASCADE)
#     tags = ListField(StringField(max_length=30))
#     meta = {'allow_inheritance': True}


# class TextPost(Post):
#     content = StringField()


# class ImagePost(Post):
#     image_path = StringField()


# class LinkPost(Post):
#     link_url = StringField()
