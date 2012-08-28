# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Cidadania S. Coop. Galega
#
# This file is part of e-cidadania toolset.
#
# e-cidadania is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# e-cidadania is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with e-cidadania. If not, see <http://www.gnu.org/licenses/>.

import sys, os
import subprocess
import shutil
import pdb

#pdb.set_trace()
cwd = os.getcwd()
repos = [
    "git://github.com/cidadania/e-cidadania.git",
    "git://github.com/oscarcp/e-cidadania.git",
    "git://gitorious.org/e-cidadania/mainline.git",
    "git://repo.or.cz/e_cidadania.git",
]

def download_code(branch='master'):

    """
    Download the latest code from the e-cidadania repositories. It the
    clone fails it will try with the next repository until it finds
    a working one.
    """
    i = 0
    print "\n >> Getting e-cidadania codebase from %s..." % repos[i].split('/')[2]
    print "DEBUG: BRANCH=%s" % branch
    done = False
    while not done:
        if i <= (len(repos) - 1):
            try:
                get_code = subprocess.check_call('git clone -b ' + branch + ' ' + repos[i] + ' ecidadania > /dev/null 2>&1', shell=True)
                done = True
            except:
                print " -- Couldn't get the code from %s" % repos[i].split('/')[2]
                i += 1
        else:
            import shutil
            print "\n EE Couldn't get the e-cidadania codebase. This can be caused by an old copy of the codebase."
            print " -- Trying to delete the old codebase..."
            try:
                os.chdir('../')
                shutil.rmtree('ecidadania/')
                print " -- Code succesfully deleted. Please run the application again.\n"
                os.chdir('scripts/')
            except:
                print " -- There was some error trying to delete the old codebase. Exiting.\n"
            sys.exit()

if __name__ == "__main__":
    download_code()