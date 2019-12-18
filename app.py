from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):  # remember to not put your password on github
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll down for us
            time.sleep(2)

            tweetLinks = [i.get_attribute('href')
                          for i in bot.find_elements_by_xpath("//a[@dir='auto']")]  # looking for all the element where they have an attribute dir=auto
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))  # once I have all the hrefs data then I can filter them out to store only the ones with the string "status" in it

            print(filteredLinks)
            for link in filteredLinks:
                bot.get(link)
                time.sleep(3)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(10)

minh = TwitterBot('tuilatrai123','allenwalker1997')
minh.login()
minh.like_tweet('webdevelopment')