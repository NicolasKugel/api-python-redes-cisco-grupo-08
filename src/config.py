# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("NC_BASE_URL")
USUARIO = os.getenv("NC_USERNAME")
PASSWORD = os.getenv("NC_PASSWORD")
NRO_TICKET = os.getenv("NRO_TICKET")
