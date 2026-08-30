#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة استبدال الروابط في كل صفحات الموقع مرة واحدة.
الاستخدام:
  python3 replace_urls.py

سيسألك عن:
  1) نطاق GitHub Pages الخاص بك (مثال: https://myuser.github.io/my-site)
  2) رابط الموقع الهدف (الذي تريد جلب الزوار إليه)
  3) اسم الموقع/البراند (اختياري — اتركه فارغاً للإبقاء على "موسوعة اليوم")
"""
import os, sys, io

BASE = os.path.dirname(os.path.abspath(__file__))  # مجلد tools
ROOT = os.path.dirname(BASE)                        # جذر المشروع

EXTS = {'.html', '.xml', '.txt', '.js', '.css', '.md'}

def main():
    print('=' * 55)
    print(' أداة ربط صفحات موسوعة اليوم — GitHub Pages')
    print('=' * 55)
    gh = input('1) نطاق GitHub Pages (مثال https://user.github.io/repo): ').strip().rstrip('/')
    target = input('2) رابط الموقع الهدف (مثال https://mysite.com): ').strip().rstrip('/')
    brand = input('3) اسم البراند (اضغط Enter للإبقاء على "موسوعة اليوم"): ').strip()

    if not gh or not target:
        print('❌ يجب إدخال النطاق والرابط الهدف.')
        sys.exit(1)

    if gh.startswith('http://') or target.startswith('http://'):
        print('⚠️  تنبيه: يُفضل استخدام https:// وليس http://')

    replaced = 0
    for dirpath, _, files in os.walk(ROOT):
        for fn in files:
            ext = os.path.splitext(fn)[1].lower()
            if ext not in EXTS:
                continue
            path = os.path.join(dirpath, fn)
            try:
                with io.open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            original = content
            content = content.replace('https://USERNAME.github.io/REPO', gh)
            content = content.replace('https://TARGET-SITE.com', target)
            if brand:
                content = content.replace('موسوعة اليوم', brand)
            if content != original:
                with io.open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                replaced += 1
                print('  ✔ تحديث:', os.path.relpath(path, ROOT))

    print('-' * 55)
    print(f'✅ تم تحديث {replaced} ملف. الموقع مربوط بالكامل وجاهز للرفع!')
    print('   الخطوة التالية: ارفع الملفات إلى GitHub ثم اطلب الفهرسة من Search Console.')

if __name__ == '__main__':
    main()
