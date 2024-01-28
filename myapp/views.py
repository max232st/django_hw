# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main = '''
<h2>Framework Django</h2>
    '''
    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Я студент GB!!!</h2>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)
