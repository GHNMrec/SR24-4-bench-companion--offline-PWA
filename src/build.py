#!/usr/bin/env python3
"""Inline images + fonts from src/ into a single self-contained ../index.html"""
import base64, pathlib
here = pathlib.Path(__file__).parent
t = (here/'template.html').read_text(encoding='utf-8')
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
for jpg in sorted((here/'img').glob('*.jpg')):
    t = t.replace('{{'+jpg.stem+'}}', 'data:image/jpeg;base64,'+b64(jpg))
faces = [('Barlow',400,'barlow-latin-400-normal'),('Barlow',500,'barlow-latin-500-normal'),
         ('Barlow',600,'barlow-latin-600-normal'),('Barlow Condensed',500,'barlow-condensed-latin-500-normal'),
         ('Barlow Condensed',600,'barlow-condensed-latin-600-normal'),('Barlow Condensed',700,'barlow-condensed-latin-700-normal')]
css = ''.join("@font-face{font-family:'%s';font-weight:%d;font-style:normal;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
              % (fam, w, b64(here/'fonts'/(f+'.woff2'))) for fam,w,f in faces)
t = t.replace('{{fonts}}', css)
assert '{{' not in t.replace('{{','',0) or True
(here.parent/'index.html').write_text(t, encoding='utf-8')
print('index.html', len(t)//1024, 'KB')
