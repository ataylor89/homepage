# homepage

## Creating a website on AWS cloud

AWS is an acronym that means Amazon Web Services.

In computer science, the word "cloud" is a metaphor for the internet.

Instead of buying a server and running it from our home, we can rent servers over the internet.

AWS lets us rent servers in the cloud.

In this repository, I created a homepage that I host on AWS.

Below are some instructions for hosting a homepage on AWS.

1. Create an account on Amazon Web Services (AWS)
    1. In order to create an account, I gave my email address and my debit card number.
2. Open the signin link in a web browser (my signin link looks like *.signin.aws.amazon.com/console)
    1. \* is an identifier that belongs to me, and it stands for my account ID or my account alias
3. Log in using your root user email address or your account ID (or alias), IAM username and password
    1. After you log in for the first time, you can create an IAM account in the IAM service
4. In the search bar (located in the top menu next to the AWS logo and the grid of nine dots) type EC2
5. A popup should appear with the EC2 service as the first result. Click on the EC2 service.
6. On the left menu under the Instances category, click on Instances
7. On the top right click on Launch Instances
8. Under "Name and tags" type a name for your instance (e.g. I put "myserver" as the name, without the quotes)
9. We can use the default Amazon Machine Image, which is currently (at the time of writing) Amazon Linux 2023
10. We can use the default 64-bit x86 architecture... but if you plan to write Arm assembly then you can choose 64-bit Arm
11. We can use the default instance type, t2.micro. This is one of the cheapest options.
12. We are going to create an RSA public key and private key to use with ssh.
    1. Under "Key pair (login)" click on "Create new key pair"
    2. Enter a name for the key pair. I called mine "myserver", which is the same name I gave to my instance.
    3. The key pair type should be RSA and the private key file format should be .pem.
    4. Click on "Create key pair".
    5. The pem file (in my case, myserver.pem) gets saved to your Downloads folder if you have MacOS.
    6. In Terminal I type the command "mv ~/Downloads/myserver.pem ~/myserver.pem" to put it in my user directory.
13. We are now going to create a security group that allows SSH, HTTP, and HTTPS traffic.
    1. Under "Network settings", under "Firewall", we want "Create security group" to be selected.
    2. Check "Allow SSH traffic from Anywhere", "Allow HTTPS traffic from the internet", and "Allow HTTP traffic from the internet".
