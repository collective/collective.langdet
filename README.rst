Introduction
============

collective.langdet tries to automatically detect the language of a file.
It is meant for monolingual sites where you occasinally upload files in
another language and content editors forget to add the correct metadata.

It does the language detection when a file is created, not when it is
replaced by another file. It may also be usefull for multilingual sites
where you upload files via webdav, but this is as yet untested.

It uses the python package 'guess-language' which supports over 60 languages
