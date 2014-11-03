#!/usr/bin/env python
'''
Created on 2014.11.03

@author: fubo01
'''
from django.http import HttpResponse;
import hashlib;
def check_token(dictParas):
    TOKEN = 'fbwinghsa';
    sig = dictParas['signature'];
    liData = [TOKEN,dictParas['timestamp'],dictParas['nonce']];
    liData.sort();
    strCont = ''.join(liData);
    strRet = hashlib.sha1(strCont).hexdigest();
    if(strRet == sig):
        return 1;
    return 0;
def parse_message(dictParas):
    #parse message
    dictMessage = {};
    return (1,dictMessage);
def process_message(dictInfo):
    #Add more process(To-Do)
    strRet = '';
    return (1,strRet);
def generate_echo_message(strRet):
    #create echo message
    strResp = '';
    return (1,strResp)
def interface(request):
    #html = "<html><head>hello</head><body>"+request.GET['access_token']+"</body></html>";
    dict_get = request.GET;
    dict_post = request.POST;
    ret = 1;
    strResponse = '';
    if(dict_get.keys()!=[]):
        #get request token
        ret = check_token(dict_get);
        if(ret == 1):
            return HttpResponse(dict_get['echostr']);
        else:
            print "[Error] token failed";
            return HttpResponse('');
    if(request.method == 'POST'):
        #get request message
        (code,dictInfo) = parse_message(dict_post);
        if(code != 1):
            print "[Error] Error message";
            return HttpResponse('');
        (code,strRet) = process_message(dictInfo);
        if(code != 1):
            print "[Error] Error message process";
            return HttpResponse('');
        (code,strRep) = generate_echo_message(strRet);
        if(code != 1):
            print "[Error] Error create response";
            return HttpResponse('');
        HttpResponse(strRep);
    print "[Error] No request"
    return HttpResponse('');
