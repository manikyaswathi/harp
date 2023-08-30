from pymongo.mongo_client import MongoClient
import uuid, os, json

from Constants import *


def get_template(filename):
    f = open(filename)
    template_json = json.load(f)
    f.close()
    return template_json


def connect_db():
    global URI, DB_CLIENT
    
    DB_CLIENT = MongoClient(URI)
    connection_status = -1
    try:
        resp = DB_CLIENT.admin.command('ping')
        print("+ Pinged your deployment. You successfully connected to MongoDB!", resp)
        connection_status = 0
    except Exception as e:
        connection_status = 1
        DB_CLIENT = None
        print("-",e)
    return  connection_status


def create_Collection(DBCollection="HARP_Test_Collection"):
    global DB_CLIENT, HARP_DB, TEMPLATES
    create_status = -1
    try:
        print("+ Creating Collection: "+DBCollection)
        db_Collection = HARP_DB[DBCollection]
        print("+ Inserting a Dummy Document: ")
        UUID = str(uuid.uuid1())
        doc_template = get_template(os.path.join(TEMPLATES, DBCollection+".JSON"))
        doc_template["_id"]["UUID"] = UUID
        ins = db_Collection.insert_one(doc_template)
        print("InsertionID", ins.inserted_id)
        create_status = 0
    except Exception as e:
        create_status = 1
        DB_CLIENT = None
        print("-",e)
    return  (create_status, db_Collection)



def create_DB(DBtype="default", DBname="HARP_Test_DB", DBCollection="HARP_Test_Collection"):
    global DB_CLIENT, HARP_DB, DB_COLLECTIONS
    create_status = -1

    dblist = DB_CLIENT.list_database_names()
    if DBname in dblist:
            print("+ The database exists!")
            HARP_DB = DB_CLIENT[DBname]
            create_status = 0
    else:
        print("+ The database DOES NOT exist in Server("+URI+"). Creating a new DB.")
        try:
            print("+ Creating DB: "+DBname)
            HARP_DB = DB_CLIENT[DBname]
            create_status = 0
        except Exception as e:
            create_status = 1
            print("-",e)
    # collectLists= HARP_DB.list_collection_names()
    if create_status == 0 and DBtype == "test":
        try:
            print("+ Creating Collection, if doesnt exits: "+DBCollection)
            status, db_collect_name = create_Collection(DBCollection)
            create_status = status
        except Exception as e:
            create_status = 1
            print("-",e)
    elif create_status == 0 and DBtype == "default":
        # type == "Default"
        for c in DB_COLLECTIONS:
            # if c not in dblist:
            try:
                print("+ Creating Collection, if doesnt exits: "+c)
                status, db_collect_name = create_Collection(DBCollection=c)
                create_status = status
            except Exception as e:
                create_status = 1
                print("-",e)
    else:
        create_status = 1

    return  create_status


def setup_HARP_DB():
    global URI, HARP_DB_NAME
    db_setup_status = -1
    try:
        connection_status = connect_db()
        if connection_status != 0:
            raise Exception("Failed to establish connection to URI("+URI+")")
        create_DB_status = create_DB(DBtype="default", DBname=HARP_DB_NAME)
        if create_DB_status != 0:
            raise Exception("Failed to create a DB("+HARP_DB_NAME+")")
        if connection_status ==0 and create_DB_status == 0:
            db_setup_status = connection_status
        else:
            db_setup_status = 1
    except Exception as e:
        print(e)
        db_setup_status = 1

    return db_setup_status



def check_DB_SetUp(DBname="HARP_Test_DB"):
    global DB_CLIENT, HARP_DB, DB_COLLECTIONS
    list_status = -1
    miss_collect=[]
    try:
        dblist = DB_CLIENT.list_database_names()
        if DBname in dblist:
            print("+ The database exists in list:", dblist)
            collectLists= HARP_DB.list_collection_names()
            for c in DB_COLLECTIONS:
                if c not in collectLists:
                    miss_collect.append(c)
            if len(miss_collect) > 0:
                 print("- Some/All collections DO NOT exist in list:", collectLists)
                 list_status = 1
            else:
                print("+ All the Collections exists in DB"+DBname)
                list_status = 0
        else: 
            print("- The database DOES NOT exists in list:", dblist)
            list_status = 1
    except Exception as e:
        print(e)
       
    return  list_status



def return_Collection_Handle(DBCollection="HARP_Test_Collection"):
    global URI, DB_CLIENT, HARP_DB_NAME, TEMPLATES
    db_collect_status = -1
    db_Collection = None
    try:
        connection_status = connect_db()
        if connection_status != 0:
            raise Exception("Failed to establish connection to URI("+URI+")")
        HARP_DB = DB_CLIENT[HARP_DB_NAME]
        db_Collection = HARP_DB[DBCollection]
        db_collect_status = 0
        
    except Exception as e:
        print(e)
        db_collect_status = 1
    return (db_collect_status, db_Collection)

