
import os
from datetime import datetime 
import yaml
import gc
from src import getmy as getmy
from pathlib import Path

# import get_configure.py; purpose: to create dictionaries from yaml config files

# CONFIG FILES 
## There are 2 config files that are used in this code: 
## global_default_variables.yaml
    # folder_structure_path: ## location for the folder structure
    #   folder_structure.yaml
    # base: ## location that you would like to create a new project
    #   ~/ongoing
    # template_path: ## location that you store all the templates
    #   templates/


configdir = Path(__file__).resolve().parent / "config"

folder_config = os.path.join(configdir, "folder_structure.yaml")
global_config = os.path.join(configdir, "global_default_variables.yaml")


folder_structure = getmy.get_yaml_section(folder_config, "folder_structure")
    # data structure:
    # {'first level_folder':{'second_level_folder': [...],}, ...}

new_file_location = getmy.get_yaml_section(folder_config, "new_file_location")
    # data structure:
    # {"file_type" : "location_to_create"}

template_names = getmy.get_yaml_section(folder_config, "new_file_templates")
    # data structure:
    # {"file_types" : "name_of_template"}

new_file_extensions = getmy.get_yaml_section(folder_config, "new_file_extensions")
    # data structure:
    # {"file_types" : "extension"}

global_config = getmy.get_yaml_section(global_config, "global")
    # data structure:
    # {"folder_structure_path" : "path to folder structure yaml",
    #  "base" : "directory to create new projects",
    #  "template_path" : "directory to where you store templates"}


######### UTILITY FUNCTIONS ###########
# utility function: create folder trees in base_path, with folder structure specified
def create_folders_from_structure(structure, base_path):
    for name, content in (structure or {}).items():
        folder_path = os.path.join(base_path, name)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(content, list):
            for item in content:
                if isinstance(item, str):
                    os.makedirs(os.path.join(folder_path, item), exist_ok=True)
                elif isinstance(item, dict):
                    create_folders_from_structure(item, folder_path)
        elif isinstance(content, dict):
            create_folders_from_structure(content, folder_path)

## customised function that will be used later to get the content of a template
def load_template(file_type):
    template_mapping = getmy.get_yaml_section(folder_config, 'new_file_templates')
    template_name = template_mapping[file_type]
    template_file_path = os.path.join('./src/create_project/', global_config['template_path'], template_name)
    print(template_file_path)
    if not os.path.exists(template_file_path):
        raise FileNotFoundError(f"No template found for file type: {file_type}")
    with open(template_file_path, 'r') as f:
        return f.read()
    
#######################################    

### create project folder trees after inquiring the user to input a project name
def create_project(config_path = folder_config):

    #input project name
    project_name = input("Enter your project name: ").strip()

    #create base project directory
    base_project_dir = os.path.join(global_config['base'], project_name)
    os.makedirs(base_project_dir, exist_ok=True)

    #create folder tree using the customized function we defined above
    create_folders_from_structure(folder_structure, base_project_dir)
    print(f"Folders created under: {base_project_dir}")

#######################################    

def list_projects(base_path=None):
    """Return a sorted list of project directory names under base_path.

    If base_path is None, the function will fall back to
    global_config['base'] if present, otherwise os.getcwd(). Hidden
    directories (starting with '.') are excluded.
    """
    base = base_path or global_config.get('base') or os.getcwd()
    try:
        entries = [
            name
            for name in os.listdir(base)
            if os.path.isdir(os.path.join(base, name)) and not name.startswith('.')
        ]
    except FileNotFoundError:
        return []
    return sorted(entries)


def choose_project(base_path=None):
    """Interactively choose a project from the directories under base_path.

    Returns the selected project name as a string, or None if cancelled / not found.
    """
    projects = list_projects(base_path)
    if not projects:
        print(f"No projects found in {base_path or global_config.get('base') or os.getcwd()}")
        return None

    print("Available projects:")
    for i, p in enumerate(projects, start=1):
        print(f"{i}. {p}")

    choice = input("Enter number or name of project (leave blank to cancel): ").strip()
    if not choice:
        return None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            return projects[idx]
        print("Invalid selection: index out of range")
        return None
    if choice in projects:
        return choice
    print("Invalid selection: name not found")
    return None


################################

def new_file(file_name = None, file_type = None , project_name = None, location_to_create = new_file_location):

    # get allowed choices
    options = getmy.dict_key_list(location_to_create)

    if not project_name:
        project_name = choose_project(base_path=None)

    if not project_name:
        print("No project selected — aborting file creation.")
        return None

    # choose file_type if not provided
    if not file_type:
        print("Available file types:")
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")
        choice = input("Enter number or name of file type: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if idx < 0 or idx >= len(options):
                raise ValueError("Invalid selection")
            file_type = options[idx]
        else:
            if choice not in options:
                raise ValueError(f"Invalid selection: {choice}")
            file_type = choice

    if not file_name:
        file_name = input("Enter base file name (without extension): ").strip()

    rel_path = location_to_create[file_type]
    target_dir = os.path.join(global_config['base'], project_name, rel_path)

    # Ensure target directory exists to avoid FileNotFoundError on open()
    try:
        os.makedirs(target_dir, exist_ok=True)
    except Exception as e:
        print(f"Failed to create target directory {target_dir}: {e}")
        return None

    # Load template (handle missing template more gracefully)
    try:
        template_content = load_template(file_type)
    except FileNotFoundError as e:
        print(f"Warning: {e} — continuing with empty template content.")
        template_content = ""

    # Ensure base file name
    if not file_name:
        # default to file_type as base name
        file_name = file_type or 'file'

    # determine extension (fall back to md)
    ext = new_file_extensions[file_type] if isinstance(new_file_extensions, dict) else 'md'
    ext = ext.lstrip('.') if isinstance(ext, str) else 'md'

    # Generate file name (append date)
    filename = f"{file_name}_{datetime.now().strftime('%Y%m%d')}.{ext}"
    file_path = os.path.join(target_dir, filename)

    # Write file
    try:
        with open(file_path, 'w') as f:
            f.write(template_content)
    except Exception as e:
        print(f"Failed to write file {file_path}: {e}")
        return None

    print(f"File created: {file_path}")


