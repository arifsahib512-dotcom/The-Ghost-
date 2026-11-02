[app]
title = Ghost App
package.name = ghostapp
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license_agreement = True
android.ant = auto
