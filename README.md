Automate data extraction from web portals using Selenium

This project automates the process of checking SMS balances across multiple web portals. It uses Selenium to extract balance data in real time and then sends automated notifications via email and Skype. 
This ensures that users are always informed about their current SMS balance, helping them avoid unexpected service disruptions.
The system runs on a schedule, eliminating the need for manual checks and making SMS balance monitoring seamless and efficient.

✨ Key Features

-Automates data extraction from web portals using Selenium
-Sends real-time alerts via email and Skype
-Ensures timely awareness of SMS credit levels
-Reduces manual effort and enhances operational efficiency


🌐 Powered by Selenium: Automated Web Interaction
This project uses Selenium WebDriver to automate interactions with web browsers. Selenium is a powerful tool that allows the script to:
•
Open Web Pages: Automatically navigate to the Portals login pages.
•
Log In: Fill in usernames and passwords to log into the portals.
•
Extract Data: Find and read the portal balance or any other info you want directly from the web pages.
•
Simulate User Actions: Perform actions like clicking buttons and hovering over elements, just like a human user would.


Selenium makes it possible for this script to interact with complex websites and gather the necessary data without manual intervention, making the balance or any other info you want to check process fully automated.


🛠️ Prerequisites
To run this project, you need to have the following software and libraries installed on your system:
•
Python 3.x: This script is written in Python 3.
•
Google Chrome: Google Chrome browser is needed for the Selenium WebDriver.
•
ChromeDriver: Download the ChromeDriver that matches your installed Chrome browser version. You should add it to your system's PATH, or specify its path in the script.
•
ChromeDriver Download Link: https://chromedriver.chromium.org/downloads



📦 Required Python Libraries
Install the following Python libraries using pip:
Bash
pip install selenium skpy


⚙️ Setup and Configuration
1.
Download the Code: Download this project's code to your local system.
2.
Set up ChromeDriver: Make sure your ChromeDriver version matches your Chrome browser version and that it's added to your system's PATH variable. If not, you can specify the full path to ChromeDriver when calling webdriver.Chrome(), like this:
3.
Configure Credentials: Update your portals, Skype, and email credentials within the script. Find the following lines and fill them in with your information:


🚀 Usage
To run the script, open your terminal or command prompt, navigate to the project directory, and run the following command:
Bash
python your_script_name.py
The script will automatically open the browser, log in, collect balances, and send notifications via Skype and email.



⚠️ Important Notes and Troubleshooting
•
Headless Mode: By default, the browser runs in visible mode. If you don't want to see the browser window, you can uncomment the line chrome_options.add_argument("--headless").
•
Selenium WebDriver Errors: If you get a WebDriverException or similar error, make sure your ChromeDriver version is compatible with your Chrome browser version.
•
Skype Login Errors: If you get a SkypeAuthException, check if your Skype username and password are correct. Skype API might sometimes ask for CAPTCHA or other security verifications that are hard to handle automatically.
•
Email Errors: If you have trouble sending emails, make sure your sender_email and password are correct and that "Less Secure App Access" is enabled for your email provider (if using Gmail).

