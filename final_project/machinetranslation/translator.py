"""Translator Module"""

import os
from   ibm_watson import LanguageTranslatorV3
from   ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from   dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def get_language_translator_instance():
    """Return IBM Language Translator Instance"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator


def englishToFrench(englishText):
    """Function to Translate from English to French"""
    language_translator = get_language_translator_instance()

    if englishText:
        frenchText = language_translator.translate(
            text=str(englishText),
            model_id='en-fr').get_result()

        return frenchText['translations'][0]['translation']
    return 'Invalid Input'


def frenchToEnglish(frenchText):
    """Function to Translate from French to English"""
    language_translator = get_language_translator_instance()

    if frenchText:
        englishText = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()

        return englishText['translations'][0]['translation']
    return 'Invalid Input'
