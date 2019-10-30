from django.shortcuts import render

posts = [
    {
        'title': "Aidan's Computer Science II Assignments Blog"
    },
    {
        'title': 'Assingment 1: Scanner Input and Reversing Strings',
        'content': ' This was our first assignment of the class and as such was quite simple. We had one class that, using the scanner import, took in an input that we distance. Next, we took in another input designated as the time, and finally outputted the velocity of an object that had traveled the respective distance in the respective time. Our second class, reverse, simply took in a number (as a string), reversed it, and finally outputted it to the user.',
    },
    {
        'title': "Assignment 2: Guessing Game ",
        'content': 'This assignment pushed us to learn a lot of new concepts and incorporate it into an interactive game. We were given a file containing roughly 2,500 words, and the objective of the player was to guess one of those words. After the program has chosen one of the 2,500 words at random, the player would type a word as input. If they were correct, the program would output correct. If not, the program would output the amount of letters that were in their guess that are also found in the answer. If the player gave up, they could type clear to stop the game and reveal the answer. Of course, I also programmed in a cheat code of xxxxx and the program would reveal the answer, though it would print out that the player had cheated at the end of the game.',
    },
    {
        'title': "Assignment 3: Linked Lists ",
        'content': 'In this assignment, we implemented linked lists and various methods associated with them. Specifically, we implemented the following methods: getFirst(), getLast(), add(), addAfter(), set(), lastIndex(), clone(), removeAll(), equals(), and split(). It’s important to note that most of these methods took in inputs specific to their function. After implementing all of these methods per our professor’s directions, we tested all of them using provided data.',
    },
    {
        'title': "Assignment 4: Queues and Stacks ",
        'content': 'In this assignment, we were given a data set of music notes that when played would play a familiar song such as Jingle Bells. Our task was to alter these data as a queue or stack and manually implement methods such as enqueue(), dequeue(), isEmpty(), duration(), timeRepeat(), size(), makeString(), tempoChange(), appendMelody(), and reverseMelody(). This assignment proved especially challenging as we had many more classes such as node and note and we had to interact with many different aspects of the same piece of data such as its pitch and duration.',
    },
    {
        'title': "Assignment 5: Huffman Coding and Trees ",
        'content': 'The objective of this assignment was to write a program that encoded a message via Huffman Coding and that was still capable of recovering the original message. In order to do this, we were not allowed to use any java tree but had to create our own tree and node classes and manually implement their various methods. This assignment made sure we understood the previous data structures and concepts covered in class. The program ended by outputting the encoded message and a frequency table.',
    },
    {
        'title': "Assignment 6: Data Structures ",
        'content': 'In our final assignment, we were tasked to use various data structures to calculate the frequency of which the words contained in three different text files appear. These files were of very different sizes, and each word would be stored in a data structure along with its frequency counter. The program would ask the user for a word that they wanted to search for or place into the data structures, and output whether that word was found in the files and the amount of time it took to perform all 6 actions. For this assignment, I chose to compare stacks and queues.',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
