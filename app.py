import time
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("https://www.pingodoce.pt")

#Aceitar cookies 
time.sleep(3)
btnAcceptCookis=driver.find_element("id", "onetrust-accept-btn-handler").click()
if btnAcceptCookis:
      btnAcceptCookis.click()
#Pesquisar 
imputSearch=driver.find_element("name", "s")
imputSearch.send_keys("Receitas de Panquecas")
imputSearch.send_keys(Keys.RETURN)

#Contar  'panquecas'
el=driver.find_elements('xpath',"//div[@class='search-results']//*[contains( translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'panquecas')]")
print('Total  de palavra panquecas - ',len(el))





  


