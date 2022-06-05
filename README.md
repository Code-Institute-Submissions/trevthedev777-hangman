# Hangman Game

My Hangman python game tests your vocabulary skills but allowing you to guess the words correctly or each letter per turn. The Objective of the game is to guess the word correctly before the Death of Hangman

![Mock Up](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/13%20Live%20On%20Heroku.jpg?raw=true)

[Hangman Game Live Link](https://hangmanpythongame.herokuapp.com/)

## Features

- This backend application was designed to be run using the terminal only, the objective was to show the neccessary skills to build. run, test and deploy an application that can run on a Heroku mock terminal 
- The application has a created module of automatically generated words for the game and the credits will be found in the credits section of the README.md file
 

### Features left to implement
- ErrorHandling
- Scoreboard

## Technologies

- Python 3
  - The structure of the application was developed using Python as the main language.
- Gitpod
  - The website was developed using Gitpod
- GitHub
  - Source code is hosted on GitHub and deployed using Git Pages.
- Git
  - Used to commit and push code during the development of the Website
- Heroku
  - Application succesfully deployed to Heroku

## Testing

- The application was tested constantly through each conditional and input declaration
    - That users could not repeat their guesses
    - That users were not able to enter numbers as answers
    - That users could quit the game at any time
    - That the game restarted after completion
    - That each step of hangmans state was aligned with the tries given
    - That only six guesses were allowed before the game ended

![Repeated Guesses](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/03%20Repeated%20Guess.jpg?raw=true)

Manual tests were also performed to ensure the application was accessible as possible and some accessibility issues were identified.

There were no known issues identified in these tests

**Game Play**

* The rules will display on start
* You have 6 chances to guess the word or letters correctly
* Each wrong guess brings hangman closer to an impending doom!
* Save him by either guessing the whole word or the correct letter each round

![Gameplay State: Incorrect First Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/02%20First%20Incorrect%20Guess.jpg?raw=true)
![Gameplay State: Incorrect Second Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/04%20Second%20Incorrect%20Guess.jpg?raw=true)
![Gameplay State: Incorrect Third Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/05%20Third%20Incorrect%20Guess.jpg?raw=true)
![Gameplay State: Incorrect Fourth Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/06%20Fourth%20Incorrect%20Guess.jpg?raw=true)
![Gameplay State: Incorrect Fifth Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/07%20Fifth%20Incorrect%20Guess.jpg?raw=true)
![Gameplay State: Incorrect Sixth Guess](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/08%20Sixth%20Incorrect%20Guess.jpg?raw=true)

**Game Board**

* Each guess shows the progressive state of hangmans journey to save him
* The word will display at the bottom of the image of hangman, if you have correct guesses, they will show in the correct place of the word
![Correct Guesses](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/12%20Correct%20Guess.jpg?raw=true)


**End of Game**

* There is a prompt after the game is over on if you would like the game to restart or to exit the application, if you select "Y" then the "Let's Play Hangman!" message shows and you press a key to start
* If the user wishes to stop playing after the round, they should just enter "N" and the application will stop running

![End of Game, Y](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/10%20Restart%20Game%20after%20end.jpg?raw=true)
![End of Game, N](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/11%20Exit%20app%20after%20end%20game.jpg?raw=true)


**Pep8 Validation Report**

This application passed the basic guidelines and principles of Pep8 as stated on the website (https://peps.python.org/pep-0008/)
![Pep8 Validator Results](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/09%20Pep8%20Validation.jpg?raw=true)

## Deployment

- This website was deployed to Heroku which acts as a cloud pltform that allows developers to host their backend applications through a live mock terminal for other users to access the application

![Heroku](https://github.com/trevthedev777/hangman/blob/main/assets/readme_imgs/13%20Live%20On%20Heroku.jpg?raw=true) 


### Version Control

The application was created using Gitpod and pushed to Github to the remote repository ‘https://github.com/trevthedev777/hangman’.

The following git commands were used throughout development to push code to the remote repo:

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on GitHub.

### Deployment to Heroku

- Create or Log in to your Heroku account
- On your dashboard click on create new application
- Enter the name of the application and state your region
- Deployment method was linked to my Github account
- In settings I had to insert a Config Var or Key: PORT and Value: 8000
- Added build packs of Python and Node.js
- Select deploy site and watch the magic and enjoy your efforts

## Credits 

* Marcel my mentor for helping me through a really hard time in life and helping me to progress through all my projects
  his advice and suggestions have helped make me a better developer
* Readme inspired by Trevor Lehmann - https://github.com/trevthedev777/javascriptQuizGameMultipleChoice/blob/main/README.md
* Hangman was inspired by youtube tutorial - https://www.youtube.com/watch?v=cJJTnI22IF8
* Code Institute for providing the template for teh Python essentials project 
