from django.test import TestCase, Client
from django.contrib.auth.models import User

from .forms import SignUpForm
from .models import Profile, Group


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1, username="testuser", password="TestPassword123")
        Profile(first_name="test", last_name="user", email="test@test.com", date_of_birth="1970-01-01",
                user=User.objects.get(username="testuser"), description="desc").save()

    def testUser(self):
        test_user = User.objects.get(username="testuser", password="TestPassword123")
        self.assertEqual(test_user.username, "testuser")
        self.assertEqual(test_user.password, "TestPassword123")

        test_profile = Profile.objects.all().get(user_id=test_user.id)
        self.assertEqual(test_profile.first_name, "test")
        self.assertEqual(test_profile.last_name, "user")


class GroupTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testleader", password="TestPassword123")
        User.objects.create(username="group_member_1", password="TestPassword123")
        User.objects.create(username="group_member_2", password="TestPassword123")
        Profile(first_name="test1", last_name="user", email="test@test.com", date_of_birth="1970-01-01",
                user=User.objects.get(username="group_member_1"), description="desc").save()
        Profile(first_name="test2", last_name="user", email="test@test.com", date_of_birth="1970-01-01",
                user=User.objects.get(username="group_member_2"), description="desc").save()

    def testGroup(self):
        group_leader = User.objects.get(username="testleader")
        member_list = []
        member_list.append(Profile.objects.get(first_name="test1"))
        member_list.append(Profile.objects.get(first_name="test2"))
        Group(name="test group", group_leader=group_leader, location="Test location").save()
        test_group = Group.objects.get(name="test group")
        test_group.members.set(member_list)
        self.assertEqual(test_group.group_leader.username, "testleader")
        self.assertEqual(test_group.members.get(first_name="test2").first_name, "test2")


class SignUpFormTestCase(TestCase):
    def test_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(form.fields["email"].help_text, 'Required. Inform a valid email address.')
        self.assertEqual(form.fields["description"].help_text, 'Optional.')

    def test_invalid_form(self):
        form = SignUpForm(data={'first_name': "firstname", 'last_name': "lastname", 'date_of_birth': "01-01-1990"})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = SignUpForm(data={'first_name': "firstname", 'last_name': "lastname", 'email': "test@test.com",
                                'date_of_birth': "01-01-1990", 'password1': "a6{eYw?REL?%,A.s",
                                'password2': "a6{eYw?REL?%,A.s", 'username': "testuser321"})
        self.assertTrue(form.is_valid())


class LoginPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def testLogin(self):
        response = self.client.get("/GroupUp/login/")
        self.assertEqual(response.status_code, 200)


class FindGroupPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        User.objects.create_user(username="user1", password="Password123")
        group_user = User.objects.create_user(username="group_user", password="Password123")
        Group(name="test group1", group_leader=group_user, location="Test location1").save()
        Group(name="test group2", group_leader=group_user, location="Test location2").save()

    def test_number_of_groups(self):
        self.client.login(username="user1", password="Password123")
        response = self.client.get("/GroupUp/groups_overview/")
        self.assertEqual(response.status_code, 200)
        number_of_groups_html = len(response.context['groups'])
        number_of_groups_db = len(list(Group.objects.all()))
        self.assertEqual(number_of_groups_html, number_of_groups_db)
        self.assertEqual(number_of_groups_html, 2)


