###############################################################################
#   
#   PROJECTS
#
#   @file projects.py
#   
###############################################################################

"""
    # Projects

    ##### Version 0.1.0

    ## 💬 Description

    Functions that work with projects.

    ## 🚧 Things to Do

        * Make sure that the recent move of all `target` and `tools`
          directories to the `projects` folder is reflected in the
          code.

    ©️ Copyright © 2026 Russell Alan Klein. All rights reserved.

    Released under the MIT license.
"""

import os
from pathlib import Path
from pprint import pprint as pp

from .constants import (
    CWD_FILE,
    FOLDER_PICT,
    HIDDEN_FOLDER_NAME,
    PROJECTS_DIR
)
from .files import cd, cwd

DEBUG = False

def find_projects() -> list:
    """ Search the `PROJECTS_DIRECTORY` for folders that contain a folder
        named `.toolbox`.

        # Return

        A `list` of `toolbox`-enabled projects.
    """
    projects = list()
    folder_names = [ s for s in os.listdir(PROJECTS_DIR)
                     if (PROJECTS_DIR / s).is_dir()
                   ]
    if DEBUG:
        print("Folder names:")
        pp(folder_names)
        print()
    for s in folder_names:
        if DEBUG:
            print(f"Candidate: {s}")
        if HIDDEN_FOLDER_NAME in os.listdir(PROJECTS_DIR / s):
            if DEBUG:
                print(f"Folder {s} contains a project")
            projects.append(s)
    return projects

def current_project() -> str:
    """
        # Return

        The name of the current project as a str.

        >>>
    """
    return Path(CWD_FILE.read_text().strip()).name

def select_project() -> str:
    """ Prompt the user to select a new project and make it current. """
    choices = find_projects()
    
    while True:
        choice = input(f"Projects: {choices}: \n")
    
        matches = [c for c in choices if c.startswith(choice)]
    
        if len(matches) == 1:
            choice = matches[0]
            break
    
        print("Invalid or ambiguous choice.")
    
    cd(PROJECTS_DIR / choice)
    CWD_FILE.write_text(str(cwd()))
    print(f"{FOLDER_PICT}Current project: {cwd().name}")
