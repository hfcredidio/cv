import os
import jinja2
import json

from data import decrypt


cvdata = decrypt('data.bin', os.getenv('CVKEY'))

for c in cvdata['publications']:
    c['authors'] = ', '.join(c['authors'])

env = jinja2.Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'])
env.loader = jinja2.FileSystemLoader('.')
template = env.get_template('template.html')
render = template.render(cv=cvdata)

with open('cv.html', 'w') as frender:
    print(render, file=frender)
