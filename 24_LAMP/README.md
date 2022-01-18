# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: ~10 minutes

### Prerequisites:

- A DigitalOcean account (possibly with free credits from the [GitHub student edu pack](https://education.github.com/pack))
- Basic knowledge of terminal commands (like `cd`, `nano`, or the like)

### Creating a Droplet

1. Log into your DigitalOcean account and head on over to https://cloud.digitalocean.com/projects/
2. At the top right, click the green "Create" button then click "Droplets"
3. Select "Ubuntu 20.04 (LTS) x64" as the distribution if it isn't already
4. Under "Choose a plan" select the amount of computing power and storage you'll need for your project
   - If you aren't sure how much you need, leaving it as default is fine
5. Under "Choose a datacenter region" select the closest region to you
6. Under "Authentication" choose Password and type in a password
   - We will disable passwork authentication later on
7. Scroll down and click the "Create Droplet" button

### Setting up User Accounts

1. In your "Droplets" page clck on the droplet you just made
2. Open up your terminal and enter the command `$ ssh root@[ipv4_address]`
   - The ipv4 address can be found on the page for your droplet
3. Type in the password you set up before and log into the root account
4. Run the commands `$ ufw allow OpenSSH` and `$ ufw enable` to set up a basic firewall
5. Run the command (replacing "[name]" with the desired user name) `$ adduser [name]`
6. Type in a password and confirm it, following the rest of the steps to create the account
7. Run the command `$ usermod -aG sudo [name]` to grant the account sudo privileges
8. Run the command `$ exit` to log out of the root account
9. Run the command `$ ssh-copy-id [name]@[ipv4_address]` and type in the password you set for the account
10. Run the command `$ ssh [name]@[ipv4_address]` and log in
11. Run the command `$ sudo nano /etc/ssh/sshd_config`
12. Edit the following lines to disable root logins and password authentication ([old] -> [new]):
   ```
   PermitRootLogin yes -> PermitRootLogin no
   PasswordAuthentication yes -> PasswordAuthentication no
   #PubkeyAutentication yes -> PubkeyAutentication yes
   ```
11. Run the command `$ sudo systemctl reload sshd` to make the config changes go into effect

### Installing Apache2

1. While logged in to your user account, run the command `$ sudo apt install apache2`
   - If there is an error saying unable to access the package IP, type `$ sudo apt update` to get latest changes to packages 
3. Run the command `$ sudo ufw allow in "Apache"` to allow http traffic
4. In your web browser, navigate to "http://[ipv4_address]" and you should see the default Apache2 page

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/

---

Accurate as of (last update): 2022-01-17

#### Contributors:   
Liesel Wong, pd2   
