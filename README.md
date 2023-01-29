# Django `static` Example

## Resources

* [How to manage static files (e.g. images, JavaScript, CSS) - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/static-files/)
* [How to deploy static files - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/)

## `static` Files

* Serve `static` files:
  * `images` - The directory which contains the images.
    * It can be found in both `static-dev` (on both development and production servers) and `static-prod` (on production server).
  * `css`
  * `fonts`
  * `img`
  * `js`

### Pertinent Files and Constants

#### Constants

* `STATIC_URL` - The URL to use when referring to static files located in `STATIC_ROOT`:
  * We use Django template tag `static` to refer to location of the static file `Dezzi_02.png`.

    ```html
    <img
        ...
        src="{% static 'images/Dezzi_02.png' %}"
        ...
        />
    ```

  -OR-
  * We hard-code the location of the static file `Dezzi_02.png`.

    ```html
        <img
            ...
            src='/static-url/images/Dezzi_02.png'
            ...
            />
    ```

* `STATIC_ROOT` - The absolute path to the directory where collectstatic will copy the static files and place them in one directory for deployment.
  * `STATIC_ROOT` is not set in `development.py` since Django doesn't need to move any files while we're in development. This helps us avoid having to run `collectstatic` every time we make a change to a static file.
* `STATICFILES_DIRS` - A list of locations of additional static files.
  * We are using it in this example to point to the `static-dev` directory to serve static files in development.

#### Files

* [`config/settings/common.py`](./config/settings/common.py):

  ```python
  #...
  STATIC_URL = '/static-url/'
  #...
  STATICFILES_DIRS = [
      BASE_DIR / 'static-dev',
  ]
  #...
  ```

* [`config/settings/production.py`](./config/settings/production.py):
  
    ```python
    #...
    STATIC_ROOT = BASE_DIR / 'static-prod'
    #...
    ```

* [`config/settings/development.py`](./config/settings/development.py):

### `images` Location in Browser

* `<SERVER_ROOT>/static-url`

### `images` Location in DEV (Project/Repository root)

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

### `STATIC` File Location in PROD

* `ls -al`:

  ```bash
  ~ $ ls -al
  ...
  drwx------  4 u43188 dyno  4096 Jan 26 03:55 static-prod
  ...
  ~ $
  ```

* `ls -al static-prod/`:

  ```bash
  ~ $ ls -al static-prod/
  ...
  drwx------  6 u43188 dyno 4096 Jan 26 03:55 admin
  drwx------  2 u43188 dyno 4096 Jan 26 03:55 images
  ...
  ~ $
  ```

* `ls -al static-prod/admin/`:

  ```bash
  ~ $ ls -al static-prod/admin/
  ...
  drwx------ 3 u43188 dyno 4096 Jan 26 03:55 css
  drwx------ 2 u43188 dyno 4096 Jan 26 03:55 fonts
  drwx------ 3 u43188 dyno 4096 Jan 26 03:55 img
  drwx------ 4 u43188 dyno 4096 Jan 26 03:55 js
  ...
  ~ $
  ```

* `ls -al static-prod/images/`:

  ```bash
  ~ $ ls -al static-prod/images/
  ...
  -rw------- 1 u43188 dyno 238966 Jan 26 03:55 Dezzi_02.png
  ...
  ~ $
  ```
