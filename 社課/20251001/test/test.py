from ntust_courses import search_courses, search_all_courses, print_courses
import requests, json, time
from ntust_courses import core

# ⚠️ 小心修改
core.API_URL = "https://querycourse.xinshou.tw/querycourse/api/courses" # 目前非選課時間，自架浮動人數服務
#core.API_URL = "https://querycourse.ntust.edu.tw/querycourse/api/courses"

# ✅ 可以修改
courses = search_courses(course_no="PE112A032")
print_courses(courses)

# ✅ 可以修改
courses = search_courses(course_name="羽球")
print_courses(courses)

WEBHOOK_URL = "https://discord.com/api/webhooks/1422907372099211328/QFXNy46_KXkUf3FSrBC9oU3_un5ur1E5IMTvyE6vmLRUv5_YrMceTmNEdzqw-S9pSmvF"  # ← 換成你自己的 Webhook URL

resp = requests.post(WEBHOOK_URL, json={"content": "我啟動了！"}, timeout=10)
if resp.status_code != 204:
  print("發送失敗:", resp.status_code)
else:
  print("發送成功")

