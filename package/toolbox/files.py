###############################################################################
#   
#   FILE SYSTEM
#   
###############################################################################

import os
from pathlib import Path

from .constants import (FOLDER_PICT,
                        WARNING_PICT,
                       )

# ═══════════════════════════════════ cwd ═══════════════════════════════════
def cwd()-> Path:
    """ # Return
          `Path` to the current working directory.
    """
    return Path.cwd()

# ═══════════════════════════════════ pwd ═══════════════════════════════════
def pwd():
    """Print `cwd()` and return it."""
    CWD = cwd()
    print(f'{FOLDER_PICT}Current working directory: {CWD}')
    return CWD

# ═══════════════════════════════════ cd ═══════════════════════════════════
def cd(p:str|Path)->Path|None:
    """Change the current working directory."""
    p = Path(p)
    if not p.exists():
        print(f'{WARNING_PICT}WARNING: Directory {str(p)} does not exist!')
        return
    os.chdir(p)
    return p

# ═════════════════════════════════ hidden ═════════════════════════════════
def hidden(p: Path | str | None) -> bool:
    """ # Return

        `True` if any part of the `Path` is hidden (`.startswith('.')`).

        🚧 _TODO_: Really should include files that end with `'~'`, `'#'`, etc. 
    """
    return any(map(lambda s: s.startswith('.'), p.parts))

# ═══════════════════════════════════ lsd ═══════════════════════════════════
def lsd(p: Path | str | None = None, output = True) -> list[Path]:
    """ List the given directory.

        # Parameters

            * `p`: `Path` to the directory, a `str` representing that
                   path, or `None`, in which case `cwd` is assumed.
            * `output`: Whether to print the resulting list. `True` by default.
            
        # Return

        A `list` of the files within `p`.
        
        🚧 _TODO_:  This needs to have a recursive option.
        🚧 _TODO_:  Fancy colored output like `bash` displays.

    """
    if not p: p = Path.cwd()
    p = Path(p)
    paths = [path for path in p.glob('*') if not hidden(path)]
    if output:
        pp(list(map(str, paths)))
    return paths

def ensure_valid_path(p):
    try:
        if not p.parent.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            print(f"📂 Created parent directories for '{p}'")
    except Exception as e:
        print(f"❌ Failed to create directories: {e}")
        return False
    return True

