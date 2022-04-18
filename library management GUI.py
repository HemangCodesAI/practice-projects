from logging import root
from textwrap import fill
import tkinter as tk
from tkinter import RIGHT, Y, Entry, Label, Scrollbar, filedialog,Text
import os

root = tk.Tk()
available_books =[ "Fundamentals of Wavelets ",  "Data Smart ",  "God Created the Integers ",  "Superfreakonomics ",  "Orientalism ",  "Nature of Statistical Learning Theory, The ",  "Integration of the Indian States ", "Drunkard's Walk, The", 'Image Processing & Mathematical Morphology', 'How to Think Like Sherlock Holmes', 'Data Scientists at Work', 'Slaughterhouse Five', 'Birth of a Theorem', 'Structure & Interpretation of Computer Programs', 'Age of Wrath, The', 'Trial, The', "Statistical Decision Theory'", 'Data Mining Handbook', 'New Machiavelli, The', 'Physics & Philosophy', 'Making Software', 'Analysis, Vol I', 'Machine Learning for Hackers', 'Signal and the Noise, The', 'Python for Data Analysis', 'Introduction to Algorithms', 'Beautiful and the Damned, The', 'Outsider, The', 'Complete Sherlock Holmes, The - Vol I', 'Complete Sherlock Holmes, The - Vol II', 'Wealth of Nations, The', 'Pillars of the Earth, The', 
        'Mein Kampf', 'Tao of Physics, The', "Surely You're Joking Mr Feynman", 'Farewell to Arms, A', 'Veteran, The', 'False Impressions', 'Last Lecture, The', 'Return of the Primitive', 'Jurassic Park', 'Russian Journal, A', 'Tales of Mystery and Imagination', 'Freakonomics', 'Hidden Connections, The', 'Story of Philosophy, The', 'Asami Asami', 'Journal of a Novel', 'Once There Was a War', 'Moon is Down, The', 'Brethren, The', 'In a Free State', 'Catch 22', 'Complete Mastermind, The', 'Dylan on Dylan', 'Soft Computing & Intelligent Systems', 'Textbook of Economic Theory', 'Econometric Analysis', 'Learning OpenCV', 'Data Structures Using C & C++', 'Computer Vision, A Modern Approach', 'Principles of Communication Systems', 'Let Us C', 'Amulet of Samarkand, The', 'Crime and Punishment', 'Angels & Demons', 'Argumentative Indian, The', 'Sea of Poppies', 'Idea of Justice, The', 'Raisin in the Sun, A', "All the President's Men", 'Prisoner of Birth, A', 'Scoop!', 'Ahe Manohar Tari', 'Last Mughal, The', 'Social Choice & Welfare, Vol 39 No. 1', 'Radiowaril Bhashane & Shrutika', 'Gun Gayin Awadi', 'Aghal Paghal', 'Maqta-e-Ghalib', 'Beyond Degrees', 'Manasa', 'India from Midnight to Milennium', "World's Greatest Trials, The", 'Great Indian Novel, The', 'O Jerusalem!', 'City of Joy, The', 'Freedom at Midnight', 'Winter of Our Discontent, The', 'On Education', 'Free Will', 'Bookless in Baghdad', 'Case of the Lame Canary, The', 'Theory of Everything, The', 'New Markets & Other Essays', 'Electric Universe', 'Hunchback of Notre Dame, The', 'Burning Bright', 'Age of Discontuinity, The', 'Doctor in the Nude','Identity & Violence', 'Beyond the Three Seas', "World's Greatest Short Stories, The", 'Talking Straight', "Maugham's Collected Short Stories, Vol 3", 'Phantom of Manhattan, The', 'Ashenden of The British Agent', 'Zen & The Art of Motorcycle Maintenance', 'Great War for Civilization, The', 'We the Living', 'Artist and the Mathematician, The', 'History of Western Philosophy', 'Selected Short Stories', 'Rationality & Freedom', 'Clash of Civilizations and Remaking of the World Order', 'Uncommon Wisdom', 'One', 'Karl Marx Biography', 'To Sir With Love', 'Half A Life', 'Discovery of India, The', 'Apulki', 'Unpopular Essays', 'Deceiver, The', 'Veil: Secret Wars of the CIA', 'Char Shabda', 'Rosy is My Relative', 'Moon and Sixpence, The', 'Political Philosophers', 'Short History of the World, A', 'Trembling of a Leaf, The', 'Doctor on the Brain', 'Simpsons & Their Mathematical Secrets','From Beirut to Jerusalem', 'Code Book, The', 'Age of the Warrior, The', 'Final Crisis', 'Killing Joke, The', 'Flashpoint', 'Batman Earth One', 'Crisis on Infinite Earths', 'Numbers Behind Numb3rs, The', 'Superman Earth One - 1', 'Superman Earth One - 2', 'Justice League: Throne of Atlantis', "Justice League: The Villain's Journey", 'Death of Superman, The', 'History of the DC Universe', 'Batman: The Long Halloween', 'Life in Letters, A', 'Information, The', 'Journal of Economics, vol 106 No 3', 'Elements of Information Theory', 'Power Electronics - Rashid', 'Power Electronics - Mohan', 'Neural Networks', 'Grapes of Wrath, The', 'Vyakti ani Valli', 'Statistical Learning Theory', 'Empire of the Mughal - The Tainted Throne', 'Empire of the Mughal - Brothers at War', 'Empire of the Mughal - Ruler of the World', "Empire of the Mughal - The Serpent's Tooth", 'Empire of the Mughal - Raiders from the North', 'Mossad', 'Jim Corbett Omnibus', '20000 Leagues Under the Sea', 'Batatyachi Chal', 'Hafasavnuk', 'Urlasurla', 'Pointers in C', 'Cathedral and the Bazaar, The', 
        'Design with OpAmps', 'Think Complexity', "Devil's Advocate, The", 'Ayn Rand Answers', 'Philosophy: Who Needs It', "World's Great Thinkers, The", 'Data Analysis with Open Source Tools', "Broca's Brain", 'Men of Mathematics', 'Oxford book of Modern Science Writing', 'Justice, Judiciary and Democracy', 'Arthashastra, The', 'We the People', 'We the Nation', 'Courtroom Genius, The', 'Dongri to Dubai', 'History of England, Foundation', 'City of Djinns', "India's Legal System", 'More Tears to Cry', 'Ropemaker, The', 'Angels & Demons', 'Judge, The', 'Attorney, The', 'Prince, The', 'Eyeless in Gaza', 'Tales of Beedle the Bard', 'Girl with the Dragon Tattoo', "Girl who kicked the Hornet's Nest", 'Girl who played with Fire', 'Batman Handbook', "Murphy's Law", 'Structure and Randomness', 'Image Processing with MATLAB', 'Animal Farm', 'Idiot, The', 'Christmas Carol, A']
