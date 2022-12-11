# Some notes on AI

A couple of weeks ago, [chatGPT]() was released. It showed up on my twitter feed
and I saw some interessting responsed from that chat bot.
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
	featureMatrix << 1, 2, 
					 3, 4;

	VectorXd responseVector(2);
	responseVector << 5,
					  6;

	VectorXd coefficients = leastSquaresEstimator(featureMatrix, responseVector);

	std::cout << coefficients << std::endl;

	return 0;
}
```

It took me a while to fully understand the implications of this short interaction with that chat bot.
It was merely enough to explain what the input and output of the function was supposed to be, and the bot generated
a valid least squares routine without me even having to explain the operations necessary to arrive at the solution.
That means the bot was able to understand the request from the short context I was giving (least squares estimator).

Another example that where a soltuion was less obvious:

```sh
I have SNP genotype data on a parent offspring trio. How can I check for the validty of the pedigree
given the genotypes of the trio? In C++ please
```
