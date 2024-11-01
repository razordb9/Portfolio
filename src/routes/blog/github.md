---
title: Important GitHub commands
date: '2024-01-01'
subtext: 'This would be my approche for creating a web design business'
publisher: 'Thomas Hudson-Zaußnig'
image: ''
categories: 
    - business
    - webdesign
---

# GIT

## Commands may needed
| Command | Description |
| :---------------------- | :---------------------- |
|git branch | listing of all repository on the brank|
|git branch feature | creates new branch, feature is the branch name|
|git checkout feature | switch to different branch, feature is the branch name|
|git branch -d <branchname># | delete branch|
|git commit -am "commit message" | combines git add and git commit in one line changes on another branch or only in the other branch and not in the master branch |
|git merge branchname | I wanto to merge into the master branch |
|git push --set-upstream origin feature |
|git fetch | takes the commits from the origin (remote e.g. GitHub) and downloads them locally
|git merge origin/master |
|git pull | git pull is a compination of git fetch + git merge origin/master|
|git config --global user.name "example" | set global user|
|git config --global user.email "example@abc.com" | set global email address|
|git config --global --list | list global config|
|git init| initialize git|
|git clone https://github.com/razordb9/lacture0.git | clone a repository from github 
Repository | storage place where you store the projects|
|git log | log of all commits done |
|git reset --hard <commit> | reset whole repository|
|git reset --hard origin/master | reset git project|
|git reset --hard hash of commit seen in git log | don't know|
|git add <filename> | include file next time i save a repository|
|git commit | take a snapshot of the repository at the current moment and save it |
|git commit -m "message" | what happens in any change of saves|
|git status | tells you whats currently going on in the repository|
|git push | upload your repository to github|
|git pull | download the latest version of repository from github|
|git pull origin master | update local repository with remote repository|




github page -> settings in the repository -> scroll down to github pages and enable sourc master branch


touch hallo.html -> create empty html file


git merge conflict looks like:
```
<<<<<<< HEAD
    <h1>Test test2 test3</h1>
=======
    <h1>Test Test2 TEst3 Test4</h1>
>>>>>>> 9cbba984781e551466d8f8e3745c21a947300fdc
```

