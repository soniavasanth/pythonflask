#f = open("sonafile.txt", "x")

# f = open("sonafile.txt", "w")
# f.write("hi the place where i live is nc")
# f.write("\n""the county that i live is wake county")
# f.close()

# f = open("sonafile.txt", "r")
# print(f.read())
# f.close()

# import os
# if os.path.exists("sfile.txt"):
#   os.remove("sfile.txt")
# else:
#   print("The file does not exist")

# USING CONTENT MANAGER

with open("sonafile.txt","r") as f:
     content=f.read()
     print(content)



# with open("sonafile.txt","r") as f:
#     content=f.readline()
#     print(content)
    
    

