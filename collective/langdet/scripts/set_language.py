# -*- coding: utf-8 -*-
import logging

from guess_language.guess_language import guessLanguage, UNKNOWN

logger = logging.getLogger('collective.langdet')

def setLanguage(self):
    brains = self.portal_catalog(portal_type = 'File')
    j = len(brains)
    i = 0
    k = 0
    for brain in brains:
        i +=1
        context = brain.getObject()
        text = context.SearchableText().strip().lstrip(context.id).decode('utf-8', 'ignore')
        language = guessLanguage(text)
        if language != context.Language():
            logger.info('%i/%i' %(i,j))
            logger.info('Content language %s' % context.Language())
            logger.info('Detected language %s' % language)
        if language != context.Language() and language != UNKNOWN:
            logger.info('Set language %s' % language)
            context.setLanguage(language)
            k += 1
    logger.info('Set language completed')
    logger.info('%i language settings updated' % k)
