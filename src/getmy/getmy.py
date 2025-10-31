import yaml

# create list of keys form a dictionary
def dict_key_list(dictionary):
    get_keys = dictionary.keys()
    keys_to_list = list(get_keys)
    return keys_to_list

# return a dictionary that is specified in "section_name" in the yaml file "config_path"
def get_yaml_section(config_path, section_name):
    with open(config_path, 'r') as f:
        yaml_content = yaml.safe_load(f) or {}
    section = yaml_content[section_name]
    return section