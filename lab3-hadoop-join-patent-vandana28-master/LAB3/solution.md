To solve this problem, I have used 3 mappers and 3 reducers.

```Mapper1.py:```

So the patent file and the citation file is given as input through system input and the files are split line by line. The citation file has just two splits, and I have recorded them in their respective variables, citing and cited.
The patent file is separately split and the state from the patent file is recorded. When there are no states available, a "-" symbol is printed.
Mapper1 outputs the cited state, the citing state and the states obtained through the patent file.

```Reducer1.py:```

The output from the mapper 1 is taken as the input to reducer 1. Here the join is done based on the cited state. 
So for every cited value, the reducer checks if the state is available, if it isn't available , the citing value for that line, is appended into a list. The reducer keeps track of a particular state for a cited number and appends that state to all patents that don't have a state. When the reducer encounters a new cited number, it resets its list and location and does the process again. The output of this reducer 1 would be sorted based on cited number. The output would have cited value, a citing value and a cited state. 

```Mapper2.py:```

Mapper 2 takes reducer1's output and the patent file. It does the same role as mapper1 and prints out the splits of reducer1 output and patent file [patent number and state].
This is printed as an output to reducer2

```Reducer2.py:```

Reducer 2 initially takes in 2 dictionaries, one dictionary stores the output of reducer 1 by taking the citing and cited number as keys and cited state as value. The second dictionary stores the patent number as key and the corresponding patent state as value.
Now I checked if the citing number is available in the patent dictionary, if it is the patent state is appended to another dictionary that has the citing number, cited number, cited state as the key. Here the patent state ie the citing state becomes the value. 
Now when I print this dictionary 3, the intermediate table is printed out.
Finally, to obtain the citing number along with the number of same state citations, a number of conditions are checked and the count is calculated.
This final citing number along with the count is pushed into the final dictionary which is the output of reducer 2.


```Mapper3.py:```

The mapper 3 takes in the reducer2's output and the patent file and prints them for the reducer 3 to take in as input.

```Reducer3.py:```

I have used two dictionaries here, one dictionary to keep track of the citing number and the counts, the other dictionary to hold the patent number as the key as its respective splits as values. If the citing number is available in the patent dictionary,then the citing number's count is appended to the the patent dictionary and the final result is displayed.


```Colloboration Policy:```

Initial discussions with Pradyoth Srinivasan about the input/output mechanisms of Hadoop.
