from selenium import webdriver
from selenium.webdriver.common.by import By
import time

liste = ["Deutschland", "Vereinigte Staaten", "China", "Russland", "Frankreich", "Indien", "Brasilien", "Kanada", "Spanien", "Japan", "Mexiko", "Australien", "Italien", "Argentinien", "Südafrika", "Indonesien", "Vereinigtes Königreich", "Niger", "Ägypten", "Schweden", "Polen", "Türkei", "Iran", "Nigeria", "Ukraine", "Pakistan", "Chile", "Demokratische Republik Kongo", "Portugal", "Republik Kongo", "Irak", "Norwegen", "Südkorea", "Thailand", "Bangladesch", "Peru", "Algerien", "Finnland", "Schweiz", "Neuseeland", "Österreich", "Saudi-Arabien", "Vietnam", "Kasachstan", "Kolumbien", "Mongolei", "Dänemark", "Marokko", "Nordkorea", "Philippinen", "Niederlande", "Belgien", "Irland", "Afghanistan", "Griechenland", "Sudan", "Äthiopien", "Island", "Kenia", "Malaysia", "Venezuela", "Belarus", "Bolivien", "Syrien", "Ghana", "Mali", "Tschad", "Tschechien", "Laos", "Libyen", "Myanmar", "Tansania", "Tunesien", "Ungarn", "Estland", "Kroatien", "Lettland", "Rumänien", "Serbien", "Angola", "Israel", "Jemen", "Namibia", "Nepal", "Oman", "Taiwan", "Albanien", "Kambodscha", "Kuba", "Litauen", "Somalia", "Uruguay", "Bulgarien", "Paraguay", "Südsudan", "Vereinigte Arabische Emirate", "Ecuador", "Kamerun", "Luxemburg", "Panama", "Senegal", "Sri Lanka", "Togo", "Uganda", "Bosnien und Herzegowina", "Kosovo", "Malta", "Singapur", "Slowakei", "Slowenien", "Usbekistan", "Vatikanstadt", "Andorra", "Haiti", "Liechtenstein", "Madagaskar", "Monaco", "Guatemala", "Honduras", "Katar", "Mauretanien", "Mosambik", "Zypern", "Armenien", "Benin", "Bhutan", "Botswana", "Costa Rica", "Elfenbeinküste", "Jamaika", "Jordanien", "Libanon", "Sambia", "San Marino", "Simbabwe", "Turkmenistan", "Aserbaidschan", "Eritrea", "Fidschi", "Gabun", "Gambia", "Georgien", "Guinea", "Kirgisistan", "Malawi", "Moldawien", "Montenegro", "Nicaragua", "Nordmazedonien", "Papua-Neuguinea", "Ruanda", "Zentralafrikanische Republik", "Bahamas", "Bahrain", "Belize", "Brunei", "Burkina Faso", "Burundi", "Dominikanische Republik", "El Salvador", "Guyana", "Kuwait", "Lesotho", "Liberia", "Malediven", "Nauru", "Palau", "Suriname", "Tadschikistan", "Tonga", "Antigua und Barbuda", "Barbados", "Dominica", "Dschibuti", "Eswatini", "Föderierte Staaten von Mikronesien", "Grenada", "Guinea-Bissau", "Kap Verde", "Kiribati", "Komoren", "Mauritius", "Osttimor", "Salomonen", "Samoa", "São Tomé und Príncipe", "Seychellen", "Sierra Leone", "St. Kitts und Nevis", "St. Lucia", "St. Vincent und die Grenadinen", "Trinidad und Tobago", "Tuvalu", "Vanuatu", "Äquatorial-Guinea", "Marshallinseln"]

driver = webdriver.Safari()
driver.get("https://www.jetpunk.com/user-quizzes/1268665/rette-die-menschheit-indem-du-lander-erratst")

time.sleep(8)
driver.switch_to.frame("gdpr-consent-notice")
driver.find_element(By.XPATH, '//*[@id="save"]').click()

time.sleep(2)
driver.switch_to.default_content()

time.sleep(2)
bt = driver.find_element(By.XPATH, '//*[@id="start-button"]').click()

time.sleep(0.25)
bo = driver.find_element(By.XPATH, '//*[@id="txt-answer-box"]')

for el in liste:
    bo.clear()
    bo.send_keys(el)

time.sleep(600)

driver.quit()