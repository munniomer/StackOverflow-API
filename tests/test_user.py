"""Test user module"""
from tests.basetest import BaseTest


class TestUSer(BaseTest):
    """User tests class"""

    def test_if_no_data(self):
        """Tests if no data is provided in user signup"""
        respon = self.client.post(
            "/api/v1/auth/signup")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))

    def test_if_fields_missing(self):
        """Tests if some fields are missing in user signup"""
        respon = self.client.post(
            "/api/v1/auth/signup", json=self.new_user7, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))

    def test_user_registration(self):
        """tests if new user can register"""

        respon = self.client.post("/api/v1/auth/signup", json=self.new_user, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn('User successfully created',
                      str(respon.data))

    def test_valid_username(self):
        """tests if username is valid"""

        respon = self.client.post("/api/v1/auth/signup", json=self.new_user1, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('PLease check if username is empty or less 3 letters or contains numbers',
                      str(respon.data))

    def test_valid_email(self):
        """tests if email is valid"""

        respon = self.client.post("/api/v1/auth/signup", json=self.new_user2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please enter a valid email',
                      str(respon.data))

    def test_if_email_exist(self):
        """Tests if email is valid"""
        self.client.post(
            "/api/v1/auth/signup", json=self.new_user4, content_type='application/json')
        respon = self.client.post(
            "/api/v1/auth/signup", json=self.new_user3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That email exists. use a unique email',
                      str(respon.data))

    def test_if_username_exist(self):
        """Tests if email is valid"""
        self.client.post(
            "/api/v1/auth/signup", json=self.new_user3, content_type='application/json')
        respon = self.client.post(
            "/api/v1/auth/signup", json=self.new_user4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That username exists. use a unique username',
                      str(respon.data))

    def test_if_password_valid(self):
        """Tests if passwords are empty or less than 3"""
        respon = self.client.post(
            "/api/v1/auth/signup", json=self.new_user5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please check if your password is empty or less than 3',
                      str(respon.data))

    def test_if_password_match(self):
        """Tests if passwords match"""
        respon = self.client.post(
            "/api/v1/auth/signup", json=self.new_user6, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('confirm password does not match password',
                      str(respon.data))