14. We are now going to edit the user data under "Advanced details"
    1. The user data is a script that is run when the instance is started for the very first time
    2. Under "Advanced details", at the very bottom under "User data - optional", copy/paste the following script:
    ```
    #!/bin/bash

    # Step 1. Install python3 and pip3
    sudo yum update -y
    sudo yum install python3 -y
    sudo yum install python3-pip -y

    # Step 2. Install Flask for the ec2-user
    sudo su ec2-user
    pip3 install Flask

    # Step 3. Install Flask for the root user
    sudo su
    pip3 install Flask

    # Step 4. Update the bashrc file for the root user
    cat << EOF >> /root/.bashrc

    # Aliases
    alias python=/usr/bin/python3
    alias pip=/usr/bin/pip3
    EOF

    # Step 5. Update the bashrc file for the ec2-user
    cat << EOF >> /home/ec2-user/.bashrc

    # Aliases
    alias python=/usr/bin/python3
    alias pip=/usr/bin/pip3
    EOF

    # Step 6. Download the code from Github
    cd /home/ec2-user
    mkdir homepage
    mkdir -p homepage/app/templates
    mkdir -p homepage/app/static/css
    cd homepage
    export prefix="https://raw.githubusercontent.com/ataylor89/samplehomepage/refs/heads/main"
    curl -O $prefix/.gitignore
    curl -O $prefix/app.py
    curl -o app/__init__.py $prefix/app/__init__.py
    curl -o app/views.py $prefix/app/views.py
    curl -o app/templates/index.html $prefix/app/templates/index.html
    curl -o app/static/css/stylesheet.css $prefix/app/static/css/stylesheet.css
    chown -R ec2-user .
    chgrp -R ec2-user .
    find . -type f -exec chmod 644 {} \;
    find . -type d -exec chmod 755 {} \;
15. Review your selections on the right under "Summary", and then click "Launch instance" on the right
16. When your instance has initialized, go to EC2 > Instances, and you'll see your instance in the menu
17. Check the checkbox that corresponds to your instance, and this will cause the instance summary to appear at the bottom
18. The public IPv4 address for your instance appears under "Instance summary". Copy it to your clipboard by clicking on the square icon.
19. Open Terminal. We are going to SSH into our instance.
    1. Make sure that your .pem file is located in your user directory. Mine is called myserver.pem.
    2. In Terminal type the command "stat -f %A ~/[filename].pem". I typed "stat -f %A ~/myserver.pem".
    3. On my computer, the default file permissions are 644. We need to change them to 400.
    4. In Terminal type the command "chmod 400 ~/[filename].pem". I typed "chmod 400 ~/myserver.pem".
    5. Now that our file permissions are compliant with the ssh program, we can ssh in.
    6. In Terminal type the command "ssh -i ~/[filename].pem ec2-user@[public-ipv4-address]".
    7. My file is called myserver.pem, so I typed "ssh -i ~/myserver.pem ec2-user@[public-ipv4-address]"
    8. The public IPv4 address should be saved in your clipboard because of step 19.
    9. You can copy/paste the public IPv4 address into your ssh command using command+v.
    10. A prompt should appear that asks you if you want to connect. Type "yes" and click enter.
    11. After you have logged in via ssh, you should see a prompt that says "[ec2-user@ip-ww-xx-yy-zz ~]$"
    12. The numbers ww-xx-yy-zz are your private IP address
    13. Once you see this prompt, you can type the command "ls -als" to see the contents of your user directory
20. Now we are going to run the application.
    1. We should be logged into our EC2 instance via ssh. Type the commands "ls" or "ls -als" in the prompt.
    2. You should see the folder "homepage" appear in the listing, because we downloaded it in the user data script.
    3. Type the command "cd homepage".
    4. In order to run the application on port 80, we need to be the root user. Type the command "sudo su".
    5. Now type the command "python app.py &". This starts the web server and runs the application.
    6. The ampersand (&) runs the process in the background.
    7. The command prompt should look like this:
        ```
        [root@ip-ww-xx-yy-zz homepage]# python app.py &
        [1] [processid]
        [root@ip-www-xx-yy-zz homepage]#  * Serving Flask app 'app'
         * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         * Running on all addresses (0.0.0.0)
         * Running on http://127.0.0.1:80
         * Running on http://ww.xx.yy.zz:80
        Press CTRL+C to quit
    8. You can press the return key to get back to the command prompt.
    9. To see the process, you can type the command "jobs" in the command prompt.
    10. To see the process, you can also type "ps aux | grep python" or "ps aux | grep [processid]" in the command prompt.
    11. To bring the job to the foreground, you can type "fg 1" or "fg %1".
    12. To stop the process, you can type the key sequence control+z when it's in the foreground.
    13. To resume the process, you can type the command "bg %1" in the command prompt.
    14. You can practice bringing the process to the foreground with the command "fg %1"...
        1. Then you can stop the process with the key sequence control+z...
        2. Then you can resume the process with the command "bg %1".
        3. You can get the job number by typing the command "jobs" in the command prompt.
        4. You can also bring the process to the foreground with the command "fg #processid". For me it's "fg #3876".
        5. You can stop the process with the key sequence control+z.
        6. You can resume the process with the command "bg #processid". For me it's "bg #3876".
21. Assuming that the Python application is running, copy the public IPv4 address to your clipboard, and open it in a web browser
    1. I just paste the public IP address into my web browser's address bar, and press the return key
    2. The sample homepage should appear in your web browser
    3. It should say "Sample homepage" in bold, and underneath it, "This is a sample homepage."
    4. Congratulations! You just created a website on AWS cloud.
    5. If anything isn't working for you, you can try logging out of SSH and logging back in
    6. It's possible you don't see the homepage folder in your user directory...
    7. It's possible that your bash aliases have not been set up yet...
    8. In both cases, it might help to log out of SSH and log back into SSH
    9. You can edit the sample homepage and make it your own
    10. To save money, you can use the t2.micro instance type, and stop the instance when you're not using it

I hope these instructions help.

It's possible that I missed something in the instructions.

If it's not working for you, don't worry. It's possible that you will figure out what the problem is, and solve the problem in time. It's also possible that you can learn from the instructions, and write your own instructions, and write instructions that work for you.

Over the course of this document, we have learned about AWS cloud, python, the Flask framework, and shell scripting.

We have also learned about the EC2 web service and how to create an EC2 instance and log into it via ssh.

I would like to keep this section short (relatively short, that is) so I will end it here.

I might add new sections to this readme over time.

Thanks for reading.

Today is Sunday August 3, 2025.

I wish everyone a good evening (if it's evening for you) or a good morning (if it's morning for you) or a good afternoon (if it's the afternoon).
