#!/usr/bin/env python
# -*- coding: utf-8 -*-

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