from redis_updater import download_sheet, update_db, insert_groups

print("\nDownloading sheet...")
if download_sheet():
    print("Downloaded sheet")
else:
    print("Error downloading sheet")
    exit()

print("Inserting groups...")
insert_groups()
print("Groups inserted")

print("\nUpdating db...")
update_db()
print("Updated db")
