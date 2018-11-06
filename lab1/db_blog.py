from pymongo import MongoClient

uri = "mongodb://admin:admin1@ds241530.mlab.com:41530/c4e23-blog"

#1 ket noi db
client = MongoClient(uri)

#2 lay ra db mac dinh
db = client.get_database()

#3 lay ra collection
posts = db["posts"] #lazy loading
movies = db["movies"]

#4 create data
new_post = {
    "title":"Hom nay toi buon",
    "content":"Toi van di code dao",
}
new_movie = {
    "title":"Vua di vua khoc",
    "rating":8.0,
}

#5 insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

#5 read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    
    print(p["title"])
    print(p["content"])
    print("==========")

#6 clode connection
client.close()