import os
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) == 1:
    raise NameError('No lint file specified')

if not os.path.isfile(sys.argv[1]):
    raise IOError('Invalid file specified')

RUNNER_WORKSPACE = os.environ['RUNNER_WORKSPACE']
REPO_NAME = os.environ['GITHUB_REPOSITORY'].split('/')[1]

checkstyle = ET.Element('checkstyle')
checkstyle.attrib['version'] = '8.0'

for issue in ET.parse(sys.argv[1]).getroot().iter('issue'):
    file = ET.SubElement(checkstyle, 'file')
    file.attrib['name'] = issue[0].attrib['file'].replace(f'{RUNNER_WORKSPACE}/{REPO_NAME}/', '')

    error = ET.SubElement(file, 'error')

    if 'line' in issue[0].attrib:
        error.attrib['line'] = issue[0].attrib['line']
    else:
        error.attrib['line'] = str(0)

    if 'column' in issue[0].attrib:
        error.attrib['column'] = issue[0].attrib['column']
    else:
        error.attrib['column'] = str(0)

    error.attrib['severity'] = 'error'

    issueId = issue.attrib['id']
    message = issue.attrib['message']
    error.attrib['message'] = f'{issueId}: {message}'

checkStyleFile = ET.ElementTree(checkstyle)
checkStyleFile.write('output_checkstyle.xml')
