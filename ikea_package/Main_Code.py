import logging
import random
import re
import unittest
# from lib2to3.pgen2 import driver
from lib2to3.pgen2 import driver

from selenium import webdriver

from ikea_package.Easy_Locators import locators




# from selenium.webdriver.ie.webdriver import WebDriver


class Main_Automation(unittest.TestCase):
    logger = logging.getLogger('LogResults')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
    logger.addHandler(ch)
    logging.basicConfig(filename='logresults.log', filemode='w', level=logging.DEBUG )

    logger.debug ( 'debug message' )
    logger.info ( 'info message' )
    logger.warn ( 'warn message')
    logger.error('error message')
    logger.critical('critical message')

    #driver: WebDriver = webdriver.Firefox ()
    #driver: WebDriver = webdriver.Ie()
    #driver.set_page_load_timeout ( 20 )

    def setUp(self):
       self.driver = self.browser("ie")
       self.driver.set_page_load_timeout ( 30 )
       self.driver.maximize_window ()
       self.driver.implicitly_wait ( 30 )

    #def setUp(self):
      #  self.driver = webdriver.Firefox ()
     #   self.driver.set_window_size ( 1920, 1080 )
    #    self.driver.maximize_window ()
   # def setUp(self):
     #   self.driver = webdriver.ie()
    #    self.driver.set_window_size( 1920, 1080 )
    #    self.driver.maximize_window()



    def browser(self, browser):

        if browser == 'chrome':
            return webdriver.Chrome()
        elif browser == 'firefox':
            return webdriver.Firefox()
        elif browser == 'ie':
            return webdriver.Ie()
        elif browser == 'safari':
            return webdriver.Safari()
        elif browser == 'opera':
            return webdriver.Opera ()
        elif browser == 'edge':
            return webdriver.Edge ()

#    def get_url(self):
#       return self.driver.current_url


    def value(self, Easy_Locators):
        return locators[Easy_Locators][0]

    def find_element(self, xpath):
        xpath_value = self.value(xpath)
        return self.driver.find_element_by_xpath( xpath_value )

    def get_text(self, element):
        return self.driver.find_element_by_xpath ( element ).text

    def set_text(self, element, value):
        #self.wait_until_element_located(element)
        #self.find_element(element).clear()
        self.find_element(element).send_keys(value)


    def random_product_no(self):
        product_number = "%d.%d.%d" % (random.randint(000,999), random.randint(000,999), random.randint(00,99))
        return product_number



    def recaptcha(self):
        frame = driver.find_element_by_xpath ( '//iframe[contains(@src, "recaptcha")]' )
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath ( "//*[@id='recaptcha-anchor']" )

    def Login(self):

        self.driver.get ( self.value ( "enter_for_login_page" ) ) #web browser sayfayi açması için gerekli

        self.find_element("member_email_textbox").send_keys("nilarolat@gmail.com")
        self.find_element("member_password_textbox").send_keys("nilABC1919")
        self.find_element ( "member_login_button" ).click ()
        #self.recaptcha ()
        #self.find_element("member_captcha_button").click()
        #self.driver.switch_to.alert.accept ()
        #driver.quit()


    def Siqnup(self):

        self.driver.get(self.value("new_signup_link"))
        self.find_element("new_form_name").send_keys("nil")
        self.find_element ( "new_form_surname" ).send_keys ( "okcu" )
        self.find_element("new_form_email").send_keys("asd@gmail.com")
        self.find_element("new_form_bday").send_keys("01.01.1980")
        self.find_element("new_form_password").send_keys("asd10ABC")
        self.find_element("new_form_repeat_pass").send_keys("asd10ABC")
        self.find_element("new_form_mobile_no").send_keys("541111111")
        self.find_element("new_form_sex").click()
        self.find_element("gender_choise").click()
        self.find_element("ikea_check_box").click()
        self.find_element("notification_box").click()
        self.find_element("register_button").click()
        #driver.quit()

#ürün kodunu random olarak atayarak aramak!
    def product_search(self,product):
        self.find_element("product_search_box").click()
        self.set_text(element='product_search_box',value=product)
        self.find_element("search_button").click()
        self.find_element("alertx").click()

    def manuel_search(self):
        self.find_element("product_search_box").click()
        self.find_element("product_search_box").send_keys("303.273.08")
        self.find_element("search_button").click()
        print("Product's name is : %s " %(self.find_element('product_name').text))
        print ("Price is : %s " % (self.find_element ( 'product_price' ).text))
        print ("Product info is : %s " % (self.find_element ( 'product_info' ).text) )


       # self.logger.info ( " [*] Create new user : %s %s, should succeed." % (first_name, last_name) )


    def stock_control(self):
        self.driver.get ( 'https://www.ikea.com.tr/' )
        self.find_element("product_search_box").click()
        self.find_element("product_search_box").send_keys("303.273.08")
        self.find_element("search_button").click()
        self.find_element("stock_store_control").click()
        self.find_element("stock_control_combobox").click()
        self.find_element("combobox_izmir").click()
        self.find_element("check_stock_button").click()


    def location_check_izmir_store(self):
        self.driver.get ( 'https://www.ikea.com.tr/' )
        self.find_element("bize_ulasin").click()
        self.find_element("izmir_sube").click()


    def facebook_link(self):
        self.driver.get('https://www.ikea.com.tr/')
        self.find_element("facebook_link").click()

    def twitter_link(self):
        self.driver.get('https://www.ikea.com.tr/')
        self.find_element("twitter_button").click()

    def pinterest_link(self):
        self.driver.get ( 'https://www.ikea.com.tr/' )
        self.find_element("pinterest_button").click()
        #self.driver.quit()






       # browser = webdriver.Firefox ()  # Get local session of firefox
       # browser.get ( "http://www.yahoo.com" )  # Load page
       # assert "Yahoo!" in browser.title
       # elem = browser.find_element_by_name ( "p" )  # Find the query box
        #driver.quit ()  # Close the browser window








#    def social_media_check(self):
#        self.driver.get ( 'https://www.ikea.com.tr/' )
#        driver.find_element_by_xpath ("/html/body/form/header/div[5]/div[2]/a[1]").click ()

#NOT: Find fonksiyonu ile bir string içindeki linki çekebilir, yazdırabilirsin/ import re (regular expression)
#    def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
   #     url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
   #     return url
    #string = 'Link for facebook : https://www.facebook.com/IKEATurkiye'
   #print ( "Urls: ", Find(string))






















