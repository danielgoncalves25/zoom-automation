import csv
import time
from selenium import webdriver
import pyautogui

# Based URL for UMass Boston zoom meetings.
zoomUrl = 'https://umassboston.zoom.us/j/'
targetClass = str(input('Enter your class: ' ))

foundClass = False
meetingId = ''
meetingPassword = ''

# Read through the csv file and extract the meeting Id and the password
with open('class.txt') as classList:
    classes = csv.reader(classList, delimiter=',')
    for row in classes:
        currentClass = row[0]
        if currentClass == targetClass:
            foundClass = True
            meetingId = row[1]
            meetingPassword = row[2]
            break

if foundClass:
    zoomUrl += f'{meetingId}#success'
    driver = webdriver.Chrome('./chromedriver.exe')
    # Opens Chrome browser
    driver.get(zoomUrl)
    # Click the launched meeting button, opens up Zoom
    launch = driver.find_element_by_class_name('_1FvRrPS6').click()
    time.sleep(5)
    driver.quit()
    # Types the password in the Zoom application
    pyautogui.write(meetingPassword)
    # Clicks join meeting button
    pyautogui.click(x=960, y=650)
    # Closes the browser
else:
    print(f'{targetClass} was not found in the file. Please check if you typed in the current ')