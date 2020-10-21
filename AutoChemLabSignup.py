from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def run():

	#Login Info
	SCusr = "email" #Schoology Login Email
	SCpwd = "password" #Schoology Login Password
	SGusr = "email" #Sign Up Genius Username
	SGpwd = "password" #Sign Up Genius Password

	browser = webdriver.Chrome()
	time.sleep(1)
	try:
		browser.get("https://fortbendisd.schoology.com")
		time.sleep(1)

		browser.find_element_by_id("i0116").send_keys(SCusr)
		browser.find_element_by_class_name("btn.btn-block.btn-primary").click()#find_element_by_id("idSIButton9").click()
		time.sleep(2)

		browser.find_element_by_id("i0118").send_keys(SCpwd)
		browser.find_element_by_id("idSIButton9").click()
		time.sleep(1)
		
		browser.get("https://fortbendisd.schoology.com/course/2174800011/updates")
		updateText = browser.find_element_by_class_name("update-body.s-rte").text
		signUpURL = "https://" + updateText.split("\n")[1].split("https://")[1]#"https://www.signupgenius.com/go/9040E4AA8AA2EABF85-test"#
		browser.get("https://www.signupgenius.com/register")

		browser.find_element_by_tag_name("html").send_keys(Keys.END)
		browser.find_element_by_id("email").send_keys(SGusr)
		browser.find_element_by_id("pword").send_keys(SGpwd)
		browser.find_element_by_id("loginBtnId").click()

		now = datetime.now()
		future = datetime(now.year, now.month, now.day,15,0)
		print(str(now)+" "+str((future-now).total_seconds()))
		time.sleep(max(0,(future-now).total_seconds()))

		#print("Reached Sign Up at: " + str(datetime.now()))
		browser.get(signUpURL)
		time.sleep(1)
		
		browser.find_element_by_tag_name("html").send_keys(Keys.END)
		time.sleep(1)
		browser.find_element_by_class_name("SUGbutton.rounded").click()

		browser.find_element_by_class_name("giantsubmitbutton.rounded.link_cursor").click()
		time.sleep(1)

		browser.find_element_by_class_name("btn.btn-lg.btn-success.ng-binding").click()
		print("Successfully Signed Up at: " + str(datetime.now()))
		time.sleep(3)

	except Exception as e:
		print(str(e))
		browser.close()
		time.sleep(1)
		run()

	browser.close()


def main():
	now = datetime.now()
	future = datetime(now.year,now.month,now.day,14,45) #24-hour time of when to begin running program
	
	print((future-now).total_seconds())
	time.sleep((future-now).total_seconds())
	
	run()		
    

if __name__ == '__main__':
    main()