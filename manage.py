#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def handler(environ, start_response):
    """Handler para serverless no Vercel."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    
    # Aqui você importa o WSGI application, que é o ponto de entrada para a aplicação.
   from django.core.wsgi import get_wsgi_application
   handler = get_wsgi_application()
    
    # Retorna a aplicação WSGI para o Vercel.
    return application(environ, start_response)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
handler = application

if __name__ == '__main__':
    main()
