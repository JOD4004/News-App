from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi=NewsApiClient(api_key='...............')
    if request.method=='POST':
        q=request.POST['word']
        headlines=newsapi.get_top_headlines(q=q)
    else:
        headlines=newsapi.get_top_headlines()

    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    
    return render(request,'index.html',{'mylist':mylist})

def business(request):
    newsapi=NewsApiClient(api_key='.................')
    headlines=newsapi.get_top_headlines(category='business')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'business.html',{'mylist':mylist})

def entertainment(request):
    newsapi=NewsApiClient(api_key='.................')
    headlines=newsapi.get_top_headlines(category='entertainment')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'entertainment.html',{'mylist':mylist})

def general(request):
    newsapi=NewsApiClient(api_key='.....................')
    headlines=newsapi.get_top_headlines(category='general')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'general.html',{'mylist':mylist})

def health(request):
    newsapi=NewsApiClient(api_key='...................')
    headlines=newsapi.get_top_headlines(category='health')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'health.html',{'mylist':mylist})

def science(request):
    newsapi=NewsApiClient(api_key='.........................')
    headlines=newsapi.get_top_headlines(category='science')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'science.html',{'mylist':mylist})

def sports(request):
    newsapi=NewsApiClient(api_key='........................')
    headlines=newsapi.get_top_headlines(category='sports')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'sports.html',{'mylist':mylist})

def technology(request):
    newsapi=NewsApiClient(api_key='.........................')
    headlines=newsapi.get_top_headlines(category='technology')
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist=zip(news,desc,img,url)
    return render(request,'technology.html',{'mylist':mylist})
