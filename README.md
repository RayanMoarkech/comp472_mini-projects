# comp472_mini-projects
This repo holds all the mini-projects of COMP472.

## Install Pre-requisites
Some packages need to be installed to complete the project. Do the following:
```
pip3 install -r requirements.txt
```

## Dataset
The dataset is stored in gzip `./goemotions.json`.
Description:
```
It is a modified version of the original GoEmotion dataset, created by [Demszky et al., 2020]
The dataset we will use for this assignment is a modified version of the original GoEmotion, 
where only posts annotated with a single emotion (and a single sentiment) are kept, 
and the data is formatted in json. 
The json file contains triplets made of the post, its emotion and its sentiment.
```
The dataset is organized in an array with each element containing:
```
[
 human-annotated Reddit comment,
 emotions,
 sentiments: positive/negative/ambiguous/neutral
] 
```