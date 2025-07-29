from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import smtplib
from skpy import SkypeAuthException
from skpy import Skype
from selenium.webdriver.support.ui import Select
import time


# ---------------------------------------------------------------------------------------------------------
def send_skype_message(skype_username, skype_password, message):
    try:
        skype = Skype(skype_username, skype_password)
        group_chat_id = ''
        skype_chat = skype.chats.chat(group_chat_id)
        skype_chat.sendMsg(message)
        print("SMS Balance Skype message sent successfully!")
    except Exception as e:
        print(f"SMS Balance   Error sending Skype message: {e}")

# Function to send email alert
def send_email_alert(sender_email, receiver_email, password, message):
    try:
        # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("SMS Balance Email alert sent successfully!")
    except Exception as e:
        print(f"SMS Balance Error sending email: {e}")



chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# --------------------------------------------GP Balance---------------------------------------
def login_and_get_balance(username, password):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://gpcmp.grameenphone.com/#/')
        wait_driver = WebDriverWait(driver, 5)
        print(f"Logging in as {username}")

        username_field = wait_driver.until(EC.presence_of_element_located((By.ID, 'name')))
        username_field.send_keys(username)

        password_field = wait_driver.until(EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)
        print(f"Logged in as {username}")

        balance_element = wait_driver.until(
            EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'Cur. Balance:')]//span"))
        )
        current_balance = balance_element.text
        print(f"Current Balance for {username}: {current_balance}")

        driver.quit()
        return current_balance

    except Exception as e:
        print(f"Error collecting balance for {username}: {e}")
        driver.quit()
        return None


# --------------------------------------------Mobireach Balance---------------------------------------

def run_balance_mobi_reach(username,password):

    try:
        driver_MR = webdriver.Chrome(options=chrome_options)
        driver_MR.get('https://portal.mobireach.com.bd/signin')
        wait_driver_MR = WebDriverWait(driver_MR, 5)
        print("Opens mobireac Browser")

        username_field = wait_driver_MR.until(EC.presence_of_element_located((By.ID, 'basic_username')))
        username_field.send_keys(username)

        password_field = wait_driver_MR.until(EC.presence_of_element_located((By.ID, 'basic_password')))
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)
        print("Logged in to  Mobireach..")

        try:
            alert = driver_MR.switch_to.alert
            alert.accept()
        except:
            pass
        print("Please enter OTP to the browser..")

        WebDriverWait(driver_MR, 30).until(EC.url_contains("https://portal.mobireach.com.bd/verify-otp"))
        print("Redirected to OTP page. Please enter the OTP in the browser and submit it.")

        # Wait for URL to change to home page after OTP submission
        WebDriverWait(driver_MR, 300).until(
            lambda driver: driver.current_url.startswith("https://portal.mobireach.com.bd/mobireach/Home"))
        print("OTP submitted successfully and redirected to home page.")

        try:
            agree_button = wait_driver_MR.until(
                EC.presence_of_element_located((By.XPATH, "//button[span[contains(text(), 'Agree')]]"))
            )
            agree_button.click()
            print("Clicked the 'Agree' button.")
        except Exception as e:
            print(f"Error handling 'Agree' button: {e}")

        # Hover over the dollar icon to reveal the tooltip
        dollar_icon = wait_driver_MR.until(
            EC.presence_of_element_located((By.XPATH, "//span[@role='img' and @aria-label='dollar']")))
        ActionChains(driver_MR).move_to_element(dollar_icon).perform()
        time.sleep(3)

        api_balance_element = wait_driver_MR.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'API Balance :')]//strong")))
        api_balance = api_balance_element.text
        print("API Balance:", api_balance)

        time.sleep(3)
        driver_MR.quit()
        return api_balance

    except Exception as e:
        print(f"Error collecting API balance : {e}")

# ---------------------------------------------------------------------------------------------------------
balance_1 = login_and_get_balance('', '')
balance_2 = login_and_get_balance('', '')
balance_3 = run_balance_mobi_reach('', '')
balance_4 = run_balance_mobi_reach('', '')
# balance_5 = login_and_get_balance('', '')



combined_message = f"Subject:SMS Balance Update\n\n"
combined_message += f"GP SMS Balance TK: {balance_1} BDT\n"
combined_message += f"GP SMS Balance TP: {balance_2} BDT\n"
combined_message += f"Mobireach -TK SMS balance (Progoti 2): {balance_3 } BDT\n"
combined_message += f"Mobireach -TP SMS Balance(Progoti 4): {balance_4} BDT\n"
# combined_message += f"Non masking SMS balance(Progoti 3): {balance_5} BDT\n"


combined_message_skype = f"SMS Balance Update\n"
combined_message_skype += f"GP SMS Balance TK: {balance_1} BDT\n"
combined_message_skype += f"GP SMS Balance TP: {balance_2} BDT\n"
combined_message_skype += f"Mobireach - TK SMS balance (Progoti 2): {balance_3} BDT\n"
combined_message_skype += f"Mobireach - TP SMS Balance(Progoti 4): {balance_4} BDT\n"
# combined_message_skype +=  f"Non masking SMS balance(Progoti 3): {balance_5} BDT\n"

# ---------------------------------------------------------------------------------------------------
skype_username = "sample@gmail.com"
skype_password = ""
print("Message format:", combined_message_skype)
send_skype_message(skype_username, skype_password,combined_message_skype)

# Replace these with your actual email credentials
sender_email = "sample@gmail.com"
receiver_email = "sample@gmail.com"
password = ""
send_email_alert(sender_email, receiver_email, password, combined_message)
# ---------------------------------------------------------------------------------------------------