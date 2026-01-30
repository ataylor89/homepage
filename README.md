# readme

## Requirements

This project has two external dependencies, Flask and requests.

They can be installed with the following commands:

    % pip install Flask
    % pip install requests

Alternatively, they can be installed using the requirements.txt file as an input.

    % pip install -r requirements.txt

In case you're wondering, Flask is a popular web framework for Python.

Flask sets up a web server behind the scenes, and it has decorator methods for routing an HTTP request to a request handler.

The requests library is also very useful, because it facilitates HTTP requests.

The weather page uses the requests library to get the latest weather data, by making an HTTP request to a weather service and parsing the response.

## Usage

After installing the external dependencies, Flask and requests, the homepage app can be run with the following commands:

    % cd ~/Github/homepage/src
    % python main.py

This starts up the web server on localhost:8081.

You can visit the webpage by opening a browser and entering localhost:8081 or 127.0.0.1:8081 in the URL bar.

The name "localhost" and the IP address "127.0.0.1" both refer to the local machine.

The web server is listening on port 8081 so the port has to be set to 8081.

You can actually see in src/main.py that the host is set to "127.0.0.1" and the port is set to 8081.

## Creating a symbolic link

It's nice to be able to run a Python program from any directory, when you're using a command-line interface like Terminal.

For this reason, I often create symbolic links to some of my programs, and store them in my ~/bin directory.

We can create a symbolic link to src/main.py with the following commands:

    % cd ~/bin
    % ln -s ~/Github/homepage/src/main.py homepage.py

Now it should show up in the ~/bin folder.

    % ls -als

You should see a line that says `homepage.py -> /path/to/homepage/src/main.py`, where `/path/to` stands for a path on your filesystem.

If your file structure is different from mine, then you can replace all references to `~/Github` with the appropriate path.

There are a couple more steps before running the file. First, we have to make the `~/Github/homepage/src/main.py` file executable.

We can do this with the following command:

    % chmod +x ~/Github/homepage/src/main.py

Next, we have to add `~/bin` to our PATH variable, so that the shell knows where to find our symbolic links.

We can do this by editing the `~/.zprofile` file (if we are using zsh) or `~/.bash_profile` (if we are using bash).

    % echo $SHELL
    /bin/zsh

    % vi ~/.zprofile

My `~/.zprofile` file includes the following lines:

    alias python="python3"
    alias pip="pip3"

    export PATH="/Users/myusername/bin:$PATH"

Having completed all these steps, we can test our symbolic link.

    % cd ~
    % homepage.py
    [homepage] Loaded key /Users/<username>/Github/homepage/keys/rsa/default.txt
    [homepage] Loaded key /Users/<username>/Github/homepage/keys/xor/default.txt
    [homepage] Welcome to the homepage web application
     * Serving Flask app 'homepage'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:8081
    Press CTRL+C to quit

It works. All we have to do is type the command `homepage.py`, and it invokes the homepage app.

I wanted to explain the steps involved in configuring a symbolic link. To summarize, we took the following steps:

1. We made the `~/Github/homepage/src/main.py` file executable with the `chmod +x` command.
2. We added the shell directive `#!/usr/bin/env python3` to the top of the `main.py` file.
3. We created a symbolic link in the `~/bin` folder with the `ln -s ~/Github/homepage/src/main.py homepage.py` command.
4. We added the `~/bin` folder to our PATH variable by editing the `~/.zprofile` configuration file.
5. We tested the symbolic link in a Terminal window by typing the `homepage.py` command and verifying that it works.

I think that concludes this section. I wanted to explain this subject in detail, because in my opinion, symbolic links are very useful.

A symbolic link can make it a lot easier to run your program. (You don't have to navigate to its directory before running it.)

Also, it can improve the user experience.
