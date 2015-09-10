#!/usr/bin/env python

"""
List repositories on Github belonging to organisations, teams, etc
"""

# Technical Debt
# --------------

# Known Bugs
# ----------

import argparse
import codetools
import textwrap

gh = codetools.github(authfile='~/.sq_github_token')

# Argument Parsing
# ----------------

parser = argparse.ArgumentParser(
    prog='github_list_repos',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''

    List repositories on Github using various criteria

    Examples:

    github_list_repos.py lsst
    
    '''),
    epilog='Part of codekit: https://github.com/lsst-sqre/sqre-codekit'
)

parser.add_argument('organisation')

parser.add_argument('--teams', action='store_true')

parser.add_argument('--hide')

opt = parser.parse_args()

# Do Something
# ------------

org = gh.organization(opt.organisation)

for repo in org.iter_repos():

    if not opt.teams:
        print repo.name
    else:

        teamnames = [t.name for t in repo.iter_teams()]

        if opt.hide:
            teamnames.remove(opt.hide)

        print repo.name + " : " + "\t".join(teamnames)








