# 🔧 PythonAnywhere Deployment Fix Guide

**Status**: CRITICAL - Multiple deployment errors detected  
**Priority**: HIGH - Database schema mismatch & missing files  
**Date**: 2025-11-12

---

## 📊 Error Analysis

### Error Timeline:
```
06:43:29 - ModuleNotFoundError: No module named 'mysite.settings'
13:52:50 - ModuleNotFoundError: No module named 'crispy_forms' 
14:00:22 - ModuleNotFoundError: No module named 'payment.urls'
14:02:45 - DisallowedHost: 'ahmaddani.pythonanywhere.com' not in ALLOWED_HOSTS
14:05:16 - OperationalError: no such table: core_layanan
14:12:54 - TemplateDoesNotExist: registration/login.html
14:45:37 - OperationalError: no such column: core_layanan.created_at
```

### Root Causes:
1. ❌ **Database not migrated** - New models (with created_at, updated_at) not synced
2. ❌ **Missing packages** - crispy_forms, crispy_bootstrap5 not installed in venv
3. ❌ **Templates not collected** - Static/template files missing
4. ❌ **ALLOWED_HOSTS misconfigured** - Domain not whitelisted
5. ❌ **payment.urls may have syntax errors** - Can't be imported

---

## ✅ Step-by-Step Fix (PythonAnywhere)

### STEP 1: Open PythonAnywhere Bash Console

Go to: https://www.pythonanywhere.com/user/ahmaddani/consoles/

Click "Create a new console" → "Bash"

---

### STEP 2: Fix ALLOWED_HOSTS in settings

```bash
cd ~/bengkel-autocare
nano bengkel/settings.py
```

**Find this section:**
```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.pythonanywhere.com']
```

**If not present, add it. Verify it includes:**
```python
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'ahmaddani.pythonanywhere.com',
    '.pythonanywhere.com',
]
```

**Save**: Press `Ctrl+X`, then `Y`, then `Enter`

---

### STEP 3: Pull Latest Changes from GitHub

```bash
cd ~/bengkel-autocare
git pull origin main
```

**Expected output:**
```
Already up to date.
(or shows new commits if any)
```

---

### STEP 4: Install Missing Packages

```bash
pip install django-crispy-forms crispy-bootstrap5 pillow
```

**Expected output:**
```
Successfully installed django-crispy-forms crispy-bootstrap5
```

---

### STEP 5: Create & Run Migrations

```bash
cd ~/bengkel-autocare
python manage.py makemigrations
```

**Should show:**
```
No changes detected in 'core'
No changes detected in 'booking'
No changes detected in 'payment'
```

**Then migrate:**
```bash
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, core, booking, payment
Running migrations:
  Applying core.0001_initial... OK
  Applying booking.0001_initial... OK
  Applying payment.0001_initial... OK
  (plus other migrations)
```

---

### STEP 6: Verify No Errors

```bash
python manage.py check
```

**Should show:**
```
System check identified no issues (0 silenced).
```

If there are errors, read them and fix before proceeding.

---

### STEP 7: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

**Expected output:**
```
Copying '...'
...
123 static files copied to '/home/ahmaddani/bengkel-autocare/staticfiles'
```

---

### STEP 8: Verify payment.urls

```bash
python manage.py shell
```

**Then in Python shell:**
```python
from payment import urls
print("payment.urls loaded successfully!")
exit()
```

**If you see error:**
- Go back and check for syntax errors in `payment/urls.py`
- Verify all imports are correct

---

### STEP 9: Restart PythonAnywhere Web App

1. Go to: https://www.pythonanywhere.com/user/ahmaddani/webapps/
2. Find: `ahmaddani.pythonanywhere.com`
3. Click "Reload" button (green button at top)
4. Wait 30 seconds for app to restart

---

### STEP 10: Test Website

Open in browser: https://ahmaddani.pythonanywhere.com/

**Expected behavior:**
- ✅ Home page loads with services
- ✅ Login link in navbar works
- ✅ No 500 errors in console

---

## 🔍 Verification Checklist

After completing all steps, verify:

- [ ] `python manage.py check` shows no issues
- [ ] Database tables exist: `sqlite3 db.sqlite3 ".tables"`
- [ ] core_layanan table has columns: `sqlite3 db.sqlite3 ".schema core_layanan"`
- [ ] Static files collected: `ls staticfiles/ | head`
- [ ] Web app reloaded successfully
- [ ] Home page loads without errors
- [ ] Admin panel accessible: `/admin/`
- [ ] Login page displays properly

---

## 🆘 Troubleshooting

### Problem: `no such table: core_layanan`
**Solution**: Run migrations: `python manage.py migrate`

### Problem: `No module named 'crispy_forms'`
**Solution**: Install package: `pip install django-crispy-forms crispy-bootstrap5`

### Problem: `TemplateDoesNotExist: registration/login.html`
**Solution**: Ensure templates exist in local repo and were pushed to GitHub

### Problem: `DisallowedHost` error
**Solution**: Add domain to ALLOWED_HOSTS in settings.py and restart

### Problem: `ModuleNotFoundError: No module named 'payment.urls'`
**Solution**: Check syntax in payment/urls.py, run: `python -c "from payment import urls"`

### Problem: Web app still shows old code
**Solution**: Hard refresh browser (Ctrl+Shift+R) and restart web app

---

## 📋 Important PythonAnywhere Commands

```bash
# Check logs
tail -100 /var/log/ahmaddani_pythonanywhere_com_error.log

# Check if templates exist
find ~/bengkel-autocare/templates -name "*.html" | head -20

# Verify virtual environment
which python
pip list | grep -i django

# Check database
sqlite3 ~/bengkel-autocare/db.sqlite3 "SELECT name FROM sqlite_master WHERE type='table';"

# Test import
python -c "from bengkel import settings; print(settings.ALLOWED_HOSTS)"
```

---

## 📲 Manual Command Sequence (Copy-Paste)

If above steps don't work, run this complete sequence:

```bash
cd ~/bengkel-autocare && \
git pull origin main && \
pip install -r requirements.txt && \
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
python manage.py check
```

Then restart web app from dashboard.

---

## 🎯 Expected Final State

After all fixes:

| Component | Status |
|-----------|--------|
| Database tables | ✅ Created (core_layanan, booking_booking, etc.) |
| Static files | ✅ Collected to staticfiles/ |
| Templates | ✅ Available in templates/ |
| Packages | ✅ Installed (Django, crispy-forms, etc.) |
| ALLOWED_HOSTS | ✅ Includes ahmaddani.pythonanywhere.com |
| Web app | ✅ Running without errors |
| Home page | ✅ Loads with services list |

---

## 🚨 If Still Not Working

1. **Check error log:**
   ```bash
   tail -200 /var/log/ahmaddani_pythonanywhere_com_error.log
   ```

2. **Check web config:**
   - Go to Web App settings → WSGI configuration
   - Ensure it points to: `/home/ahmaddani/bengkel-autocare/bengkel/wsgi.py`

3. **Verify Python version:**
   ```bash
   python --version  # Should be 3.10+
   ```

4. **Check virtual env path:**
   - Web app should use venv at: `/home/ahmaddani/bengkel-autocare/venv`

5. **Test direct import:**
   ```bash
   python manage.py shell
   >>> from core.models import Layanan
   >>> print(Layanan.objects.all())
   ```

---

**Last Updated**: 2025-11-12  
**Next Review**: After deployment  
**Status**: Ready for deployment fix

