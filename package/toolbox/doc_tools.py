###############################################################################
#   
#   DOCUMENTATION
#   
###############################################################################

"""
    # 📘 Documentation

    ##### Version 0.1.0

    ## 💬 Description

    Helpers for `lab/docs.ipynb`.

    projects/
    ├── cgi-bin/
    ├── hw/
    ├── peroxide/
    ├── toolbox/
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

from functools import partial, singledispatch
import inspect
from pathlib import Path
import subprocess

from IPython.display import Markdown
import nbformat
import pyperclip

from .constants import *
from .output import error

# ═══════════════════════════════ display_doc ═══════════════════════════════
def display_doc(func):
    """
        Display a function or class docstring as Markdown in Jupyter Lab
        safely, avoiding duplicated headers.

        :param func: The function to document.
        🚧 _TODO_: Polish up the output. Right now it's not displayed as Markdown.
               The problem is indentation of the docstring.
    """
    doc = func.__doc__.strip() or ""
    # Split lines and remove any that are blank at the start
    lines = doc.splitlines()
    print(f"Number of lines: {len(lines)}")
    print(f"First line: {lines[1]}")
    print(f"Length of `lines[0]`: {len(lines[1])}")
    leading_spaces = 0
    i = 0
    j = 0
    for i in range(len(lines[0])):
        if lines[0][i] != SPACE:
            break
        leading_spaces += 1
        
    print(i)
    print(lines[0][0])
    lines = [ line[leading_spaces:] for line in lines ]
    cleaned_doc = "\n".join(lines)
    display(Markdown(cleaned_doc))

# ═════════════════════════════ display_source ═════════════════════════════
@singledispatch
def display_source(arg)->None:
    """Print an error message and depart."""
    error(f': display_source : bad argument : {arg} : Argument must be str or Path')

@display_source.register
def _(s:str, lang:str='python')->None:
    """ Display the given string as Markdown.

        :param s: String containing source code to display.
        :param lang: Language of the source code.

        :todo: Make sure that `lang` has a valid value.
               If not, just do something generic.
    """
    display(Markdown(f'```{lang}\n{s}'))

@display_source.register
def _(p:Path, lang:str='python')->None:
    """ Open a file and display its contents as source code.

        :param p: Path to the input file.
    """
    display_source(p.read_text(), lang=lang)

@display_source.register
def _(obj:object, lang:str='python')->None:
    """ 
        Display an object's source code as Markdown.

        :param obj: The object.
    """
    display_source(inspect.getsource(obj))

def doxify(text, print_result=True):
    # Just add comment delimiters and asterisks.
    lines = text.split('\n')[1:]
    result = ['/**']
    result.extend([' * ' + s for s in lines])
    result.pop()
    result.append(' */')
    result = '\n'.join(result)
    if print_result: print(result)
    pyperclip.copy(result + NEWLINE)
    print("Docstring copied to clipboard")
    return result
    
# ═════════════════════════════════ rdocify ═════════════════════════════════
@singledispatch
def rdocify(arg, file_doc=False) -> str | None:
    """ Consider this an error. """
    error(f'rdocify : bad argument : {arg} : Argument  must be `str` or `Path`')

@rdocify.register
def _(s: str, file_doc=False) -> str | None:
    s = NEWLINE.join(map(lambda s: CPP_COMMENT + (EXCLAMATION if file_doc else SLASH)
                                   + SPACE + s, s.strip().split(NEWLINE)))
    pyperclip.copy(s + NEWLINE)
    return s

@rdocify.register
def _(p:Path, file_doc=False) -> str | None:
    """ Open the file and pass its text to `rdocify(str)`. """
    return rdocify(p.read_text(), file_doc)

# ══════════════════════════════════ clear ══════════════════════════════════
def clear():
    """ Clear the outputs of all Jupyter notebook code cells. """
    # print("Running `clear()`...")
    for path in Path("lab").glob("*.ipynb"):
        notebook = nbformat.read(path, as_version=4)
        # print(f"Clearing {path}")

        for cell in notebook.cells:
            if cell.cell_type == "code":
                cell.outputs = []
                cell.execution_count = None

        nbformat.write(notebook, path)
        print(f"{CHECK_PICT} Jupyter output cleared.")
        return 0
    
# ══════════════════════════════════ banner ══════════════════════════════════
def banner(text: str, style="rust") -> str | None:
    """ Convert `s` to a source code banner. """
    # `style` must be "py" or "rust"
    if not style in COMMENT_STYLES:
        error("Unknown style")
        return
    if style == "rust":
        left = ASTERISK + SPACE * 3
        top = SLASH + COMMENT_BORDER + NEWLINE + ASTERISK + NEWLINE
        bottom = ASTERISK + NEWLINE + BOTTOM_BORDER + NEWLINE
    elif style == "py":
        left = HASH_MARK + SPACE * 3
        top = PY_COMMENT_BORDER + NEWLINE + left + NEWLINE
        bottom = left + NEWLINE + PY_COMMENT_BORDER + NEWLINE
    value = top + NEWLINE.join([
        left + s for s in text.strip().split(NEWLINE)
    ]) + NEWLINE + bottom
    pyperclip.copy(value)
    return value

# ══════════════════════════════ function_header ══════════════════════════════
def function_header(s: str, style="rust", bar_width=16) -> str:
    """
        Decorate a string with a bar heading like the one above.

        # Parameters

        ## Arguments

            * `s`: The string to decorate.

        ## Keyword Arguments
        
            * `style`: The comment style. Can (must) be `'py'` or `'rust'`.
                       `'rust'` by default.
            * `bar_width`: _Deprecated_
    """
    LEFT = HASH_MARK if style=="py" else CPP_COMMENT
    BAR_WIDTH = int((SOURCE_TEXT_WIDTH - len(s) - len(LEFT) - 3) / 2)
    BAR = BOX_DRAWING_DOUBLE_HORIZONTAL * BAR_WIDTH
    value = LEFT + SPACE + BAR + SPACE + s.strip() + SPACE + BAR + NEWLINE
    pyperclip.copy(value)
    return value
    
# ══════════════════════════════ block_comment ══════════════════════════════
def block_comment(s: str, indents=(0,4), style='rust') -> str:
    """ Encase `s` in a block comment. 

        # Parameters

            * `s``
              : The comment string, presumably multiple lines.
            * `indents`
              : A tuple. `[0]` is the number of tabs.
                         `[1]` is the number of spaces in each tab.

        # Return
        
            The parameter string as a block comment in the requested style.

        # TODO

            * Wrap `s` to a width that will fit within `SOURCE_TEXT_WIDTH`.
              That's currently on the user to ensure, if it gets done at all.
    """
    text_lines = s.strip().split(NEWLINE)
    LEFT = HASH_MARK if style == 'py' else CPP_COMMENT
    output_lines = [ LEFT + SPACE + line for line in text_lines ]
    return NEWLINE.join(output_lines)

# ══════════════════════════════ typing_guide ══════════════════════════════
def typing_guide():
    print(SPACE * 71 + WARNING_PICT + "==> " + CRITICAL_PICT)
