from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Github():
    def __init__(self,username,password):
        self.browser=webdriver.Firefox()
        self.username=username
        self.password=password
        self.followerlist=[]
    def sign_İn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        userinput=self.browser.find_element("xpath","//*[@id='login_field']").send_keys(self.username)
        passinput=self.browser.find_element("xpath","//*[@id='password']").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element("xpath","//*[@id='login']/div[4]/form/div/input[13]").click()
    def loadfollowers(self):
        items=self.browser.find_elements("css selector",".d-table.table-fixed.col-12.width-full")
        for i in items:
            self.followerlist.append(i.find_element("css selector",".Link--secondary").text)
    def getFollowers(self,pages,username):
        if pages>=1:
            self.browser.get(f"https://github.com/{username}?tab=followers")
            time.sleep(3)
            items=self.browser.find_elements("css selector",".d-table.table-fixed.col-12.width-full")
            for i in items:
                self.followerlist.append(i.find_element("css selector",".Link--secondary").text)
            count=1
            while True:
                count+=1
                links=self.browser.find_element("class name","paginate-container").find_elements("tag name","a")
                if len(links)==1:
                    if links[0].text=="Next":
                        links[0].click()
                        time.sleep(5)
                        self.loadfollowers()
                    else:
                        break
                else:
                    if len(links)==2:
                        for link in links:
                            if link.text=="Next":
                                link.click()
                                time.sleep(5)
                                self.loadfollowers()
                            else:
                                continue
                if count==pages:
                    self.browser.close()
                    break
        
Username=input("Enter your username")
Password=input("Enter your password")
while True:
    choice=int(input("1-Login to GitHub\n2-Fetch GitHub Follower Data\n3-View follower list\n4-Exit\nChoice: "))
    if  choice==1:
        github=Github(Username,Password)
        github.sign_İn()
    elif choice==2:
        how_many_page=int(input("How many pages do you want? "))
        username=input("Enter the username whose follower list you want to retrieve.")
        github=Github(Username,Password)
        github.getFollowers(how_many_page,username)
    elif choice==3:
        print(github.followerlist)
    else:
        break