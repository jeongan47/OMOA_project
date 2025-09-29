from django.apps import AppConfig


class RankingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ranking"

    def ready(self): # 서버가 실행될 때 같이 실행되는 함수
        import os
        from ranking.models import Netflix_movieRank, Netflix_tvRank, Amazon_movieRank, Amazon_tvRank, Disney_Rank, Wavve_movieRank, Wavve_tvRank

        if not os.environ.get('APP'):
            os.environ['APP'] = 'True'
            from ranking.models import Last_update
            from datetime import date
            if not Last_update.objects.all():
                print("no data in update!")
                Last_update.objects.create(last_date = date.today())
                print("made data in update!")

            today = Last_update.objects.order_by('-id').first() # 마지막으로 데이터 크롤링을 한 날짜 담은 테이블의 데이터를 불러오기
            print("마지막 업뎃 날짜: ",today.last_date)
            if not today.last_date == date.today(): # 만약 오늘의 날짜와 마지막 데이터 크롤링을 한 날짜가 다르다면 새로 크롤링을 실행
                print("crwaling start!!!")
                today.delete()
                Last_update.objects.create(last_date = date.today())

                print("오늘 날짜: ",date.today())
                
                netflix_movie_url = "https://www.netflix.com/tudum/top10/south-korea"
                netflix_tv_url = "https://www.netflix.com/tudum/top10/south-korea/tv"
                amazon_movie_url = "https://flixpatrol.com/top10/"
                amazon_tv_url = "https://flixpatrol.com/top10/"
                disney_all_url = "https://www.disneyplus.com/ko-kr"
                wavve_movie_url = "https://www.wavve.com/category/main?mainCode=GN59"
                wavve_tv_url = "https://www.wavve.com/category/main?mainCode=GN56"

                netflix_movieranks = Netflix_movieRank.objects.all()
                netflix_tvranks = Netflix_tvRank.objects.all()
                amazon_movieranks = Amazon_movieRank.objects.all()
                amazon_tvranks = Amazon_tvRank.objects.all()
                disney_ranks = Disney_Rank.objects.all()
                wavve_movieranks = Wavve_movieRank.objects.all()
                wavve_tvranks = Wavve_tvRank.objects.all()

                netflix_movieranks.delete()
                netflix_tvranks.delete()
                amazon_movieranks.delete()
                amazon_tvranks.delete()
                disney_ranks.delete()
                wavve_movieranks.delete()
                wavve_tvranks.delete()

                crawler(netflix_movie_url, "netflix", "movie")
                crawler(netflix_tv_url, "netflix", "tv")
                crawler(amazon_movie_url, "amazon", "movie")
                crawler(amazon_tv_url, "amazon", "tv")
                crawler(disney_all_url, "disney", "all")
                crawler(wavve_movie_url, "wavve", "movie")
                crawler(wavve_tv_url, "wavve", "tv")

                print("crawling Ends!!!!!!!!!")

def crawler(link, platform, mt):
# !!!!!! pip install beautifulsoup4
# !!!!!! pip install lxml 반드시 할 것
# !!!!!! pip install selenium 반드시 할 것
    import time
    from selenium import webdriver
    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen
    from ranking.models import Netflix_movieRank, Netflix_tvRank, Amazon_movieRank, Amazon_tvRank, Disney_Rank, Wavve_movieRank, Wavve_tvRank
        

    if "netflix" in platform: # 넷플릭스일 경우
        page = urlopen(link)
        soup = bs(page, "lxml")

        
        # 수프에 순위 목록 넣기
        m_list = soup.select("tbody > tr")

        if "movie" in mt:
            num = 1
            for m in m_list:
                Netflix_movieRank.objects.create(content_rank = num,
                                                content_name = m.button.text,
                                                content_period = m.select("td")[1].text,
                                                content_img = m.img["src"])
                num += 1
        elif "tv" in mt:
            num = 1
            for m in m_list:
                Netflix_tvRank.objects.create(content_rank = num, # m.span.text
                                            content_name = m.button.text,
                                            content_period = m.select("td")[1].text,
                                            content_img = m.img["src"]) 
                num += 1

    elif "amazon" in platform: # 아마존일 경우

        page = urlopen(link)
        soup = bs(page, "lxml")

        if "movie" in mt: # 영화일 경우
            m_list = soup.select("div#toc-amazon-prime-movies tbody > tr")

            for m in m_list:
                Amazon_movieRank.objects.create(content_rank = m.select("td")[0].text[:-1],
                                                content_name = m.select("td")[1].text.strip(),
                                                content_img = "flixpatrol.com" + str(m.select("td")[1].a.div.picture.img["src"]))

        elif "tv" in mt: # tv프로그램일 경우
            m_list = soup.select("div#toc-amazon-prime-tv-shows tbody > tr")

            for m in m_list:
                Amazon_tvRank.objects.create(content_rank = m.select("td")[0].text[:-1],
                                            content_name = m.select("td")[1].text.strip(),
                                            content_img = "flixpatrol.com" + str(m.select("td")[1].a.div.picture.img["src"]))

    elif "disney" in platform: # 디즈니일 경우
        
        page = urlopen(link)
        soup = bs(page, "lxml")
        
        m_list = soup.select("ul.sliderMedia > li.sliderItem> div > a > div > div > figure > picture > img")
        num = 1
        for m in m_list:
            Disney_Rank.objects.create(content_rank = num,
                                        content_name = str(m["alt"]),
                                        content_img = str(m["src"]))
            num += 1

    elif "wavve" in platform: # 웨이브일 경우

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome()

        driver.get(link)

        time.sleep(5)

        soup = bs(driver.page_source, "lxml")
        
        m_list = soup.select("div.ranking-band div.swiper-wrapper > div")

        if "movie" in mt: # 영화일 경우
            num = 1
            for m in m_list[0:10]:
                Wavve_movieRank.objects.create(content_rank = num,
                                            content_name = m.div.a.select("div")[1].div.picture.img["alt"],
                                            content_img = m.div.a.select("div")[1].div.picture.img["src"])
                num += 1
            driver.quit()

        elif "tv" in mt: # tv프로그램일 경우
            num = 1
            for m in m_list[0:10]:
                Wavve_tvRank.objects.create(content_rank = num,
                                            content_name = m.div.a.select("div")[1].div.picture.img["alt"],
                                            content_img = m.div.a.select("div")[1].div.picture.img["src"])
                num += 1
            driver.quit()
        
