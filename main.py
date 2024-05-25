from threading import Thread
from config import *
from redis_updater import download_sheet, update_db
from notification_worker import start_notification_worker
from server import start_server

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

print("\nStarting REST API server...")
Thread(target=start_server).start()
print("Done")

print("\nStarting notification worker...")
Thread(target=start_notification_worker).start()
print("Done")