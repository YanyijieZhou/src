#!/usr/bin/env bash
set -euo pipefail
# Wrapper to call create_project() function from create_project.py
# Use absolute path to the actual module location
MODULE_DIR="/Users/yanyijiezhou/ongoing/src/my_py"
python3 -c "import sys; sys.path.insert(0, '${MODULE_DIR}'); from create_project.create_project import create_project; create_project()"



# chmod +x ~/ongoing/src/my_py/create_project/scripts/create_project_py.sh && mkdir -p ~/bin && cp ~/ongoing/src/my_py/create_project/scripts/create_project_py.sh ~/bin/create_project && ls -lh ~/bin/create_project
# source ~/.zshrc && which create_project
# echo $PATH | tr ':' '\n' | grep -i bin
# echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc && tail -3 ~/.zshrc
# export PATH="$HOME/bin:$PATH" && which create_project