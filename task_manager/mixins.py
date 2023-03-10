from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from statuses.models import Status
from labels.models import Labels


class MyUserPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.get_object().id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.warning(self.request, _('You have no permissions'))
            return redirect(
                reverse_lazy('users_list')
            )
        else:
            messages.warning(self.request, _('You must log in'))
            return redirect(
                reverse_lazy('login')
            )


class DelProtectionMixin():

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        try:
            object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            if isinstance(object, Labels):
                messages.error(self.request, _('You can not delete Label which is used'))
            if isinstance(object, Status):
                messages.error(self.request, _('You can not delete Status which is used'))
        return redirect(self.success_url)
