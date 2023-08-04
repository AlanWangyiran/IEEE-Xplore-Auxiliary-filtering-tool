# Author: ALan Wang
# Date: 2023-08-04
# All rights reserved, do not copy or distribute without permission

import requests
import jsonpath
import time
import pandas as pd
from tqdm import tqdm


def again_ip():

    tunnel = ""

    username = ""
    password = ""

    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }
    return proxies


def ieee(key,page):
    cookies = {
        'fp': '5f9d8b849d21fdf428d756ded20274ea',
        's_ecid': 'MCMID%7C17104739619710553583090421869932477196',
        'cookieconsent_status': 'dismiss',
        'WLSESSION': '203580044.20480.0000',
        'TS01b03060': '012f350623c72893aff2baafa13f5e9d9c4e2bff14f003a949a2a5efa5e23844f13b6304d50c68fc63773f1a000c404c9adb79a78d',
        'JSESSIONID': 'o4e5Y3lhMj2ydf0DUePeL91nI1bu8S2iPqsBkPjZN0wsMgK0AvFB!-564931762',
        'ipCheck': '123.125.173.99',
        '__gads': 'ID=ca3911ea61c699f4:T=1691032460:RT=1691032460:S=ALNI_MY_7fUOWY6dirPbEF_wzrttVBWlUQ',
        '__gpi': 'UID=00000c267859ab51:T=1691032460:RT=1691032460:S=ALNI_MagaFqYtYbTnls3NtWgPpjy6h-mtg',
        'AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg': '1',
        'AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg': '359503849%7CMCIDTS%7C19573%7CMCMID%7C17104739619710553583090421869932477196%7CMCAAMLH-1691637260%7C11%7CMCAAMB-1691637260%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1691039660s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19545%7CvVersion%7C5.0.1',
        's_cc': 'true',
        'cto_bundle': 'P8BJBl9KenBtS2w3MzNyOVptTFB4R0d0S0F4QlBCakdSTndSMHFBbkVQd0o0d2tkeHZNRXZIZGtCQ3pvVTd2bzhBOW91Ykw1eWg1UjNTMTBWMkpUa3lVaHZuejdIMGJBb2ROak9iSURkczRlZ2Y3V2slMkJQTkRndEtyUGlidnFZNHdhTm4wSmJVVFY0aGthWjlEempGMUwlMkZzR3VRJTNEJTNE',
        'TSaeeec342027': '080f8ceb8aab20002244b78d1a292af34eb95460787462142058828be53067c7baa158b318e8e05908e5c96de5113000888c84ed54acaf6b2eb53afd1991dc9b3b31ce3497c327f7201025ae6f7c1c62f221785a8af6b895c603b4029b093105',
        'utag_main': 'v_id:0189065e6009000f19ab26b77c4f0506f003d06700bd0$_sn:3$_se:10$_ss:0$_st:1691034435462$vapi_domain:ieee.org$ses_id:1691032459972%3Bexp-session$_pn:4%3Bexp-session',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'fp=5f9d8b849d21fdf428d756ded20274ea; s_ecid=MCMID%7C17104739619710553583090421869932477196; cookieconsent_status=dismiss; WLSESSION=203580044.20480.0000; TS01b03060=012f350623c72893aff2baafa13f5e9d9c4e2bff14f003a949a2a5efa5e23844f13b6304d50c68fc63773f1a000c404c9adb79a78d; JSESSIONID=o4e5Y3lhMj2ydf0DUePeL91nI1bu8S2iPqsBkPjZN0wsMgK0AvFB!-564931762; ipCheck=123.125.173.99; __gads=ID=ca3911ea61c699f4:T=1691032460:RT=1691032460:S=ALNI_MY_7fUOWY6dirPbEF_wzrttVBWlUQ; __gpi=UID=00000c267859ab51:T=1691032460:RT=1691032460:S=ALNI_MagaFqYtYbTnls3NtWgPpjy6h-mtg; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=359503849%7CMCIDTS%7C19573%7CMCMID%7C17104739619710553583090421869932477196%7CMCAAMLH-1691637260%7C11%7CMCAAMB-1691637260%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1691039660s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19545%7CvVersion%7C5.0.1; s_cc=true; cto_bundle=P8BJBl9KenBtS2w3MzNyOVptTFB4R0d0S0F4QlBCakdSTndSMHFBbkVQd0o0d2tkeHZNRXZIZGtCQ3pvVTd2bzhBOW91Ykw1eWg1UjNTMTBWMkpUa3lVaHZuejdIMGJBb2ROak9iSURkczRlZ2Y3V2slMkJQTkRndEtyUGlidnFZNHdhTm4wSmJVVFY0aGthWjlEempGMUwlMkZzR3VRJTNEJTNE; TSaeeec342027=080f8ceb8aab20002244b78d1a292af34eb95460787462142058828be53067c7baa158b318e8e05908e5c96de5113000888c84ed54acaf6b2eb53afd1991dc9b3b31ce3497c327f7201025ae6f7c1c62f221785a8af6b895c603b4029b093105; utag_main=v_id:0189065e6009000f19ab26b77c4f0506f003d06700bd0$_sn:3$_se:10$_ss:0$_st:1691034435462$vapi_domain:ieee.org$ses_id:1691032459972%3Bexp-session$_pn:4%3Bexp-session',
        'Origin': 'https://ieeexplore.ieee.org',
        'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=super%20resolution&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&pageNumber=10',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    num = 0
    list2 = []
    for a in range(1,int(page)+1):
        json_data = {
            'newsearch': True,
            'queryText': key,
            'highlight': True,
            'returnType': 'SEARCH',
            'matchPubs': True,
            'pageNumber': a,
            'returnFacets': [
                'ALL',
            ],
        }
        #proxies = again_ip()

        response = requests.post('https://ieeexplore.ieee.org/rest/search',
                                cookies=cookies,
                                headers=headers,
                                json=json_data,
                                #proxies=proxies,
                                verify=False)
        res_json = response.json()
        for b in res_json['records']:

            time.sleep(0.5)

            title = b['articleTitle']

            publicationTitle = b['publicationTitle']

            year = b['publicationYear']

            authors = '; '.join(jsonpath.jsonpath(b,'$..searchablePreferredName'))

            url = b['documentLink']
            url = 'https://ieeexplore.ieee.org' + url

            list2.append([title, publicationTitle, year, authors,url])
            num += 1
            shijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            print(f"获取{num}条数据成功-----{title}-----{shijian}")
    print(f"已完成候选列表采集，共{num}条数据。")
    return list2

def to_execel(list2):
    shijian = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

    df = pd.DataFrame(list2,columns=['title', 'publicationTitle', 'year', 'authors', 'url'])

    #df.to_excel(f".//ieee_{shijian}.xlsx", index=False)
    tmp_name = "ieee_" + shijian
    df.to_excel(f"D:\\CodeSpace\\{tmp_name}.xlsx", index=False)
    print("数据已保存。")
def loading_CCF():
    df_CCF = pd.read_excel("CCF_list.xlsx", header=0)
    return df_CCF
def filter(paper_list):
    print("开始进行资格筛选")
    df_CCF = loading_CCF() #符合资质的会议期刊
    final_list = []
    count = 0
    for paper in tqdm(paper_list):
        date = int(paper[2])
        if(date >= 2018): #近五年的论文
            sources = paper[1]
            Abbr = ""
            if "(" in sources and ")" in sources: #若存在缩写
                left = sources.index("(")
                right = sources.index(")")
                # 从左括号到右括号之间的子字符串中提取字母部分Clipped Hyperbolic Classifiers
                for char in sources[left + 1:right]:
                    if char.isalpha():
                        Abbr += char #获取缩写
                for element in df_CCF['Abbr']:
                    if type(element) != str: #跳过空行
                        continue
                    #element = element.replace(" ", "")#修正一下格式
                    if Abbr in element: #符合期刊会议资质
                        First_author = paper[3].split(';')
                        paper[3] = First_author[0] #找到第一作者
                        count = count + 1
                        final_list.append(paper)
                        print(f"已找到{count}条符合资格数据。")
            else: #若不存在缩写
                for name in df_CCF['Full Name']:
                    if name in sources: #符合期刊会议资质
                        First_author = paper[3].split(';')
                        paper[3] = First_author[0]  # 找到第一作者
                        count = count + 1
                        final_list.append(paper)
                        print(f"已找到{count}条符合资格数据。")

    print("已完成筛选。")
    return final_list





if __name__ == '__main__':

    key = input("请输入查询关键字：")
    page = input("请输入爬取页数：")
    pre_df = ieee(key,page)
    to_execel(pre_df)
    final_df = filter(pre_df)
    to_execel(final_df)
