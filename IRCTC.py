import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

# 🚀 Setup Undetected Chrome Driver
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

# 🌐 Open IRCTC Website
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(3)

# 🛑 Handle Popups (if any)
try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
    ).click()
    print("✅ Popup closed.")
except:
    print("⚠️ No popups found.")

# 🔑 Click on 'LOGIN' Button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'LOGIN')]"))
    )
    login_button.click()
    print("✅ Login Page Opened!")
except:
    print("❌ Login button not found!")
    driver.quit()
    exit()

# ⏳ Wait for Username & Password Fields
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='userid']"))
    )
    password = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")

    username.send_keys("V_Thanush")  # Replace with your IRCTC Username
    password.send_keys("Amma@1974")  # Replace with your IRCTC Password
    print("✅ Credentials Entered!")
except:
    print("❌ Username or Password field not found!")
    driver.quit()
    exit()

# ❗ Wait for Manual Captcha Entry
input("👉 Enter Captcha manually in the browser, then press Enter here...")

# ✅ Click 'SIGN IN' Button
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='SIGN IN']"))
    )
    sign_in_button.click()
    print("✅ Clicked on SIGN IN button.")
except:
    print("❌ SIGN IN button not found!")
    driver.quit()
    exit()

# ⏳ Verify Login Success
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Welcome')]"))
    )
    print("✅ Login Successful!")
except:
    print("❌ Login Failed! Check Credentials.")
    driver.quit()
    exit()

# 🚆 **Start Ticket Booking Process**

# 1️⃣ Enter Source Station
try:
    from_station = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='From*']"))
    )
    from_station.click()
    from_station.send_keys("MAS")  # Change to your station
    time.sleep(2)
    from_station.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    print("✅ Source Station Entered!")
except Exception as e:
    print("❌ Source Station field not found!", e)

# 2️⃣ Enter Destination Station
try:
    to_station = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='To*']"))
    )
    to_station.click()
    to_station.send_keys("SBC")  # Change to your station
    time.sleep(2)
    to_station.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    print("✅ Destination Station Entered!")
except Exception as e:
    print("❌ Destination Station field not found!", e)

# 3️⃣ Select Travel Date
try:
    date_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='journeyDate']"))
    )
    date_field.click()
    time.sleep(2)

    # Pick a date dynamically (7 days from today)
    travel_date = (datetime.today() + timedelta(days=7)).strftime("%d")

    date_xpath = f"//a[text()='{travel_date}']"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, date_xpath))
    ).click()
    
    print("✅ Travel Date Selected!")
except Exception as e:
    print("❌ Travel Date selection failed!", e)

# 4️⃣ Click on 'Search' Button
try:
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']"))
    )
    search_button.click()
    print("✅ Searching for Trains...")
except:
    print("❌ Search Button not found!")

# ⏳ Wait for Train List to Load
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'train_avl_enq_box')]"))
    )
    print("✅ Train List Loaded Successfully!")
except:
    print("❌ No Trains Found or Delay in Loading!")

# 5️⃣ Select First Available Train & Click 'Book Now'
try:
    book_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Book Now')])[1]"))
    )
    book_now_button.click()
    print("✅ Clicked on 'Book Now' for First Available Train!")
except:
    print("❌ 'Book Now' Button Not Found!")

# 🎟️ Proceed to Passenger Details
try:
    passenger_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='passengerName']"))
    )
    passenger_name.send_keys("Thanush V")  # Replace with passenger's name
    print("✅ Passenger Name Entered!")

    passenger_age = driver.find_element(By.XPATH, "//input[@formcontrolname='passengerAge']")
    passenger_age.send_keys("23")  # Replace with age
    print("✅ Passenger Age Entered!")

    # Select Gender
    gender_dropdown = driver.find_element(By.XPATH, "//select[@formcontrolname='passengerGender']")
    gender_dropdown.click()
    driver.find_element(By.XPATH, "//option[text()='Male']").click()
    print("✅ Gender Selected!")
except:
    print("❌ Passenger Details Entry Failed!")

# ⏳ **At This Point, Manually Complete Payment Process**
print("👉 Manually Complete Payment and Confirm Ticket Booking!")

# 🔴 Close Browser After Some Time
time.sleep(10)
driver.quit()
