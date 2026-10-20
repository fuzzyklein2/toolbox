###############################################################################
#   
#   LIST TOOLS
#
#   @file lists.py
#   
###############################################################################

"""
    # List Tools

    ##### Version 0.1.0

    ## 💬 Description

    Tools for working with `list`s.

    ## 📑 Contents

    ### Functions

        * `empty`


    ## 🚧 Things to Do        


    ©️ Copyright © 2026 Russell Alan Klein. All rights reserved.

    Released under the MIT license.
"""

from functools import singledispatch

# ══════════════════════════════════ empty ══════════════════════════════════

@singledispatch
def empty(arg)->bool:
    """
        ⚠️ It's an error to call this function with any unregistered type!

        # Return

            `True` if the `list` is empty and `False` otherwise.
    """
    error(f': empty : bad argument : {arg} : Argument must be a `list`.')

@empty.register
def _(L:list)->bool:
    return len(L) == 0

