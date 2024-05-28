from threading import Thread
from redis_updater import download_sheet, update_db

print("Starting MTUSI timetable programm complex")

print("\nDownloading sheet...")
if download_sheet():
    print("Done")
else:
    print("Error downloading sheet")
    exit()

print("\nUpdating db...")
update_db()
print("Done")
