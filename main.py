import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PHONE = os.environ["phone"]
common_ = webdriver.ChromeOptions()
common_.add_experimental_option("detach", value=True)
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3800451741&f_TPR=r604800&f_WT=2&geoId=103644278&origin=JOBS_HOME_REMOTE_JOBS"

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# drive into Chrome as your primary browser
driver = webdriver.Chrome(options=common_)
driver.get(url=URL)

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

email_ = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
email_.send_keys("pythondanielpython@gmail.com")
time.sleep(2)

# put the password
password_ = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
password_.send_keys("Danielcodes", Keys.ENTER)
time.sleep(3)

all_job_listing = driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[2]/span")
print("I got it")



for JOB in all_job_listing:
    JOB.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
# driver.quit()



# # apply for the job
# apply = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span")
# apply.click()
# time.sleep(2)
#
# # We create a space for our phone number
# phone = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input")
# phone.send_keys(PHONE, Keys.ENTER)











# Click on the next
# next_ = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span")
# next_.click()
# put a wait time to make it look legit
# time.sleep(3)
# # Toggle the increae your chance of being viewd, off
# view = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div")
# view.click()
#
# # continue with your application
# continue_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/footer/div/div/button/span")
# continue_application.click()
#
# #Now we apply for the Job
# apply_job = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/a")
# print(apply_job.text)



# driver.quit()