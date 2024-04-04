from django import template
from django.urls import reverse # from django.urls for Django >= 2.0
from django.urls import resolve # from django.urls for Django >= 2.0
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import gettext_lazy 
import json
from django.conf import settings
import environ

env = environ.Env()
environ.Env.read_env()

register = template.Library()


              
@register.tag(name='translate_url')
def do_translate_url(parser, token):
    language = token.split_contents()[1]
    return TranslatedURL(language)
    

class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language
    def render(self, context):
        request_language = self.language
        requested_path=context['request'].path.split('/')[1]
        path=''
        domain=''
        with open('app\paths.json', 'r',encoding="utf8") as j:
            contents = json.loads(j.read())

        for content in range(len(contents)):
            for cont in range(len(contents[content])):
                for key, value in contents[content]['mainpath'].items():
                    requested_path=context['request'].path.split('/')[1]
                    if value=='/'+requested_path:
                        path=contents[content]['mainpath'][request_language]
        with open('app\domains.json', 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
        for data in range(len(dom)):
            for key,value in dom[data].items():
                if key==request_language:
                    domain=value
        returnpath=domain+path
        print("returnpath",returnpath)
        return returnpath
