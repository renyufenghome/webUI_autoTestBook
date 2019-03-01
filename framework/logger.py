import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):
        # 创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq=time.strftime("%Y%m%H%M",time.localtime(time.time()))
        # log_path=os.path.dirname(os.getcwd()+ '/Logs/')  项目根目录下/Logs  保存日志
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        #如果case组织结构式 /testsuit/featuremode/xxx。py，那么得到的相对路径的父路径就是项目跟目录
        log_name=log_path +rq +'.log'
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)


        #定义handler的输出格式
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

    def getlog(self):
            return self.logger