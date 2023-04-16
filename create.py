import json

from mongoengine import disconnect

from models import Author, Quote

# from models import User, TextPost, LinkPost, ImagePost


def load_json_author(file):
    with open(file, 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for atr in authors:
            author = Author(
                fullname=atr['fullname'],
                born_date=atr['born_date'],
                born_location=atr['born_location'],
                description=atr['description']
            ).save()


def load_json_quote(file):
    with open(file, 'r', encoding='utf-8') as f:
        quotes = json.load(f)        
        for qt in quotes:
            quote_author = Author.objects(fullname=qt["author"])    
            quote = Quote(
                author=quote_author[0],
                tags=qt['tags'],
                content=qt['quote']
            ).save()

if __name__ == '__main__':
    load_json_author('authors.json')
    load_json_quote('quotes.json')



    # ross = User(email='ross@example.com')
    # ross.first_name = 'Ross'
    # ross.last_name = 'Lawley'
    # ross.save()

    # john = User(email='john@example.com', first_name='John',
    #             last_name='Lawley').save()

    # post1 = TextPost(title='Fun with MongoEngine', author=john)
    # post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    # post1.tags = ['mongodb', 'mongoengine']
    # post1.save()

    # post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    # post2.link_url = 'http://docs.mongoengine.com/'
    # post2.tags = ['mongoengine']
    # post2.save()

    # tolya = User(email='python_guru@example.com',
    #              first_name='Anatoliy', last_name='Safonov').save()
    # post3 = ImagePost(title='MongoDB picture', author=tolya)
    # post3.image_path = 'https://res.cloudinary.com/hevo/image/upload/v1626694700/hevo-blog/MongoDB-sm-logo-500x400-1-1.gif'
    # post3.tags = ['Senior', 'Pomidor']
    # post3.save()

    disconnect()
