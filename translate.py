#!/usr/bin/env python

import sys
import re
import json
# if (sys.version_info[0] < 3):
#     import urllib2
#     import urllib
#     import HTMLParser
# else:

import html.parser
import urllib.request
import urllib.parse

agent = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}

user_lang = "hi"

def unescape(text):
    # if (sys.version_info[0] < 3):
    #     parser = HTMLParser.HTMLParser()
    # else:
    parser = html.parser.HTMLParser()
    return (parser.unescape(text))


def translate(to_translate, to_language="auto", from_language="auto"):
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    # if (sys.version_info[0] < 3):
    #     to_translate = urllib.quote_plus(to_translate)
    #     request = urllib2.Request(link, headers=agent)
    #     raw_data = urllib2.urlopen(request).read()
    # else:
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    request = urllib.request.Request(link, headers=agent)
    raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)

def detect_language(query):
    query = urllib.parse.quote(query)
    base_link = "http://apilayer.net/api/detect?access_key=ce52dd6e5323750069aebf6b9e1a6582&query=%s"
    link = base_link % (query)

    request = urllib.request.Request(link, headers=agent)

    raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode('utf-8')
    return json.loads(data)

def translate_to_english(query):
    lang = detect_language(query)
    lang_code = lang["results"][0]["language_code"]
    user_lang = lang_code
    result = translate(query, "en", user_lang)

    return result

def translate_from_english(query, to_language=user_lang):
    result = translate(query, to_language, "en")

    return result