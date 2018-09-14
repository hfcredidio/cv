import os
import json

from data import decrypt
from jinja2 import Template


cvdata = decrypt('data.bin', os.getenv('CVKEY'))

for c in cvdata['publications']:
    c['authors'] = ', '.join(c['authors'])

template = Template(open('template.html').read())
render = template.render(cv=cvdata)

with open('cv.html', 'w') as frender:
    print(render, file=frender)
