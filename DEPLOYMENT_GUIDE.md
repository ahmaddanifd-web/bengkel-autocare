# 🚀 Deployment Guide - Bengkel AutoCare

## Option 1: Deploy ke Render (Recommended)

### Prerequisites:
- GitHub repository sudah di-push
- Render account (https://render.com)

### Steps:

1. **Sign up ke Render:**
   - Go to: https://render.com/register
   - Sign up dengan GitHub account

2. **Create Web Service:**
   - Dashboard → New ↓ → Web Service
   - Connect GitHub → Select `bengkel-autocare` repository
   - Choose branch: `main`

3. **Configure Service:**
   ```
   Name: bengkel-autocare
   Environment: Python 3
   Region: Singapore (untuk Asia)
   Build Command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   Start Command: gunicorn bengkel.wsgi:application
   Plan: Free
   ```

4. **Add Environment Variables:**
   - Dashboard → Service → Environment
   - Add these variables:
   
   ```
   DEBUG=False
   DJANGO_SECRET_KEY=<generate-new-secret-key>
   MIDTRANS_SERVER_KEY=<your-midtrans-key>
   MIDTRANS_CLIENT_KEY=<your-midtrans-key>
   ```

5. **Create PostgreSQL Database:**
   - Dashboard → New ↓ → PostgreSQL
   - Name: `bengkel-db`
   - Region: Singapore
   - Plan: Free
   - Copy connection string ke `DATABASE_URL`

6. **Deploy:**
   - Click "Deploy"
   - Wait 5-10 minutes
   - Visit: `https://bengkel-autocare.onrender.com`

---

## Option 2: Deploy ke Railway

### Steps:

1. **Sign up:** https://railway.app
2. **Import Project:** 
   - New Project → Deploy from GitHub
   - Select repository
3. **Add PostgreSQL:**
   - Add plugin → PostgreSQL
4. **Configure Environment:**
   - Add variables dari `.env.example`
5. **Deploy:** Automatic

---

## Option 3: Deploy ke PythonAnywhere

### Steps:

1. **Sign up:** https://www.pythonanywhere.com
2. **Upload project** via Git clone
3. **Setup virtualenv** di PythonAnywhere
4. **Configure WSGI** file
5. **Add domain** (custom atau pythonanywhere domain)

---

## Generate Django Secret Key

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Atau gunakan online generator: https://djecrety.ir/

---

## Production Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY diubah (use `get_random_secret_key()`)
- [ ] ALLOWED_HOSTS sesuai domain
- [ ] Database: PostgreSQL (production)
- [ ] Static files: collectstatic dijalankan
- [ ] Media files: upload ke S3 (optional)
- [ ] Email: configure SMTP
- [ ] Logging: setup error tracking
- [ ] SSL/HTTPS: auto-enabled di Render
- [ ] Backup database: regular schedule

---

## Troubleshooting

### Error: "No module named 'crispy_bootstrap5'"
```bash
pip install -r requirements.txt
```

### Error: "static files not found"
```bash
python manage.py collectstatic --noinput
```

### Error: "database does not exist"
```bash
python manage.py migrate
```

### Error: "ModuleNotFoundError: No module named 'gunicorn'"
```bash
pip install gunicorn
```

### Logs not showing?
Di Render dashboard:
- Select service → Logs tab
- Real-time log streaming

---

## Domain Setup

### Point custom domain ke Render:

1. Go to: Service Settings → Custom Domains
2. Add your domain (e.g., `bengkel.com`)
3. Update DNS records:
   - Type: CNAME
   - Name: `bengkel`
   - Value: `bengkel-autocare.onrender.com`
4. Wait 15-30 minutes untuk DNS propagation

---

## Environment Variables Reference

```env
# Required
DEBUG=False
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@host:port/db

# Midtrans
MIDTRANS_SERVER_KEY=Mid-server-key
MIDTRANS_CLIENT_KEY=Mid-client-key
MIDTRANS_ENVIRONMENT=production

# Optional: Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=app-password

# Optional: AWS S3
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

---

## Monitor Application

**Render Dashboard:**
- Service health
- Deployment history
- Environment logs
- CPU/Memory usage

**Django Admin:**
- https://your-domain/admin
- Monitor bookings & transactions
- View user activity

---

## Scaling

Free tier limits:
- 0.5 CPU
- 512MB RAM
- PostgreSQL: 90-day inactivity auto-deletion

Upgrade to paid untuk:
- Unlimited resources
- Custom domains
- Better uptime

---

## Backup & Recovery

**Database backup:**
```bash
python manage.py dumpdata > backup.json
```

**Restore:**
```bash
python manage.py loaddata backup.json
```

**Auto-backup di Render:**
- PostgreSQL → Backups tab
- Set retention policy

---

## Performance Optimization

1. **Enable caching:**
   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
           'LOCATION': 'my_cache_table',
       }
   }
   ```

2. **Database indexing:**
   - Add `db_index=True` ke fields sering di-query

3. **Compress static files:**
   ```bash
   python manage.py collectstatic --compress
   ```

4. **CDN untuk media files:**
   - Gunakan AWS CloudFront

---

## Next Steps

- [ ] Deploy ke staging dulu
- [ ] Test semua fitur di production
- [ ] Setup monitoring & alerts
- [ ] Create backup strategy
- [ ] Document production processes
- [ ] Setup CI/CD pipeline (GitHub Actions)

---

## Support

- Django Docs: https://docs.djangoproject.com
- Render Docs: https://render.com/docs
- Midtrans Docs: https://docs.midtrans.com

---

**Happy deploying!** 🎉
