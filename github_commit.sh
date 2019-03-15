echo -n "Enter your commit messasge: " 
read commit_message

git pull origin master
git status
git add .
git add --all
git commit -m "$commit_message"
git push origin

