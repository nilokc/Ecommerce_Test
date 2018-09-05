import unittest
from datetime import time
from idlelib import browser
from lib2to3.pgen2 import driver

from pip._vendor.distlib.compat import raw_input
from selenium.webdriver.ie import webdriver
from selenium.webdriver.common.keys import Keys
from ikea_package.Main_Code import Main_Automation

class TestCasesAll(Main_Automation):

    def test_FirefoxBrowser(self):
        driver = self.driver
        driver.get('https://www.ikea.com.tr/')
        self.assertIn ( "IKEA Mağazaları", self.get_text(self.value("IKEA_MAGZA")))

                 #def test_IEBrowser(self):
                 #    driver = self.driver
                  #   driver.maximize_window()
                    # driver.implicitly_wait( 20 )
                     #driver.get("https://www.ikea.com.tr/")
                       #self.assertIn("IKEA Mağazaları",self.get_text(self.value("IKEA_MAGZA")))


    def test_setup(self):
        self.setUp()
        self.driver.get(self.value("login_page"))
        self.assertIn("IKEA",self.driver.title)



    def test_browsers(self):

       self.Login()
       self.assertIn("Güvenlik doğrulamasını kontrol ederek tekrar deneyiniz.", self.get_text(self.value("Message")))

    def test_Sign_Up(self):
       self.Siqnup ()
       self.assertIn("Güvenlik doğrulamasını kontrol ederek tekrar deneyiniz.",self.get_text(self.value("Message2")))


    def test_product_code(self):
        self.driver.get ('https://www.ikea.com.tr/')
        self.product_search ( product=self.random_product_no())

        try:
            not_null = self.find_element('rasgele_bulunan_no').text
            self.assertTrue (not_null>0 )

        except:

            self.assertIn ( "IKEA Mağazaları", self.get_text ( self.value ( "IKEA_MAGZA" ) ) )
           # self.assertIn('new', self.driver.title)



    def test_manuel_search(self):
        self.driver.get ( 'https://www.ikea.com.tr/' )
        self.manuel_search()
        self.assertIn("Daha Fazla Bilgi",self.get_text(self.value("more_info")))


    def test_stock_control(self):
        self.stock_control()

        try:
            not_null = self.find_element('stock_text').text
            self.assertTrue(not_null>0)

        except:
            print("out of stock")


    def test_izmir_adress(self):
        self.location_check_izmir_store()
        self.assertIn("Forum Bornova Kazım Dirik Mahallesi 372.Sokak, No:34 PK:35100 Bornova-İzmir",self.get_text(self.value("izmir_adress")))



    def test_facebook_links(self):
        self.facebook_link()
        self.assertTrue("facebook_link")

    def test_twitter_links(self):
        self.twitter_link()
        self.assertTrue("twitter_button")


    def test_pinterest_link(self):

        self.pinterest_link()
        self.driver.get("https://www.pinterest.com/ikeaturkiye/")
        self.assertIn("Pinterest", self.driver.title)
 #       elem = driver.find_element_by_name("q")
 #       elem.send_keys("selenium")
 #       elem.send_keys(Keys.RETURN)
 #       self.assertIn("Pinterest", driver.title)












if __name__ == '__main__':
    unittest.main ()
