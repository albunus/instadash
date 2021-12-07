from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile,Comments


class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects("albunus")
        self.profile_user = Profile(profile_pic='image.png', bio="about me",user=self.user)
        self.profile_user.save()

    def test_instance_true(self):
        self.profile_user.save()
        self.assertTrue(isinstance(self.profile_user, Profile))


class CommentTestClass(TestCase):

    def setUp(self):
        self.user = User.objects("albunus")

        self.my_profile = Profile(profile_pic='image.png',bio="about me",user=self.user)
        
        self.my_profile.save()

        self.photo = Image(pic='image.png',caption="testing", profile='',user=self.user)
        self.photo.save()

        self.new_comment = Comments(image=self.photo, comment_user=self.my_profile, comment="Interesting")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comments.objects.all().delete()
        
        
class ImageTestClass(TestCase):

    def setUp(self):

        self.user = User.objects("albunus")

        self.my_profile = Profile(profile_pic='image.png',bio="about me",user=self.user)
        self.my_profile.save()

        self.photo = Image(pic='image.png', caption="testing", profile=self.my_profile)

    def test_instance_true(self):
        self.photo.save()
        self.assertTrue(isinstance(self.photo, Image))

    def test_save_image(self):
        self.photo.save()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)