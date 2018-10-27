import datetime
from django.utils import timezone
from django.test import TestCase
from .models import User,Diary

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        在将来发布的问卷应该返回False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = User(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
