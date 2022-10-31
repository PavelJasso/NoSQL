import redis
r = redis.Redis()

r.mset({"Katedra Informatiky": "Jiří Škvor", "Katedra Fyzika": "Eva Hejnová"})
print(r.get("Katedra Fyzika"))

