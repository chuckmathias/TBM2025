# venv setup / activate
source venv/bin/activate

# Install requirements.txt
pip install -r requirements.txt

# Fixing sqlite issues...
export LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
python -c "import sqlite3; print(sqlite3.sqlite_version)"

# How to run the server...
python manage.py runserver

# How to update your main.scss
Run this in another terminal
npx sass --watch static/scss/main.scss:static/css/main.css
Make Changes
Then Hard Refresh the Page (Ctrl+Shift+R)

# GitHub Project Managment...
git pull origin main
git add .
git commit -m "Describe your changes here"
git push origin main

# Making Migrations
python manage.py makemigrations
python manage.py migrate
python manage.py runserver