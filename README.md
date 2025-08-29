# Incomplete-and-Partially-ordered-Plan-Recognition-for-Sensemaking-of-Information-Storygames
Submitted to the 2025 AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment. Details a method by which agents or people's observations can be simulated, based on known states of the world or observed actions.

## Evaluation Codebase

This program is meant to compare pr2plan (Ramirez and Geffner, 2009) against pr2plan_complex. It requires several executables be moved to the top level directory. Each of these executables relies on an FF parser, for which bison and flex are required. See the [FD website](https://www.fast-downward.org/latest/documentation/) for more info. You may be able to use [brew](https://brew.sh) for an easy install. (`brew install bison`)

This ZIP requires you to run all the data requirements; or, you can copy-paste from the analysis sibling folder.


### Virtual Environment for Python

We provide the libraries we use for both running and analyzing the tests with `requirements.txt`. You need only follow the normal Python venv creation guidelines and then import the packages necessary using that!

### pr2plan (Ramirez and Geffner, 2009)
See obs-compiler.tar.bz2 found in the main directory, or download [here](https://sites.google.com/site/prasplanning/file-cabinet). Compile with `cd mod-metric-ff; make libff; cd ..; make all`, and work as best you can through any bugs. It may help to comment out the STATIC line in the Makefile, as some systems (including Mac) don't like it. When compiled, copy the executable 'pr2plan' to this directory. If `make libff` gives you trouble here, likely it will give you the same trouble in pr2plan_complex, so take notes of how you fix issues.

### pr2plan_complex
See the complex_observation_compiler folder. Compile with `cd mod-metric-ff; make libff; cd ..; make all`. When compiled, copy the executable 'pr2plan' to the top level directory.

### Compiling an optimal planner - Fast Downward
This evaluation uses a specially built optimal planner, Fast Downward. You only need to build it following their build-from-source instructions to run the same tests as we have. We provide the specific version of FD used in the fast-downward folder. FD's parser is brittle in comparison to other parsers, so any other domains may cause some issues. 

### Running the evaluation:
To run the evaluation run `harness.py`. By default this runs a (lengthy) evaluation on the problems in `Benchmark_Problems`, and reports the results in both a text table and latex-ready table. This is a long process, so feel free to pare down the settings. Just make sure those settings match the .obs files available. (Or generate your own .obs files)

To run it as it exists in our paper:

```
python harness.py --settings simple
```

### Analyzing the Evaluation

```
python analyze.py
```