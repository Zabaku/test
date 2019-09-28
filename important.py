# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents, OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode,LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from urllib.parse import urlencode, quote
from pathlib import Path
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
import time, random, sys, json, codecs, subprocess, re,urllib.request,urllib.error,urllib.parse, os, shutil, requests, timeit, ast, pytz, threading, atexit, traceback, base64, pafy, livejson, timeago, math, argparse

try:
    if __modified__ != 'Zero Cool':
        sys.exit('++ Error : Please use lib linepy-modified, you can find it on github')
except Exception as e:
    sys.exit('++ Error : Please use lib linepy-modified, you can find it on github')
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def update_non_existing_inplace(original_dict, to_add):
    for key, value in original_dict.items():
        if key not in to_add:
            to_add[key] = value
        if type(value) == dict:
            for k, v in value.items():
                if k not in to_add[key]:
                    to_add[key][k] = v
    original_dict.update(to_add)
    return original_dict

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'
        
def sendTemplate(to, data):
    kiki = LiffChatContext(to)
    ratedit = LiffContext(chat=kiki)
    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))