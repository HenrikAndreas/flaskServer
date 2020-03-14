import os

def getPosts():
    # Getting relative path 
    path = os.path.relpath('data\\posts.dat', os.path.dirname(__file__))

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
    path = os.path.relpath('data\\posts.dat', os.path.dirname(__file__))
    database = open(path, 'a') 
    database.write(f'{author},{date},{title},{content}\n')
    database.close()

    

