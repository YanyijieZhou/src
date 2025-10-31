

# README

## Structure of the project folder and the source package:

```
Root Folder/
├── projects/
│   └── (newly created project folders will be here)
├── src/
│   └── getmy/
│   └── create_project/
│       └── create_project.py
│       └── config/
│       └── templates/
|  └── script_to_run.py
```


## Introduction to the package modules:

### getmy.py

This module provides utility functions for dictionary operations

1. dict_key_list(d): Returns a list of keys from the given dictionary d.

2. get_yaml_section(config_path, section): Reads a YAML file from config_path and returns the specified section as a dictionary.

### create_project.py

This module handles the creation of new project folders based on predefined templates and configurations.
Main Functions:

1. create_project(config_path = default_config_path)

   - Creates a new project folder in the 'projects' directory.

   - Uses folder structures defined in 'folder_structure.yaml'.

2. list_projects(base_path=None)

   - Lists all existing project folders in the 'projects' directory.

3. new_file(file_name = None, file_type = None , project_name = None, location_to_create = new_file_location)

    - Creates a new file of specified type in the given project folder using templates.

## How to use the package:

- Copy the src/ folder into your root project directory: src/ should be at the same level as your projects/ folder.

- Create a .py script (e.g., script_to_run.py) in the root folder to utilize the package functions.

- Copy the following code into your script_to_run.py to import the module and use its functions:


```

import sys
sys.path.append("../src")
from src import create_project as cp

```

```
cp.create_project()
```

This will pop up prompts to guide you through creating a new project folder.


```
new_file()
```
This will pop up prompts to guide you through creating a new file in an existing project folder.



## How to configure templates and folder structures:

1. Folder Structure Configuration:
   - The folder structure for new projects is defined in 'folder_structure.yaml' located in 'src/create_project/config/'.
   - You can modify this YAML file to change the default folder structure for new projects.

2. File Templates:
   - File templates are stored in 'src/create_project/templates/'.
   - You can add or modify templates here to customize the files created in new projects.
   - Ensure that the template file names correspond to the file types you want to create.
