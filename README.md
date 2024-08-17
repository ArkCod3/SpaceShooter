# Space Shooter
Game project to learn about Python, game engines, and collaborative development.

## How do I contribute?
1. <a href="#how-to-setup-a-python-virtual-environment">Setup a virtual environment</a> running **Python 3.12**.

2. <a href="#how-to-activate-a-python-virtual-environment">Activate the virtual environment</a>.

3. Create a branch from the latest commit in the master branch.
   * Name the branch according to the feature you are adding.

4. Make all required changes on your feature branch, and when finished, merge it to the master branch.

5. If you don't need your branch anymore, then delete it from the remote to avoid clutter of inactive branches.

## How to setup a Python virtual environment?
1. Install Python **3.12** in your system.

2. Navigate to the project's root directory and execute the following instructions on the command-line.
   * If on Windows, please note that instructions provided are for **Command Prompt (CMD)**, not **PowerShell**.

3. ```pip install virtualenv```.

4. ```python3.12 -m venv env```.
   * Creates an enviroment named "**env**" that uses Python **3.12**.

5. Activate the virtual environment.

6. Install all required dependencies with: ```pip install -r requirements.txt```

## How to activate a Python virtual environment?
### Windows
1. Open a terminal running **Command Prompt (CMD)** in the parent directory of your created environment.
2. Run ```env\Scripts\activate.bat```
   * **env** is the name of the environment.
   * The use of **backslashes (\\)** is important.

### Linux
1. Open a terminal with it's working directory set to the environment's parent directory.
2. Run ```source env/bin/activate```.<br></br>

If activation is successful you should see **(env)** at the beginning of your command prompt.
   * Example: ```(env) C:\Users\user\SpaceShooter>```

## How to deactivate or reset Python virtual environment?
* Deactivate (exit) the virtual enviroment by running ```deactivate``` on the command-line
* To reset the virtual enviroment simply delete the directory that contains the virtual enviroment and perform setup again.
   * Keep in mind that the environment will need to re-install dependencies everytime you do this.

## How to use Pygame?
* <a href="https://www.pygame.org/docs/">Pygame documentation</a>