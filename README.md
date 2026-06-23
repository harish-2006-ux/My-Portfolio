# Harish V M — Portfolio

A full-stack personal portfolio with a password-protected admin panel.
Built with Python (Flask) + HTML/CSS/JavaScript.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python app.py

3. Open in browser:
   http://localhost:5000

## Admin Panel

Visit: http://localhost:5000/admin
Default password: harish123

Change the password in app.py → ADMIN_PASSWORD = "your_new_password"

## Folder Structure

portfolio/
├── app.py              ← Flask backend
├── data.json           ← All your portfolio data
├── requirements.txt
└── templates/
    ├── index.html      ← Public portfolio
    ├── login.html      ← Admin login
    └── admin.html      ← Admin dashboard

## What you can manage from the admin panel

- About Me (name, title, bio, links)
- Projects (add / edit / delete)
- Skills (add / edit / delete with % level)
- Certifications (add / edit / delete)
- Education (add / edit / delete)

## Deploy to Render (Recommended)

### Quick Deploy
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. Go to [Render.com](https://render.com) and sign up/login

3. Click "New +" → "Web Service"

4. Connect your GitHub repository

5. Render will automatically detect the `render.yaml` file and configure everything

6. Click "Create Web Service"

7. Your portfolio will be live at: `https://your-app-name.onrender.com`

### Manual Configuration (if needed)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Environment Variables**:
  - `SECRET_KEY`: (auto-generated)
  - `ADMIN_PASSWORD`: harish123 (change this!)

## Deploy for free

Push to GitHub, then deploy on:
- Render.com (Python/Flask support)
- Railway.app
- PythonAnywhere.com
