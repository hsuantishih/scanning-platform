str = '<create_target_response status="201" status_text="OK, resource created" id="c0a07fd2-93cb-477f-b810-fd3cdbe43e0f"/>'

import xml.etree.ElementTree as ET

root = ET.fromstring(str)
id = root.get('id')
print(id)