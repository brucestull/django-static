# Django `static` Example

## Resources

* [How to manage static files (e.g. images, JavaScript, CSS) - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/static-files/)
* [How to deploy static files - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/)

## Features

* Serve 'static' files:
  * Images
  * `CSS`

## URLs

* Application URL:
  * <https://flynnt-knapp-django-static.herokuapp.com/>
* Git URL:
  * <https://git.heroku.com/flynnt-knapp-django-static.git>

## `images` Location in Browser

* `<SERVER_ROOT>/static-url`

## `images` Location in DEV

* `static`
  * `ls .\static-dev\images\`:

  ```powershell
  (django-static) PS C:\Users\FlynntKnapp\Programming\django-static> ls .\static-dev\images\
  
      Directory: C:\Users\FlynntKnapp\Programming\django-static\static-dev\images
  
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a---           1/25/2023    07:51         238966 Dezzi_02.png
  
  (django-static) PS C:\Users\FlynntKnapp\Programming\django-static>
  ```

## `STATIC` File Location in PROD

* `ls -al`:

  ```bash
  ~ $ ls -al
  total 116
  drwx------ 10 u43188 dyno  4096 Jan 26 03:57 .
  drwxr-xr-x 11 root   root  4096 Jan 24 17:32 ..
  drwx------  4 u43188 dyno  4096 Jan 26 03:55 accounts
  drwx------  4 u43188 dyno  4096 Jan 26 03:55 config
  -rw-------  1 u43188 dyno  7405 Jan 26 03:54 .gitignore
  drwx------  4 u43188 dyno  4096 Jan 26 03:55 .heroku
  -rw-------  1 u43188 dyno 35149 Jan 26 03:54 LICENSE
  -rw-------  1 u43188 dyno   674 Jan 26 03:54 manage.py
  drwx------  2 u43188 dyno  4096 Jan 26 03:54 notes
  -rw-------  1 u43188 dyno   264 Jan 26 03:54 Pipfile
  -rw-------  1 u43188 dyno  4358 Jan 26 03:54 Pipfile.lock
  -rw-------  1 u43188 dyno    96 Jan 26 03:54 Procfile
  drwx------  2 u43188 dyno  4096 Jan 26 03:55 .profile.d
  -rw-------  1 u43188 dyno  2401 Jan 26 03:54 README.md
  -rw-------  1 u43188 dyno   145 Jan 26 03:55 requirements.txt
  -rw-------  1 u43188 dyno    13 Jan 26 03:55 runtime.txt
  drwx------  3 u43188 dyno  4096 Jan 26 03:54 static-dev
  drwx------  4 u43188 dyno  4096 Jan 26 03:55 static-prod
  drwx------  3 u43188 dyno  4096 Jan 26 03:54 templates
  ~ $
  ```

* `ls -al static-prod/`:

  ```bash
  ~ $ ls -al static-prod/
  total 16
  drwx------  4 u43188 dyno 4096 Jan 26 03:55 .
  drwx------ 10 u43188 dyno 4096 Jan 26 03:57 ..
  drwx------  6 u43188 dyno 4096 Jan 26 03:55 admin
  drwx------  2 u43188 dyno 4096 Jan 26 03:55 images
  ~ $
  ```

* `ls -al static-prod/admin/`:

  ```bash
  ~ $ ls -al static-prod/admin/
  total 24
  drwx------ 6 u43188 dyno 4096 Jan 26 03:55 .
  drwx------ 4 u43188 dyno 4096 Jan 26 03:55 ..
  drwx------ 3 u43188 dyno 4096 Jan 26 03:55 css
  drwx------ 2 u43188 dyno 4096 Jan 26 03:55 fonts
  drwx------ 3 u43188 dyno 4096 Jan 26 03:55 img
  drwx------ 4 u43188 dyno 4096 Jan 26 03:55 js
  ~ $
  ```

* `ls -al static-prod/images/`:

  ```bash
  ~ $ ls -al static-prod/images/
  total 244
  drwx------ 2 u43188 dyno   4096 Jan 26 03:55 .
  drwx------ 4 u43188 dyno   4096 Jan 26 03:55 ..
  -rw------- 1 u43188 dyno 238966 Jan 26 03:55 Dezzi_02.png
  ~ $
  ```
