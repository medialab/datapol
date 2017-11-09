# Députés profiles extraction script

This python script first read a csv file containing the list of the députés to build up a set then reads a large file of tweets to store députés' profile descriptions and their evolution through time.

## Installation

Be sure to have python 3 installed.

Then use pip to install the script's dependencies.

```
pip install -r requirements.txt
```

## Usage

The script need to have the `deputes.csv` & `tweets.csv` file in the same directory.

Results will end in a file named `profiles.csv`.

```
./process.py
# or
python process.py
```
