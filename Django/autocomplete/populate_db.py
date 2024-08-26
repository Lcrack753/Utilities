import os
import django
from faker import Faker
import random
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Ajusta esto según tu estructura
django.setup()

# Importa tu modelo
from autocomplete.models import Autocomplete
# from config.settings import DEFAULT_AUTO_FIELD
# Inicializa Faker
fake = Faker()

def populate_data(num_entries):
    for _ in range(num_entries):
        # Genera datos aleatorios usando Faker
        instance = Autocomplete(
            name=fake.name(),
            last=fake.last_name(),
            age=random.randint(10,80),
            # Añade más campos según tu modelo
        )
        instance.save()

if __name__ == '__main__':
    populate_data(100)  # Cambia 100 por la cantidad de datos que desees generar