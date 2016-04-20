Set up SSH key
==============

SSH, also known as Secure Socket Shell, is a network protocol that provides us with a secure way to access a remote computer. Once you set up your SSH key and add it to your Github account, you don't have to type username and password when you push your commits to the remote repository.

1. Checking for existing SSH keys:

   * Go to your local repository and check whether you have SSH key or not::

      ls -al ~/.ssh

   * If you already have the SSH key, you will see the one of the following filenames for the public SSH key:

      - ``id_rsa.pub``, ``id_ecdsa.pub``, ``id_ed25519.pub``, or ``id_rsa.pub``

   * If you don't see SSH key or don't want to use the one you have, you can generate a new one (see 2).

2. Generating a new SSH key and adding it to the ssh-agent:

   * Generate a SSH key::

      ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

   * After you paste the above command to the terminal, you will get the following message:

      - ``Enter a file in which to save the key (/Users/you/.ssh/id_rsa)`` Hit enter to continue.
      - ``Enter passphrase (empty for no passphrase)`` Add passphrase if you want; otherwise, hit enter to continue.
      - ``Enter same passphrase again`` Type the passphrase again or hit enter to continue.

   * You will see:

      - ``Your identification has been saved in /home/oski/.ssh/id_rsa.``
      - ``Your public key has been saved in /home/oski/.ssh/id_rsa.pub.``, which means that you have SSH key now!

   * Add it to the ssh-agent::

      eval $(ssh-agent -s)
      ssh-add ~/.ssh/id_rsa

   * Now, you are ready to add the SSH key to Github.

3. Adding a new SSH key to your Github account:

   * Copy the SSH key to your clipboard::

      clip < ~/.ssh/id_rsa.pub

   * Or you can use and copy the output::

      cat ~/.ssh/id_rsa.pub

   * Go to Github and click your profile in the top-right corner.

   * Click the SSH and GPG keys on the right panel and click New SSH key.

   * Give a label to this SSH key, paste the key into Key field and click Add SSH key.

4. Testing your SSH connection:

   * Enter::

      ssh -T git@github.com

   * You will see

      - ``The authenticity of host 'github.com (192.30.252.1)' can't be established. RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48. Are you sure you want to continue connecting (yes/no)?``

   * Type yes and you should see:

      - ``Hi username! You've successfully authenticated, but GitHub does not provide shell access.``

5. Switching remote URLs from HTTPS to SSH:

   * Since you probably already add your remote URL using HTTPS (check by ``git remote -v``, you need to change it into SSH::

      git remote set-url origin git@github.com:USERNAME/OTHERREPOSITORY.git

   * You can verify again by ``git remote -v`` and next time you push your commits to the origin, you don't have to type username and password anymore!

For more detailed discussion, read `SSH key documentation <https://help.github.com/categories/ssh/>`__ on Github.
