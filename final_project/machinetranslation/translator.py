"""Module providing Function Translate EN2FR and FR2EN."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3( version=VERSION, authenticator=authenticator)
language_translator.set_service_url(url)


def englishtofrench(englishtext):
    """Funtion to Translate English to French"""
    translation=language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    frenchtext=translation.get("translations")[0].get("translation")
    return frenchtext


def frenchtotnglish(frenchtext):
    """Funtion to Translate French to English"""
    translation = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    englishtext = translation.get("translations")[0].get("translation")
    return englishtext

if __name__ == '__main__':
    text = englishtofrench("")
    print(text)
    