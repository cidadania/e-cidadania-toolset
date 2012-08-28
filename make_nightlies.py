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

import os, sys
import downloader
import tarfile
import datetime
import shutil
import config

def exclude_gitdir(file):
	"""
	This function searches for the git directory, if available, it will be
	excluded from the nightly.
	"""
	_return = False
	if file.find('.git/') > -1:
		_return = True
	return _return

downloader.download_code()

print " >> Compressing tar.gz file..."
now = datetime.datetime.now().strftime('%Y%m%d')
fname = 'ecidadania-nightly-%s.tar.gz' % now

f = tarfile.open(fname, 'w:gz')
f.add('ecidadania/', exclude=exclude_gitdir)
f.close()

print " >> Copying the file into destination..."
try:
	shutil.copy(fname, config.DOWNLOADS_DIR)
except:
	print " EE Couldn't copy the nighly."