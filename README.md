<img src="/images/Personal Logo, Design 1.0.png" align="right" width="225" height="150"/>

# Basic Overview [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
Using backtracking search with forward checking, this Python program by DC David finds a solution for the n-Queens Puzzle for up to n=52.

### Sample output:
<img src="/images/step9.png" width="900" height="600">

<br>

# Overview of the n-Queens Puzzle
The n-Queens puzzle is the problem of placing 'n' chess queens on an n-by-n chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. Solutions exist for all natural numbers n with the exception of n = 2 and n = 3. The 8-Queens puzzle is a more specific example of the n-Queens problem of placing eight non-attacking queens on an 8×8 chessboard.

<br>

# Installation and Usage
### Download the program:
  <details>
    <summary> Go to the <a href="https://github.com/cs-dcdavid/n-Queens-Puzzle">n-Queens Puzzle Github Repository</a>. </summary>
    <img src="/images/step1.PNG">
  </details>
  <details>
    <summary> Click on 'Code' and then 'Download ZIP'. </summary>
    <img src="/images/step2.png">
  </details>
  <details>
    <summary> Confirm the download by clicking on 'Accept.' </summary>
    <img src="/images/step3.png">
  </details>
  <details>
    <summary> On your Downloads folder, right click on the archive and then select 'Extract All...' </summary>
    <img src="/images/step4.png">
  </details>
  <details>
    <summary> Optionally, choose a directory to save the folder. Select 'Extract.' </summary>
    <img src="/images/step5.png">
  </details>

### Run the program:
  <details>
    <summary> Run the program by selecting 'n_queens_puzzle' or 'n_queens_puzzle.py.' </summary>
    <img src="/images/step6.png">
  </details>

### Use the program by following the prompt:
  <details>
    <summary> Typing-in any integer 'n' from 1 to 52 to get a solution to the n-Queens puzzle. </summary>
    <img src="/images/step7.png" width="900" height="600">
  </details>
  <details>
    <summary> Typing-in '8' gets a solution to the 8-Queens puzzle. </summary>
    <img src="/images/step8.png" width="900" height="600"> <br>
    <img src="/images/step9.png" width="900" height="600">
  </details>
  <details>
    <summary> Typing-in '2' or '3' does not get a solution to the 2-Queens/3-Queens puzzle because there are no solutions to the n-Queens puzzle for n = 2 and n = 3. </summary>
    <img src="/images/step10.png" width="900" height="600"> <br>
    <img src="/images/step11.png" width="900" height="600">
  </details>
  <details>
    <summary> Typing-in '10' gets a solution to the 10-Queens puzzle. However, for any integer 'n' greater than or equal to 10, the program requires confirmation by typing in 'y' if the user wants to proceed or 'n' if not. The program requires confirmation because it starts to slow down starting at n = 10 because it has to explore up to 17 trillion possibilities; therefore as a consequence, the program might take a long time loading. Pressing Ctrl+C (Windows) or Cmd+. (Mac) force exits the program. </summary>
    <img src="/images/step12.png" width="900" height="600"> <br>
    <img src="/images/step13.png" width="900" height="600"> <br>
    <img src="/images/step14.png" width="900" height="600"> <br>
    <img src="/images/step15.png" width="900" height="600">
  </details>
  <details>
    <summary> Typing in 'gibberish' or any non-integer input throws an error. </summary>
    <img src="/images/step16.png" width="900" height="600"> <br>
    <img src="/images/step17.png" width="900" height="600">
  </details>
