from django.db import models
from django.utils.translation import gettext as _
from users.models import MyUser
from statuses.models import Status
from labels.models import Labels


class Task(models.Model):

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(
        max_length=700,
        default='',
        verbose_name=_('Description')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    executor = models.ForeignKey(
        MyUser,
        related_name='executor',
        on_delete=models.PROTECT,
        verbose_name=_('Executor')
    )
    author = models.ForeignKey(
        MyUser,
        related_name='author',
        on_delete=models.PROTECT,
        verbose_name=_('Author')
    )
    status = models.ForeignKey(
        Status,
        models.PROTECT,
        verbose_name=_('Status')
    )
    labels = models.ManyToManyField(
        Labels,
        through='LabelToTask',
        verbose_name=_('Labels'),
        blank=True
    )

    def __str__(self):
        return self.name


class LabelToTask(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    labels = models.ForeignKey(Labels, on_delete=models.PROTECT, null=True)
