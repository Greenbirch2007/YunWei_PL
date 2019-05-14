


import os




themes =['１．Python语言与Linux系统管理',"2.python生态工具","３．打造命令行工具","４．文本处理","５．linux系统管理","６．使用python监控linux系统","７．文档于报告","８．网络","9.python自动化管理","１０．深入浅出Ａnsible","11.使用python打造mysql专家系统"]

base = "/home/g/YunWei_PL/过书目/Python Linux系统管理与自动化运维/"
for i in themes:
    file_name = base + str(i)
    os.mkdir(file_name)