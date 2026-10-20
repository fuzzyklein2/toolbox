###############################################################################
#   
#   DATES & TIMES
#   
###############################################################################

"""
    # Dates and Times

    ##### Version 0.1.0

    ## 💬 Description

    Tools for working with `datetime`s.

    ## 📑 Contents

    ### Functions

        * `now`

    ## 🚧 Things to Do        


    ©️ Copyright © 2026 Russell Alan Klein. All rights reserved.

    Released under the MIT license.
"""

from datetime import datetime as dt

# ═══════════════════════════════════ now ═══════════════════════════════════
def now(as_str=False):
    """
        Return the current date and time.
    """
    if as_str: return str(dt.now())
    return dt.now()
