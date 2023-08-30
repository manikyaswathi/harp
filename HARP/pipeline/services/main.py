import sys, os

from Pipeline.Utils import DButils, GeneralUtils
from Pipeline.SystemManager.System import CyberInfrastructre

# export HARP_HOME="/Users/swathimanikyavallabhajosyula/Documents/GitHub/TAPIS/HARP_API"

def default_DB_create_testing():
    connection_status = DButils.connect_db()
    print("++ connection_status (0:Success, 1:Failed):", connection_status)

    create_DB_status = DButils.create_DB()
    print("++ create_DB_status (0:Success, 1:Failed):", create_DB_status)

    list_status = DButils.check_DB_SetUp()
    print("++ list_DB (0:Success, 1:Failed):", list_status)


def create_HARP_DB():
    status = DButils.setup_HARP_DB()
    return status




def test_db_operations():
    ci = CyberInfrastructre()
    ci_json = GeneralUtils.generate_sample("CyberInfrastructres")
    ci_json["_id"]["Name"]="OSC"
    ci_json["_id"]["Portal"]="https://osc.edu"
    ci_json["_id"]["Clusters"]=["ownes", "pitzer", "ascend"]
    ci_json["_id"]["Projects"]=["PAS0536"]

    print("a. Insert New Doc")
    failed, return_message = ci.create_CI(ci_json)

    print("b. Read New Doc")
    ci_pattern={"_id.Name": "OSC"}
    failed, return_message, resp_doc = ci.read_CI(ci_pattern)
    print("STATUS:", failed, return_message)
    print(resp_doc)

    # print("b. Update New Doc")
    # failed, return_message = ci.update_CI(ci_json)
    # print("STATUS:", failed, return_message)

    
    return 0



print("******* Testing Utils *************")
# print("1. Testing creating Dummy DB structre")
# default_DB_create_testing()
print("2. Testing creating HARP DB structre")
create_HARP_DB()
# print("3. Test Inserion")
# test_db_operations()