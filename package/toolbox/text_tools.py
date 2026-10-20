###############################################################################
#   
#   TEXT TOOLS
#   
###############################################################################

from grep import grep # Local `./contrib/grep`. Not the one on PyPI.
from rich import print as rp

from .constants import(
    NEWLINE,
    PERIOD,
    SRC_FILE_EXTS,
)

from .files import lsd

from .output import(
    debug,
    error,
    info,
    warn,
)

# ══════════════════════════════════ grepy ══════════════════════════════════
def grepy(
    pattern,
    project_name,
    source_only=True,
    output=True,
) -> list:
    """
        Find `pattern` in the project source directory, presumed to be in `CWD`.
    """
    DEBUG = True
    if output: debug("Running grepy")
    REGEX = grep(pattern, words_only=False)
    FILES = lsd(project_name, output=False)
    TODOS = dict()
    for f in FILES:
        if output: info(f"Scanning {f}")
        lines = list()
        if f.suffix.lstrip(PERIOD) in SRC_FILE_EXTS:
            t = f.read_text()
            m = t | REGEX
        
            LINES = t.split(NEWLINE)
            line_nos = list(m.matches.matching_lines())
            # print(f"`lines` is a {type(m.matches.matching_lines)}.")
            # lines = list(m.matches.matching_lines())
        
            if line_nos:
                n = max(map(lambda i: len(str(i)), line_nos))
                lines = [
                    f"{str(i + 1).rjust(n)}: {LINES[i].lstrip()}"
                    for i in line_nos
                ]

                if source_only:
                    lines = [
                        f"{str(i + 1).rjust(n)}: {LINES[i].lstrip()}"
                        for i in line_nos
                        if not (
                            LINES[i].lstrip().startswith('/') or
                            LINES[i].lstrip().startswith('*') or
                            LINES[i].lstrip().startswith('//')
                        )
                    ]
            
            if lines:
                if output:
                    rp(f"{pattern} found in [yellow]{f.name}[/yellow]:")
                    # lines = [s.lstrip() for s in lines]
                    for s in lines:
                        print(s)
                TODOS[f.name] = lines
                del lines
                
    return TODOS

