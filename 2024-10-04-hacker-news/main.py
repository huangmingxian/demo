import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
from rich import print

class HackerNewsScraper:
    def __init__(self, pages=1):
        """
        初始化爬虫
        
        :param pages: 要爬取的页面数量
        """
        self.base_url = "https://news.ycombinator.com/"
        self.pages = pages
    
    def fetch_page(self, url, max_retries=3):
        """
        获取指定URL的页面内容
        
        :param url: 要获取的页面URL
        :param max_retries: 最大重试次数
        :return: 解析后的BeautifulSoup对象
        """
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # 如果响应状态不是200，将引发HTTPError异常
                return BeautifulSoup(response.text, 'html.parser')
            except requests.RequestException as e:
                print(f"获取页面时发生错误 (尝试 {attempt + 1}/{max_retries}): {e}")
                if attempt + 1 < max_retries:
                    time.sleep(2)  # 在重试之前等待2秒
        
        print("无法获取页面，达到最大重试次数")
        return None
    
    def parse_stories(self, soup):
        """
        从BeautifulSoup对象中解析新闻条目
        
        :param soup: BeautifulSoup对象
        :return: 包含新闻信息的字典列表
        """
        stories = []
        for item in soup.find_all('tr', class_='athing'):
            try:
                title_link = item.find('span', class_='titleline').find('a')
                if not title_link:
                    continue
            
                title = title_link.text
                url = title_link['href']
                
                subtext = item.find_next_sibling('tr')
                if not subtext:
                    continue
            
                score_span = subtext.find('span', class_='score')
                points = score_span.text.split()[0] if score_span else '0'
                
                stories.append({
                    'title': title,
                    'url': url,
                    'points': points
                })
            except AttributeError as e:
                print(f"解析条目时出错: {e}")
            except Exception as e:
                print(f"处理条目时发生未知错误: {e}")
        
        return stories
    
    def save_to_csv(self, stories, filename):
        """
        将新闻条目保存到CSV文件
        
        :param stories: 包含新闻信息的字典列表
        :param filename: 要保存的CSV文件名
        """
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'url', 'points'])
            writer.writeheader()
            writer.writerows(stories)
    
    def run(self):
        """
        运行爬虫的主方法
        
        获取多个页面、解析新闻、保存结果
        """
        all_stories = []
        for page in range(1, self.pages + 1):
            url = f"{self.base_url}news?p={page}"
            print(f"正在爬取第 {page} 页...")
            soup = self.fetch_page(url)
            if soup is None:
                print(f"无法获取第 {page} 页，跳过")
                continue
            
            stories = self.parse_stories(soup)
            all_stories.extend(stories)
            
            if page < self.pages:
                time.sleep(2)  # 在请求之间添加延迟，以避免对服务器造成过大压力
        
        if not all_stories:
            print("未找到任何新闻条目")
            return
        
        filename = f"hacker_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.save_to_csv(all_stories, filename)
        print(f"已保存 {len(all_stories)} 条新闻到 {filename}")

if __name__ == "__main__":
    pages_to_scrape = int(input("请输入要爬取的页面数量: "))
    scraper = HackerNewsScraper(pages=pages_to_scrape)
    scraper.run()
