# The steam engine of our time

Large Language Models (LLM) and their equivalents for visual and audio content
are powering a new generation of automation tools for cognitive tasks of all kind.
What those LLMs do: The input is text (a word, a sentence, a whole article)
and the model will predict how the text is going to continue. That sounds simple
enough, but if a model like that has been trained on a big enough data-set
in conjunction with some clever engineering around input and output, those models show astonoishing
behaviour. 

Domain experts are fine tuning those models with AI companies to specialize them for 
a wide array of cognitive tasks: [software development](https://github.com/features/copilot),
[law firms](https://jobs.ashbyhq.com/harvey/6dd09981-8d4a-419a-a294-1c93947a11c1), [creative writing](https://dl.acm.org/doi/fullHtml/10.1145/3490099.3511105), 
[scientific writing](https://galactica.org/explore/), etc.

A user friendly program that lets you interface directly with the biggest LLM out there (GPT-3)
is [chatGPT](https://openai.com/blog/chatgpt/). Try it out to get a feel for what this technology
can do. The potential is revolutionary. But it also raises a lot of security and ethical questions,
especially because true human like artificial intelligense is within reach

https://twitter.com/ScienceMagazine/status/1600929470411640863?s=20&t=aX4BW9FW4lPC5x5ES1wwZQ

# Not Artificial Intelligence, yet

A couple of weeks ago, OpenAI released a chatbot called chatGPT[link].
Doesnt sound very interessting at first, but it exposes breakthroughs
in aritifical intelligence research to the public that have been made 
over the last 3 years.
The main engine behind the technology are Large Language Models (LLMs), GPT-3 
being one of the biggest ones right now. Those models are trained
on massive amounts of digital text in any language and any context.
What those models do: The input is text (a word, a sentence, a whole article)
and the model will predict how the text is going to continue. That sounds simple
enough, but if a model like that has been trained on a big enough data-set
in conjunction with some clever prompt-priming, those models show astonoishing
behaviour. 

This is a technological revolution that is happening at this very moment
and it is going to affect every aspect of our life.
We don't have true artificial, human like, intelligence yet. But we are getting
really close.

Some immediate implications:

Software Development

- LLMs will likely generate the bulk of software code ([assist](https://github.com/features/copilot), prototype, debug, whole development loop)
- LLMs will generate machine code without executable programs based on general language input alone (no programming lanugages)
- Applications will run in the ML models without any machine code at all. Model acts as the [computer](https://www.engraved.blog/building-a-virtual-machine-inside/)

Creative Writing, Audio, Video and Image creation

- Diffusion Models(https://www.unite.ai/nvidias-ediffi-diffusion-model-allows-painting-with-words-and-more/) generate visual content at scale
- Artists will have to understand how to "prime the prompt" of those models to achieve desired result
- Creative and high quality content becomes commodity
- LLMs for science (https://galactica.org/explore/)

Robotics

- Human language as the main user interface for robots
- Allows the AI to step out of the digital space into real world


# Some notes on AI

A couple of weeks ago, [chatGPT](https://chat.openai.com/) was released. It showed up on my twitter feed
and I saw some interessting responses from that chat bot.
I tried it out, mostly curious about it's abilities to generate, modify and debug code (C++ and R).

I can't remember which exact response blew me away, but it was an answer to a request like this

```sh
Write me a C++ function that does the following:
Based on a feature matrix for the regressors and a response vector for the dependant variable, return
the least squares estimator for the regression coefficients
```

The response was:

```cpp
#include <Eigen/Dense>
#include <iostream>

using namespace Eigen;

//Least squares estimator function
VectorXd leastSquaresEstimator(MatrixXd featureMatrix, VectorXd responseVector){
	VectorXd coefficients;
	//Calculate the coefficients using the formula coefficients = (X^T * X)^-1 * X^T * y
	coefficients = (featureMatrix.transpose() * featureMatrix).inverse() * featureMatrix.transpose() * responseVector;
	return coefficients;
}

//Test code
int main(){

	MatrixXd featureMatrix(2,2);
	featureMatrix << 1, 2, 3, 4;

	VectorXd responseVector(2);
	responseVector << 5, 6;

	VectorXd coefficients = leastSquaresEstimator(featureMatrix, responseVector);

	std::cout << coefficients << std::endl;

	return 0;
}
```

It took me a while to fully understand the implications of this short interaction with that chat bot.
It was merely enough to explain what the input and output of the function was supposed to be, and the bot generated
a valid least squares routine without me even having to explain the operations necessary to arrive at the solution.
That means the bot was able to understand the request from the short context I was giving (least squares estimator).

Another example that was a soltuion was less obvious:

```sh
I have SNP genotype data on a parent offspring trio. 
How can I check whether the pedigree is valid, given the genotypes of the
trio? In R please
```

```sh
I have 3 sequences of characters. Every character can only be "A" or "B".
The first two sequences are complete. The third sequence has missing values.
Please fill in the missing values and incorporate the information you have seen
in the first two sequences and note that the imputed character at any position
must be present in of the the first two sequences.

Here are the sequences (missing values are indivated by an underscore ("_")):
1. AAABBAABA
2. AABBABABA
3. A_BB_BAAB
```

# How does this work?

The main engine behind chatGPT is the general language model GPT-3 that was trained using a [transformer neural net](https://arxiv.org/pdf/1706.03762.pdf).
In essense, these language models are trained to predict the next sequence of words (or tokens) given the input text (prompt input, for example).
That means the generated continuation of the text from the model, heavily depends on the context given
by the input. 

# Immediate implications and use cases

 - Given the coding abilities of chatGPT
  - Massive productivity boost using chatGPT for "paired programming"
  - Covers the entire development loop: Problem statement, solution brainstorming, implementation, debugging, compilation
  - First commercial product, is a smart auto-complete called [github copilot](https://github.com/features/copilot)

 - 
