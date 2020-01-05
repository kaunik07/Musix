import requests
from lxml import html
from bs4 import BeautifulSoup

def songSearch():
    pageUrl = 'https://chiasenhac.vn/tim-kiem?q='
    mode="&filter=ten-bai-hat"
    s= input('Enter the song name : ')
    page = requests.get(pageUrl+s+mode).text
    # tree = html.fromstring(page.content)
    # song = tree.xpath('//*[@id="nav-music"]/ul/li[1]/div[2]/div/h5/a/span/font/font')

    soup = BeautifulSoup(page,'lxml')
    link=[]

    #song
    song=[]
    for i in soup.find_all("h5", class_="media-title mt-0 mb-0"):
        r=i.a
        song.append(r.get("title"))
        link.append(r.get("href"))

    #artist
    artistFind = soup.find_all("div",class_="author")
    artist=[]
    for i in range(5,len(artistFind)):
        artist.append(str(artistFind[i]))
    
    for i in range(len(artist)):
        # print(type(i))
        s1 = artist[i].find(">")+1
        s2 = artist[i].find("<",2)
        t=artist[i][s1:s2]
        artist[i]=t

    n=len(artist)

    #print search list
    for i in range(n):
        print(i+1,". ",song[i]," - ",artist[i])

    return (song,artist,link)


