###############################################################################
#   
#   INITIALIZATION
#
#   @file __init__.py
#   
###############################################################################

"""
    # 🛠️ Rust Toolbox

    ##### Version 0.1.0

    ## 💬 Description

    🐍 Python tools for 🦀 Rust projects.

    This project is part of a workspace that includes my 2 favorite
    Rust projects. Its purpose is to make building them simpler than it
    already is, and it's already pretty easy since they are Rust projects.

    The workspace is laid out like this:
    
        projects/
    ├── Cargo.toml      ⚙️
    ├── peroxide/       🦀
    ├── hw/             🦀
    └── tools/          🐍
    └── cgi-bin/        🌐

    ## 🚧 Things to Do

        * Make sure that the recent move of all `target` and `tools`
          directories to the `projects` folder is reflected in the
          code.

    ©️ Copyright © 2026 Russell Alan Klein. All rights reserved.

    Released under the MIT license.
"""

import os
from pathlib import Path
import tomllib

# Uncomment these lines to test the entire module.
from .build import *
from .constants import *
from .doc_tools import *
from .files import *
from .git_tools import *
from .lists import *
from .obj_tools import *
from .output import *
from .projects import *
from .testing import *
from .text_tools import *
from .time import *

from .constants import ( 
    CURRENT_PROJECT_NAME,
    CURRENT_PROJECT_PATH,
    FOLDER_PICT
)

os.chdir(CURRENT_PROJECT_PATH)
print("Toolbox intialized")
CURRENT_PROJECT = Path.cwd().name
print(f"{FOLDER_PICT}Current project: {CURRENT_PROJECT_NAME}")

TOOLBOX_DIR_NAME = str(Path(__file__).resolve().parent.parent.parent)
print(f"{FOLDER_PICT}Toolbox directory: {TOOLBOX_DIR_NAME}")