Introduction
============

collective.langdet tries to automatically detect the language of a file.
It is meant for monolingual sites where you occasionally upload files in
another language and content editors forget to add the correct metadata.

It does the language detection when a file is created, not when it is
replaced by another file. It may also be useful for multilingual sites
where you upload files via webdav, but this is as yet untested.

It uses the python package 'guess-language' which supports over 60
languages. A script for determining the language of all your current
files and changing their language into the language detected is included
in the scripts directory. You can execute it as an external method.