issued_books=[]
# scroll_bar = Scrollbar(root)
# scroll_bar.grid(fill=Y)
def search():
    
    for book in  available_books: 
        mylabel0 = tk.Label(root, text=available_books)
        mylabel0. grid() 
def borrowBook():
        if bookName in   available_books:
            myLabel1 = Label(root, text="You have been issued {bookName}. Please keep it safe and return it within 30 days")
            myLabel1. grid()
            available_books.remove(bookName)
            issued_books.append(bookName)
            
        elif bookName in issued_books:
            myLabel2 = Label(root, text="Sorry the book has already been issued by someone else")
            myLabel2. grid()
        else:
            myLabel3 = Label(root,text="In valid entry!!")
            myLabel3. grid()
def returnBook():
    if bookName in issued_books:
        available_books.append(bookName)
        issued_books.remove(bookName)
        myLabel4 = Label(root, text="Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        myLabel4. grid()
    else:
            myLabel5 = Label(root,text="In valid entry!!")
            myLabel5. grid()
def addBook():
    available_books.append(bookName)        
    myLabel4 = Label(root, text="Thanks for donating this book! Have a great day ahead!")
    myLabel4. grid()
bookName = Entry(root)
bookName.grid(row=0,column=0,columnspan=3)
request_book = tk. Button(root, text="Request Book", padx=10,
                      pady=5, fg="white", bg="red" ,command=borrowBook)
request_book.grid(row=2,column=0)
return_book = tk. Button(root, text="Return Book", padx=10,
                      pady=5, fg="white", bg="red",command=returnBook)
return_book.grid(row=2,column=1)
add_book = tk. Button(root, text="Add Book", padx=10,
                      pady=5, fg="white", bg="red",command=addBook)
add_book.grid(row=2,column=2)
search_book = tk. Button(root, text="Search Book", padx=10,
                      pady=5, fg="white", bg="red",command=search)
search_book.grid(row=2,column=3)

root.mainloop()


        
