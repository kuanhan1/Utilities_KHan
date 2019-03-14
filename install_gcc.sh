# Instructions for installing GCC 4.9 on various platforms.
# The commands show instructions for GCC 4.9, but any higher version will also work!
# Ubuntu (https://askubuntu.com/questions/466651/how-do-i-use-the-latest-gcc-on-ubuntu/581497#581497)
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-5 g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5
