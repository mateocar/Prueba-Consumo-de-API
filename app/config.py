import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://4advance.co/testapi/get.php")
USER_ID = os.getenv("USER_ID", "A1B7T3")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./prueba.db")

