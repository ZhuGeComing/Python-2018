
import requests
from bs4 import BeautifulSoup as bs

class Douban:
    '''
    豆瓣爬虫类
    '''
    def __init__(self):
        '''
        类的初始化函数
        '''
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0"
        }

    def run(self):
        '''
        类的主体函数
        '''
        self.crawling_movieTop250()

    def crawling_movieTop250(self):
        '''
        爬取电影top250
        '''
        baseUrl = "https://movie.douban.com/top250?start="
        num = 0
        while num < 250:
            response = requests.get(baseUrl+str(num), headers=self.headers)
            soup = bs(response.text, "lxml")
            response.close()
            divs = soup.find_all("div", { "class": "hd" })
            spans = soup.find_all("span", { "class": "rating_num" })
            for item1, item2 in zip(divs, spans):
                bdyLink = self.crawling_bdyLink(item1.a.span.text)
                print(item1.a.span.text, item2.text)
                print(bdyLink)
                self.write_to_file(item1.a.span.text+" "+item2.text+"\n"+bdyLink+"\n\n")
            num += 25
        print("\n爬取已完成")

    def crawling_bdyLink(self, resourceName):
        '''
        爬取电影的百度云链接
        # 根据百度网盘搜索引擎来查找资源的，用的是pansoso
        '''
        rep = requests.get("http://www.pansoso.com/zh/"+resourceName, headers=self.headers)
        soup2 = bs(rep.text, "lxml")
        rep.close()
        res = soup2.find("a", { "target": "_blank" })
        if res:
            url = "http://www.pansoso.com" + res.get("href")
            rep = requests.get(url, headers=self.headers)
            soup3 = bs(rep.text, "lxml")
            rep.close()
            res = soup3.find("a", { "class": "red" })
            if res:
                rep = requests.get(res.get("href"), headers=self.headers)
                soup4 = bs(rep.text, "lxml")
                rep.close()
                res = soup4.find("a", { "class": "btn-download" })
                return res.parent.text.replace("百度网盘", res.get("href"))
        return ""

    def write_to_file(self, text):
        '''
        爬取数据写入文件
        '''
        with open("res.txt", "a", encoding="utf8") as fp:
            fp.write(text)


# mian
if __name__ == "__main__":
    myDouban = Douban()
    myDouban.run()

