content = '''
Cua quy
Van ban cua toi
'''

# with open("content.txt","w") as f:
#     f.write(content)

with open("content.txt", "r") as f:
    c = f.read()
    print(c)


# #1 open file
# f = open("content.txt", "w") # write

# #2 write file
# f.write(content)
# #3 close file
# f.close()
