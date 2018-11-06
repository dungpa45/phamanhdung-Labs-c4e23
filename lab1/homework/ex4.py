from pymongo import MongoClient
from collections import Counter
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1 ket noi db
client = MongoClient(uri)

#2 lay ra db mac dinh
db = client.get_database()

#3 lay ra collection
customers = db["customers"]

# read data
customers_list = customers.find()

# 1 Prepare data

dem = Counter(c['ref'] for c in customers_list)

machine_counts = [dem['events'],dem['ads'], dem['wom'], dem['event']]
machine_name = [*dem.keys()]

pyplot.pie(machine_counts, labels=machine_name,
           autopct="%.3f%%", shadow=True, explode=[0, 0.05, 0.1,0])
pyplot.title("Percentage of each reference")
pyplot.axis("equal")
#4 Show
pyplot.show()




client.close()
