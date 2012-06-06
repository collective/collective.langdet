# -*- coding: utf-8 -*-
import logging

from guess_language.guess_language import guessLanguage, UNKNOWN

logger = logging.getLogger('collective.langdet')


def set_detected_language(context, event):
    if hasattr(context, 'SearchableText') and hasattr(context, 'Language'):
        text = context.SearchableText().strip().lstrip(context.id).decode('utf-8', 'ignore')
        language = guessLanguage(text)
        logger.debug('Detected language %s' % language)
        if language != context.Language() and language != UNKNOWN:
            logger.debug('Set language %s' % language)
            context.setLanguage(language)
