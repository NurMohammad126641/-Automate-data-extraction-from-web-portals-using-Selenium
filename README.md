🚀 SMS Balance Monitor & Notification Bot
Automates data extraction from web portals using Selenium

📖 Project Overview
This project automates the process of checking SMS balances across multiple web portals. It uses Selenium to extract balance data in real time and then sends automated notifications via email and Skype.

This ensures that users are always informed about their current SMS balance, helping them avoid unexpected service disruptions. The system runs on a schedule, eliminating the need for manual checks and making SMS balance monitoring seamless and efficient.

✨ Key Features
✅ Automates data extraction from web portals using Selenium

📩 Sends real-time alerts via email and Skype

🧠 Ensures timely awareness of SMS credit levels

🛠️ Reduces manual effort and enhances operational efficiency

🌐 Powered by Selenium: Automated Web Interaction
This project uses Selenium WebDriver to automate interactions with web browsers. Selenium enables the script to:

🌍 Open Web Pages: Automatically navigate to portal login pages

🔐 Log In: Fill in usernames and passwords to log into portals

📊 Extract Data: Locate and read balance or other relevant info directly from web pages

🖱️ Simulate User Actions: Click buttons, hover, and interact with dynamic elements just like a real user

Selenium makes it possible for this script to interact with complex websites without human involvement—making the balance checking process fully automated.

🛠️ Prerequisites
Ensure the following software and tools are installed on your system:

Python 3.x – Required to run the script

Google Chrome – Browser used by Selenium WebDriver

ChromeDriver – Must match your Chrome browser version

🔗 Download ChromeDriver

⚠️ Add ChromeDriver to your system's PATH, or provide the path in the script when initializing webdriver.Chrome().

📦 Required Python Libraries
Install the necessary libraries using pip:

bash
Copy
Edit
pip install selenium skpy
⚙️ Setup and Configuration
Download the Code: Clone or download the project to your local machine.

Set up ChromeDriver:

Ensure the version matches your installed Chrome browser

Either add it to your system's PATH or use the full path in the script

Configure Credentials:

Update your portal, Skype, and email credentials in the script

Locate the relevant lines and input your own values accordingly

▶️ Usage
To run the script, open your terminal or command prompt, navigate to the project directory, and execute:

bash
Copy
Edit
python your_script_name.py
The script will:

Launch Chrome browser

Log into your specified portals

Extract SMS balance data

Send notifications via Skype and email

⚠️ Important Notes & Troubleshooting
Headless Mode:
To run Chrome in headless mode (no visible browser window), uncomment:

python
Copy
Edit
chrome_options.add_argument("--headless")
WebDriver Errors:
If you face WebDriverException, verify that your ChromeDriver version matches your Chrome browser version.

Skype Login Issues:
If you encounter SkypeAuthException, double-check your credentials. The Skype API may occasionally prompt for CAPTCHA or security checks that can't be automated.

Email Sending Issues:
Ensure that your sender_email and password are correct.
For Gmail, enable "Less Secure App Access" or set up an App Password if using 2FA.

