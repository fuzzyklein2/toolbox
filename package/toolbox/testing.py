import os
from pathlib import Path
import sys

from .build import syscmd
from .constants import UNDERSCORE
from .output import error

# ═══════════════════════════════ test_tools ═══════════════════════════════

def test_tools():
    """ Execute the modules in this package. """
    EXE = sys.executable
    SOURCE_FILES = [s for s in os.listdir("tools/src/tools")
                    if not s.startswith(UNDERSCORE)
                        and s.endswith('py')
                   ]
    for f in SOURCE_FILES:
        path = Path(f)
        mod = path.stem
        cmd_line = f"{EXE} -m tools.{mod}"
        process = syscmd(cmd_line)
        if process.returncode:
            error(f"`{mod}` execution failed!")
            print(process.stderr)
            break
        # print(process.stdout)
    return process.returncode
