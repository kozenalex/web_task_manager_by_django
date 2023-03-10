from django.test import TestCase
from users.models import MyUser
from task.models import Task
from labels.models import Labels
from statuses.models import Status


class TestModels(TestCase):

    def setUp(self):

        self.user = MyUser.objects.create_user(username='alex_alexov', password='qwerty')
        self.label = Labels.objects.create(name='testl')
        self.status = Status.objects.create(name='test_st')
        self.task = Task.objects.create(
            name='TestTask',
            description='testetstet',
            executor=self.user,
            author=self.user,
            status=self.status
        )

    def test_verbose_label(self):

        verbose = self.label._meta.get_field('name').verbose_name
        self.assertEqual(verbose, 'Имя')

    def test_verbose_status(self):

        verbose = self.status._meta.get_field('name').verbose_name
        self.assertEqual(verbose, 'Имя')

    def test_verbose_task(self):

        verbose_name = self.task._meta.get_field('name').verbose_name
        verbose_status = self.task._meta.get_field('status').verbose_name
        verbose_author = self.task._meta.get_field('author').verbose_name
        verbose_extr = self.task._meta.get_field('executor').verbose_name
        verbose_labels = self.task._meta.get_field('labels').verbose_name
        self.assertEqual(verbose_name, 'Имя')
        self.assertEqual(verbose_author, 'Автор')
        self.assertEqual(verbose_extr, 'Исполнитель')
        self.assertEqual(verbose_labels, 'Метки')
        self.assertEqual(verbose_status, 'Статус')
