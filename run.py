#!/usr/bin/python
#  -*- coding:utf-8 -*-

# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import pyodbc
# import numpy as np
import urllib.request
import json
# import os
import time

def getDataFromDouban(s):
    # 数据字典
    data = {}
    data['q'] = s
    # data['count'] = '50'

    # 注意Python2.x的区别
    url_values = urllib.parse.urlencode(data)

    # print(url_values)

    url = "https://api.douban.com/v2/book/search?"
    full_url = url + url_values

    result = urllib.request.urlopen(full_url).read()
    z_data = result.decode('UTF-8')
    # print(class(z_data))
    # print(z_data)
    z_data = json.loads(z_data)
    # print(z_data)
    # print(z_data['books'][0]['tags'])
    result = {}
    for book in z_data['books']:
        for tag in book['tags']:
            if tag['name'] in result:
                result[tag['name']] = result[tag['name']] + 1
            else:
                result[tag['name']] = 0
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    ans = set()
    cnt = 0
    for obj in result:
        ans.add(obj[0])
        cnt = cnt + 1
        if cnt>=3:
            break
    # print(result)
    return ans


# conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=127.0.0.1,1433;DATABASE=libData;UID=sa;PWD=xu695847')
# cursor = conn.cursor()

# y = [[] for i in range(3)]
#
# x = [[] for i in range(3)]
# xx = ['本科生','正式职工',"硕士研究生"]
# sum = 0

if __name__ == '__main__':
    cnt = 0

    file_object1 = open("file1.txt",'r',encoding='utf-8')
    f1 = open("fileout1.txt", "w", encoding='utf-8')
    try:
      while True:
          line = file_object1.readline()
          if line:
              line = line[:-1]
              line = line.lstrip()
              result = getDataFromDouban(line)
              time.sleep(8)
              ans = line
              for str in result:
                # print(str)
                ans = ans + ',' + str
              cnt = cnt + 1
              print(cnt,ans)
              f1.writelines(ans+'\n')
              if(cnt==5):
                  break
          else:
              break
    finally:
        file_object1.close()
        f1.close()

# ok = 0
# for i in xx:
#     str1 = "select count(CONVERT(varchar(100), date, 12)),CONVERT(varchar(100), date, 12),peopleKind from enter_data where peopleKind = '"+i+"' group by CONVERT(varchar(100), date, 12),peopleKind order by CONVERT(varchar(100), date, 12)"
# str1 = "select History_Title from book_key"
# cursor.execute(str1)
# rows = cursor.fetchall()
# print(rows)
# f1 = open("file1.txt","w",encoding='utf-8')
# f2 = open("file2.txt","w",encoding='utf-8')
# f3 = open("file3.txt","w",encoding='utf-8')
# for row in rows:
#     cnt = cnt + 1
#     print(cnt,row[0])
#     if cnt<7856:
#         f1.writelines(row[0]+'\n')
#     elif cnt<17856:
#         f2.writelines(row[0]+'\n')
#     else:
#         f3.writelines(row[0]+'\n')
#
# f1.close()
# f2.close()
# f3.close()

# for row in rows:
    # str1 = str(row[0])
    # cnt = cnt + 1
    # try:
    #     y[cnt].append(row[0])
        # if cnt == 0:
        # x[cnt].append(row[1])
        # xx.append(cnt*100)
        # y.append(row[0]*1.0)
        # x.append(row[1])
    # except:
    #     print(row)
#         sum = sum + row[0]
# cnt = cnt + 1
    # if cnt < 10186:
    #     print("人数 = "+str(cnt),"总数 = "+str(sum),"比例 = "+str(sum/1404148*100)+"%")
    # print(x,y)
# plt.figure(figsize=(8,4))

# npy = np.array(y);
# ymean = npy.mean();
# ys = np.sqrt(((npy-ymean)**2).sum()/(npy.size - 1))
#
# print(ys)
#
# npy2 = (npy - ymean)/ys;
# y[0] = y[1]
# fig,ax = plt.subplots(3)
# mpl.rcParams['font.sans-serif'] = ['simHei']
# mpl.rcParams['axes.unicode_minus'] = False
# # draw_pie(x,y)
# # print(len(x))
# # x = np.array(x)
#
# colors = ['black','red','darkseagreen','gray','lightsteelblue','palevioletred','skyblue','yellowgreen','violet']
# lines = ['-','-.',':']
# i = 0
# # plt.title(u'日期-入馆次数')
# for sp in ax:
#     y1 = np.array(y[i])
#     x1 = np.array(x[i])
#     sp.plot(x1,y1,linestyle = lines[i],label=xx[i],color = colors[0],marker='x')
#     sp.legend(loc='upper left')
#     sp.set_xlabel(u'日期')
#     sp.set_ylabel(u'人数')
#     if i == 0 :
#         sp.set_title(u'日期-入馆次数')
#     i = i + 1
#         # plt.plot(x, y[i], color=colors[i], label=xx)
#     # plt.plot(x,y[i],color=colors[i],'r')
# # plt.bar(x,y,0.4,color="green")
# # plt.xticks(np.arange(cnt)+100,x)
# # plt.xlabel(u'日期')
# # plt.ylabel(u'人数')
#
# # plt.xlim(230,900)
# # plt.ylim(-20,40)
# plt.show()
