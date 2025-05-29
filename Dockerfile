# Базовий образ Python
FROM python:3.11-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл із залежностями
COPY requirements.txt .

# Встановлюємо всі залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі інші файли проєкту в контейнер
COPY . .

# Створюємо директорію для збереження повідомлень
RUN mkdir -p storage

# Відкриваємо порт 3000 для доступу до додатку
EXPOSE 3000

# Команда запуску додатку
CMD ["python", "app.py"]
