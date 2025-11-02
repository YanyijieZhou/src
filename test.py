import sys
sys.path.append("../src")
import os
os.getcwd()
from src import create_project as pf


pf.load_template('meeting')

pf.create_project()

pf.list_projects()

pf.new_file()

from src import getmy as gm
