# Import dependencies
import argparse

# Azure dependencies
from azure.mgmt.storage import StorageManagementClient

# Get resource names from args
parser = argparse.ArgumentParser(description="Example",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-rg", "--resource-group", help="Name of the resource group to create")
parser.add_argument("loc", help="Azure resource location")
args = parser.parse_args()
print(args.loc)

# Get other parameters as well

# Check if exists
rs_exists = True #or false
if rs_exists:
    use_it = input("Yes - y, No - n")
    if (use_it.lower() == "y"):
        create = False
    else: 
        create = True
else:
    create = True

if create:
    name_exists = True # or false
    while name_exists:
        new_name = input("Name allready exists, choose a new one: ")
        name_exists = False
    success = create_resource_group()
    if success:
        print("Created successfully")
    else:
        print("Something went wrong & error")
# Do you want to use them or create a new one

# Deploy

# Check if deployed

def create_resource_group():
    pass

def check_if_storage_account_exists():
    pass
