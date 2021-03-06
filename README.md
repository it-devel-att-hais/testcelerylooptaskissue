# This app was created for repeat celery (django celery beat) loop task execution error
### [Link to issue](https://github.com/celery/django-celery-beat/issues/376)

### How to up app
```
git clone https://github.com/it-devel-att-hais/testcelerylooptaskissue.git
cd testcelerylooptaskissue/
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```
### Now need to up dockers with percona and redis (better do this in second terminal)
```
docker-compose up
```
### Return to previous terminal with active venv
```
./manage.py migrate
```
This must run all exists migration
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, django_celery_beat, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying django_celery_beat.0001_initial... OK
  Applying django_celery_beat.0002_auto_20161118_0346... OK
  Applying django_celery_beat.0003_auto_20161209_0049... OK
  Applying django_celery_beat.0004_auto_20170221_0000... OK
  Applying django_celery_beat.0005_add_solarschedule_events_choices_squashed_0009_merge_20181012_1416... OK
  Applying django_celery_beat.0006_periodictask_priority... OK
  Applying sessions.0001_initial... OK
```
### Next create superuser for access to django admin
```
./manage.py createsuperuser
```
======
```
Username (leave blank to use 'johndoe'): admin
Email address: fake@email.com
Password: admin123
Password (again): admin123
Superuser created successfully.
```
### Next go to django admin
* http://127.0.0.1:8000/admin/ 
* login: admin | password: admin123
* Choose part  **PeriodicTask**
* For now you will see empty

## Set up celery worker and beat

* Open new terminal for run celery worker
* Enter in project folder and activate venv
* After, run this command
```
celery -A testlooptask worker -l info
```
* Open one more terminal for run celery beat
* Enter in project folder and activate venv
* After, run this command
```
celery -A testlooptask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
* **For now worker and beat must work**

# (After all setups) Steps for repeat loop task execution
* [Return to admin panel with periodic tasks](http://127.0.0.1:8000/admin/django_celery_beat/periodictask/)
* Now you must see at least 2 period tasks
> * print_hello_world: */1 * * * * (m/h/d/dM/MY) Asia/Almaty
> * celery.backend_cleanup: 0 4 * * * (m/h/d/dM/MY) Asia/Almaty
* Select [**print_hello_world: */1 * * * * (m/h/d/dM/MY) Asia/Almaty**](http://127.0.0.1:8000/admin/django_celery_beat/periodictask/2/change/)
* Add new crontab
* Make new crontab around 20 minutes ago and choose UTC timezone
* Save PeriodicTask

![Create new crontab](https://i.ibb.co/84p1Hnk/132.png)

![Create new crontab](https://i.ibb.co/7j5zhb3/134.png)

**Be careful. After update this tasks worker start to run this task in loop**
### Screen I have chance to make
![First screen](https://i.ibb.co/cbHVqcW/135.png)

![Second screen](https://i.ibb.co/0K0F0PB/136.png)

![Third screen](https://i.ibb.co/VmCNGD6/137.png)<a href="https://ibb.co/C29tyvL">
