#!/usr/bin/python3
# coding=utf-8
import os
import re
from unittest import result
from atlassian import Confluence
import traceback


"""This example shows how to export pages """

confluence = Confluence(url="http://c.hsyuntai.com:80/", username="ytdenglt", password="denglt@202211")


def save_page(pageId,fileName,childPath):
    subPath=childPath.split('/')
    cPath= os.getcwd()
    for i in range(len(subPath)):
        cPath= os.path.join(cPath,subPath[i])
        if(os.path.exists(cPath)==False):
            os.mkdir(cPath)
    fileFullName = cPath + "/"+ fileName + ".doc"
    file = open(fileFullName, "wb")
    response = confluence.get_page_as_word(pageId)
    file.write(response)
    file.close()
    print(fileFullName,"Completed")

def savePageChildByPageId(pPageId,pPageTitle):
    page_ge = confluence.get_page_child_by_type(pPageId, type='page', start=None, limit=500, expand=None)
    pages = list(page_ge)
    if (len(pages) == 0):
        return 0
    pattern = re.compile(r'(?<=pageId=)\d+')
    for i in range(len(pages)):
        webui = pages[i]['_links']['webui']
        pageId = pattern.findall(webui)[0]
        pageTitle = pages[i]['title']
        pageTitle = pageTitle.replace('/',':')
        if (savePageChildByPageId(pageId,pPageTitle+"/"+pageTitle) == 0):
            save_page(pageId, pageTitle, pPageTitle)
    return 1

if __name__ == "__main2__":
    spaces = ["pha"]
    for space in spaces:
        pages = confluence.get_all_pages_from_space(space=space, start=0, limit=10000)
        for i in range(len(pages)):
            print(i,':',pages[i]['title'],pages[i]['_links']['webui'])
       
        start_data ="2015/02/15"
        end_data ="2022/12/01"
        # cqls='space="{}" and type="page" and created <="{}" and created >="{}"'.format(space, end_data,start_data)
        cqls='space="{}" and type="page" '.format(space)

        answers = confluence.cql(cqls, start=0,limit= 10000 ,expand=True)["results"]

        pattern = re.compile(r'(?<=pageId=)\d+')
        for i in range(len(answers)):
            try:
                if(answers[i]['content']['type'] == 'page' and answers[i]['excerpt'] != ''):
                    webui = answers[i]['content']['_links']['webui']
                    pageId = pattern.findall(webui)[0]
                    page_title = answers[i]['content']['title']
                    print(i,':',page_title,webui)
                   # response = confluence.get_page_as_word(pageId)
                   # save_file(response, page_title, space)
                    pass
            except Exception as e:
                traceback.print_exc()
                print(e)
            else:
                # 未发生错误
                pass
    
if __name__ == "__main__":
    savePageChildByPageId(2228181,"药商后台")