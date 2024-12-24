![Banner](./Screenshots/banner.png)

---

Welcome to the **Django Delights** project! This application is a robust inventory management system tailored for restaurants or food-related businesses. Built using Django and powered by **Class-Based Views (CBVs)**, it offers an intuitive interface and efficient CRUD operations for seamless management.

---

## 🖋️ Table of Contents
1. [Overview](#-overview)
2. [Features](#-features)
3. [Screenshots](#-screenshots)
4. [Dependencies](#-dependencies)
5. [Installation](#-installation)
6. [Admin Credentials](#-admin-credentials)

---

## 📜 Overview

Django Delights combines the simplicity of Django with a user-friendly frontend to create a dynamic inventory management system. Key functionalities include:
- User authentication.
- CRUD operations for ingredients, menu items, and purchases.
- Real-time tracking of inventory and purchase costs.

---

## ✨ Features

- **User Authentication** 🔑:
  - Sign-up and login capabilities with Django's built-in authentication system.

- **Inventory Management** 📦:
  - Add, view, update, and delete ingredients, menu items, and purchases.

- **Class-Based Views** ⚡:
  - Cleaner and reusable view logic for all CRUD operations.

- **Dynamic Templates** 🖌️:
  - Responsive templates for enhanced user experience.

---

## 🗄️ Screenshots

![Home Page](./Screenshots/home.png)

![Ingredients Page](./Screenshots/ingredients.png)

![Menu Items Page](./Screenshots/menuitems.png)

![Menu Item Detail Page](./Screenshots/menuitem_detail.png)

![Purchases Page](./Screenshots/purchases.png)

---

## 📦 Dependencies

This project requires the following Python libraries:
- **Django**: Backend framework for building the application.
- **SQLite**: Default database for Django projects.

Install all dependencies with:
```bash
pip install -r requirements.txt
```
---

## 🚀 Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/USMAN-FAIZYAB-KHAN/Django-Delights.git
   cd Django-Delights
   ```
3. Set up a virtual environment (optional but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install Dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
5. Run the development server:

    ```bash
   python manage.py runserver
   ```
Visit `http://127.0.0.1:8000/` to explore the application.
       
---

## 🗝️ Admin Credentials

To log in and test the application, use the following credentials:

- **Username:** admin  
- **Password:** P@ssword123
