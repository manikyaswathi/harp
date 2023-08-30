# from pymongo.mongo_client import MongoClient
import uuid, os, json

from Pipeline.Utils import DButils

from Constants import *
"""
CRUD - Create, Read, Update and Delete the documnets in a selected collection
View - List Doduments in Collection

"""

def create_item(CollectionType, JSON_Value):
    status, collectionsHandle = DButils.return_Collection_Handle(DBCollection=CollectionType)
    return_status = ""
    return_code = 0
    try:
        ins = collectionsHandle.insert_one(JSON_Value)
    except Exception as e:
        return_status = "- "+e
        return_code = 1
    return return_code, return_status


# read 'return_q' matches for read items
def read_item(CollectionType, JSON_Pattern, return_q=1):
    status, collectionsHandle = DButils.return_Collection_Handle(DBCollection=CollectionType)
    resp = []
    return_code = 0
    match_collection = None
    try:
        match_collection = list(collectionsHandle.find(JSON_Pattern))
        print(match_collection)
    except Exception as e:
        return_code = 1
        print("-", e)
    if len(match_collection) > 0:
        resp = match_collection[:return_q]
    return return_code, resp


def update_item(CollectionType, JSON_pattern, JSON_Value, update_q="one"):
    status, collectionsHandle = DButils.return_Collection_Handle(DBCollection=CollectionType)
    return_status = ""
    return_code = 0
    try:
        if update_q == "one":
            collectionsHandle.update_one(JSON_pattern, JSON_Value)
        else:
           x = collectionsHandle.update_many(JSON_pattern, JSON_Value)
           return_status= x.modified_count+" documents updated."
    except Exception as e:
        return_code = 0
        return_status = "- "+ e

    return return_code, return_status


def delete_item(CollectionType, JSON_pattern, delete_q="one"):
    status, collectionsHandle = DButils.return_Collection_Handle(DBCollection=CollectionType)
    return_status = ""
    return_code = 0
    try:
        if delete_q == "one":
            collectionsHandle.delete_one(JSON_pattern)
        else:
            x = collectionsHandle.delete_one(JSON_pattern)
            return_status = x.deleted_count + " documents deleted."
            return_code = 1
    except Exception as e:
         return_status = "- " + e
    return return_code, return_status
       



# read 'return_q' matches for read items
def view_collection(CollectionType, JSON_Pattern=None, return_q=1):
    status, collectionsHandle = DButils.return_Collection_Handle(DBCollection=CollectionType)
    resp = []
    return_code = 0
    try:
        if JSON_Pattern:
            match_collection = list(collectionsHandle.find(JSON_Pattern))
        else:
            match_collection = list(collectionsHandle.find())
    except Exception as e:
        print("-", e)
        return_code = 0
    if len(match_collection) > 0:
        resp = match_collection[:return_q]
    return return_code, resp
   