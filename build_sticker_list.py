# -*- coding: utf-8 -*-
"""扫描 img/stickers 目录，生成 stickers-list.js，供 index.html 使用。新增贴纸后重新运行此脚本即可。"""
import os

STICKERS_DIR = os.path.join(os.path.dirname(__file__), 'img', 'stickers')
OUTPUT_JS = os.path.join(os.path.dirname(__file__), 'stickers-list.js')

def main():
    if not os.path.isdir(STICKERS_DIR):
        os.makedirs(STICKERS_DIR, exist_ok=True)
    names = []
    for f in sorted(os.listdir(STICKERS_DIR)):
        path = os.path.join(STICKERS_DIR, f)
        if os.path.isfile(path) and not f.startswith('.') and f != '说明.txt':
            names.append(f)
    # 写入 JS 数组，UTF-8
    with open(OUTPUT_JS, 'w', encoding='utf-8') as out:
        out.write('// 由 build_sticker_list.py 自动生成，请勿手改\n')
        out.write('var STICKER_FILES = ')
        out.write(repr(names))
        out.write(';\n')
    print('已生成 stickers-list.js，共 %d 个贴纸' % len(names))

if __name__ == '__main__':
    main()
