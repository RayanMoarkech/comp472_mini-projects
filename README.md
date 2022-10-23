# comp472_mini-projects
[This repo](https://github.com/RayanMoarkech/comp472_mini-projects) currently holds the mini-project 1 of COMP472.

![Python 3.6](https://img.shields.io/badge/python-v3.7-blue)

<p align="left"> 
    <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
    </a> 
    <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> 
        <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> 
    </a> 
    <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> 
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> 
    </a>
</p>

---

## The Team

Team Name: `Codeine`

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/RayanMoarkech">
                <img src="https://avatars.githubusercontent.com/u/34872331?v=4" width="120px;" alt="Profile Picture"/>
                <br>
                <b>Rayan Moarkech</b>
            </a>
            40089399
        </td>
        <td align="center">
            <a href="https://github.com/LujainKhalaf">
                <img src="https://avatars.githubusercontent.com/u/67845184?v=4" width="120px;" alt="Profile Picture"/>
                <br>
                <b>Lujain Khalaf</b>
            </a>
            40086330
        </td>
        <td align="center">
            <a href="https://github.com/samimerhi">
                <img src="https://avatars.githubusercontent.com/u/50461308?v=4" width="120px;" alt="Profile Picture"/>
                <br>
                <b>Sami Merhi</b>
            </a>
            40136648
        </td>
    </tr>
</table>

---

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

## Running the Code

Run the main function inside the file `main.py`.
This will run all the assignment code in chronological manner. 
Function calls are maid in the main function to call specific tasks for each exercise number.
