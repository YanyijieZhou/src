import sys
sys.path.append("../src")
import os
os.getcwd()
from src.my_py import create_project as pf


pf.load_template('meeting')

pf.create_project()

pf.list_projects()

pf.new_file()

from src.my_py import getmy as gm
