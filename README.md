# Mirror Keyboard
[![N|Solid](https://secure.gravatar.com/avatar/7273c58dc017eec83667b50742ff6368?s=80)](https://www.linkedin.com/in/amitasviper/)

This is a small python program based on client-server architecture to use a common keyboard to controll to different computer machines.

### Installation
1. Clone the current project to your local machine:
    ```sh
    $ git clone https://github.com/amitasviper/mirror-keyboard
    ```
2. Install the project dependecies via pip:  `pip install <package_name>`
   ```
   1. pyxhook
   2. uniput
   ```
3. Run the server on the machine whose keyboard you want to use
    ```
    >> python keyIntServer.py
    ```
4. Run the client on the machine not having a keyboard
    ```
    >> python keyStrokes.py
    ```
