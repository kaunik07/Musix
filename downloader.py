import requests
from lxml import html
from bs4 import BeautifulSoup
from search import *
from tqdm import tqdm
# import wget
import os

def downloadSong():
    song,artist,pageUrl=songSearch()
    num=list(map(int,input("Enter the song number: ").split()))
    n=len(num)

    for i in num:
        page=requests.get(pageUrl[i-1]).text
        soup = BeautifulSoup(page,'lxml')

        songDown = soup.find_all("a",class_="download_item")[1]
        url = songDown.get("href")
        # print(os.path.dirname(os.path.abspath(__file__)))
        filename=os.path.dirname(os.path.abspath(__file__))+"/Downloads/"+song[i-1]+"-"+artist[i-1].replace(";",",")+".mp3"
        name=song[i-1]+"-"+artist[i-1].replace(";",",")+".mp3"
        # wget.download(url,name)
        

        # print(DownLink)
        print("Downloading *-----------* "+name)
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        t=tqdm(total=total_size, unit='iB', unit_scale=True)
        # filename=song[i-1]+" - "+artist[i-1]
        with open(filename, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")
        print()
    print("done!!!")
