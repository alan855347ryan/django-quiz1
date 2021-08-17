"""
WSGI config for quizgk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

reload(sys)     
sys.setdefaultencoding("utf-8")


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizgk.settings')



application = get_wsgi_application()
