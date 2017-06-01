#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '73a62055c012487b9312db1d7ac7de61'


def aiQurey(text):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'sv'  # optional, default value equal 'en'

    request.session_id = "2"

    request.query = text

    response = request.getresponse()

    return response.read()

