import xml.etree.ElementTree as ET

# 假設回傳的XML資料存在response變數中
response = '<start_task_response status="202" status_text="OK, request submitted"><report_id>2115050d-3f3e-4b42-9956-257983f59979</report_id></start_task_response>'

# 將XML轉換為ElementTree物件
root = ET.fromstring(response)

# 取得report_id
report_id = root.find('report_id').text

print(report_id)

# <get_reports report_id="2115050d-3f3e-4b42-9956-257983f59979" format_id="5057e5cc-b825-11e4-9d0e-28d24461215b"/>
# <get_tasks task_id="9e0081b8-e093-4525-8327-1adcb00676b9"/>