[app]
title = The Ghost
package.name = theghost
package.domain = com.theghost.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
p4a.bootstrap = sdl2
p4a.branch = master
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
