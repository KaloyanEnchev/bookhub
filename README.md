📚 BookHub
BookHub is a Django web application for browsing books and managing user reviews.
It demonstrates Django fundamentals such as models, views, templates, forms, and URL routing.

🚀 Features:
📖 View a list of books
🔍 Book detail pages
✍️ Create, edit, and delete reviews
🧩 Django templates & template inheritance
🗂️ URL configuration with named routes
💾 SQLite database
🛠️ Tech Stack

Python 3
Django
SQLite
HTML / Django Templates
Git & GitHub

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/KaloyanEnchev/bookhub.git
cd bookhub

2️⃣ Create a virtual environment
python -m venv .venv

Activate it:
Windows:
.venv\Scripts\activate

macOS / Linux:
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Run the development server
python manage.py runserver

Open your browser at:
http://127.0.0.1:8000/

📂 Project Structure
bookhub/
│
├── books/              # Books app
├── reviews/            # Reviews app
├── templates/          # HTML templates
├── staticfiles/        # Static files
├── db.sqlite3          # Database
├── manage.py
└── requirements.txt

🧪 Learning Goals:
This project was created to practice:
Django CRUD operations
Working with related models
Forms and validation
Clean project structure
Git & GitHub workflow

👤 Author
Kaloyan Enchev
GitHub: @KaloyanEnchev

📄 License
This project is for educational purposes
