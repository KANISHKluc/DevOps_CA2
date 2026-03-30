import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

class TestStudentFeedbackForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome driver (Selenium 4.6+ auto-downloads the driver)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        
        # Get absolute path to index.html and ensure URI format
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, 'index.html').replace('\\', '/')
        cls.file_path = f"file:///{path}"
        
    def setUp(self):
        # Open page before each test
        self.driver.get(self.file_path)
        # Give some time for rendering
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_page_opens_successfully(self):
        """Check whether the form page opens successfully"""
        self.assertIn("Student Feedback Registration Form", self.driver.title)

    def test_02_mandatory_fields_blank(self):
        """Leave mandatory fields blank and check error messages"""
        submit_btn = self.driver.find_element(By.ID, "submitBtn")
        submit_btn.click()
        
        # Verify validation kicked in (classes updated to 'invalid')
        classes = self.driver.find_element(By.ID, "nameGroup").get_attribute("class")
        self.assertIn("invalid", classes)

    def test_03_invalid_email_format(self):
        """Enter invalid email format and verify validation"""
        self.driver.find_element(By.ID, "emailId").send_keys("invalidemail")
        self.driver.find_element(By.ID, "submitBtn").click()
        
        classes = self.driver.find_element(By.ID, "emailGroup").get_attribute("class")
        self.assertIn("invalid", classes)

    def test_04_invalid_mobile_number(self):
        """Enter invalid mobile number and verify validation"""
        self.driver.find_element(By.ID, "mobileNumber").send_keys("12345") # Only 5 digits
        self.driver.find_element(By.ID, "submitBtn").click()
        
        classes = self.driver.find_element(By.ID, "mobileGroup").get_attribute("class")
        self.assertIn("invalid", classes)

    def test_05_dropdown_selection(self):
        """Check whether dropdown selection works properly"""
        select = Select(self.driver.find_element(By.ID, "department"))
        select.select_by_value("Computer Science")
        self.assertEqual("Computer Science", self.driver.find_element(By.ID, "department").get_attribute("value"))

    def test_06_reset_button_works(self):
        """Check whether Reset works correctly"""
        self.driver.find_element(By.ID, "studentName").send_keys("John Doe")
        self.driver.find_element(By.ID, "resetBtn").click()
        self.assertEqual("", self.driver.find_element(By.ID, "studentName").get_attribute("value"))

    def test_07_valid_data_successful_submission(self):
        """Enter valid data and verify successful submission"""
        # Fill in valid data
        self.driver.find_element(By.ID, "studentName").send_keys("John Doe")
        self.driver.find_element(By.ID, "emailId").send_keys("john.doe@example.com")
        self.driver.find_element(By.ID, "mobileNumber").send_keys("9876543210")
        
        Select(self.driver.find_element(By.ID, "department")).select_by_value("Computer Science")
        self.driver.find_element(By.ID, "genderMale").click()
        
        comments = "This is a great course and I learned a lot from it." # 11 words
        self.driver.find_element(By.ID, "feedbackComments").send_keys(comments)
        
        # Submit
        self.driver.find_element(By.ID, "submitBtn").click()
        
        # Check success message visibility
        time.sleep(0.5) # wait for DOM update
        success_msg = self.driver.find_element(By.ID, "successMessage")
        
        # The exact inner style text can vary, check that display is 'block' instead
        style = success_msg.get_attribute("style")
        self.assertIn("display: block", style)

if __name__ == "__main__":
    unittest.main()
