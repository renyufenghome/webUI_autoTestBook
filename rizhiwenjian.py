import logging
#创建一个logging对象
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



#日志输出至哪里  handler
ch=logging.StreamHandler()   #日志输出至控制台
fh=logging.FileHandler('./tools')   #日志输出至文件夹
logger.addHandler(ch)  #添加对应的方法
logger.addHandler(fh)


# 日志输出的格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelnams)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)