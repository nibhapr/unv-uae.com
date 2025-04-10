# 🌍 UNV-UAE Django Project

This is a Django-based web application using **Bootstrap**, **Python 3.10.4** and **SQLite3** as the default database engine. Redis is optionally supported for caching or background task handling. The project runs locally and is also deployed at [https://unv-uae.com](https://unv-uae.com).

---

## 🔧 Technologies Used

- Python 3.10.4
- Bootstrap
- SQLite3 (development database)
- Redis (optional)
- HTML / CSS / JavaScript (via Django Templates)

## 🛠️ Local Setup Instructions

### 1. Clone the Project
[`git clone https://github.com/amananilofficial/unv-uae.com.git`]
[`cd unv-uae.com`]

### 2. Create and Activate a Virtual Environment
py -3.10 -m venv myenv
[`.\myenv\Scripts\Activate.ps1`]    # For Windows PowerShell
[`pip install -r requirements.txt`]

### 3. Collect Static Files
[`python manage.py collectstatic --clear`]

### 4. Run Migrations
[`python manage.py makemigrations`]
[`python manage.py migrate`]

### 5. Create a Superuser
[`python manage.py createsuperuser`]

### 6. Run the Development Server
[`python manage.py runserver`]

### 🌐 Access URLs
### Local Development URLs
Main Site: http://127.0.0.1:8000/ <br>
Admin Panel: http://127.0.0.1:8000/admin/

### Production (Live Site)
Main Site: https://unv-uae.com/ <br>
Admin Panel: https://unv-uae.com/admin/

### 📞 Contact Information

- 📧 **Gmail:** [amananiloffical@gmail.com](mailto:amananiloffical@gmail.com)  
- 📱 **Phone:** [`+91 7892939127`](tel:+917892939127) *(clickable on mobile)*
- <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/WhatsApp_icon.png" width="20"/> **WhatsApp:** [+91 7892939127](https://wa.me/917892939127)  
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="20"/> **LinkedIn:** [amananilofficial](https://www.linkedin.com/in/amananilofficial)  
- <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="20"/> **Instagram:** [@amananilofficial](https://instagram.com/amananilofficial)


