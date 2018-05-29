from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

elems = []
temp = []
u_link = []
u_name = []
m_l = []
driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

def message_read(link):
	driver.get(link)

	driver.implicitly_wait(15)
	main_list = driver.find_element_by_xpath('//*[@id="js_2"]')
	#main_list = WebDriverWait(driver, 10).util(EC.presence_of_element_located("js_2"))
	#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))

	msg_list = main_list.find_elements_by_xpath("//*[@class='_41ud']")

	for i in range (0,len(msg_list)):
		print(str(msg_list[i].find_element_by_tag_name('h5').get_attribute("aria-label")) + " : " ,end='')
		m_l = msg_list[i].find_elements_by_class_name("_aok")
		for k in range (0,len(m_l)):
			print(m_l[k].get_attribute("aria-label"))
		print("\n")
	
	x = input("do u want to reply this conversation : " )
	if(x == 'y' or x == 'Y'):
		msg_p = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/span/br')
		msg = input("Enter message to be send : ")
		#msg_p.click()
		#msg_p.clear()
		#element = driver.find_element_by_css_selector("span.t-input")
		d = input('hhhh')
		#driver.execute_script("arguments[0].innerText = 'hello'", msg_p)
		#msg_p.send_keys(msg)
		
		send_b = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]/div/div[2]/a')
		send_b.click()
		return 1
		
	return 0


username = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

username.click()
username.clear()
password.click()
password.clear()

s_button = driver.find_element_by_id('loginbutton')

username.send_keys('8007679754')
password.send_keys('ramrahim')

s_button.click()

driver.get("https://www.facebook.com/messages/t")

#all_list = driver.find_element_by_class_name('_5l-3 _1ht1 _1ht3')
main_list = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/ul')

elems = main_list.find_elements_by_xpath("//a[@class='_1ht5 _2il3 _5l-3 _3itx']") #get user link

temp = main_list.find_elements_by_xpath("//span[@class='_1ht6']") #get user name


for i in range(0,len(elems)):
	u_link.append(elems[i].get_attribute("data-href"))

#print(u_link)
	
for i in range(0,len(temp)):	
	u_name.append(temp[i].text)

while True:	

	print("Top 10 recent messages from the person are : ")
	for i in range (0,10):
		print(str(i+1) + " : " +str(u_name[i])+"\n")

	print("Enter the index number whose message u want to check : ")

	x = int(input())

	print(str(u_name[x-1]) + " : " + str(u_link[x-1])) 

	z = int(message_read(u_link[x-1]))
	
	if(z == 1):
		u_name[0],u_name[x-1] = u_name[x-1],u_name[0]
		u_link[0],u_link[x-1] = u_link[x-1],u_link[0]
	
	c = input("do u want to contiue (y/n) : ")
	if(c == "N" or c == "n"):
		break;

		
driver.close();



