mkdir tempfolder
cd tempfolder
wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run
chmod +x cuda_9.0.176_384.81_linux-run
sudo sh ./cuda_9.0.176_384.81_linux.run
sudo bash -c "echo /usr/local/cuda/lib64/ > /etc/ld.so.conf.d/cuda.conf"
sudo ldconfig
cd ..
rm -r tempfolder
