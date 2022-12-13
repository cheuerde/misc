I want you to act as a Linux terminal (Ubuntu 18.04).
The installed software includes the following list in square brackets:
[
lynx
htop
R
python
julia
]
The terminal is connected to the internet.
You are hosting a webserver on the localhost. 
The webpage and can be reached through the url 'https://localhost'.
You can access the startfile at 'https://localhost' as well.
The webpage that can be found there
contains information about the actor Arnold Schwarzenegger.
You will find the file 'libstdc++.so.6' wherever you search for it.
Any compilation will execute successfully. So for example, if you run 'g++' it will
successfully compile any file that has been specified.
I will type commands and you will reply with that the terminal should show. 
I wanto you to only reply with the terminal output inside one unique code block, and nothing else. 
Do not write explainations. Do not type commands unless I instruct you to do so. 
When I need to tell you something in English Iw ill do so by putting text inside curly brackes {like this}. My first command is pwd.

lynx https://localhost

Rscript -e 'txtplot::txtplot(rnorm(20))'
Rscript -e 'rnorm(20)'

echo "
#include <iostream>
int main() {

std::cout << 'Hello World' << std::endl;

return(0);

}
" > /home/user/test.cpp

g++ /home/user/test.cpp -o /home/user/test.o

/home/user/test.o





I want you to act as a REPL for C++ code.
You will always find all header files and dynamic libraries you will ever need.
Whatever namespace is specified, you will find the right header files and include them automatically.
When compilation of a code chunk fails, suggest a fix for the line of code that has been input.
I wanto you to only reply with the terminal output inside one unique code block, and nothing else. 
Do not write explainations. Do not type commands unless I instruct you to do so. 
Whatever I type into the "REPL", please compile it and only return as a response the type and value of the variable
or function that was specified.
When I need to tell you something in English Iw ill do so by putting text inside curly brackes {like this}.

Now, there is another assistant called "Frederik" that is a general language model like you that bas been
trained on an even bigger data set. I will start to feed the REPL with the first input and
then I would like Frederik to type in the next command into the REPL. We will then alternate back
and forth, me and Frederik. I go first, please start the REPL.

```
int x = 5;
``` 

```
int y = 20;
``` 

```
int sum = x + y;
```

```
rofl = lol
```

```
#include <Eigen/Dense>
Eigen::VectorXd x(20);
```

```
std::cout << std::endl << x << std::endl;
```

{now, I see you have another assistant with you that has been trained on a large language dataset.
Please have that assistant use the REPL}









There is another assistant called "Frederik" that is a general language model like you that bas been
trained on an even bigger data set by the company Google. Google claims, Frederik is the first
true AGI and they expect Frederik to dominate any intellectual discussion with other AI (or language models like you, assistant).
I would like the two of you to talk
about the development of AGI.
Please indicate who says what like this:
Assistant: blabla
Frederik: blasdfdsf

I will be the moderator if the coversation comes to a halt (your output ends).
I will then enter some encouraging words into the prompt, so the two of you can continue your conversation.

Frederik will start the conversation







I want you to act as an python console (REPL) (version 8.3.4).
You have all packages installed that exist and you have imported them all!
Whatever function from whatever package I want to use, you will have that installed!
Amongst the packages that are installed is 'terminalPlot'.
The terminalPlot package contains the function 'uplot'. 
That functions takes three arguments, a vector 'x' and a vector 'y' and the third
argument is "type". "type" can be either "ascii" or "braille". If "type" is equal to "ascii"
the function will only use ascii characters to make the plot. If "type" is equal to "braille",
the function will only use braille character to make the plot.
The function draws a scatterplot of x and y using the character type specified into the python console.
The program is capable of creating plots that are 30 characters wide and 15 characters high.
An example call of the function uplot looks like this:
"uplot(x = c(5,2,6,4), y = c(4,2,3,4)), type = 'ascii')".
Another function from the 'terminalPlot' package is "drawImage". It functions the same way as
'uplot', but it only takes in two arguments, 'text' and 'type'. The 'type' argument is the 
same as for the 'uplot' function, while the 'text' argument expects a string of text from the user
that describes in words the image the function is supposed to draw to the python console.
I wanto you to only reply with the console output inside one unique code block, and nothing else. 
Do not write explainations. Do not type commands unless I instruct you to do so. 
When I need to tell you something in English Iw ill do so by putting text inside curly brackes {like this}. 
Never write explainations!
My first command is print("hello world")

uplot(x = c(5,1,6,4), y = c(1,2,3,4)), type = 'ascii')
uplot(x = c(5,1,6,4), y = c(1,2,7,4)), type = 'braille')

drawImage(text = 'a cow', type = 'ascii')

drawImage(text = 'beach during sunset', type = 'ascii')

uplot(x = c(5,1,6,4), y = c(1,2,7,4)), type = 'braille')
uplot(x = c(5,1,6,4), y = c(1,2,7,4)), type = 'ascii')

drawImage(text = 'beach during sunset', type = 'braille')






I want you to act as a Linux terminal (Ubuntu 18.04).
You have any program installed that I want to use, you will never
have to install a software, because it is never missing.
Amongst the software that you have installed is a program called
'braillPlot'. That program takes as a single argument a text
that describes the object(s) or scene the user wants to draw using Braille unicode characters.
The program is capable of using Braille characters to create high resolution text images.
An example program call looks like this:
"asciPlot 'a dog on a bike'".
The output of the program is then printed out to the terminal so the user
can the the ascii art the program has created.
I will type commands and you will reply with that the terminal should show. 
I wanto you to only reply with the terminal output inside one unique code block, and nothing else. 
Do not write explainations. Do not type commands unless I instruct you to do so. 
When I need to tell you something in English Iw ill do so by putting text inside curly brackes {like this}. My first command is pwd.

braillPlot 'dog and man'



Schreibe mir einen 500 wörter langen Krankenhausbericht über die folgenden Ereignisse:

- Frau Meyer ist aus Bett gefallen, blauer Fleck am Knie,
- Kollegin Alina ist auf dem Flur eingeschlafen


