##PRE-REQ:
1.	User needs to create their keys (per the current lab guide, Section 3, Exercises: 1, 2).
2.	Create an account on github.com
3.	Upload keys onto github.com
  1.	Account Settings, “SSH and GPH Keys” (on left pane), then select “New SSSH Key” (upper right)
4.	Make sure you add your key to your ssh-agent:
  1.	eval “$(ssh-agent –s)” (checking if agent is running)
  2.	2.	ssh-add ~/.ssh/id_rsa
5.	Finally if keys’ don’t work do:
  1.	in your local directory
  2.	git remote (this will list your remotes)
  3.	git remote remove <remote name you found>
  4.	git remote add origin git@github.com:username/repro.git


##METHOD 1 (simplest)
1. Using your web browser, create a new repo on github.com. For this example, call it “new-repo”, (but don’t add any files to it)
2. clone this “new-repo” onto your computer:
  1. cd to the directory you want to store your github repository then issue the following command in your terminal window:
  2. git clone https://github.com/<user-name>/new-repo
3. add files as needed in the new-repo directory on your computer.
4. add/commit/push as needed – (use exact commands)  


##METHOD 2 
1.	create new local directory on your computer
  1. cd into your new local directory
  2. type ‘git init’ 
2. add files as needed
3. add/commit as needed – (use exact commands)
4. got to github.com and create a new-repo. Name it the exact name as your local directory you already created. (don’t add any files into it)
5. In your local directory enter:
  1. git remote add origin https://github.com/<user-name>/<repo name you just created>
  2. git push —set-upstream origin master


##METHOD 3 (making an exact duplicate) 
1. create a new repo on github.com (call it “new-repo” for example)
2. on your desktop:
  1. git clone —bare https://github.com/exampleuser/<old-repo>.git (this would be a source repo you want a copy of)
3) cd  old-repo.git
  1. git push —mirror https://github.com/exampleuser/new-repo.git
4) cd ..
  1. rm -rf <old-repo>.git
5) git clone https://github.com/exampleuser/new-repo



##METHOD 4 [forking, used to create separate work stream (versions of code) with your collaborators]
1. Using your web browser, find the repo you want to fork on github.com. Github will add this forked branch to your github repos.
2. Clone this repo to your laptop following the steps from method 1.2
3. You can add, edit etc.. add/commit/push etc… this forked branch. 

If you wish, at some point in your develop lifecycle you’d have the option of merging this fork with the original repo

