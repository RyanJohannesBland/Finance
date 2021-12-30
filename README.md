#### Financial Planner

### Development
1. Navigate into root directory of app
Backend:
2. docker run -it -p 8000:8000 -v "$(PWD)":/app python:3.9 bash
3. cd /app/FinancialPlanner && python manage.py runserver 0.0.0.0:8000
4. Navigate to localhost:8000 in web browser.

Frontend:
2. docker run -it -p 8080:8080 -v "$(PWD)":/app node:16 bash
3. npm install -g @vue/cli
4.