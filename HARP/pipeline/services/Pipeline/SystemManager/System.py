# Model: model_controller
from Pipeline.Utils import ModelUtils



class CyberInfrastructre(object):

    def __init__(self):
        self.item_type = "CyberInfrastructres"
        self.desc = "Cyber-Infrastructres"

    def validity_check(self, JSON_val=None, operation=None):
        # To-do
        return 0


    def create_CI(self, CI_item):
        valid = self.validity_check(JSON_val=CI_item, operation='create')
        return_message=""
        failed = 0
        if valid == 0: 
            return_code, return_status = ModelUtils.create_item(self.item_type, CI_item)
            if return_code == 0:
                return_message = "Succesfully added entry to "+ self.desc + " Collection"
            else:
                return_message = return_status
        else:
            sucfailedcess = 1
            return_message = "Invalid JSON! Failed to add entry to "+ self.desc + " Collection"
        return failed, return_message
    

    def read_CI(self, CI_pattern):
        valid = self.validity_check(JSON_val=CI_pattern, operation='create')
        return_message=""
        resp_doc = None
        failed = 0
        if valid == 0: 
            return_code, resp_doc = ModelUtils.read_item(self.item_type, CI_pattern)
            return_message = "Succesfully read values from "+ self.desc + " Collection"
            if return_code and len(resp_doc) == 0:
                return_message+= "No values to view from Collection"
            elif return_code == 1:
                return_message = "Failed to read from "+ self.desc + " Collection"
        else:
            failed = 1
            return_message = "Invalid JSON! Failed to read from "+ self.desc + " Collection"
        return failed, return_message, resp_doc
         

    def update_CI(self, CI_pattern, CI_item):
        valid = self.validity_check(JSON_val=CI_item, operation='create')
        return_message=""
        failed = 0
        if valid == 0: 
            return_code, return_status =  ModelUtils.update_item(self.item_type, CI_pattern, CI_item)
            if return_code == 0:
                return_message = "Succesfully updated values to "+ self.desc + " Collection." + "("+ return_status+")"
            else:
                return_message = "Failed to update values to "+ self.desc + " Collection." + "\nERROR:"+ return_status
        else:
            failed = 1
            return_message = "Invalid JSON! Failed to update  "+ self.desc + " Collection"
        return failed, return_message
    
       

    def delete_CI(self, CI_pattern):
        valid = self.validity_check(JSON_val=CI_pattern, operation='create')
        return_message=""
        failed = 0
        if valid == 0: 
            return_code, return_status =  ModelUtils.delete_item(self.item_type, CI_pattern)
            if return_code == 0:
                return_message = "Succesfully deleted values from "+ self.desc + " Collection." + "("+ return_status+")"
            else:
                return_message = "Failed to delete from "+ self.desc + " Collection." + "\nERROR:"+ return_status
        else:
            failed = 1
            return_message = "Invalid JSON! Failed to delete from "+ self.desc + " Collection"
        return failed, return_message
        

    def view_CIs(self):
        return_message=""
        failed = 0
        return_code, return_vals =  ModelUtils.delete_item(self.item_type)
        if return_code == 0:
            return_message = "Succesfully read the collection: "+ self.desc + " Collection."
            return_message += "["+",".join(return_vals)+"]"
        else:
            failed = 0
            return_message = "Failed to fetcg collection: "+ self.desc + "." + "\nERROR:"
    
        return failed, return_message
         
