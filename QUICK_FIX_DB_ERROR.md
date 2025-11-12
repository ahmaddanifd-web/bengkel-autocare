# 🔴 QUICK FIX: Database Schema Mismatch

**Error**: `sqlite3.OperationalError: no such column: core_layanan.created_at`

**Cause**: Database has old schema. Models now include `created_at`, `updated_at`, `is_active` fields that don't exist in the old database.

**Solution**: Delete old database and recreate with new schema.

---

## ⚡ ONE-COMMAND FIX (PythonAnywhere Bash Console)

```bash
cd ~/bengkel-autocare && \
rm db.sqlite3 && \
python manage.py migrate && \
python manage.py check && \
echo "✅ Database fixed!"
```

Then **Reload web app** from PythonAnywhere dashboard.

---

## 📝 Step-by-Step If Above Doesn't Work

### 1. SSH into PythonAnywhere
Go to: https://www.pythonanywhere.com/user/ahmaddani/consoles/
Click: "Create new console" → "Bash"

### 2. Navigate to project
```bash
cd ~/bengkel-autocare
```

### 3. Delete old database (⚠️ WARNING: LOSES OLD DATA!)
```bash
rm db.sqlite3
```

### 4. Create new database with migrations
```bash
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, core, booking, payment
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  (... more migrations ...)
```

### 5. Verify
```bash
python manage.py check
```

**Should show:**
```
System check identified no issues (0 silenced).
```

### 6. Reload web app
Go to: https://www.pythonanywhere.com/user/ahmaddani/webapps/
Click green "Reload" button next to `ahmaddani.pythonanywhere.com`

---

## ✅ Test After Fix

Open in browser: https://ahmaddani.pythonanywhere.com/

**Should work:**
- ✅ Home page loads
- ✅ Services display without error
- ✅ No 500 error in console

---

## 🆘 If Still Fails

Check the error log:
```bash
tail -50 /var/log/ahmaddani_pythonanywhere_com_error.log
```

Then send us the new error message.

---

**Status**: Ready to fix  
**Time**: 2-3 minutes  
**Risk**: Low (just recreates empty database)

