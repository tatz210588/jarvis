# from docx import Document


# document = Document()
# document.add_heading("Hello Tatz", 1) # 0= title, 1=heading 1 format
# p=document.add_paragraph("Heykvhb vkvhbj vhkvhv khjkhg")
# p.add_run("hell ya").bold = True
# p.add_run(" and more hell ya")
# p.add_run(" no no")

# document.add_paragraph("This is one",style="List Bullet")
# document.add_paragraph("This is two",style="List Bullet")

# document.save("test.docx")

import re

def split_between_keywords(text, keyword1, keyword2):
    pattern = re.compile(f'{re.escape(" about ")}(.*?){re.escape(" at ")}', re.DOTALL)
    matches = pattern.findall(text)
    return matches

# text = "Please set a reminder about drinking water at 1305"
# print(split_between_keywords(text, " about ", " at "))
# print(text.split('at ')[1:])

#query = "Jarvis can you set a reminder for drinking water in 2 minutes from now"
#query = "Jarvis can you set me a reminder for drinking water at 9:00 p.m."
query = "Jarvis set an alarm for 7:55 p.m."

import datetime

# now = datetime.datetime.now()
# five_pm = datetime.datetime(now.year, now.month, now.day, 17, 0)  # 17:00 is 5 PM
# difference = five_pm - now
# seconds = difference.total_seconds()

# print(seconds)

# text = split_between_keywords(query, " about ", " at ") #drinking water
# print(text)
# time = query.split('at ')[1:] #5 pm
# print(time)
# hour = int(time[0].split(':')[0]) + 12
# print(hour)
# minute = int(time[0].split(':')[1][:2])
# print(minute)
# amorpm = query[-4:]
# print(amorpm)
# now = datetime.datetime.now()
# reminderTime = datetime.datetime(now.year, now.month, now.day, hour, minute)  # 17:00 is 5 PM
#                 #         
# print( round((reminderTime - now).total_seconds()/60))

# reminder_detail = query.split("set a reminder for")[1].strip()

# # Naive way of getting minutes, improve this based on your requirement.
# minutes_match = re.search(r'in (\d+) minutes', reminder_detail)
# minutes_from_now = int(minutes_match.group(1)) if minutes_match else 0


# reminder_text = reminder_detail.split(" in")[0].strip() if minutes_match else reminder_detail

# print(reminder_text)
# print(minutes_from_now)

#set_reminder(reminder_text, minutes_from_now)

#say(f"Reminder set for: {reminder_text}")

match = re.search(r"set an alarm for (\d+):(\d+)", query.lower())
if match:
    hour, minute = map(int, match.groups())
    print(hour)
    print(minute)
