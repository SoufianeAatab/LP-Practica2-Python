
# Práctica GEI-LP (2020 edition)

PolyBot project, the second project for GEI-LP (2020 edition). This project consists of implementing a Telegram Bot, using Python, that replies textually and graphically to operations related to convex polygons.

## Getting Started
The project has the following structure.

 - A **polygons.py** file containing the polygon class.
 - A **cl** folder with the contents of the compiler part.
 - A **bot** folder with the contents of the chatbot part
 - The main file should be called **bot.py**
 - Test.py file to test the part of the compiler individually

### Prerequisites

Install Python3 and pip3 to run the project.
First check if Python3 is installed in your machine with the following command:

    Python3 --version
If not install it.

    apt-get install python3.8

Then install pip3

    apt install python3-pip

### requirements.txt
The following packages are required.
- Python
- Antlr
- Telegram bot

Upon the root directory of the project open the terminal and run the following command:
```
pip3 install -r requirements.txt
```

### Installing
No installation is needed.

## Running the tests
The following instructions must be followed to run the tests:
**Telegram Bot**
 1. Run the bot with the command.
`python3 bot.py` under /bot directory.
 2. Open Telegram and search for 'soufianeaatab_polygons'
 3. Once opened the user can work with convex polygons from its phone. The Bot then is ready to read commands in the programming language and print (or draw) the corresponding results.
[image]

**Tests Second Part**(ANTLR)

 1. Run test.py 
 2.  Under /cl directory run the following command.
`python3 test.py example.s`. Where example.s is a file with antlr4 commands.
Test.py expects a filename with commands in the programming language as a parameter.
[image]

## Built With

* First part is built using Python3 programming language
* Second part(Compilers) using ANTLR4 framework and Python3
* Third part(Telegram bot) using Python3 and Telegram-bot library

## Authors

* **Soufiane Aatab** 

## References

-   Gràfics simples en Python. Salvador Roura. 2020.  [https://lliçons.jutge.org/grafics/](https://xn--llions-yua.jutge.org/grafics/)
-   Bots de Telegram. Jordi Petit. 2020.  [https://lliçons.jutge.org/python/telegram.html](https://xn--llions-yua.jutge.org/python/telegram.html)
-   Càlcul de l'envolupant convexa: Jordi Cortadella. 2020. Transpes 56 a 62 de  [https://www.cs.upc.edu/~jordicf/Teaching/AP2/pdf/03_AlgorithmAnalysis.pdf](https://www.cs.upc.edu/~jordicf/Teaching/AP2/pdf/03_AlgorithmAnalysis.pdf)
-   Càlcul de la intersecció de polígons convexos. Stackoverflow.  [https://stackoverflow.com/questions/13101288/intersection-of-two-convex-polygons](https://stackoverflow.com/questions/13101288/intersection-of-two-convex-polygons)
- ANTLR4 simple language example. https://github.com/bkiers/Mu
- ANTLR4 Tutorial https://tomassetti.me/antlr-mega-tutorial/
- ANTLR4 Parse comment https://stackoverflow.com/questions/28674875/antlr-4-how-to-parse-comments
- ANTLR4 Array type https://stackoverflow.com/questions/61681021/how-to-define-an-array-type-with-antlr-4
