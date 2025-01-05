import time
import json
import os
import smtplib
import certifi
import ssl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# User input and initialization
username = input("Enter username: ")
siteUrl = f"https://leetcode.com/u/{username}/"
file_path = f"{username}_last_question.json"
last_question_solved = None

# Load the last solved question from a file
def load_last_question():
    global last_question_solved
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            last_question_solved = data.get("last_question_solved")
            print(f"Last question solved (loaded): {last_question_solved}")
    else:
        print("No previous data found. Starting fresh.")

# Save the last solved question to a file
def save_last_question():
    global last_question_solved
    with open(file_path, 'w') as f:
        json.dump({"last_question_solved": last_question_solved}, f)
        print(f"Saved last question: {last_question_solved}")

# Open the browser with the given URL
def open_browser(url):
    print("     -----------> Opening Browser")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.maximize_window()
    return driver

# Close the browser
def close_browser(driver):
    print("     -----------> Closing Browser")
    driver.close()

# Fetch the data from the LeetCode profile page
def fetch_page_data(browser):
    global last_question_solved
    time.sleep(4)
    page_source = browser.page_source
    WebDriverWait(browser, 10).until(EC.title_contains(f"{username} - LeetCode Profile"))
    
    soup = BeautifulSoup(page_source, 'html.parser')
    if browser.title == f"{username} - LeetCode Profile":
        print("\n\n------------------- Parsing data -------------------\n\n")
        question_block = soup.find('div', class_='bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg px-4 pb-4 pt-4')
        question = question_block.find('a', class_='flex h-[56px] items-center rounded px-4 bg-fill-4 dark:bg-dark-fill-4')

        if question:
            question_name = question.find('div')['data-title']
            question_date = question.find('span', class_='text-label-3 dark:text-dark-label-3 lc-md:inline hidden whitespace-nowrap').text
            question_url = f"https://leetcode.com/problems/{question_name.replace(' ', '-')}"
            print(f"Last Question Solved: {last_question_solved}")
            
            # Notify only if a new question is solved
            if last_question_solved is None or last_question_solved != question_name:
                print(f"New question solved: {question_url}")
                last_question_solved = question_name  # Update the last question solved
                save_last_question()  # Save the updated last solved question
                notify(question_url, question_date)
            else:
                print("No new question solved.")
        else:
            print("No questions found or unable to parse.")
    else:
        print("Page does not exist or connection failed.")

# Send email notification about the new solved question
def notify(url, date):
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587
    EMAIL_ID1 = "example1@gmail.com"#sender mail id
    EMAIL_ID2 = "example2@gmail.com"#reciver mail id
    PASSWORD = "your password" //create app password in ur google account
    
    try:
        context = ssl.create_default_context(cafile=certifi.where())  # Use certifi's CA certificates
        server = smtplib.SMTP(SMTP_SERVER, PORT)
        server.starttls(context=context)
        server.login(EMAIL_ID1, PASSWORD)

        subject = "LeetCode Notification: New Question Solved"
        body = f"Hi there,\n\nThe latest question solved by {username} is:\n{url}\n{date}\n\nBest regards,\nYour LeetCode Tracker"
        msg = f"Subject:{subject}\n\n{body}"

        server.sendmail(EMAIL_ID1, EMAIL_ID2, msg)
        server.quit()

    except Exception as e:
        print(f"Error is {e}")

# Main function to run the whole process

def main():
    load_last_question()
    browser = None
    try:
        browser = open_browser(siteUrl)
        print("Tracker started. Press Ctrl+C to stop.")
        
        while True:
            fetch_page_data(browser)
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if browser:
            close_browser(browser)

# Run the main function
if __name__ == "__main__":
    main()
