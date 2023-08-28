from os import path

from django.conf.urls.static import static

from config import settings
from mailing.apps import MailingConfig
from mailing.views import Productlistview
app_name = MailingConfig.name

from django.urls import path
from mailing.views import Productlistview

urlpatterns = [
    path('', Productlistview.as_view(), name='home'),
]
