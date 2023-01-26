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

## Images Location in DEV

* `static`
  * `ls static/images/`:

  ```powershell
  PS C:\Users\FlynntKnapp\Programming\django-static> ls static/images/
  
      Directory: C:\Users\FlynntKnapp\Programming\django-static\static\images
  
  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a---           1/25/2023    07:51         238966 Dezzi_02.png
  
  PS C:\Users\FlynntKnapp\Programming\django-static>
  ```

## Images Location in PROD

* `staticfiles`
  * `ls -al`:

    ```bash
    ~ $ ls -al
    total 116
    drwx------ 10 u51836 dyno  4096 Jan 26 03:06 .
    drwxr-xr-x 11 root   root  4096 Jan 24 17:32 ..
    drwx------  4 u51836 dyno  4096 Jan 26 03:05 accounts
    drwx------  4 u51836 dyno  4096 Jan 26 03:05 config
    -rw-------  1 u51836 dyno  7405 Jan 26 03:05 .gitignore
    drwx------  4 u51836 dyno  4096 Jan 26 03:05 .heroku
    -rw-------  1 u51836 dyno 35149 Jan 26 03:05 LICENSE
    -rw-------  1 u51836 dyno   674 Jan 26 03:05 manage.py
    drwx------  2 u51836 dyno  4096 Jan 26 03:05 notes
    -rw-------  1 u51836 dyno   264 Jan 26 03:05 Pipfile
    -rw-------  1 u51836 dyno  4358 Jan 26 03:05 Pipfile.lock
    -rw-------  1 u51836 dyno    96 Jan 26 03:05 Procfile
    drwx------  2 u51836 dyno  4096 Jan 26 03:05 .profile.d
    -rw-------  1 u51836 dyno   528 Jan 26 03:05 README.md
    -rw-------  1 u51836 dyno   145 Jan 26 03:05 requirements.txt
    -rw-------  1 u51836 dyno    13 Jan 26 03:05 runtime.txt
    drwx------  3 u51836 dyno  4096 Jan 26 03:05 static
    drwx------  4 u51836 dyno  4096 Jan 26 03:05 staticfiles
    drwx------  3 u51836 dyno  4096 Jan 26 03:05 templates
    ~ $
    ```

  * `ls staticfiles/images/`:

    ```bash
    ~ $ ls staticfiles/images/
    Dezzi_02.png
    ~ $
    ```
