# import re
#
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '0', content)
# print(content)

import re

import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result[1])

#
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
# if result:
#     print(result.group(1), result.group(2))


# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s(\d\d\d)\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# import re
#
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))

# import re
#
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)


# import re
#
# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result.group())


# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
#
#
# import re
#
# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))


# import json
# import requests
# from requests.exceptions import RequestException
# import re
# import time
#
#
# def get_one_page(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None
#
#
# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>', re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             #'time': item[4].strip()[5:],
#             #'score': item[5] + item[6]
#         }
#
#
# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#
#
# def main(offset):
#     url = 'http://maoyan.com/board/6?offset=' + str(offset)
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         main(offset=i * 10)
#         time.sleep(1)