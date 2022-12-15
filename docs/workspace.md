# Starting instructions

- [Prepare workspace for use](#prepare-workspace-for-use)
- [Creator functions](#crud-workspace-functions)
- [Support & Errors](#🛠support)

## Prepare workspace for use
First you have make setup for all config files that workspace use,
after you can use all function of workspace

    workspace.py --setup

## **CRUD** workspace functions
... Create, Read, Update and Delete
### Create workspace
You need this fields for new workspace: Name, Alias, Directory Path and run apps & commands.

    workspace.py -c
    workspace.py --create

### Read workspace
You can read also edit workspace from workspace config.

    \Users\<UserName>\.workspace\config.json

### Update workspace
For edit or update some option in workspace since name until runs apps & commands

    workspace.py -u WORKSPACE_NAME_OR_ALIAS

## 🛠Support 
This contain some helpers from dev documentation for fix some errors

### Read ,inspect or fix file
if sometime workspace not run or script get error, you can read config.json or edit script of *workspace.py*.

Config file is into folder with name *.workspace* in location
    
    **Windows (OS)
    \Users\<UserName>\.workspace\