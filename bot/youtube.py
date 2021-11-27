# -*- coding: utf-8 -*-
import re
from typing import cast
from data import config
import aiohttp
import asyncio

import csv
from aiohttp_requests import requests
from lxml import html
from urllib.parse import urljoin
from urllib import parse
import json

channelcrawler_link = "https://channelcrawler.com"


class YouTube:
    """Parser"""

    csv_filename = ""
    csv_file = ""
    output = []
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=windows-1251'}
    payload = {
            "_method": "POST",
            "data[query][name]": "",
            "data[query][min_published_on]": "",
            "data[query][max_published_on]": "",
            "data[query][min_subs]": "",
            "data[query][max_subs]": "",
            "data[query][min_views]": "",
            "data[query][max_views]": "",
            "data[query][min_videos]": "",
            "data[query][max_videos]": "",
            "data[query][min_last_video_date]": "",
            "data[query][max_last_video_date]": "",
            "data[query][description]": "",
            "query[category_id][]": [],
            "query[country_id][]": [],
            "query[language_id][]": [],
            "query[topic_id][]": []
        }

    def __init__(self) -> None:
        self.output = []
        self.csv_filename = self.csv_file = ""

    async def __youtube_video_desc_parse__(self, id):
        content = ""

        headers = {"Accept-Language": "en-US,en;q=0.5"}
        page = await requests.get(f'https://www.youtube.com/watch?v={id}', headers=headers)
        json_data = re.compile('ytInitialData = ({.*?});', re.DOTALL)
        text = await page.text()
        data = json.loads(json_data.search(text).group(1))

        try:
            if data.get("contents"):
                desc = data["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][1]["videoSecondaryInfoRenderer"].get("description")
                if desc:
                    desc = desc.get("runs")
                    if desc:
                        for txt in desc:
                            content += txt.get("text")
        except: pass

        content = content.replace("\n", " ").replace("\n\n", " ").replace("\r\n", " ").replace("\r", " ")
        return content

    async def __youtube_video_parse__(self, url):
        video_id = ""

        headers = {"Accept-Language": "en-US,en;q=0.5"}
        page = await requests.get(f'{url}/videos', headers=headers)
        json_data = re.compile('ytInitialData = ({.*?});', re.DOTALL)
        text = await page.text()
        data = json.loads(json_data.search(text).group(1))

        try:
            if data.get("contents"):
                tabs = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]

                for t in tabs:
                    if t.get("tabRenderer"):
                        if t["tabRenderer"].get("title") == "Videos":
                            videos = t["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]
                            if videos.get("gridRenderer"):
                                if videos.get("gridRenderer").get("items"):
                                    video_id = videos["gridRenderer"]["items"][0]["gridVideoRenderer"]["videoId"]

        except: pass
        return await self.__youtube_video_desc_parse__(video_id)

    async def __youtube_about_parse__(self, url):
        social_links = []
        active = False
        desc = ""

        headers = {"Accept-Language": "en-US,en;q=0.5"}
        page = await requests.get(f'{url}/about', headers=headers)
        json_data = re.compile('ytInitialData = ({.*?});', re.DOTALL)
        text = await page.text()
        data = json.loads(json_data.search(text).group(1))

        print(url)
        if data.get("contents"):
            active = True
            tabs = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]

            for t in tabs:
                if t.get("tabRenderer"):
                    if t["tabRenderer"].get("title") == "About":
                        links = t["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"].get("primaryLinks")
                        if links:
                            for link in links:
                                raw_url = link["navigationEndpoint"]["urlEndpoint"]["url"]
                                url_start = 3 + raw_url.find('&q=')
                                soc_url = parse.unquote_plus(raw_url[url_start:len(raw_url)])

                                social_links.append(soc_url)

            desc = await self.__youtube_video_parse__(url)

        output = {'links': social_links, 'active': active, 'first_desc': desc}
        return output

    async def __channelcrawler_parse__(self, page):
        text = await page.text(encoding='utf-8', errors='ignore')
        response = html.fromstring(text)

        i = 0
        row = response.xpath("//div[contains(@class,'channel')]")
        for each_row in row:
            youtube = await self.__youtube_about_parse__(each_row.xpath('//h4[1]/a[1]/@href')[i])

            self.output.append({
                'Channel Name': (each_row.xpath('.//h4/a/@title')[:1] or [None])[0],
                'Link': each_row.xpath('//h4[1]/a[1]/@href')[i],
                'Description':(each_row.xpath('.//small/following-sibling::a/@title')[:1] or [None])[0].replace("\n", " "),
                'Category':(each_row.xpath('.//h4/following-sibling::small/b/text()')[:1] or [None])[0],
                'Subscriber':( (each_row.xpath('normalize-space(.//p[1]/small/text()[1])').split(' ')) [:1] or [None])[0],
                'Total videos':( (each_row.xpath('normalize-space(.//p[1]/small/text()[2])').split(' ')) [:1] or [None])[0],
                'Total Views':( (each_row.xpath('normalize-space(.//p[1]/small/text()[3])').split(' ')) [:1] or [None])[0],
                'Country':( each_row.xpath('.//h4/img/@title') [:1] or [None])[0],
                'Links': youtube['links'],
                'Active': youtube['active'],
                'Content': youtube['first_desc']
            })

            i += 1
    
        next_page = response.xpath('//ul[@class="pagination"]/li[@class="next"]/a/@href')
        if next_page:
            url = urljoin(channelcrawler_link, next_page[0])
            await self.__channelcrawler_parse__(await requests.get(url))

    def set_channel_subs_min(self, data):
        self.payload["data[query][min_subs]"] = data

    def set_channel_subs_max(self, data):
        self.payload["data[query][max_subs]"] = data

    def set_channel_views_min(self, data):
        self.payload["data[query][min_views]"] = data

    def set_channel_views_max(self, data):
        self.payload["data[query][max_views]"] = data

    def set_channel_creation_min(self, data):
        self.payload["data[query][min_published_on]"] = data

    def set_channel_creation_max(self, data):
        self.payload["data[query][max_published_on]"] = data

    def set_channel_latest_min(self, data):
        self.payload["data[query][min_last_video_date]"] = data

    def set_channel_latest_max(self, data):
        self.payload["data[query][max_last_video_date]"] = data

    def set_channel_videos_min(self, data):
        self.payload["data[query][min_videos]"] = data

    def set_channel_videos_max(self, data):
        self.payload["data[query][max_videos]"] = data

    def set_channel_name(self, data):
        self.payload["data[query][name]"] = data

    def set_channel_keywords(self, data):
        self.payload["data[query][description]"] = data

    def add_category(self, id):
        self.payload["query[category_id][]"].append(id)

    def add_country(self, id):
        self.payload["query[country_id][]"].append(id)

    def add_country(self, id):
        self.payload["query[country_id][]"].append(id)

    def add_language(self, id):
        self.payload["query[language_id][]"].append(id)

    def add_topic(self, id):
        self.payload["query[topic_id][]"].append(id)


    def set_csv_filename(self, filename):
        self.csv_filename = filename

    async def get_channels_info(self):

        self.csv_file = f'temp/{self.csv_filename}.csv'
        header = ["Channel Name", "Link", "Description", "Category", "Subscriber", "Total videos", "Total Views", "Country", "Links", "Active", "Content"]
        page = await requests.post('https://www.channelcrawler.com/ru', data=self.payload, headers=self.headers)
        print(page.url)
        with open(self.csv_file, 'w', encoding='utf-8-sig',newline='') as f: 
            w = csv.DictWriter(f, header, delimiter ='$')
            w.writeheader()
            await self.__channelcrawler_parse__(page)
            for i in self.output: w.writerow(i)


