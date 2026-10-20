###############################################################################
#   
#   CONFIGURATION
#
#   @file config.py
#   
###############################################################################

"""
    # ⚙️ Configuration

    ##### Version 0.1.0

    ## 💬 Description

    
    The `.config` contains a folder for each project:

    ~
    ├── .config/
        ├── peroxide/
        ├── hw/
        └── toolbox/
                config.json
                cwd.txt
        └── cgi-bin/

    In addition, the `.config/strum` directory contains config
    file(s) that pertain to the overall project being developed.

    ## 🚧 Things to Do

        * Make sure that the recent move of all `target` and `tools`
          directories to the `projects` folder is reflected in the
          code.

    ©️ Copyright © 2026 Russell Alan Klein. All rights reserved.

    Released under the MIT license.
"""

import json
import os
from pathlib import Path

from .constants import (
    STRUM_CONFIG_DIR,
    CONFIG_FILE_NAME,
    STRUM_CONFIG_FILE,
    STRUM_DIR,
    TOOLBOX_DIR_NAME
)

def current_project() -> str:
    """ # Return

        Name of the current project.
    """
    CURRENT_PROJECT_FILE = Path.home() / 

def load(p: Path) -> dict:
    with p.open() as f:
        d = json.load(f)
    return d

def dump(d: dict, path: Path) -> dict:
    with path.open('w') as f:
        json.dump(d, f)

def configure(key: str, value: str, path: Path) -> dict:
    """ Add `key : value` to the JSON file at path. """
    if not path.exists() or len(path.read_text()) == 0:
        path.write_text('{}')
    d = load(path)
    d[key] = value
    d = dump(d, path)

"""
CONFIG = {
    "toolbox_dir" : f"{STRUM_DIR / TOOLBOX_DIR_NAME}",
}

if not STRUM_CONFIG_FILE.exists(): STRUM_CONFIG_FILE.touch()
with STRUM_CONFIG_FILE.open('w') as f:
    json.dump(CONFIG, f)
"""