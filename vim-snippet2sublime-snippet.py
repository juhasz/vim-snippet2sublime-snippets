#!/usr/bin/python
# Filename: cat.py

import sys
import re

def convert(filename):
  snippets = file(filename)
  snippet = ''
  name = ''
  while True:
    line = snippets.readline()

    ''' If a new snippet starts, write the previous one if any. '''
    if line.startswith('snippet '):
      if name:
        to_xml(name, snippet)
      name = line.split(),
      name = name[0][1]
      snippet = ''

    elif not line.startswith('#'):
      ''' Remove the first tab characters for right indention. '''
      if line.startswith('\t'):
        line = line[1:]
      snippet += line

    if len(line) == 0:
      break
  snippets.close()

def to_xml(name, snippet):
  xml =  '<snippet>\n'
  xml += '  <tabTrigger>' + name + '</tabTrigger>\n'
  xml += '  <content><![CDATA[' + snippet + ']]></content>\n'
  xml += '</snippet>'

  ''' Escape the right '$' characters. '''
  xml = re.sub('(\$[a-zA-Z0-9_])', '\\\\\\1', xml)

  ''' Pattern for project name. '''
  project_name = '${TM_FILENAME/([^.]*)\..*$/$1/}'
  xml = xml.replace('`Filename()`', project_name)

  f = file(name + '.sublime-snippet', 'w')
  f.write(xml)
  f.close()

# Script starts from here
if len(sys.argv) < 2:
  print 'No action specified.'
  sys.exit()

for filename in sys.argv[1:]:
  convert(filename)
