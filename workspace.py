#!/usr/bin/env python

import os 
import sys, getopt
import json
import argparse
import pathlib



system_name = os.getenv("username")

system_user_path = "C://Users//%s//" % (system_name)

setup_folders = ["DBs","ES6","HW","scripts","PROJECT"]

config_directory = "%s//.workspace" % (system_user_path)
config_dir_exist = os.path.isdir(config_directory)
config_json_file = "%s//config.json" % (config_directory)


class Setup():
    def __init__(self):        
        self.is_config_setup = os.path.exists(config_json_file)
        if self.is_config_setup == False:
           self.create()
        else:
            return None
            

    def create(self):
        Config.auto()
        # print("exec")
        # os.chdir("%s" % (system_setup_path))
        # os.mkdir("C:/Users/Development Team/Documents/new-dir")
        # if is_setup == True: return True

        # print(system_setup_path)
        # os.mkdir(r"%s" % (system_setup_path))
        
        # for folderName in setup_folders:
        #     os.mkdir(r"%s/%s" % (system_setup_path,folderName))
    

class Workspace():
    def __init__(self):
        is_config_setup = os.path.exists(config_json_file)
        if is_config_setup == False:
            Setup()

        self.updateOption = ["Change Name","Change alias","Change directory path","Add/Remove"]

    def select(self):
        WorkspacesDetails = self.getDetails()
        if WorkspacesDetails == False:
            print("\n[?] You should create workspace for run function\n")
            return False

        WorkspacesNames = WorkspacesDetails['names']
        WorkspacesNamesLen = len(WorkspacesNames)
        if WorkspacesNamesLen == 0: print("\n[?] Not found some workspace in config \n")

        OrderText = ''
        for i in range(WorkspacesNamesLen):
            NaturalOrder = (i + 1)
            workspaceName = WorkspacesNames[i]
            OrderText = "\n%s) %s\n" % (NaturalOrder, workspaceName)

            workspace_selection = input("%s\n Write workspace order number(): " % (OrderText))
            if workspace_selection.isnumeric() == False:
                while True:
                    print("a")
                    workspace_selection = input('%s\nPlease, enter numeric selection of workspace():' % (OrderText))
                    if workspace_selection.isnumeric() == True: break
            
            if int(WorkspacesNamesLen) >= int(workspace_selection):
                indexOfWorkspace = (int(workspace_selection) - 1)
                selected_workspace = WorkspacesNames[indexOfWorkspace]
                return selected_workspace
            else:
                return False

    def create(self):

        name = input('Enter name for new workspace (): ')
        if not name or len(name) == 0: 
            name = input('Please, Enter new workspace new: ')
            if not name or len(name): 
                print("\n[?] Should enter name for new workspace \n")
                return False

        alias = input('Enter short name for quick start ():')
        print(alias.isspace())
        
        if not alias or len(name) == 0:
            alias = input('Plase, enter short name for quick start ():')
            if not alias or len(alias) == 0:
                print("\n[?] Should enter alias for new workspace \n")
                return False

        directory_path = input('Enter directory path for workspace (): ')
        if not directory_path or len(directory_path) == 0: 
            print("\n[?] Should enter directory path \n")
            return False
            
        if os.path.exists(directory_path) == False:
            creatorQuestion = input("it isn't exist. Do you create folder? [Y] or [N]:").lower()
            print(len(creatorQuestion))
            if creatorQuestion == "n" or len(creatorQuestion) == 0: 
                print("\n[?] Should create folder for create it \n")
                return False
            else:
                os.mkdir(directory_path)
                print("\n[+] workspace directory has been created \n")

        insert_apps = input('Do you add apps, insert exe file. [Y] or [N]:')
        run_apps = []

        if insert_apps.lower() == "y":
            while True:
                inp = input("Enter run app file location: ")
                if not inp:
                    break
                run_apps.append(inp)

        insert_run_commands = input('Do you add commands for run. [Y] or [N]: ')
        run_commands=[]

        if insert_run_commands.lower() == "y":
            while True:
                inp = input("Write command for run: ")
                if not inp:
                    break
                run_commands.append(inp)
        
        custom = {
            "name": name,
            "alias": alias,
            "DirectoryPath": directory_path,
            "run": { "apps":run_apps, "commands":run_commands }
        }
        
        # Validate date for then append on custom(object)
        Config.add(custom)
    def update(self,workspace_name): 
        if workspace_name:
            workspace = self.get(workspace_name)
            print(workspace)
            return False
            if workspace == False:
                print("\n[?] Not found some workspace in config \n")
            else:
                def updates_selection(): 
                    update_option = ''
                    workspace_edit = workspace
                    update_selection_array = self.updateOption
                    for i in range(len(update_selection_array)):
                        update_option += "\n%s) %s" % ((i + 1),update_selection_array[i])

                    selected_option = input("\n%s\n\nChoose types of update (): " % (update_option))
                    match (int(selected_option) - 1):
                        case 0:
                            # Name
                            new_workspace_name = input("\nCurrent Workspace Name: %s\nNew Workspace Name (): " % (workspace['name']))
                            workspace_edit['name'] = new_workspace_name
                            pass
                        case 1:
                            # Alias
                            print("2")
                        case 2:
                            # Directory Path
                            print("3")
                        case 3:
                            # Add/Remove Apps & Commands
                            print("4")
                    return workspace
                    
                save_workspace = updates_selection()
                while True: 
                    save_checkout = input("Do you want do another changes? [Y] [N] ():")
                    if save_checkout.lower() == "y":
                        save_workspace = updates_selection()
                    else:
                        self.save(save_workspace)
                        break   
        else:
            selected_workspace = self.select()
            if selected_workspace == False:
                pass
            else:
                self.update(selected_workspace)

    def run(self,workspace_name):
        if workspace_name:
            workspace = Workspace().get(workspace_name)
            if workspace == False:
                print("\n[?] %s ,you should create workspace \n" % (workspace_name))
            else:
                workspaceDirectoryPath = workspace['DirectoryPath']
                workspaceRun = workspace['run']
                workspaceApps = workspaceRun['apps']
                workspaceCommands = workspaceRun['commands']

                for app in workspaceApps:
                    if app: os.startfile(r"%s" % (app))
                for command in workspaceCommands:
                    if command:
                        os.chdir(r"%s" % (workspaceDirectoryPath))
                        os.system(r"%s" % (command))
                print('[WORKSPACE] %s is started' % (workspace_name))
        else:  
            selected_workspace = self.select()
            if selected_workspace == False:
                pass
            else:
                self.run(selected_workspace)

    def recent():       
        print("recently opened")

    def save(self,workspace):
        print(workspace)

    def get(self,workspace_name):
        workspaces_json = Config().config['custom']
        print(len(workspaces_json))
        for workspace in workspaces_json:
            index =+ 0
            if workspace['name'] == workspace_name or workspace['alias'] == workspace_name:
                print(index)
                return workspace
            else:
                return False

    def getDetails(self):
        ObjectReturn = { "names":[], "Directories": [] }
        CustomArray = Config().config['custom']
        print(CustomArray)
        if len(CustomArray) != 0: 
            for space in CustomArray:
                ObjectReturn["names"].append(space["name"])
                ObjectReturn["Directories"].append(space["DirectoryPath"])
                print(space["name"])
            return ObjectReturn
        else:
            return False    


