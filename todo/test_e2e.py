from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from todo.models import ToDo

class ToDoE2ETestCase(StaticLiveServerTestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()  
        self.admin_user = User.objects.create_superuser(username='vikash', password='123', email='vikashvermacom92@gmailc.om')
        self.todo = ToDo.objects.create(title="Test Task", description="This is a test task")
    

    def tearDown(self):
        self.driver.quit()

    def test_create_todo(self):
        self.driver.get(f'{self.live_server_url}/admin/')  
        self.driver.find_element(By.NAME, 'username').send_keys('vikash')
        self.driver.find_element(By.NAME, 'password').send_keys('123')
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()  

        self.driver.get(f'{self.live_server_url}/todo/create/') 
        self.driver.find_element(By.NAME, 'title').send_keys('E2E Task')
        self.driver.find_element(By.NAME, 'description').send_keys('This is an E2E test')
        self.driver.find_element(By.NAME, 'due_date').send_keys('2024-12-31')
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()  

        self.assertIn("E2E Task", self.driver.page_source)

    def test_list_todos(self):
        self.driver.get(f'{self.live_server_url}/todo/')
        self.assertIn("Test Task", self.driver.page_source)

        