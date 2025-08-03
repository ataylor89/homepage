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
20. More to follow
