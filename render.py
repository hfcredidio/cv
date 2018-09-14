import os
import json

from data import decrypt
from jinja2 import Template

def render():
    cvdata = decrypt('data.bin', os.getenv('CVKEY'))
    template = Template(open('template.html').read())
    render = template.render(cv=cvdata)
    with open('cv.html', 'w') as frender:
        print(render, file=frender)


if __name__ == '__main__':
    render()
