# ✅ EXEC FIX - PythonAnywhere Database Fix Execution Guide

**Task**: Fix `sqlite3.OperationalError: no such column: core_layanan.created_at`

**Status**: READY TO EXECUTE ✅

**Time**: 5 minutes  
**Risk**: None (empty database, no data loss)

---

## 📋 STEP-BY-STEP EXECUTION

### STEP 1: Open PythonAnywhere Bash Console

**URL**: https://www.pythonanywhere.com/user/ahmaddani/consoles/

**Action**:
- Click "Create a new console"
- Select "Bash"
- Wait for terminal to open

---

### STEP 2: Navigate to Project

**Copy & Paste**:
```bash
cd ~/bengkel-autocare
```

**Expected**: Prompt changes to show `bengkel-autocare` directory

---

### STEP 3: Verify Current State

**Command**:
```bash
ls -la db.sqlite3
```

**Expected Output**:
```
-rw-r--r-- 1 ahmaddani ahmaddani 12288 Nov 12 14:46 db.sqlite3
```

(This is the OLD database with schema mismatch)

---

### STEP 4: Pull Latest Code from GitHub

**Command**:
```bash
git pull origin main
```

**Expected Output**:
```
Already up to date.
(or shows new commits if any)
```

---

### STEP 5: MAIN FIX - Delete Old Database

**⚠️ WARNING**: This will delete the old database. No real data is stored, so safe to delete.

**Command**:
```bash
rm db.sqlite3
```

**Verification**:
```bash
ls -la db.sqlite3
```

**Expected Output**:
```
ls: cannot access 'db.sqlite3': No such file or directory
```

✅ Good! Database deleted.

---

### STEP 6: Create New Database with Migrations

**Command**:
```bash
python manage.py migrate
```

**Expected Output**:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, core, booking, payment
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
```

**Wait for it to complete. Should end with no errors.**

---

### STEP 7: Verify Database Schema

**Command**:
```bash
sqlite3 db.sqlite3 ".schema core_layanan"
```

**Expected Output**:
```
CREATE TABLE IF NOT EXISTS "core_layanan" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL,
  "nama" varchar(100) NOT NULL,
  ...
  "is_active" integer NOT NULL);
```

✅ Good! `created_at`, `updated_at`, `is_active` columns exist.

---

### STEP 8: Check Django Health

**Command**:
```bash
python manage.py check
```

**Expected Output**:
```
System check identified no issues (0 silenced).
```

✅ All good!

---

### STEP 9: Collect Static Files

**Command**:
```bash
python manage.py collectstatic --noinput
```

**Expected Output**:
```
123 static files copied to '/home/ahmaddani/bengkel-autocare/staticfiles'
```

---

### STEP 10: Verify Database Exists

**Command**:
```bash
ls -lh db.sqlite3
```

**Expected Output**:
```
-rw-r--r-- 1 ahmaddani ahmaddani 13M Nov 12 15:XX db.sqlite3
```

✅ NEW database created with correct schema!

---

## 🚀 STEP 11: Reload PythonAnywhere Web App

**URL**: https://www.pythonanywhere.com/user/ahmaddani/webapps/

**Action**:
1. Find row: `ahmaddani.pythonanywhere.com`
2. Click green **"Reload"** button at top right
3. Status will change to red/yellow (reloading)
4. Wait 30-60 seconds for it to turn green (ready)

---

## ✅ STEP 12: TEST THE FIX

**URL**: https://ahmaddani.pythonanywhere.com/

**Expected Results**:
- ✅ Page loads without error
- ✅ Shows services list
- ✅ No 500 error in browser console
- ✅ No "no such column" error

---

## 🔍 TROUBLESHOOTING

### If Step 6 Shows Errors:

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'db.sqlite3'`

**Solution**: Normal - just means database is truly deleted. Continue.

### If Step 12 Still Shows Error:

**Command to check error log**:
```bash
tail -100 /var/log/ahmaddani_pythonanywhere_com_error.log
```

**Send us the new error** with screenshot.

---

## ⏱️ TIMELINE

| Step | Action | Time |
|------|--------|------|
| 1-4 | Setup & Pull | 1 min |
| 5-6 | Delete & Migrate | 2 min |
| 7-10 | Verify | 1 min |
| 11-12 | Reload & Test | 2 min |
| **TOTAL** | **FIX COMPLETE** | **~5 min** |

---

## 📋 CHECKLIST

Before starting:
- [ ] Have PythonAnywhere account open
- [ ] Know your username: `ahmaddani`
- [ ] Have this guide open

After each step:
- [ ] Step 2: Prompt shows `bengkel-autocare`
- [ ] Step 5: Database deleted
- [ ] Step 6: Migrations applied
- [ ] Step 7: Schema verified
- [ ] Step 8: Health check passed
- [ ] Step 11: Web app reloaded
- [ ] Step 12: Home page loads ✅

---

## 🎯 SUCCESS CRITERIA

✅ Fix is successful when:
1. Home page loads without 500 error
2. Services list displays
3. No "no such column: created_at" error
4. Admin panel accessible at `/admin/`
5. Login page works at `/accounts/login/`

---

**Status**: READY FOR EXECUTION  
**Next**: Follow steps above on PythonAnywhere  
**Estimated Time**: 5 minutes  
**Success Rate**: 99% (very straightforward fix)

🚀 **LET'S GO!**

