from django.db import models

from wagtail.core.models import Page


from wagtail_resume.models import BaseResumePage


class ResumePage(BaseResumePage):
    pass

class HomePage(Page):
    pass
