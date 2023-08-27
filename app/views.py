from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    topicname = input('enter topicname:')
    Tobj = Topic.objects.get_or_create(topic_name=topicname)[0]
    Tobj.save()
    return HttpResponse('Inserted a data')

def insert_webpage(request):
    topicname = input('enter a topicname:')
    Tobj = Topic.objects.get_or_create(topic_name=topicname)[0]
    Tobj.save()
    webname = input('enter a name:')
    weburl = input('enter url:')
    Wobj = Webpage.objects.get_or_create(topic_name=Tobj,Name=webname,Url=weburl)[0]
    Wobj.save()
    return HttpResponse('data inserted')

def insert_accesrecord(request):
    topicname = input('enter a topicname:')
    Tobj = Topic.objects.get_or_create(topic_name=topicname)[0]
    Tobj.save()
    webname = input('enter a name:')
    weburl = input('enter url:')
    Wobj = Webpage.objects.get_or_create(topic_name=Tobj,Name=webname,Url=weburl)[0]
    Wobj.save()
    date = input('enter date:')
    author = input('enter author:')
    email = input('enter a mail:')
    Aobj = Accessrecord.objects.get_or_create(Name=Wobj,Date=date,Author=author,Email=email)[0]
    Aobj.save()
    return HttpResponse('data inserted successfully....')