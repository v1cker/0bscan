# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 9:51 PM
# @Author  : zer0i3
# @File    : waf_config.py.py

class WafConfig(object):

    PAYLOADS_LIST = [
        "<frameset><frame src=\"javascript:alert('XSS');\"></frameset>",
        " AND 1=1 ORDERBY(1,2,3,4,5) --;",
        "><script>alert(\"testing\");</script>",
        " AND 1=1 UNION ALL SELECT 1,NULL,1,'<script>alert(\"666\")</script>',table_name FROM information_schema.tables WHERE 2>1--/**/; EXEC xp_cmdshell('cat ../../../etc/passwd')#",
        "<img src=\"javascript:alert(\'XSS\');\">",
        "'))) AND 1=1,SELECT * FROM information_schema.tables ((('",
        "' )) AND 1=1 (( ' -- rgzd",
        ";SELECT * FROM information_schema.tables WHERE 2>1 AND 1=1 OR 2=2 -- qdEf '",
        "' OR '1'=1 '\"",
        "') OR \"a\"=\"a --",
        "<scri<script>pt>alert('123');</scri</script>pt>",
        ";CAT1_GALLERY_1 UNION ALL SELECT (SELECT CAST(CHAR(114)+CHAR(51)+CHAR(100)+CHAR(109)+CHAR(48)+CHAR(118)+CHAR(51)+CHAR(95)+CHAR(104)+CHAR(118)+CHAR(106)+CHAR(95)+CHAR(105)+CHAR(110)+CHAR(106)+CHAR(101)+CHAR(99)+CHAR(116)+CHAR(105)+CHAR(111)+CHAR(110) AS NVARCHAR(4000))),NULL--"
    ]