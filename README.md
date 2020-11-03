# my_randlanet
copy from git@github.com:QingyongHu/RandLA-Net.git with some change for private using

(1) Setup
This code has been tested with Python 3.5, Tensorflow 1.11, CUDA 9.0 and cuDNN 7.4.1 on Ubuntu 16.04.

Clone the repository
git clone --depth=1 https://github.com/QingyongHu/RandLA-Net && cd RandLA-Net
Setup python environment
conda create -n randlanet python=3.5
source activate randlanet
pip install -r helper_requirements.txt
sh compile_op.sh
Update 03/21/2020, pre-trained models and results are available now. You can download the pre-trained models and results here. Note that, please specify the model path in the main function (e.g., main_S3DIS.py) if you want to use the pre-trained model and have a quick try of our RandLA-Net.

(2) S3DIS
S3DIS dataset can be found here. Download the files named "Stanford3dDataset_v1.2_Aligned_Version.zip". Uncompress the folder and move it to /data/S3DIS.

Preparing the dataset:
python utils/data_prepare_s3dis.py
Start 6-fold cross validation:
sh jobs_6_fold_cv_s3dis.sh
Move all the generated results (*.ply) in /test folder to /data/S3DIS/results, calculate the final mean IoU results:
python utils/6_fold_cv.py

(3) Semantic3D
7zip is required to uncompress the raw data in this dataset, to install p7zip:

sudo apt-get install p7zip-full
Download and extract the dataset. First, please specify the path of the dataset by changing the BASE_DIR in "download_semantic3d.sh"
sh utils/download_semantic3d.sh
Preparing the dataset:
python utils/data_prepare_semantic3d.py
Start training:
python main_Semantic3D.py --mode train --gpu 0
Evaluation:
python main_Semantic3D.py --mode test --gpu 0