class Config():
    def __init__(self) :
        self.zeroInt = 0
        with open(config_json_file,'r+') as f:
            self.config = json.load(f)    
            
    def add(workspace_object):
        with open(config_json_file,'r+') as f:
            DataInsert = json.load(f)
            Workspace_Array = DataInsert['custom']
            Workspace_Array.append(workspace_object)
            DataInsert['custom'] = Workspace_Array

            f.seek(0)
            json.dump(DataInsert, f, indent=4)
            f.truncate()
            
            print("[+] workspace was saved in config file")
    def edit(workspace_object):
        with open(config_json_file,"w") as outfile:
            outfile.write()
    def auto():
        SetupConfigDirectory = os.path.exists(config_directory)
        if SetupConfigDirectory == False: 
            os.mkdir(config_directory)
            print("[+] .workspace is setup with config file")

            DefaultSchema = {
                "custom": []
            }
            ObjectInsert = json.dumps(DefaultSchema, indent=4)
            with open(config_json_file,"w") as outfile: 
                outfile.write(ObjectInsert)
                print("[+] .workspace config file created")
                return True 
        else: return False


        
Command=False
workspaceName=False;
if len(sys.argv) >= 2: 
    Command = sys.argv[1]
if len(sys.argv) >= 3: 
    workspaceName = sys.argv[2]

WorkspaceInstance = Workspace()


match Command:
    case "--recent": False
    case "-r" | "--run": WorkspaceInstance.run(workspaceName)
    case "-c" | "--create": WorkspaceInstance.create()
    case "-u" | "--update": WorkspaceInstance.update(workspaceName)
    case "-d" | "--delete": False
    case "--setup": Setup()
    case False:
        left_space = "                    "
        usage = "Usage: %s [--recent] [-r workspace_name]\n%s[-c] [-u workspace_name]\n%s[-d workspace_name]" % (sys.argv[0],left_space,left_space)
        print(usage)
    case "--help":
        parser = argparse.ArgumentParser(description="Welcome to Workspace Help script..")
        parser.add_argument("--recent",type=str, metavar='', help="Run last workspace used")
        parser.add_argument("-c","--create",type=str, metavar='', help="Create new workspace")
        parser.add_argument("-r","--run",type=str, metavar='', help="Run workspace with workspace name")
        parser.add_argument("-u","--update",type=str, metavar='', help="Update workspace info like: (Name/Alias/Directory Path/Run apps & commands)")
        parser.add_argument("-d","--delete",type=str, metavar='', help="Delete workspace using name")

        parsed_args = parser.parse_args()

    