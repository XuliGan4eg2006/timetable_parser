import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
print("Initing db.....")

print(str(r.get("ИСП9-321БП")))
