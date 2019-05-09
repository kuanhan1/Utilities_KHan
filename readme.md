# Utilities to set up environment and connections

- GCC when source-compiling a Pytorch
    - **gcc_dislink_previous_version.sh** uninstall a previously installed version (higher version)
    - **gcc_install.sh** install another version (typically an old version to be comatible with Pytorch)
- Connection-setup, commit and pull for Github.
    - **github_generate_ssh_key.sh** When first use github, setting up the environment.
    - **github_commit.sh** Naive way to do git-commit.
    - **github_pull_and_overwrite.sh** Naive way to pull a repository and overwrite the local one.

# When some abnormal things happen:

- Installing nvidia-driver
    - **driver_update_nvidia.sh** When $nvidia-smi gives the following log: NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
    - **driver_update_cuda.sh** Install CUDA
