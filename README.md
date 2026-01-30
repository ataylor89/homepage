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

There is one more step before running the file. We have to make the `~/Github/homepage/src/main.py` file executable.

We can do this with the following command:

    % chmod +x ~/Github/homepage/src/main.py

Now we can invoke the program from any directory, by typing the command `homepage.py`.

    % homepage.py
    [homepage] Loaded key /Users/<username>/Github/homepage/keys/rsa/default.txt
    [homepage] Loaded key /Users/<username>/Github/homepage/keys/xor/default.txt
    [homepage] Welcome to the homepage web application
     * Serving Flask app 'homepage'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:8081
    Press CTRL+C to quit

The shell directive at the top of main.py, `#!/usr/bin/env python3`, instructs the shell (bash or zsh) to use python3 to interpret the code.

You can actually run main.py on its own. For example,

    % cd ~/Github/homepage/src
    % ./main.py

I wanted to explain this one detail before I conclude.

Symbolic links are very useful, because they allow us to run a program from any directory, not just the directory that the program resides in.

We can run the homepage app from any directory, after configuring the symbolic link, by typing the command `homepage.py`.
