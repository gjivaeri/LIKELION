import requests
from bs4 import BeautifulSoup
from main import extract_info


MOVIE_URL = 'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")
movie_list_box = movie_soup.find("ul", {"class" : "lst_detail_t1"})
movie_list = movie_list_box.find_all('li')

print(extract_info(movie_list))