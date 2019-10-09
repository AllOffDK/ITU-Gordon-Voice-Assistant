#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import argparse
import locale
import logging

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts

step = 0
angry = False

def advanceRecipe():
    step+1

def getAngry():
    angry = True

def getSweet():
    angry = False


def recipe():
    say = ''
    if not angry:
        if step == 1:
            say = ''
        elif step == 2:
            say = ''
        elif step == 3:
            say = ''
        elif step == 4:
            say = ''
        elif step == 5:
            say = ''
        elif step == 6:
            say = ''

    elif angry:
        if step == 1:
            say = ''
        elif step == 2:
            say = ''
        elif step == 3:
            say = ''
        elif step == 4:
            say = ''
        elif step == 5:
            say = ''
        elif step == 6:
            say = ''

    
    return say

def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('yes chef',
                'no chef',
                'madder',
                'sweeter',
                'goodbye')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            text = text.lower()
            if 'yes chef' in text:
                advanceRecipe()
            elif 'no chef' in text:
                getAngry()
            elif 'madder' in text:
                getAngry()
            elif 'sweeter' in text:
                getSweet()
            elif 'goodbye' in text:
                break

if __name__ == '__main__':
    main()