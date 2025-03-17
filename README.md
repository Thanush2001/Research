# IRCTC Ticket Booking Automation using Python

## Overview
This project automates the process of booking train tickets on IRCTC using Python. The script interacts with the IRCTC website via Selenium to fill in login details, search for trains, select tickets, and complete the booking process.

## Features
- Automated login to IRCTC
- Train search based on source and destination
- Selection of available trains and ticket types
- Automated passenger detail entry
- CAPTCHA handling (manual intervention required)
- Ticket confirmation and screenshot capture

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Google Chrome or Mozilla Firefox browser
- WebDriver for the chosen browser (Chromedriver for Chrome, Geckodriver for Firefox)
- Required Python libraries:
  ```sh
  pip install selenium
  ```

## Installation
1. Clone the repository or download the script.
   ```sh
   git clone https://github.com/Thanush2001/Research.git
   cd Research
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Place the appropriate WebDriver in the project directory and set its path in the script.

## Usage
1. Update the `config.json` file with your IRCTC credentials and travel details.
2. Run the script using:
   ```sh
   python IRCTC.py
   ```
3. Follow on-screen instructions for CAPTCHA and payment processing.

## Limitations
- CAPTCHA handling requires manual intervention.
- The IRCTC website frequently updates, which may require script adjustments.
- Ensure compliance with IRCTC's policies to avoid misuse.

## Disclaimer
This script is for educational purposes only. Use it responsibly and ensure compliance with IRCTC’s terms of service.

## Author
Developed by [Thanush Veerappan]  
For more details, visit: [Your GitHub Profile](https://github.com/Thanush2001)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

