# Twilio Setup Guide for GitHub README

Here’s a breakdown designed to be easily followed, even for someone new to Twilio:

## Github

[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-yellow?logo=whatsapp&logoColor=white)](https://github.com/davidtkeane/PhoneBook-CLI)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative) 
![Version](https://img.shields.io/badge/Version-2.0-orange?logo=v)


## Twilio Setup Instructions

This project uses the Twilio Programmable SMS API to send text messages. To use this functionality, you'll need to create a Twilio account and get the necessary credentials.

**Step 1: Create a Twilio Account**

   *   Go to the Twilio website: [https://www.twilio.com/](https://www.twilio.com/)
   *   Click the "Sign up" or "Start free trial" button.
   *   Follow the instructions, which include:
        *   Providing your email address.
        *   Creating a password.
        *   Verifying your email.
        *   You'll also likely need to provide and verify a phone number (this helps with security and is a normal step).

**Step 2: Access the Twilio Console**

   *   Once signed up and verified, log into your Twilio account using your registered email and password.
   *   You will be directed to the Twilio console: [https://www.twilio.com/console](https://www.twilio.com/console)

**Step 3: Locate Your API Credentials**

   *   In the Twilio console, you'll need to find your "Account SID" and "Auth Token." Here's where to usually find them:
      *   **"Account Info" section**: This section may appear on the main dashboard, typically in the top-left corner or within a settings section. It contains your API keys.
   *   You need the following:
      *   **Account SID:** A unique identifier for your Twilio account.
      *   **Auth Token:** Your secret key for authenticating with the Twilio API. *Handle this token like a password. Do not expose it.*
   *   **To View Auth Token**: The Auth Token might be hidden by default. Look for an eye icon or a "show" button and click it. Once revealed copy the information.
   *   **Important**: Copy both the **Account SID** and **Auth Token** somewhere safe, you'll need to use these credentials in your project.
       *  You only get one chance to copy these, if lost they must be regenerated.

**Step 4: Purchase a Twilio Phone Number**

    * You need a Twilio Phone Number to send or receive text messages.
    * Look for "Phone Numbers" in the console's side menu or explore the main dashboard.
    * Click on "Buy a Number."
    * Choose a number, and complete the purchase process. Note this can incur costs (check your Twilio free credit or plan).
    * Once bought take note of this Twilio Phone number, as you will use it when using the script.

**Step 5: Securely Manage Your Credentials (Crucial)**

   *   **NEVER embed your Twilio API credentials (Account SID, Auth Token, or Twilio Phone Number) directly into your code**.
   *   Hardcoding these is a major security vulnerability, it would mean that if a script or notebook is shared the keys would be too.

   *   Instead: Store your credentials using a more secure methods, the recommended options are listed below:

   *   **Environment Variables (Recommended)**

      *  **What are they?** System environment variables are variables stored outside of code that are accessible to programs running on a computer or server.
      *  How to Set them Up:
          *  For many systems, set them directly in the terminal or system settings, for example:
         ```bash
          export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
          export TWILIO_AUTH_TOKEN="your_auth_token"
          export TWILIO_PHONE_NUMBER="+15555555555"
         ```
          *   Where to get the keys from:
              *  **Account SID**:  Located within Twilio Console account info section as described above.
              *  **Auth Token:**  Located within Twilio Console account info section, be sure to use the *show token function* as described above.
              *  **Twilio Phone Number**: Your purchased number as described above.

      *   **Note** : these can be set on Colab or on local environments, via your .bashrc or a different method. Please consult your OS docs for more details.

   *  **.env Files**
         * What are they?: Text files that store configurations variables like API keys. These must be excluded from git pushes to prevent security leaks.
         * Example content for .env:
            ```text
             TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
             TWILIO_AUTH_TOKEN="your_auth_token"
             TWILIO_PHONE_NUMBER="+15555555555"
            ```
      * Using them, libraries such as python dotenv (pip install python-dotenv) will allow your script to load and then use them.

   *   **Colab Secrets (If using Google Colab)**
          *   How?: Access the 'secrets' function by the key icon on the left-hand-side menu in Colab. Add your variables and copy the values across.

**Step 6: How to Use in Your Script**

Here’s a Python code example that demonstrates accessing credentials via OS environment variables (this is the most flexible example).

 ```python
    from twilio.rest import Client
    import os

    # Get credentials from environment variables
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Use try and catch to output the error.
    try:
         # Create the message
        message = client.messages.create(
                                      from_= twilio_phone_number,  # Your purchased Twilio Number.
                                      body='Hello, World! This is a Twilio message.', # Change message as needed
                                      to='+12223334444'  # Replace with the recipient phone number.
         )

        print("Message SID:", message.sid)

    except Exception as e:
            print (f"Error has occured when sending message {e}")
content_copy
download
Use code with caution.
Markdown

Replace the following values with your information:

* `Your Twilio Number:` The Twilio phone number you purchased, should look something like "+12223334444"
     *   `'+12223334444'`:  Replace this with the phone number you want to send a text message to.
content_copy
download
Use code with caution.
**Final Security Reminder**

   * Double-check you have not exposed the credentials in your code or GitHub repo
   * Never use credentials in a publicly accessible git repository. Use .env to avoid storing them directly into your script, but ensure that they do not commit as well (i.e by adding to the .gitignore).
content_copy
download
Use code with caution.

Let me know if you'd like any of this customized further!