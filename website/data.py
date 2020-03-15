import os

def getPosts():
    # Getting relative path 
    path = os.path.relpath('static\\data\\posts.dat', os.path.dirname(__file__))

    database = open(path, 'r')
    posts = []

    database.readline() #Ignoring the first line of the file
    for line in database:
        currentLine = line.lstrip().rstrip().split(',')
        post = {'author' : currentLine[0], 'date' : currentLine[1],
        'title' : currentLine[2], 'content' : currentLine[3]}

        posts.append(post) #Appending each individual post to a list of posts
    database.close()
    return posts

def createPost(author, date, title, content):
    path = os.path.relpath('static\\data\\posts.dat', os.path.dirname(__file__))
    database = open(path, 'a') 
    database.write(f'{author},{date},{title},{content}\n')
    database.close()


def getUserData():
    path = os.path.relpath('static\\data\\userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'r')
    userdata.readline()
    users = {}
    for line in userdata:
        currentLine = line.rstrip().lstrip().split(',')
        users[currentLine[0]] = {'password' : currentLine[1], 'id' : currentLine[2]}
    return users


def addNewUser(username, password):
    path = os.path.relpath('static\\data\\userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'a')
    userID = idGenerator()
    userdata.write(f'{username},{password},{userID}\n')
    userdata.close()


    

