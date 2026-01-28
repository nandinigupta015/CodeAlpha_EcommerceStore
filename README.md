# CodeAlpha Task 1 - Simple E-commerce Store 🛍️

## Project Name
**Ethereal Wardrobe ✨**  
An aesthetic clothing e-commerce website built using Django.

---

## ✅ Features
- User Authentication (Register / Login / Logout)
- Product Listing Page (with images)
- Product Detail Page
- Add to Cart 🛒
- Quantity Increase / Decrease
- Remove from Cart
- Checkout + Order Placement ✅
- My Orders Page + Order Items
- Categories (Filter Products)
- Search + Sort Products
- Dynamic "New Arrival" Badge ✨

---

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, Django Templates  
- **Backend:** Django (Python)  
- **Database:** SQLite (db.sqlite3)

---

## ▶️ How to Run the Project Locally (Windows)

### Prerequisites
- Python 3.10+
- Git
- VS Code / PowerShell

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/nandinigupta015/CodeAlpha_EcommerceStore.git
cd CodeAlpha_EcommerceStore
```
### 2️⃣ Go to backend folder
```
cd backend
```
### 3️⃣ Create virtual environment (first time only)
```
python -m venv env
```
### 4️⃣ Activate virtual environment
```
env\Scripts\activate
```

You should see (env) in the terminal.

### 5️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 6️⃣ Run database migrations
```
python manage.py migrate
```
### 7️⃣ Create admin (superuser)
```
python manage.py createsuperuser
```

Enter username and password.

### 8️⃣ Run the development server
```
python manage.py runserver
```
### 9️⃣ Open in browser

Website: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

