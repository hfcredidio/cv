import jinja2
import json


with open('cv.json') as fcv:
    cvdata = json.load(fcv)

for c in cvdata['publications']:
    c['authors'] = ', '.join(c['authors'])

c = cvdata['skills']['other_programming']
cvdata['skills']['other_programming'] = ', '.join(c)


env = jinja2.Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'])
env.loader = jinja2.FileSystemLoader('.')
template = env.get_template('template.html')
render = template.render(cv=cvdata)

with open('cv.html', 'w') as frender:
    print(render, file=frender)
