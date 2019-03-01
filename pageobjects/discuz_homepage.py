from selenium.webdriver.common.by import By
from framework.base import BasePage
class HomePage(BasePage):
    #登录部分
    home_page_zhanghao=(By.NAME,'username')
    home_page_pw=(By.NAME,'password')
    home_page_button=(By.CSS_SELECTOR,'.fastlg_l .vm em')


    #发帖部分
    fatie_page_moren = (By.CSS_SELECTOR, '.bm_c h2 a')
    fatie_page_biaoti = (By.NAME, 'subject')
    fatie_page_zhengwen = (By.ID, 'fastpostmessage')
    fatie_page_tijiao = (By.ID, 'fastpostsubmit')


    #回帖部分

    huitie_page_huifu=( By.ID,'post_replytmp')
    huitie_page_neirong=(By.ID,'postmessage')
    huitie_page_anniu=(By.ID,'postsubmit')

    #删帖部分
    shantie_page_moren=(By.CSS_SELECTOR, '.bm_c h2 a')
    shantie_page_duihou=(By.NAME,'moderate[]')
    shantie_page_shanchu=(By.LINK_TEXT,'删除')
    shantie_page_queding=(By.ID,'modsubmit')


    #板块管理
    bankuai_page_guanli=(By.LINK_TEXT,"管理中心")
    bankuai_page_luntan=(By.LINK_TEXT,'论坛')
    bankuai_page_add=(By.CSS_SELECTOR,'.lastboard a')
    bankuai_page_delect=(By.NAME,'newforum[1][]')
    bankuai_page_tijiao=(By.ID,'submit_editsubmit')
    bankuai_page_zhandian=(By.CSS_SELECTOR,'.btnlink a')

    #xintie
    xintie_page_xin =(By.CSS_SELECTOR,'.fl_row h2 a')
    xintie_page_biaoti = (By.NAME, 'subject')
    xintie_page_zhengwen = (By.ID, 'fastpostmessage')
    xintie_page_tijiao = (By.ID, 'fastpostsubmit')


    #搜索
    sousuo_path_shuru=(By.ID,'scbar_txt')
    sousuo_path_anniu=(By.ID,'scbar_btn')
    sousuo_path_lianjie=(By.CSS_SELECTOR,'.xs3 a')
    sousuo_path_biaoti=(By.ID,'thread_subject')

    #投票
    fatie_page_moren = (By.CSS_SELECTOR, '.bm_c h2 a')
    toupiao_path_toupiaobutton=(By.ID,'newspecial')
    toupiao_path_faqi=(By.LINK_TEXT,'发起投票')
    toupiao_path_biaoti=(By.ID,'subject')
    toupiao_path_xuanxiang1=(By.XPATH,'//*[@id="pollm_c_1"]/p[1]/input')
    toupiao_path_xuanxiang2=(By.XPATH,'//*[@id="pollm_c_1"]/p[2]/input')
    toupiao_path_tijiao=(By.ID,'postsubmit')
    toupiao_path_xuanze=(By.ID,'option_1')
    toupiao_path_tijia=(By.ID,'pollsubmit')
    toupiao_path_text1=(By.ID,'thread_subject')
    toupiao_path_text2=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[1]/td[1]/label')
    toupiao_path_text3 = (By.CSS_SELECTOR,'.pcht :nth-child(4) :nth-child(2)')
    toupiao_path_text4 = (By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[3]/td[1]/label')
    toupiao_path_text5 = (By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')







    #退出登录
    tuichu_page_tuich = (By.LINK_TEXT, '退出')


    #登录界面
    def denglu(self,zhanghao,mima):
        self.sendkeys(zhanghao,*self.home_page_zhanghao)
        self.sendkeys(mima,*self.home_page_pw)
        self.click(*self.home_page_button)


# class FatiePage(BasePage):
    #发帖部分
    def fatie(self,biaoti,zhengwen):
        self.click(*self.fatie_page_moren)
        self.shuimian(1)
        self.sendkeys(biaoti,*self.fatie_page_biaoti)
        self.sendkeys(zhengwen,*self.fatie_page_zhengwen)
        self.click(*self.fatie_page_tijiao)
        self.shuimian(5)
# class TuichuPage(BasePage):
    #回帖部分
    def huitie(self,neirong):
        self.click(*self.huitie_page_huifu)
        self.sendkeys(neirong,*self.huitie_page_neirong)
        self.click(*self.huitie_page_anniu)


    #删帖部分
    def shantie(self):
        self.click(*self.shantie_page_moren)
        self.click(*self.shantie_page_duihou)
        self.click(*self.shantie_page_shanchu)
        self.click(*self.shantie_page_queding)

    #板块管理部分
    def bankuai(self,name):
        self.click(*self.bankuai_page_guanli)
        self.change_window()
        self.shuimian(1)
        self.click(*self.bankuai_page_luntan)
        self.shuimian(1)
        self.iframe()
        self.click(*self.bankuai_page_add)
        self.sendkeys(name,*self.bankuai_page_delect)
        self.click(*self.bankuai_page_tijiao)
        self.change_window()
        self.click(*self.bankuai_page_zhandian)
        self.shuimian(1)

     #发新帖
    def faxintie(self,biaoti,zhengwen):
        self.click(*self.xintie_page_xin)
        self.shuimian(1)
        self.sendkeys(biaoti,*self.xintie_page_biaoti)
        self.sendkeys(zhengwen,*self.xintie_page_zhengwen)
        self.click(*self.xintie_page_tijiao)
    #搜索标题
    def sousuo(self,neirong):
        self.sendkeys(neirong,*self.sousuo_path_shuru)
        self.shuimian(1)
        self.click(*self.sousuo_path_anniu)
        self.change_window()
        self.click(*self.sousuo_path_lianjie)
        self.jihuo()
        self.change_window()
        p=self.text(*self.sousuo_path_biaoti)
        return p

    #投票内容
    def toupiao(self,biaoti,xuanxiang1,xuanxiang2):
        self.click(*self.fatie_page_moren)
        self.click(*self.toupiao_path_toupiaobutton)
        self.shuimian(1)
        self.jihuo()
        self.click(*self.toupiao_path_faqi)
        self.sendkeys(biaoti,*self.toupiao_path_biaoti)
        self.sendkeys(xuanxiang1,*self.toupiao_path_xuanxiang1)
        self.sendkeys(xuanxiang2, *self.toupiao_path_xuanxiang2)
        self.click(*self.toupiao_path_tijiao)
        self.click(*self.toupiao_path_xuanze)
        self.click(*self.toupiao_path_tijia)
        a=self.text(*self.toupiao_path_text1)
        b=self.text(*self.toupiao_path_text2)
        c=self.text(*self.toupiao_path_text3)
        d = self.text(*self.toupiao_path_text4)
        e = self.text(*self.toupiao_path_text5)

        print(a,b,c,d,e)
    def tuich(self):
        self.change_window()

        self.click(*self.tuichu_page_tuich)
        self.shuimian(3)


