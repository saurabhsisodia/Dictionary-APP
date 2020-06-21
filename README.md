# Dictionary-APP

### Dictionary Application using Django, NLTK, WebScraping ###

- #### Download Pronunciation of the given word from [Dictionary.com](www.dictionary.com) using WebScraping(urllib,bs4) ####

```
'url="https://www.dictionary.com/browse/%s?s=t"%word'
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
 ```
 - #### Find the meaning,synonyms and antonyms with examples of the given word using NLTK.corpus.wordnet ####
 
 ```
 from nltk.corpus import wordnet
 data=wordnet.synsets(word)
 heading=data[0].lemmas()[0].name()
 define=data[0].definition()
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
```

##### For Full code [Click Here](https://github.com/saurabhsisodia/Dictionary-APP/blob/master/Dictionary/dictionary/views.py) #####
