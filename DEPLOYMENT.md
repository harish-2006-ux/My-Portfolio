# 🚀 Deployment Guide

Your portfolio is ready to deploy! Follow these steps:

## Step 1: Push to GitHub

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it something like `my-portfolio`
   - Choose "Public" or "Private"
   - Don't initialize with README (we already have one)
   - Click "Create repository"

2. **Push your code:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Render

### Option A: Automatic Deploy (Recommended)

1. Go to **[render.com](https://render.com)** and sign up/login with GitHub

2. Click **"New +"** → **"Web Service"**

3. **Connect your GitHub repository**
   - Give Render permission to access your repos
   - Select your portfolio repository

4. **Render will auto-detect settings** from `render.yaml`:
   - ✅ Build Command: `pip install -r requirements.txt`
   - ✅ Start Command: `gunicorn app:app`
   - ✅ Python version: 3.11

5. **Click "Create Web Service"**

6. **Wait for deployment** (2-3 minutes)

7. **Your portfolio is live!** 🎉
   - URL will be: `https://YOUR-APP-NAME.onrender.com`

### Option B: Manual Configuration

If automatic detection doesn't work:

1. After connecting your repo, configure:
   - **Name**: my-portfolio
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

2. Add Environment Variables:
   - `SECRET_KEY`: (click "Generate" or use any random string)
   - `ADMIN_PASSWORD`: harish123 (⚠️ change this to something secure!)

3. Click "Create Web Service"

## Step 3: Access Your Live Portfolio

### Public Portfolio
Visit: `https://your-app-name.onrender.com`

### Admin Panel
Visit: `https://your-app-name.onrender.com/admin`
- Password: `harish123` (or whatever you set in environment variables)

## 🔐 Security Tips

1. **Change the admin password** in Render dashboard:
   - Go to your service → Environment
   - Update `ADMIN_PASSWORD` variable
   - Save changes (app will redeploy)

2. **Use a strong SECRET_KEY**:
   - Let Render generate it automatically
   - Or use: `python -c "import secrets; print(secrets.token_hex(32))"`

## 📝 Making Updates

After making changes to your portfolio:

```bash
git add .
git commit -m "Update portfolio content"
git push
```

Render will automatically detect the push and redeploy! 🔄

## 💰 Cost

**Free tier includes:**
- ✅ Free forever
- ✅ Automatic SSL certificate
- ✅ Custom domain support
- ⚠️ App sleeps after 15 minutes of inactivity (takes ~30s to wake up)

**Paid tier ($7/month):**
- ✅ No sleeping
- ✅ Faster performance
- ✅ More resources

## 🛠️ Troubleshooting

### Build Fails
- Check Python version compatibility
- Verify `requirements.txt` is correct

### App Won't Start
- Check logs in Render dashboard
- Verify `gunicorn` is in requirements.txt

### Data Not Showing
- Make sure `data.json` is not in `.gitignore`
- Check that it was committed to Git

## 🎯 Next Steps

1. ✅ Deploy to Render
2. ✅ Test your live site
3. ✅ Update admin password
4. ✅ Add custom domain (optional)
5. ✅ Share your portfolio!

---

Need help? Check the [Render docs](https://render.com/docs) or open an issue!
