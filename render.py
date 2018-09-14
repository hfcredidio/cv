import os
import json

from data import decrypt
from jinja2 import Template

def render():
    key = os.getenv('CVKEY')
    if not key:
        raise ValueError('Environment variable CVKEY not set. Note to self: check LastPass')
    cvdata = decrypt('data.bin', key)
    template = Template(open('template.html').read())
    render = template.render(cv=cvdata)
    with open('cv.html', 'w') as frender:
        print(render, file=frender)


if __name__ == '__main__':
    render()
