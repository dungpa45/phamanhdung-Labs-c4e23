from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1 ket noi db
client = MongoClient(uri)

#2 lay ra db mac dinh
db = client.get_database()

#3 lay ra collection
posts = db["posts"]

#4 create data
new_post = {
    "title": "Hôm nay tôi phởn",
    "author": "Phạm Anh Dũng",
    "content": "Sóng bắt đầu từ gió, gió bắt đầu từ đâu, em cũng không biết nữa, khi nào ta yêu nhau hey hey hey hey...",
}

#5 insert data
posts.insert_one(new_post)

#6 clode connection
client.close()
