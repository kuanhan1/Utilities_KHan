echo -n "Enter email address: " 
read email_add
ssh-keygen -t rsa -b 4096 -C "$email_add"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
# Downloads and installs xclip. If you don't have `apt-get`, you might need to use another installer (like `yum`)
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub
echo "The contents of the id_rsa.pub file have been copied to your clipboard"
echo "Go to Github => Profile => Settings => SSH and GPG keys =>  New SSH key/Add SSH key => Paste"

