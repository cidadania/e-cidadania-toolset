#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script download the latest git version of e-cidadania, compiles
the documentation and places it in the documentation website.
"""

import sys
import os
import subprocess
import argparse
import downloader
import config

class Documents():

    def __init__(self):
        downloader.download_code()
        os.chdir(config.DOCS_DIR)

    def compile_docs(self):

        """
        Compile all the documentation and languages at once.
        """
        sys.stdout.write("\n >> Compiling documentation... ")
        sys.stdout.flush()

        i = 0
        done = False
        while not done:
            if i < (len(self.formats) - 1):
                try:
                    sys.stdout.write('(%s) ' % self.formats[i])
                    sys.stdout.flush()
                    gen_docs = subprocess.check_call('make ' + self.formats[i] + ' > /dev/null 2>&1', shell=True)
                    if gen_docs == 0:
                        i += 1
                except:
                    print " -- Couldn't compile the %s documentation." % self.formats[i]
                    i += 1
            elif i == (len(self.formats) - 1):
                try:
                    sys.stdout.write('(%s) ' % self.formats[i])
                    sys.stdout.flush()
                    gen_docs = subprocess.check_call('make ' + self.formats[i] + ' > /dev/null 2>&1', shell=True)
                    if gen_docs == 0:
                        i += 1
                        done = True
                except:
                    print " -- Couldn't compile the %s documentation." % self.formats[i]
                    i += 1
            else:
                sys.exit("\n EE Couldn't generate documentation. Exiting.\n")
        print "\n"

    def pack_latex(self):

        """
        Package the LaTeX documentation into a tar.gz
        """
        print " >> Packaging the LaTeX files..."
        import tarfile
        
        os.chdir(os.getcwd() + '/build/latex/')
        i = 0
        while i <= (len(self.langs) - 1):
            tar = tarfile.open(os.getcwd() + "/../../%s/latest-%s.tar.gz" % (self.langs[i], self.langs[i]), "w:gz")
            tar.add(self.langs[i])
            tar.close()
            i += 1
            

    def copy_docs(self):

        """
        Copy the generated documentation into their respective directories.
        """
        os.chdir("../../")

        c = 0
        while c <= (len(self.formats) - 1):
            print " >> Copying the %s documentation..." % self.formats[c]
            sys.stdout.write(" >> done ")
            sys.stdout.flush()
            
            i = 0
            while i <= (len(self.langs) - 1):
                if self.formats[c] == 'latexpdf':
                    try:
                        copy_latexpdf = subprocess.check_call('cp -R build/latex/' + self.langs[i] + '/e-cidadania.pdf ../../' + self.langs[i] + '/latest-' + self.langs[i] + '.pdf', shell=True)
                    except:
                        print " -- Couldn't copy the " + self.langs[i] + " documentation."
                        pass
                    sys.stdout.write("(%s) " % self.langs[i])
                    sys.stdout.flush()
                    i += 1
                elif self.formats[c] == 'html':
                    try:
                        copy_html = subprocess.check_call('cp -R build/' + self.formats[c] + '/' + self.langs[i] + '/* ../../' + self.langs[i] + '/latest', shell=True)
                    except:
                        print " -- Couldn't copy the " + self.langs[i] + " documentation."
                        pass
                    sys.stdout.write("(%s) " % self.langs[i])
                    sys.stdout.flush()
                    i += 1
                elif self.formats[c] == 'latex':
                    try:
                        copy_latex = subprocess.check_call('cp -R ' + self.langs[i] + '/latest-' + self.langs[i] + '.tar.gz' + ' ../../' + self.langs[i], shell=True)
                    except:
                        print " -- Couldn't copy the " + self.langs[i] + " documentation."
                        print " EE Couldn't copy one or all the documentation! Exiting."
                        sys.exit(1)
                    sys.stdout.write("(%s) " % self.langs[i])
                    sys.stdout.flush()
                    i += 1
            print "\n"
            c += 1

    def make_all(self, branch):
        self.compile_docs()
        self.pack_latex()
        self.copy_docs()

doc = Documents()
doc.make_all()
