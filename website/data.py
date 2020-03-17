import os
import datetime
from idGenerator import idGenerator

def getPosts():
    # Getting relative path 
    if (os.name == 'nt'):
        path = os.path.relpath('static\\data\\posts.dat', os.path.dirname(__file__))
    elif (os.name == 'posix'):
        path = os.path.relpath('static/data/posts.dat', os.path.dirname(__file__))

    database = open(path, 'r')
    posts = []

    database.readline() #Ignoring the first line of the file
    for line in database:
        if (line.lstrip().rstrip() != '-'):
            currentLine = line.lstrip().rstrip().split('|')
            if ('#' in currentLine[3]):
                currentLine[3] = currentLine[3].replace("#", "\n")

            post = {'author' : currentLine[0], 'date' : currentLine[1],
            'title' : currentLine[2], 'content' : currentLine[3]}

            posts.append(post) #Appending each individual post to a list of posts
    posts.reverse()
    database.close()
    return posts

def createPost(author, title, content):
    date = datetime.date.today()
    date = date.strftime("%d.%m.%Y")
    if (os.name == 'nt'):
        path = os.path.relpath('static\\data\\posts.dat', os.path.dirname(__file__))
    elif (os.name == 'posix'):
        path = os.path.relpath('static/data/posts.dat', os.path.dirname(__file__))

    database = open(path, 'a')

    #Replacing all linebreaks with a '#'. Replacing them back to linebreaks when printing posts out
    content = content.replace("\n", "#").replace('\r','')
    
    database.write(f'{author}|{date}|{title}|{content}\n-\n')
    database.close()


def getUserData():
    if (os.name == 'nt'):
        path = os.path.relpath('static\\data\\userData.dat', os.path.dirname(__file__))
    elif (os.name == 'posix'):
        path = os.path.relpath('static/data/userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'r')
    userdata.readline()
    users = {}
    for line in userdata:
        currentLine = line.rstrip().lstrip().split(',')
        users[currentLine[0]] = {'password' : currentLine[1], 'id' : currentLine[2]}
    return users


def addNewUser(username, password):
    if (os.name == 'nt'):
        path = os.path.relpath('static\\data\\userData.dat', os.path.dirname(__file__))
    elif (os.name == 'posix'):
        path = os.path.relpath('static/data/userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'a')
    userID = idGenerator()
    userdata.write(f'{username},{password},{userID}\n')
    userdata.close()

    

