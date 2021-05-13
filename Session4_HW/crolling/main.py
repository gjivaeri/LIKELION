#-*- encoding: utf-8 -*-
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import csv
file = open('movie.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

def extract_info(movie_list):
    final_result = []
    for movie in movie_list:
        title = movie.find("dt", {"class" : "tit"}).find("a").text
        img_src = movie.find("div", {"class" : "thumb"}).find("img")['src']
        star = movie.find("div", {"class" : "star_t1"}).find("span", {"class" : "num"}).text

        details = movie.find("dl", {"class" : "info_txt1"}).find_all("dd") 
        released_date = details[0].text.replace("\t","").replace("\n","").replace("\r","").replace("개봉", "").split("|")[-1]
        director_name = details[1].text
        if len(details) == 2:
            actor_name = None
        else:
            actor_name = details[2].text

        movie_info = {
        'title' : title,
        'img_src' : img_src,
        'star' : star,
        'released': released_date,
        'director': director_name,
        'actor': actor_name
        }

        final_result.append(movie_info)
    for result in final_result:
        row = []
        row.append(result['title'])
        row.append(result['img_src'])
        row.append(result['star'])
        row.append(result['released'])
        row.append(result['director'])
        row.append(result['actor'])
        writer.writerow(row)
    return final_result 