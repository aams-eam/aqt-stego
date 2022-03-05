from counter_bytes_tags2 import contadortags
from counter_bytes_tags2 import contadorcomillas
from attPosition import total_capacity as count_total_att
from attPosition import max_bits_line as max_bits_att_line
import requests
from requests.exceptions import ConnectionError
import html
import pandas as pd
import matplotlib.pyplot as plt
import re


def find_tags_line (input):

    matches = re.findall(r'<(.*?)>', input)
    return matches


def web_counter_att(htmlresponse):

    num = 0 # total num of attributes

    # expand tags in one line to multiple lines
    tags = []
    for line in htmlresponse:
        tags += find_tags_line(line)

    # count bits in attributes base on the expanded lines
    for t in tags:
        complete = "<"+t+">"
        num += max_bits_att_line(complete)

    return num

def web_counter_tags(html_read):
	'''print(elem)'''
	tags=0
	for line in html_read:
		tags+=contadortags(line)
		'''print(tags)'''
	return tags

def web_counter_quotes(html_read):
	'''print(elem)'''
	quotes=0
	for line in html_read:
		quotes+=contadorcomillas(line)
		'''print(tags)'''
	return quotes

def web_counter_characters(html_read):
	'''print(elem)'''
	size=0
	for line in html_read:
		characters=list(line)
		size+=len(characters)
		'''print(size)'''
	return size

def web_counter_lines(html_read):
	'''print(elem)'''
	lines=0
	for line in html_read:
		lines+=1
		'''print(lines)'''
	return lines



def test():
    webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/']#,'https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']
    x = web_counter_att(webpage_list)
    print(x)



def main():

    try:

        df = pd.read_csv("50topStatistics.csv")

    except FileNotFoundError as e:

        print("50topStatistics.csv does not exist, creating...")

        webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/','https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']


        lines = []
        characters = []
        att_cap = []
        quotes_cap = []
        tag_cap = []

        for elem in webpage_list:

            print("URL:", elem.upper())

            # hacer peticion html
            r = requests.get(elem)
            htmlresponse = html.unescape(r.text)
            html_lines = htmlresponse.splitlines()
            html_linesb = [l.encode('utf-8') for l in html_lines]
            # calcular estadística solo de ese html
            print("COUNTING...")
            lines.append(web_counter_lines(html_linesb))
            print("lines counted")
            characters.append(web_counter_characters(html_linesb))
            print("characters counted")
            att_cap.append(web_counter_att(html_lines))
            print("attributes counted")
            quotes_cap.append(web_counter_quotes(html_linesb))
            print("quotes counted")
            tag_cap.append(web_counter_tags(html_linesb))
            print("tags counted")
            print()
            print()

        df = pd.DataFrame({"page": webpage_list,"characters": characters,"lines": lines, "att_cap": att_cap, "quotes_cap": quotes_cap, "tag_cap": tag_cap})
        df.to_csv("50topStatistics.csv", index=False)

        df = pd.read_csv("50topStatistics.csv")



    df['totalbits'] = df['characters']*8
    df['att_percentage'] = 100*(df['att_cap']/df['totalbits'])
    df['quotes_percentage'] = 100*(df['quotes_cap']/df['totalbits'])
    df['tag_percentage'] = 100*(df['tag_cap']/df['totalbits'])

    # sort df by totalbits ascending
    df.sort_values('totalbits', ascending=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df[['totalbits', 'att_percentage', 'quotes_percentage', 'tag_percentage']].head())

    fig,ax = plt.subplots(3, figsize=(12,6))
    ax[0].plot(df.index.to_list(), df.att_percentage.to_list(), color="green", label="att encoding")
    ax[1].plot(df.index.to_list(), df.quotes_percentage.to_list(), color="red", label="quote encoding")
    ax[2].plot(df.index.to_list(), df.tag_percentage.to_list(), color="orange", label="tag encoding")
    ax[0].axhline(df.att_percentage.mean(), color="green", linestyle="dashed", label="att encoding mean")
    ax[1].axhline(df.quotes_percentage.mean(), color="red", linestyle="dashed", label="quote encoding mean")
    ax[2].axhline(df.tag_percentage.mean(), color="orange", linestyle="dashed", label="tag encoding mean")
    ax[2].set_xlabel("Webpage index")
    ax[1].set_ylabel("Encoding capacity over total bits capacity (%)")
    ax[0].set_title("Capacity of encoding in top 50 visited pages")
    ax[0].grid(True)
    ax[1].grid(True)
    ax[2].grid(True)
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.show()




if __name__ == '__main__':
    main()
    # test()
