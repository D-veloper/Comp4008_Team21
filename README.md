# Comp4008_Team21 (Pushed From GitLab: https://projects.cs.nott.ac.uk/psxpn2/comp4008_team21)
In groups of 5 students, we produced a Python program for playing a new variant on the game Rummikub.

**Project Leadership and Collaboration**
As the Team Leader for our group project, I assumed the responsibility of organising the team's efforts, ensuring effective task distribution, and setting clear deadlines. My leadership extended to scheduling and facilitating regular team meetings, where I actively engaged with team members to encourage collaboration, listen to diverse opinions, and harness the unique talents within our group. This role required a proactive approach to guide the project seamlessly from initiation to completion.

**Project Planning and Time Management**
Recognizing the importance of efficient project management, I strategically divided our three-week timeline into distinct phases, focusing on concurrent frontend and backend development. Emphasizing the critical role of communication, I encouraged consistent updates and feedback between team members.

**Strategic Research and Planning**
A pivotal early phase involved dedicating approximately one week to comprehensive research and meticulous project planning. This investment in time significantly contributed to the project's overall success, fostering a smoother development process as we navigated the intricacies of game design.

**Conflict Resolution and Effective Communication**
During the course of the project, challenges arose, particularly stemming from miscommunication. In addressing conflicts, I exemplified patience and employed open dialogue, ensuring a thorough understanding of all perspectives. This approach facilitated compromises when necessary and maintained a positive team dynamic.

**Specific Contributions to Backend Development**
In my specific roles, I undertook the creation of the Gameboard class, functioning as the backend representation of the gameboard. This involved implementing logic to validate the current state of the gameboard, returning a boolean value indicating validity, and providing the positions of tiles in invalid positions.

It is crucial to note that the validation function used in the gameboard was written by another team member (@dominicmwitta), showcasing collaborative efforts in creating a robust backend infrastructure.

Furthermore, I played a pivotal role in the backend and frontend development of the computer player. While the framework for the frontend integration had been set by another teammate (@iramshn), I not only wrote some of the backend logic for the computer player but also extended the framework to seamlessly integrate the computer player with the frontend. This included writing logic for the computer player to identify valid runs and groups on its rack, updating the logic written to extend existing runs and groups on the board, and adding lines of code to visually display the computer player's moves on the frontend. I also extended this functionality into the "auto play" feature, allowing the computer play for the user.

The logic enabling the computer player's ability to extend existing groups and runs on the board was initially written by another team member (@dominicmwitta). I simply made slight updates to the logic to ensure compatibility with the frontend and seamlessly integrating it with the overall gameplay.

Additionally, I integrated sound effects into the game using sound assets and a sound class provided by another teammate (@Kwadwo Dako). This enriched the user experience by adding an auditory dimension to our gaming project.

I also integrated the Gameover screen designed by another teammate (@helen-oy) with the game over backend logic written by (@Kwadwo Dako) for the main game.

Finally, I wrote logic to toggle player turns and assisted with debuging several issues. Notably, I resolved logical errors in the validation logic, invalid positions logic, computer move generation logic and addressed issues like circular import errors


## Authors and acknowledgment
I would like to express my sincere gratitude to my exceptional team members for their unwavering dedication and collaboration throughout the duration of our project. Their unique skills, insightful contributions, and commitment to excellence played a pivotal role in the successful realization of our shared goals. 

Thank you @dominicmwitta, @iramshn, @Kwadwo Dakoand @helen-oy
