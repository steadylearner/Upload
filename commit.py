import subprocess as cmd
# from termcolor import colored

# Then, you can install all the dependencies used for this project with
# $pip install -r requirements.txt

cp = cmd.run("git add .", check=True, shell=True)

response = input("Do you want to use the default message for this commit?([y]/n)\n")
message = "update the repository"

if response.startswith('n'):
    message = input("What message you want?\n")

cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)

# Search how to skip login process for github push
# $git remote add origin git@github.com:steadylearner/Python-Blog.git
# or $git remote set-url origin git@github.com:steadylearner/Python-Blog.git
# https://help.github.com/en/articles/connecting-to-github-with-ssh
# https://github.com/settings/keys
cp = cmd.run("git push -u origin master -f", check=True, shell=True)

