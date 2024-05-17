# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddemployee():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addemployee(self):
    self.driver.get("http://localhost:8004/")
    self.driver.set_window_size(790, 816)
    self.driver.find_element(By.LINK_TEXT, "Admin Login").click()
    self.driver.find_element(By.NAME, "t1").click()
    self.driver.find_element(By.NAME, "t1").send_keys("chinoy")
    self.driver.find_element(By.NAME, "t2").click()
    self.driver.find_element(By.NAME, "t2").send_keys("1708")
    self.driver.find_element(By.NAME, "sbmt").click()
    self.driver.find_element(By.LINK_TEXT, "Add User").click()
    self.driver.find_element(By.NAME, "t1").click()
    self.driver.find_element(By.NAME, "t1").send_keys("noy")
    self.driver.find_element(By.NAME, "t2").click()
    self.driver.find_element(By.NAME, "t2").send_keys("2222")
    self.driver.find_element(By.NAME, "t3").click()
    self.driver.find_element(By.NAME, "t3").send_keys("2222")
    self.driver.find_element(By.NAME, "s1").click()
    dropdown = self.driver.find_element(By.NAME, "s1")
    dropdown.find_element(By.XPATH, "//option[. = 'General']").click()
    self.driver.find_element(By.NAME, "sbmt").click()
  