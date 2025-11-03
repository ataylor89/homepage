# setup

## Update

I was able to simplify the setup process

Instead of having to create the RSA and XOR keys manually, they are automatically generated, in the file keys.py

If the rsa and xor folders are missing, or there are no keys in the folders, it creates a default key in each folder

My family taught me that we can write an application that requires "no setup"

That was my goal... to turn this into a web application that requires no setup

It's important to point out that the external Python libraries (Flask, requests, and geopy) are still required

If you want to forego one of these requirements, you can write your own implementation and replace it with your own implementation

For example, you can write your own implementation of geopy, or remove the geocoding logic so that the project does not need geopy

You can install these software packages with the command `pip install -r requirements.txt` in the project root directory

You can also install them individually:

    pip install Flask
    pip install requests
    pip install geopy

After the external libraries are installed, we are ready to run the project, with the command

    python main.py

or

    python main.py &

The second command runs the web server in the background

If you're on AWS cloud, you can also run the web server in a screen session, like this

    # For some reason, I need to be root for my webapp to work on AWS cloud
    sudo su
    screen
    cd /home/ec2-user/homepage
    python main.py

Now we can type the key sequence `ctrl a + d` to detach the screen session

If we log out of our EC2 instance, the web server will still be running in our screen session on AWS cloud

I think that covers everything I wanted to cover

We can install the Python dependencies with the command `pip install -r requirements.txt` from the project root directory

We can run the web application with the command `python main.py &` from the project root directory

Then we can open a web browser and visit localhost (if we are running it on our personal computer) or the IPv4 address of our EC2 instance if we are running it on AWS cloud

In other words, if we are using our personal computer, we can open a web browser and visit 127.0.0.1 or localhost

The web page should appear in the web browser

I wanted to add this update because I simplified the setup process...

I minimized the number of setup requirements

The only setup requirement is to install the Python dependencies that are used by the project

My family taught me that we often use the preposition "for" after the word "requirements"

As in, the one requirement for running the webapp is to install the libraries listed in requirements.txt, or to implement them yourself, or to remove the geocoding logic so that geopy is not needed

I thought I would add that as an afterthought

The requirements for running this project are very simple: to install the necessary packages, and then run the project

I think that is a good stopping point

I also want to point out... that a "no setup" project is a good paradigm to know

This project requires no setup, or close to no setup

That was my goal when I simplified the requirements for running the application

Thanks for reading,  
Andrew

PS. The sections that follow are the old text, which I wrote before I simplified the setup requirements

## Setup and requirements (archived)

In the readme file, we talked about how to deploy a small, lightweight website (sample_homepage) to AWS cloud

In this Markdown file, we can talk about how to run the code in this repository

We can either run it locally (on our personal computer) or remotely (on AWS cloud or some other web host)

To run it locally, the following requirements have to be satisfied:

1. The external Python libraries defined in requirements.txt have to be installed, or...
    - You can replace a library like geopy with your own implementation, or...
    - You can edit the source code so that the weather page does not use geocoding
        - Geocoding is the process of converting a place name (like Mt. Everest) to coordinates (longitude and latitude)
        - You can edit the weather page so that it uses longitude and latitude, but not place names, so that there is no need for geocoding
    - It's worth pointing out that an external library is a library external to the standard library of the programming language
    - Python, Java, C, C++ all have standard libraries
    - The standard library is the built-in library, and the compiler or interpreter already knows where to find it
    - The homepage project depends on three software packages that are not part of the Python standard library: Flask, requests, and geopy
    - These software packages can be installed with the following commands:
        - You can run `pip install -r requirements.txt` from the project root directory, or...
        - You can install the packages separately with the command `pip install <packagename>`, e.g. `pip install Flask`
2. The RSA keys have to be present in algorithms/rsa/keys
    - To create the RSA keys, see the section entitled "Creating the RSA keys"
3. The XOR keys have to be present in algorithms/xor/keys
    - To create the XOR keys, see the section entitled "Creating the XOR keys"

## Creating the RSA keys (archived)

I created the RSA keys with the following commands:

    % cd ~/Github/homepage/algorithms/rsa
    % mkdir -p keys
    % python primetable.py -n 1e4
    % python keytable.py -n 64 -tmin 10 -tmax 1000
    % python keytable.py -n 64 -tmin 100 -tmax 1e4
    % python keytable.py -n 64 -tmin 1000 -tmax 1e4
    % python keygen.py -kl 64 -tmin 10 -tmax 1000 -o keys/small.txt
    % python keygen.py -kl 64 -tmin 100 -tmax 1e4 -o keys/medium.txt
    % python keygen.py -kl 64 -tmin 1000 -tmax 1e4 -o keys/large.txt
    % cp keys/large.txt keys/default.txt

Voila! We have created the RSA keys

(Fun fact: voila comes from the Latin verb videre which means "to see or look at")

Let's test out our keys by encrypting a message and then decrypting the ciphertext to see if we get the original message

    % echo "hello world today is friday october 31 2025" > helloworld.txt
    % python encrypt.py -m helloworld.txt -k keys/default.txt -o cipher.txt
    % python decrypt.py -c cipher.txt -k keys/default.txt
    hello world today is friday october 31 2025

Our test run was successful

We were able to use the key default.txt to encrypt a message and then successfully decrypt the encrypted message

The keys default, small, medium, and large are needed by our cryptography page

The cryptography page uses these keys to encrypt a message or decrypt an encrypted message

Now, let's move onto creating the XOR keys

## Creating the XOR keys (archived)

I created the XOR keys with the following commands:

    % cd ~/Github/homepage/algorithms/xor
    % mkdir -p keys
    % python keygen.py -kl 256 -o keys/small.txt
    % python keygen.py -kl 512 -o keys/medium.txt
    % python keygen.py -kl 1024 -o keys/large.txt
    % cp keys/large.txt keys/default.txt

Voila -- we have created the XOR keys

I like saying voila, but honestly, I know very little French

What languages do I know? English and Spanish

Also, a little bit of Greek, Hebrew, and Latin

Now, let's proceed

We are going to test our keys by encrypting a message and then decrypting the encrypted message to see if we get the original message

(In cryptography, we often use the phrases "message", "encrypted message", "decrypted message", and "original message")

    % echo "hello world today is friday october 31 2025" > helloworld.txt
    % python xor.py -m helloworld.txt -k keys/default.txt -o cipher.txt
    % python xor.py -m cipher.txt -k keys/default.txt
    hello world today is friday october 31 3025

Once again, our test run was successful

We were able to encrypt a message using the key default.txt

Then, we used the same key to decrypt the message, because XOR is a symmetric key algorithm

(In a symmetric key algorithm, the encryption and decryption keys are identical)

(In an asymmetric key algorithm, the encryption and decryption keys are different)

So we have finished creating our RSA and XOR keys

The RSA and XOR keys are needed by the cryptography page

The keys are used to encrypt or decrypt a message

I'm trying to think... is there anything more I should add to this section?

Honestly, I think this section is complete

I might add more to this document later on

So far we have covered three requirements that are needed by the homepage application

The first requirement is to install the external Python libraries (Flask, requests, and geopy)

The second requirement is to create the RSA keys in the algorithms/rsa/keys directory

The third requirement is to create the XOR keys in the algorithms/xor/keys directory

I'm a little afraid that I'm missing something... that there's another requirement we have not covered

If I discover later on that I left a step out, or missed a requirement, then I can update this document with the necessary information
