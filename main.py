import sqlite3
import requests
import json

MIN_CHOICE = 1
MAX_CHOICE = 5
LIKE = 1
DISLIKE = 2
SHOW_LIKES = 3
SHOW_DISLIKES = 4
EXIT = 5

def main():
    url = 'https://icanhazdadjoke.com/'
    create()
    choice = 0 
    while choice != EXIT:
        print('---- ---- ----')
        joke = get(url)
        print(joke)
        print('---- ---- ----')
        display_menu()
        choice = get_menu_choice()
        
        if choice == LIKE:
            insert(joke,like='Yes',dislike='No')
        elif choice == DISLIKE:
            insert(joke,like='No', dislike='Yes')
        elif choice == SHOW_LIKES:
            n = 'Yes'
            print('Jokes that are good for you!!!! (u dont have a good taste)')
            show(n)
        elif choice == SHOW_DISLIKES:
            m = 'No'
            print('Jokes are not good for you UP HERE!!!!')
            show(m)
        
        
def display_menu():
    print('Dads jokes are here!!!')
    print('1 - Do you like this Joke?')
    print('2 - Do you dislike this Joke?')
    print('3 - Do you want to see liked jokes?')
    print('4 - Do you like to see unliked Jokes?')
    print('5 - Exit')

def get_menu_choice():
    choice = int(input('Enter your choice: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Posiible variants are between {MIN_CHOICE} and {MAX_CHOICE}')
        choice = int(input('Enter again your choice: '))
    return choice

def requestURL(baseurl, d={}):
    req = requests.Request(method='GET', url=baseurl,params=d)
    prepped = req.prepare()
    return prepped.url

def get(baseurl):
    if isinstance(baseurl,str):
        page = requestURL(baseurl)
        response = requests.get(page, headers={'Accept': 'text/plain'})
    
    
    if response.status_code == 200:
        joke = response.text
        return joke

# SQL DISTRICT



def create():
    try:
        con = sqlite3.connect('jokes.db')
        cur = con.cursor()
        cur.execute('drop table if exists Jokes')
        cur.execute(
            '''create table if not exists Jokes (id integer primary key, joke text, like text, dislike text)'''
        )
        con.commit()
        con.close()
    except sqlite3.Error as err:
        print('Invalid creation', err)

def insert(joke, like='Yes',dislike='No'):
    try:
        con = sqlite3.connect('jokes.db')
        cur = con.cursor()
        cur.execute(
            '''insert into Jokes (joke, like, dislike) 
                values (?,?,?) ''',(joke,like,dislike)
        )
        con.commit()
    except sqlite3.Error as err:
        print('Invalid insert', err)
    

def show(like):
    try:
        con = sqlite3.connect('jokes.db')
        cur = con.cursor()
        cur.execute(
            '''SELECT joke FROM Jokes WHERE "like" = ?''', (like,)
        )
        result = cur.fetchall()
        for row in result:
            print(row[0])
            print('--- --- --- --- --- ---')
        con.close() 
    except sqlite3.Error as err:
        print('Invalid selection', err)













main()