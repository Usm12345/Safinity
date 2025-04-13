[app]
# (str) Title of your application
title = Safinity

# (str) Target platform (android, ios, etc)
target = android

# (str) Package name
package.name = safinity

# (str) Package domain (needed for android/ios packaging)
package.domain = org.safinity

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*,fonts/*,screens/**/*,models/**/*,utils/**/*,services/**/*,migrations/**/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning
version = 0.1

# (str) Application icon
icon.filename = Safinity/logo.png

# (str) Presplash image
presplash.filename = Safinity/logo.png

# (list) Application requirements
requirements = python3,kivy==2.1.0,kivymd==1.1.1,sqlalchemy==2.0.23,bcrypt==3.2.2,python-dotenv==1.0.0,plyer==2.1.0,pyjnius==1.5.0,android==0.9,setuptools==58.2.0,cython==0.29.36,pillow,requests,twilio,tomli,libffi==3.3

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_CONTACTS,WRITE_CONTACTS,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_ADVERTISE,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,BATTERY_STATS

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21
android.ndk_api = 21

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = armeabi-v7a, arm64-v8a

# (str) python-for-android branch to use
p4a.branch = develop

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.apptheme = @android:style/Theme.NoTitleBar

# (bool) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

