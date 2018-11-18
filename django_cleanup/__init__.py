# coding: utf-8
'''
    django-cleanup automatically deletes files for FileField, ImageField, and
    subclasses. It will delete old files when a new file is being save and it
    will delete files on model instance deletion.
'''
from __future__ import unicode_literals

__version__ = '3.0.0-dev'
default_app_config = 'django_cleanup.apps.CleanupConfig'
