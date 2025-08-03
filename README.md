# homepage

## Creating a website on AWS cloud

AWS is an acronym that means Amazon Web Services.

In computer science, the word "cloud" is a metaphor for the internet.

Instead of buying a server and running it from our home, we can rent servers over the internet.

AWS lets us rent servers in the cloud.

In this repository, I created a homepage that I host on AWS.

Below are some instructions for hosting a homepage on AWS.

1. Create an account on Amazon Web Services (AWS)\
1.1 In order to create an account, I gave my root user email address, my account name, and my debit card number.
2. Open the signin link in a web browser (my signin link looks like *.signin.aws.amazon.com/console)\
2.1 * is an identifier that belongs to me, and it stands for my account ID or my account alias
3. Log in using your root user email address or your account ID (or alias), IAM username and password\
3.1 After you log in for the first time, you can create an IAM account in the IAM service
4. In the search bar (located in the top menu next to the AWS logo and the grid of nine dots) type EC2
5. A popup should appear with the EC2 service as the first result. Click on the EC2 service.
6. On the left menu under the Instances category, click on Instances
7. On the top right click on Launch Instances
8. Under "Name and tags" type a name for your instance (e.g. I put "myserver" as the name, without the quotes)
9. We can use the default Amazon Machine Image, which is currently (at the time of writing) Amazon Linux 2023
10. We can use the default 64-bit x86 architecture... but if you plan to write Arm assembly then you can choose 64-bit Arm
11. We can use the default instance type, t2.micro. This is one of the cheapest options.
12. We are going to create an RSA public key and private key to use with ssh.\
12.1 Under "Key pair (login)" click on "Create new key pair"\
12.2 Enter a name for the key pair. I called mine "myserver", which is the same name I gave to my instance.\
12.3 The key pair type should be RSA and the private key file format should be .pem.\
12.4 Click on "Create key pair".\
12.5 The pem file (in my case, myserver.pem) gets saved to your Downloads folder if you have MacOS.\
12.6 In Terminal I type the command "mv ~/Downloads/myserver.pem ~/myserver.pem" to put it in my user directory.
13. We are now going to create a security group that allows SSH, HTTP, and HTTPS traffic.\
13.1 Under "Network settings", under "Firewall", we want "Create security group" to be selected.\
13.2 Check "Allow SSH traffic from Anywhere", "Allow HTTPS traffic from the internet", and "Allow HTTP traffic from the internet".
14. We are now going to edit the user data under "Advanced details"\
14.1 The user data is a script that is run when the instance is started for the very first time\
14.2 Under "Advanced details", at the very bottom under "User data - optional", copy/paste the following script:
    ```
    sudo yum -y install pip
    pip install Flask
    sudo su
    pip install Flask
14. I need to add this line in order to pick up where I left off...
14.3 The script (above) installs pip, which is Python's package manager\
14.4 The script (above) also installs the Flask package, which we will use to create a web server\
14.5 The script (above) installs Flask for both the ec2-user account and the root user account\
14.6 We need the root user account in order to run a server on port 80, so we install Flask on the root user account as well
15. Review your selections on the right under "Summary", and then click "Launch instance" on the right
16. When your instance has initialized, go to EC2 > Instances, and you'll see your instance in the menu
17. Check the checkbox that corresponds to your instance, and this will cause the instance summary to appear at the bottom
18. The public IPv4 address for your instance appears under "Instance summary". Copy it to your clipboard by clicking on the square icon.
19. Open Terminal. We are going to SSH into our instance.
19.1 Make sure that your .pem file is located in your user directory. Mine is called myserver.pem.\
19.2 In Terminal type the command "stat -f %A ~/<filename>.pem". I typed "stat -f %A ~/myserver.pem".\
19.3 On my computer, the default file permissions are 644. We need to change them to 400.\
19.4 In Terminal type the command "chmod 400 ~/<filename>.pem". I typed "chmod 400 ~/myserver.pem".\
19.5 Now that our file permissions are compliant with the ssh program, we can ssh in.\
19.6 In Terminal type the command "ssh -i ~/<filename>.pem ec2-user@<public-ipv4-address>".
19.7 My file is called myserver.pem, so I typed "ssh -i ~/myserver.pem ec2-user@<public-ipv4-address>"
19.8 The public IPv4 address should be saved in your clipboard because of step 18.\
19.9 You can copy/paste the public IPv4 address into your ssh command using command+v.\
19.10 A prompt should appear that asks you if you want to connect. Type "yes" and click enter.\
19.11 After you have logged in via ssh, you should see a prompt that says "[ec2-user@ip-ww-xx-yy-zz ~]$"\
19.12 The numbers ww-xx-yy-zz are your private IP address\
19.13 Once you see this prompt, you can type the command "ls -als" to see the contents of your user directory
20. More to follow
