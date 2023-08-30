
import os

HARP_HOME = os.getenv('HARP_HOME')

print("HARP_HOME", HARP_HOME)

# Database Details
URI = "mongodb://localhost:27017/?retryWrites=true&w=majority"
DB_CLIENT = None
HARP_DB = None

HARP_DB_NAME="HARP"
TEMPLATES = HARP_HOME+"/HARPStore/Templates/PipelineDB/"
DB_COLLECTIONS= ["CyberInfrastructres", "Clusters", "Nodes", "ClusterQueues"]
