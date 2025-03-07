from django.core.wsgi import get_wsgi_application
import os

# Configure o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinecourse.settings') 

# Obtenha a aplicação WSGI
application = get_wsgi_application()

# Exponha as variáveis que o Vercel procura
app = application
handler = application