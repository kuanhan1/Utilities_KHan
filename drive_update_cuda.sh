mkdir tempfolder
cd tempfolder
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run
chmod +x cuda_9.0.176_384.81_linux-run
# ./cuda_9.0.176_384.81_linux-run --extract=$HOME
sudo ./cuda_9.0.176_384.81_linux-run
sudo bash -c "echo /usr/local/cuda/lib64/ > /etc/ld.so.conf.d/cuda.conf"
sudo ldconfig
cd ..
rm -r tempfolder
