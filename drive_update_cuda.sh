mkdir tempfolder
cd tempfolder
cudaverison=cuda_10.1.243_418.87.00_linux.run
wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/$cudaverison
chmod +x $cudaverison
sudo sh ./$cudaverison
sudo bash -c "echo /usr/local/cuda/lib64/ > /etc/ld.so.conf.d/cuda.conf"
sudo ldconfig
cd ..
rm -r tempfolder
