import time
import requests
import json
from ntust_courses import search_courses

# 1. 使用 tracked_list 儲存我追蹤的課程識別碼(course_no)字串
tracked_list = ["CH1004301"] # 請將此替換成你要追蹤的課程識別碼列表

# 2. 重新定義 WEBHOOK_URL 字串，再發送通知
WEBHOOK_URL = "https://discord.com/api/webhooks/1422907372099211328/QFXNy46_KXkUf3FSrBC9oU3_un5ur1E5IMTvyE6vmLRUv5_YrMceTmNEdzqw-S9pSmvF"  # ← 換成你自己的 Webhook URL

# 儲存上一次查詢的課程人數
last_student_counts = {}

while True:
    changed_courses = []
    for course_no in tracked_list:
        courses = search_courses(course_no=course_no)
        if courses:
            course = courses[0] # Assuming course_no is unique and returns a single course
            # print(course)
            # current_students = course.ChooseStudent
            # course_name = course.CourseName
            # restrict_students = course.Restrict2

            current_students = course["ChooseStudent"]
            course_name = course["CourseName"]
            restrict_students = course["Restrict2"]

            if course_no not in last_student_counts:
                # First time checking this course
                last_student_counts[course_no] = current_students
                print(f"開始追蹤課程：{course_name} ({course_no})，目前人數：{current_students}/{restrict_students}")
            elif last_student_counts[course_no] != current_students:
                # Enrollment changed
                print(f"課程 {course_name} ({course_no}) 人數變動：{last_student_counts[course_no]} -> {current_students}")
                changed_courses.append({
                    "CourseName": course_name,
                    "CourseNo": course_no,
                    "ChooseStudent": current_students,
                    "Restrict2": restrict_students
                })
                last_student_counts[course_no] = current_students

    # 3. 若同時有多筆資料，將他合併傳送，避免遇到 429
    if changed_courses:
        message_content = "課程人數變動通知：\n"
        for course_info in changed_courses:
            message_content += f"- {course_info['CourseName']} ({course_info['CourseNo']})：{course_info['ChooseStudent']}/{course_info['Restrict2']}\n"

        resp = requests.post(WEBHOOK_URL, json={"content": message_content}, timeout=10)
        if resp.status_code != 204:
            print("發送失敗:", resp.status_code)
        else:
            print("發送成功")

    # 5. API 輪詢週期為 5 秒
    time.sleep(5)