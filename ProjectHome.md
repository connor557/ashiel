ASHIEL is a semantic/fuzzy logic chatbot being developed in the python language. The goal of ASHIEL is to create a Turing Test ready bruteforce. This chatbot will be written for the windows operating system in python 2.7.3.

Basically this is how it works.
There are 5 types of strings: descriptors, events, locations, persons, and objects.
Each of these are: d, e, l, p, and o respectively.
There are 5 keywords the compare these strings: is, was, in, on, maybe.

For example: dog is animal
This implies to ASHIEL that all dogs are animals without exception
Where 'dog' is an 'object', and 'animal' is an 'object'.
'is' is a keyword comparator.

Another example: dog maybe brown
This implies to ASHIEL that not all dogs are brown, but some dogs might be brown.
Where 'dog' is an 'object', and 'brown' is a 'descriptor'.
'maybe' is a keyword comparator.

The final example is that: animal maybe aggressive
This implies to ASHIEL that not all animals are aggressive, but some animals might be aggressive.
Where 'animal' is an 'object', and 'aggressive' is a 'descriptor'.
'maybe' is a keyword comparator.

ASHIEL will be able to inference that:
Because: 'dog is animal' and 'animal maybe aggressive'
Therefore: 'dog maybe aggressive'

This can be helped later with the inclusion of a 'pural' and 'singular' keyword.
Example: 'dogs plural dog' or 'animal singular animals'
So that ASHIEL can better communicate.