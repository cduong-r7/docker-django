"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#from usr/local/lib/python3.7/site-packages 
#import tcell_agent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ['TCELL_AGENT_CONFIG'] = '/Users/cduong/Desktop/docker-django/mysite/tcell/tcell_agent.config'

os.environ['TCELL_AGENT_HOME'] = '/Users/cduong/Desktop/docker-django/mysite/tcell'
application = get_wsgi_application()

import tcell_agent
tcell_agent.init()

