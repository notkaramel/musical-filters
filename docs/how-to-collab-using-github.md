# How to collaborate using GitHub
> Citation: Improved upon @notkaramel's guide in January 2023 during [ECSE 223](https://github.com/notkaramel/ECSE223-SnowShoeTours) and [ECSE 321 - Developer Guide](https://github.com/notkaramel/ECSE321-Mar1HotelSystem/wiki/0.-Developer-Guide#2-git-branches)


## Command-line nagivation basics

### File navigation
- Usually your current folder will be shown on the same line to the left (or a line above) of your cursor. Else, you can check with
```sh
pwd
```

- To list all files & folders in your current location, use `ls`. Other flags might apply such as:
```sh
ls	# to list all files & folders
ls -a	# to list all files & folders (includes hidden ones)
ls -l 	# to list files and folders with their permission on your machine.
```

- To change directory, use `cd`. Examples:
```sh
cd Desktop/ecse223-project	# To access ecse223-project that you put on the Desktop
cd ..		# To go to the parent folder of your current location
cd		# To go to your home folder (Linux & MacOS tested, not sure how Windows would work)
```

- Check if prerequisite programs available on your machine:
```sh
git -v
python --version
```
## Git basics
### Common commands for Git

```bash
# Check the status of the repository.
# Attention to your current branch and files you modified/added.
# Attention to whether your branch is behind/ahead of the remote (GitHub repo) branch, often `origin/<branch>`.
git status

# Update the repository from remote repository
git pull

# Add all changes to the staging area
git add .  # or
git add -A
# Add a specific file to the staging area 
git add <file>

# Commit the changes in the staging area
git commit -m "Commit message"

# Push the changes to the remote repository
git push
```

### Checkout to your own branch
```bash
# Create a new branch & "checkout" to it
git checkout -b branch-name # replace branch-name with your own branch name

# For example:
git checkout -b emma
```
- ❗It is recommended to name a working branch based on the feature you are working on and/or with your name (optional, tho). For example, if you are working on "feature A" and your name is Antoine, a *good* branch name would be `feature-a-antoine` or `antoine-feature-a``, or `feature-a` is acceptable. A branch name like `antoine` or `antoine-2` is objectively *bad*. Be descriptive!

### Switch/Checkout to an *exisiting* branch
```bash
git checkout <branch name>	# or
git switch <branch name>

# For example
git checkout main	# switch to main branch
git checkout emma	# switch to branch named "emma"
```

### Merging branches & Resolving Conflicts (might use `Vim` editor)
- Cases where you want to merge branch **in this project specifically** are:
	1. You want to get updates from `common-base` branch to the `main` branch.
	2. You want to get updates from the `main` branch to your own working branch.
	3. (Please do Pull Request on GitHub instead) You want to apply your changes from your own branch to the GitHub repository. E.g., you merge your branch `emma` to the `development` branch.
- And please do not merge anything into `common-base` branch
- How to:

```sh
# Switch to your target branch
git checkout <your-target-branch>

# Merge to your target branch from your reference branch
git merge <your-reference-branch>
```

- At this step, you may encounter a pop-up window asking you to write/edit a merge message, and it will be [by default] use a text editor called VIM. If you know how to use VIM, amazing! Else, no need to worry. The message has already written for you by default. All you have to do is type the following sequence: (see the lower left corner of your terminal window)
```
:wq
```
- Merge conflicts may occurs. In this case, it's recommended that you resolves conflicts on editor such as VSCode, by either choosing to keep the current changes or apply the incoming changes to your branch.

> There are more to merging branches than this (`fast-forward`, `rebase`, `squash`, etc.). Here's a link to a [very good guide](https://www.atlassian.com/git/tutorials/using-branches/git-merge) IMO, but feel free to experiment with other git functionalities.



