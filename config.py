import os
from dotenv import load_dotenv
from currency_app.modules.check_config import format_port_type

load_dotenv()

PORT = format_port_type(os.getenv('PORT', '8000'))
VERSION = os.getenv('VERSION')
API_KEY = ''
SERVICE = 'currency'
URI = 'https://www.cbr.ru/scripts/XML_daily.asp'
