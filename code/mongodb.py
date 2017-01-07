#!/usr/bin/python
"""MongoDb connection and handlers."""

from pymongo import MongoClient
from bson.objectid import ObjectId


def connect(db_name):
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    return db


def showcollections(db):
    res = db.collection_names(include_system_collections=False)
    return res


def showone(db, c_name, query):
    collection = db[c_name]
    return collection.find(query)


def showall(db, c_name):
    collection = db[c_name]
    return collection.find()


def showone_by_id(db, id):
    posts = db.posts
    res = posts.find_one({"_id": ObjectId(id)})
    return res


def getObjectId(db, data):
    posts = db.posts
    res = posts.find_one(data)
    return res['_id']


def querydocs(db, query):
    posts = db.posts
    res = []
    if not query:
        for post in posts.find():
            res.append(post)
    else:
        for post in posts.find(query):
            res.append(post)
    return res


def queryrange(db, date, condition):
    #posts = db.posts
    res = []
    collection = db['developers']
    for post in collection.find({"logs.date": date}, {"logs.$": 1}):
        res.append(post)

    if not res:
        return '-1'
    else:
        return res


def queryrange2(db, date, condition):
    #posts = db.posts
    res = []
    collection = db['developers']
    for post in collection.find({"diaries.date": date}, {"diaries.$": 1}):
        res.append(post)

    if not res:
        return '-1'
    else:
        return res


def queryrange3(db, date, condition):
    #posts = db.posts
    res = []
    collection = db['developers']
    for post in collection.find({"thinkaloud.date": date}, {"thinkaloud.$": 1}):
        res.append(post)

    if not res:
        return '-1'
    else:
        return res


def count(db, query):
    posts = db.posts
    if not query:
        res = posts.count()
    else:
        res = posts.find(query).count()
    return res


def insert(db, post):
    posts = db.posts
    insert_id = posts.insert_one(post).inserted_id
    return insert_id


def insert_bulk(db, new_posts):
    posts = db.posts
    insert_ids = posts.insert_many(new_posts).inserted_ids
    return insert_ids


if __name__ == '__main__':
    print 'MongoDB ok!'
