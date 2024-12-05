from django.test import TestCase
from django.contrib.auth.models import User
from .models import ToDo, Tag

class ToDoModelTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.tag = Tag.objects.create(name="Urgent")
        self.todo = ToDo.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-31",
            status=ToDo.StatusChoices.OPEN
        )
        self.todo.tags.add(self.tag)

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test Task")
        self.assertEqual(self.todo.description, "Test Description")
        self.assertEqual(self.todo.status, ToDo.StatusChoices.OPEN)

    def test_tag_uniqueness(self):
        duplicate_tag = Tag(name="Urgent")
        with self.assertRaises(Exception):
            duplicate_tag.save()

class ToDoAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_create_todo_api(self):
        response = self.client.post('/todo/create/', {
            'title': 'API Task',
            'description': 'Task created via API',
            'status': ToDo.StatusChoices.OPEN
        })
        self.assertEqual(response.status_code, 201)

    def test_list_todos_api(self):
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
