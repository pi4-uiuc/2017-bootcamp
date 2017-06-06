#   Lesson 9:  Hidden Markov modeling


---

### Contents

-   [Introduction](#1)
-   [Example: Generating a hidden Markov process](#2)
-   [Hidden Markov Model](#3)
-   [Generate HMM process](#4)
-   [Estimate transition and emission matrix](#5)
-   [Estimate hidden states](#6)
-   [Estimate transition and emission matrix given observations and hidden states](#7)
-   [Contributors](#8)


---

First, a standard header to load necessary libraries:

    import numpy as np
    from numpy import random as npr
    import matplotlib.pyplot as plt
    %matplotlib inline

##  [Introduction](#1)

The goal of data mining is to tease out characteristic behaviors and interesting subsets and interactions.  Random modeling, as we have seen with Monte Carlo techniques, allows you to attempt this characterization on an unbiased sample of the overall data set.

Markov modeling is used to represent time series data in which the current
state is depended on its previous state.  The [hidden Markov model (HMM)](https://infogalactic.com/info/Hidden_Markov_model) adds another wrinkle:  observation is made from hidden states.  In essence, we are attempting to infer from outcomes what the likely inputs were, a sort of zeroth-order Bayesian inference.  The goal of the hidden Markov model may be stated thus:

> The parameter learning task in HMMs is to find, given an output sequence or a set of such sequences, the best set of state transition and emission probabilities.

More broadly, this goal breaks down into [three different problem approaches](http://scikit-learn.sourceforge.net/stable/modules/hmm.html):

1.  Given the model parameters and observed data, estimate the optimal sequence of hidden states.
2.  Given the model parameters and observed data, calculate the likelihood of the data.
3.  Given just the observed data, estimate the model parameters.

We will adopt the following terminology:

1.  **observations**:  observed data (revealed samples)

2.  **hidden states**:  unobserved states to generate observations

3.  **transition probability matrix**:  a probabilistic matrix to simulate a
sequence of hidden states

4.  **emission probability matrix**:  a probabilistic matrix to generate
observations from hidden states


---

##  [Example: Generating a hidden Markov process](#2)

Suppose the weather tomorrow is only dependent on the weather today.  The next day will rain with a probability of 0.9 (with 0.1 for not rain) if the current day is rainy.  If the current day is not rainy, there is a probability of 0.4 for the next day to rain (0.6 for the next day to not rain). On a rainy day, the probability of swimming, basketball and hiking is 0.8, 0.1 and 0.1, respectively. On a non-rainy day, the corresponding probability of these sports are 0.2, 0.3 and 0.5, respectively.

![](./img/rainy.png)

Generate the hidden Markov process as follows:

1.  Denote "rainy" as 1 and "sunny" as 2;
2.  Denote "swimming", "basketball" and "hiking" as 1, 2, and 3.
3.  Suppose the first day is rainy (our starting state).

The transition matrix looks like:

|     |  1  |  2  |
| --- | --- | --- |
|  1  | 0.9 | 0.1 |
|  2  | 0.4 | 0.6 |

(Note what order the rows and columns read into each other.)

The emission matrix looks like:

|     |  1  |  2  |  3  |
| --- | --- | --- | --- |
|  1  | 0.8 | 0.1 | 0.1 |
|  2  | 0.2 | 0.3 | 0.5 |

We observe only the behaviors, or *observations* (the states $1--3$ given by the emission matrix) and wish to infer the weather *state* $\in \{ 1,2 \}$.

In code, we can represent this state of affairs as follows:

    transition = np.array( [ [ 0.9,0.1 ],[ 0.4,0.6 ] ] )
    emission   = np.array( [ [ 0.8,0.1,0.1 ],[ 0.2,0.3,0.5 ] ] )

    hiddenStateList = np.array( [ 1,2 ] );      # all possible states
    observationList = np.array( [ 1,2,3 ] );    # all possible observations

The HMM will be built progressively, step by step:

    n = 100
    states = np.zeros( ( n, ),dtype=np.int )
    obs    = np.zeros( ( n, ),dtype=np.int )

    states[ 0 ] = 2     # starting state (hidden from model)
    probVector = emission[ hiddenStateList == states[ 0 ] ]

    id = ( np.cumsum( probVector ) >= npr.rand() ).tolist().index( True )
    obs[ 0 ] = observationList[ id ]

    for i in range( 1,n ):
        probVector = transition[ hiddenStateList == states[ i-1 ] ]
        id = ( np.cumsum( probVector ) >= npr.rand() ).tolist().index( True )
        states[ i ] = hiddenStateList[ id ]

        probVector = emission[ hiddenStateList == states[ i ] ]
        id = ( np.cumsum( probVector ) >= npr.rand() ).tolist().index( True )
        obs[ i ] = observationList[ id ]

Plotting the observations and inferred states:

    fig,ax = plt.subplots()
    ax.step( range( len( states ) ),states )
    ax.plot( range( len( obs ) ),obs/2+0.5,color='orange',linestyle='',marker='o' )
    plt.xlabel( 'Time step' )
    plt.ylabel( 'Observations' )
    plt.show()


---

##  [Hidden Markov Model](#3)

[`hmmlearn`](http://hmmlearn.readthedocs.io/en/latest/) (formerly `scikit-learn.hmm`) includes a number of tools to automatically generate the HMM process:

-   [`GaussianHMM`](http://hmmlearn.readthedocs.io/en/latest/api.html#hmmlearn.hmm.GaussianHMM) Hidden Markov Model with Gaussian emissions.
-   [`GMMHMM`](http://hmmlearn.readthedocs.io/en/latest/api.html#hmmlearn.hmm.GMMHMM)	Hidden Markov Model with Gaussian mixture emissions.
- [`MultinomialHMM`](http://hmmlearn.readthedocs.io/en/latest/api.html#hmmlearn.hmm.MultinomialHMM) Hidden Markov Model with multinomial (discrete) emissions


---

##  [Generate HMM process](#4)

An example implementation of the rainy/sunny problem could look like:

    transition = np.array( [ [ 0.9,0.1 ],[ 0.4,0.6 ] ] )
    emission   = np.array( [ [ 0.8,0.1,0.1 ],[ 0.2,0.3,0.5 ] ] )

    from hmmlearn import hmm
    model = hmm.MultinomialHMM( n_components=2 )

    model.startprob_ = np.array( [ 1.0,0.0 ] )  # start as 'rainy'
    model.transmat_  = transition
    model.n_features    = 3
    model.emissionprob_ = emission

    obs -= 1
    obs.shape = ( obs.shape[ 0 ],1 )
    logprob,states_ = model.decode( obs )

Note that the basis changes from $\{ 1,2,3 \}$ to $\{ 0,1,2 \}$ and that the shape of `obs` must be two-dimensional.

Compare the results:

    states_ == ( states-1 )

> You can train an HMM by calling the fit method. The input is “the list” of the sequence of observed value. Note, since the EM algorithm is a gradient-based optimization method, it will generally get stuck in local optima. You should try to run fit with various initializations and select the highest scored model. The score of the model can be calculated by the score method. The inferred optimal hidden states can be obtained by calling predict method. The predict method can be specified with decoder algorithm. Currently the Viterbi algorithm (viterbi), and maximum a posteriori estimation (map) are supported. This time, the input is a single sequence of observed values. Note, the states in model2 will have a different order than those in the generating model.


---

##  [Estimate transition and emission matrix](#5)

    transition_guess = [ [ 0.5,0.5 ],[ 0.4,0.6 ] ]
    emission_guess   = [ [ 0.5,0.3,0.2 ],[ 0.3,0.3,0.4 ] ]

    from hmmlearn import hmm
    model = hmm.MultinomialHMM( n_components=2 )

    model.startprob_ = np.array( [ 1.0,0.0 ] )  # start as 'rainy'
    model.transmat_  = transition_guess
    model.n_features    = 3
    model.emissionprob_ = emission_guess

    states.shape = ( states.shape[ 0 ],1 )
    model = model.fit( obs )

    transition_fit = model.transmat_
    emission_fit   = model.emissionprob_


---

##  [Estimate hidden states](#6)

Suppose we only know the observations of a HMM process.  We would like to know the hidden states, emission matrix and transition states.

    n_obs = 100
    obs_new = npr.randint( 0,3,( n_obs,1 ) )

    transition = np.array( [ [ 0.9,0.1 ],[ 0.4,0.6 ] ] )
    emission   = np.array( [ [ 0.8,0.1,0.1 ],[ 0.2,0.3,0.5 ] ] )

    from hmmlearn import hmm
    model = hmm.MultinomialHMM( n_components=2 )

    model.startprob_ = np.array( [ 1.0,0.0 ] )  # start as 'rainy'
    model.transmat_  = transition
    model.n_features    = 3
    model.emissionprob_ = emission

    states.shape = ( states.shape[ 0 ],1 )
    model = model.fit( obs )

    transition_fit = model.transmat_
    emission_fit   = model.emissionprob_

    states_likely = model.predict( obs_new )

-   How can we assess this HMM?

-   Build a model using the iris dataset to identify which features predict others.


---

##  [Contributors](#8)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
