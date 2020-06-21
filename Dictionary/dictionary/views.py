from django.shortcuts import render
from nltk.corpus import wordnet
from urllib.request import urlopen,urlretrieve,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import os,shutil
from django import template
# Create your views here.


def get_audio(url,word):
    try:
        url=Request(url,headers={"User-Agent":"Mozilla/5.0"})
        html=urlopen(url)
    except HTTPError as e:
        print(e)
        return
    try:
        bsobj=BeautifulSoup(html,"html.parser")
        data=bsobj.find("div",{"id":"base-pw"}).find("audio").findAll("source")
        urlretrieve(data[1]['src'],'%s_new.mp3'%word)
        shutil.move('/home/saurabh/basic_django/mysite/%s_new.mp3'%word,'/home/saurabh/basic_django/mysite/dictionary/static/%s_new.mp3'%word)

    except AttributeError as e:
        print(e)
        return

def home(request):
	return render(request,'home.html')

def meaning(request):
	word=request.POST["search"]
	url="https://www.dictionary.com/browse/%s?s=t"%word
	get_audio(url,word)
	name='%s_new.mp3'%word
	data=wordnet.synsets(word)

	try:
		heading=data[0].lemmas()[0].name()
		define=data[0].definition()
	except:
		heading=None
		define=None
	examples=[]
	synonyms=set()
	antonyms=set()
	for d in data:
		examples.append(d.examples())
		for l in d.lemmas():
			synonyms.add(l.name())
			if l.antonyms():
				for a in l.antonyms():
					antonyms.add(a.name())
	examples=examples[:3]
	context={'name':name,'heading':heading,'define':define,'examples':examples,'synonyms':synonyms,'antonyms':antonyms}
	return render(request,'content.html',context)
