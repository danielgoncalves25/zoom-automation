import csv
import time
from selenium import webdriver
import pyautogui

# Based URL for UMass Boston zoom meetings.
# zoomUrl = 'https://umassboston.zoom.us/j/'
zoomUrl = 'https://us02web.zoom.us/j/'
targetClass = str(input('Enter your class: ' ))

foundClass = False
meetingId = ''
meetingPassword = ''
# print(time.now())
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
    driver = webdriver.Chrome('B/chromedriver.exe')
    # Opens Chrome browser and go to Zoom link
    driver.get(zoomUrl)
    driver.find_element_by_class_name('_1FvRrPS6').click()
    time.sleep(1)
    #Locate Open Zoom Button
    btn = pyautogui.locateOnScreen("Buttons/zoom_meeting_btn.png")
    pyautogui.moveTo(btn)
    pyautogui.click()
    # Closes the browser
    driver.quit()
    # Types the password in the Zoom application
    pyautogui.write(meetingPassword)
    time.sleep(1)
    # Locate Join Meeting Buttton
    btn = pyautogui.locateOnScreen("Buttons/join_meeting_btn.png")
    pyautogui.moveTo(btn)
    pyautogui.click()
else:
    print(f'{targetClass} was not found in the file. Please check if you typed in the current ')