from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
import environ
import json
env = environ.Env()
environ.Env.read_env()


def landingfunction(request):
    domain=''
    domain_status=False
    path_status=False
    main_domain = request.build_absolute_uri().split('/')[2]
    requested_domain_without_port=main_domain.split(':')[0]

    with open('app\domains.json', 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filter_domain=value.split('/')[2]
            filter_domain_without_port=filter_domain.split(':')[0]
            if requested_domain_without_port == filter_domain_without_port :
                domain=value
                domain_status=True
                lang=key
    with open('app\paths.json', 'r',encoding="utf8") as j:
            contents = json.loads(j.read())
    path_render='/'
    for content in range(len(contents)):
        for cont in range(len(contents[content])):
            for key, value in contents[content]['mainpath'].items():
                if value == '/home':
                    path_render=contents[content]['mainpath'][lang]
                    path_status=True
    if domain_status and path_status:
        requested_domain_without_port=main_domain.split(':')[0]
        # request.session[settings.LANGUAGE_SESSION_KEY] = lang
        response = HttpResponseRedirect(domain+path_render)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response
    else:
        response = render(request, 'errors/404.html')
        response.status_code = 404
        return response


def home(request):
    print("inside home function")
    return render(request, 'index.html')

def aboutus(request):
    print("inside about function")
    return render(request, 'about.html')

def services(request):
    print("inside services function")
    return render(request, 'services.html')


def RenderPageWithPathAndLang(request, path):
    lang=''
    domain=''
    domain_status=False
    path_status=False
    main_domain = request.build_absolute_uri().split('/')[2]
    requested_domain_without_port=main_domain.split(':')[0]
    with open('app\domains.json', 'r',encoding="utf8") as j:
            dom = json.loads(j.read())
    for data in range(len(dom)):
        for key,value in dom[data].items():
            filter_domain=value.split('/')[2]
            filter_domain_without_port=filter_domain.split(':')[0]
            if requested_domain_without_port == filter_domain_without_port :
                domain=value
                lang=key
                domain_status=True
    
    with open('app\paths.json', 'r',encoding="utf8") as j:
        contents = json.loads(j.read())
    path_render='/'
    for content in range(len(contents)):
        for cont in range(len(contents[content])):
            for key, value in contents[content]['mainpath'].items():
                if value == request.path:
                    path_render=value
                    lang=key
                    path_status=True

    if domain_status and path_status:
        # request.session[settings.LANGUAGE_SESSION_KEY] = lang
        response = HttpResponseRedirect(domain+path_render)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response
    else:
        response = render(request, 'errors/404.html')
        response.status_code = 404
        return response