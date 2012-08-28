e-cidadania toolset
===================

**Version:** *0.1 alpha*

e-cidadania toolset is a set of tools for automating some tasks like
documentation, nightlies, i18n catalogs, etc.

*This toolset is still on development, since most of the tools are scattered through the e-cidadania repositories. We recommend people to use the integrated
scripts in e-cidadania while we port them here.*

*This toolset is preconfigured for e-cidadania, but it's easy to modify to work with other django projects, take a look to the documentation below.*

Status:

- downloader.py: 90% - PASSED
- make_nightlies: 100% - PASSED
- make_docs: 80% - NOT TESTED
- make_i18n: 0% - NOT TESTED

downloader.py
=============

Defaults: branch: master, vcs: git

This tool downloads the source code from a list of specified repositories in the variable "*repos*". If it fails, it will try to download from another one on the list. It also can download a specific branch. Default: master.

make_nightlies.py
=================

This script is meant to be run with cron, it calls the downloader script, after that removes the git log and packs the source code in a tar.gz before copying it to the destination set at config.NIGHTLY_DIR.

make_docs.py
============

Supports: sphinx

It only works for multilanguage sphinx documentation.

This script gets a copy of the source code with *downloader.py* and compiles the documentation for every language specified in three formats: PDF, LaTeX and HTML. It also packs the LaTeX docs inside a tar.gz.

make_i18n.py
============

This script scans all your django applications in search of translation catalogs and generates/compiles/updates them automatically. You need to have some specific settings in you django project.

Setting things up
-----------------

You need to split up the django applications or third party applications from you own applications, like this:

	DJANGO_APPS = (
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.staticfiles',
	    'django.contrib.sites',
	)

	THIRDPARTY_APPS = (
	    'apps.thirdparty.smart_selects',
	    'apps.thirdparty.userprofile',
	    'apps.thirdparty.tagging',
	)

	YOURPROJECT_APPS = (
	    'core.spaces',
	    'apps.ecidadania.accounts',
	    'apps.ecidadania.proposals',
	    'apps.ecidadania.news',
	    'apps.ecidadania.debate',
	    'apps.ecidadania.staticpages',
	    'apps.ecidadania.cal',
	    'extras.custom_stuff',
	    'apps.ecidadania.voting',
	)
