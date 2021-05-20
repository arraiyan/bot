from telegram.inline.inputinvoicemessagecontent import InputInvoiceMessageContent
import inf
from inf import system_vars as env
from langdetect import detect#thisa will detect language
from textblob import TextBlob

##





####here we gonna write our additional functions
def is_other_links(message,chat_id):
    valid = True;
    verify = message
    verify=verify.lower()
    forbidden_links = env.forbidden_links
    for forbidden_link in forbidden_links:
        if forbidden_link in verify:
            valid = False
            break
    return valid

def language_detect(message):
    #language_type=detect(message)
    is_en=True
    text = str(message)
    if len(text)>3 or len(text)==3:
        lang = TextBlob(text)
        language_type=lang.detect_language()
        print(language_type)
        if not language_type == 'en':
            is_en=False
            return is_en
    else:
        return True
    return is_en

def if_it_is_forbidden_language(message):
    validation=False
    words=env.forbidden_words
    verify=message
    verify=str(verify).lower()
    for word in words:
        if word in verify:
            validation = True
            return validation
    return validation
def give_coustom_messages(message):
    data=dict()
    words=env.auto_response_keys
    message = message.lower()
    for x,y in words.items():
        if x in message:
            data[x]=y
    return data
def switch_user():
    brief=inf.system_vars.admin_to_general
    if brief:
        inf.system_vars.admin_to_general=False
    if not brief:
        inf.system_vars.admin_to_general=True

def captcha_(message):
    m=str(message)
    m=m.replace("captcha","")
    value=int(m)
    if value==env.r1[0]+env.r1[1]:
        env.captcha_is_enabled=False
        print('solved')
        return True
    return 0

def e_cap():
    env.captcha_required=True
def d_cap():
    env.captcha_required=False