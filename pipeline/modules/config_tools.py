import os, json, os, re, shutil
import pandas as pd
import numpy as np

from constants import *

def validate_config(config):
    if "application" not in config.keys():
        print(f"ERROR: Application name not provided in config")
        return False
    if "application_category" not in config.keys():
        print(f"ERROR: Application Category name not provided in config")
        return False

    return True
    

def create_application_config(src_config: dict):
    pipeline_home_path = os.getenv(PIPELINE_HOME_VAR)

    application_home = os.path.join(pipeline_home_path, APPLICATION_FOLDER_NAME)
    if not os.path.isdir(application_home):
        os.mkdir(application_home)
    
    application_path = os.path.join(application_home, src_config["application"])
    os.mkdir(application_path)

    train_path = os.path.join(application_path, TRAIN_DATASET_FOLDER_NAME)
    os.mkdir(train_path)

    #models path
    models_path = os.path.join(application_path, MODELS_FOLDER_NAME)
    os.mkdir(models_path)

    config = default_config
    config["application"] = src_config["application"] 
    config["application_category"] = src_config["application_category"]
    config["train_folder"] = train_path
    config["dataset"] = str(os.path.join(application_path, TRAIN_DATASET_FOLDER_NAME, DATASET_FILE_NAME))
    config["dataset_pca"] = str(os.path.join(application_path, TRAIN_DATASET_FOLDER_NAME, DATASET_PCA_FILE_NAME))
    config["model_commons_filename"] = str(os.path.join(application_path, MODEL_COMMONS_FILE_NAME))
    
    config_path = os.path.join(application_path, APPLICATION_CONFIG_FILE_NAME)
    with open(config_path, "w") as file:
        json.dump(config, file)

def save_application_config(config):
    application = config["application"]

    pipeline_home_path = os.getenv(PIPELINE_HOME_VAR)
    application_path = os.path.join(pipeline_home_path, APPLICATION_FOLDER_NAME, application)
    config_path = os.path.join(application_path, APPLICATION_CONFIG_FILE_NAME)

    with open(config_path, "w") as file:
        json.dump(config, file)

    

def get_application_config(application: str):
    # GET APPLICATION FOLDER FROM ENV
    pipeline_home_path = os.getenv(PIPELINE_HOME_VAR)
    print("***********", pipeline_home_path, APPLICATION_FOLDER_NAME, application)
    application_path = os.path.join(pipeline_home_path, APPLICATION_FOLDER_NAME, application)
    if not os.path.isdir(application_path): #directory doesnt exist
        print(f"Application config was not found, creating a config for `{application}`...")
        create_application_config(application)
    
    config_path = os.path.join(application_path, APPLICATION_CONFIG_FILE_NAME)
    with open(config_path, "r") as file:
        config = json.load(file)
        
    return config
    
    
def create_application_structure(config: dict):
    # GET APPLICATION FOLDER FROM ENV
    pipeline_home_path = os.getenv(PIPELINE_HOME_VAR)
    
    # Create the folder Structure 
    application_name = config["application"]
    application_category = config["application_category"]
    application_run_folder = config["cheetah_app_directory"]
    # Copy all files from run folder to train folder
    
    application_path = os.path.join(pipeline_home_path, APPLICATION_FOLDER_NAME, application_name)
    if not os.path.isdir(application_path): #directory doesnt exist
        print(f"Application config was not found, creating a config for `{application_name}`...")
        create_application_config(config)
    
    pipeline_config_path = os.path.join(application_path, APPLICATION_CONFIG_FILE_NAME)
    pipeline_config = None
    with open(pipeline_config_path, "r") as file:
        pipeline_config = json.load(file)
    
    dest_train = pipeline_config["train_folder"]
    files = os.listdir(application_run_folder)
    filenames=[]
    for filename in files:
        if re.match(r'^'+application_name+'_[0-9_]+\.csv$', filename) :
            shutil.copy2(application_run_folder+"/"+filename, dest_train+"/"+filename)
            filenames.append(filename)
    
    print("I AM MERGING ALL FILES", filenames)
    
    frames = []
    for file in filenames:
        df_test = pd.read_csv(dest_train+'/'+file)
        frames.append(df_test)
        
    result = pd.concat(frames, ignore_index=True)
    uniq_id=[i for i in range(1, result.shape[0]+1, 1)]
    result['uniq_id']=np.array(uniq_id)
    result.to_csv(dest_train+'/'+DATASET_FILE_NAME, header=True, index=False)

    # Create a pipeline configure to train and save models
    config_path = os.path.join(application_path, APPLICATION_CONFIG_FILE_NAME)
    pipeline_config = None
    with open(config_path, "r") as file:
        pipeline_config = json.load(file)
        
    return pipeline_config


default_config = {
    "application": None,
    "application_category": None,
    "dataset": None,
    "dataset_pca": None,
    "train_folder": None,
    "model_commons_filename": None,
}
