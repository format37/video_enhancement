
# FROM pytorch/manylinux-cuda117
# FROM huggingface/transformers-pytorch-gpu:4.21.1
FROM huggingface/transformers-pytorch-gpu
# FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04
WORKDIR /app

RUN pip3 install --upgrade pip
RUN apt-get update -y
RUN apt-get install wget -y

COPY upscaler_files.tar.xz /app
RUN tar -xf upscaler_files.tar.xz
RUN wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P experiments/pretrained_models
RUN wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-animevideov3.pth -P experiments/pretrained_models
RUN pip3 install basicsr &\
    pip3 install facexlib &\
    pip3 install gfpgan
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 setup.py develop

COPY sample.sh /app
# copy service/ to app
COPY service /app/service
COPY video2images.py /app
COPY images2video.py /app
COPY inference_realesrgan.py /app
COPY inference_realesrgan_video.py /app
COPY loop.py /app
# COPY server.py /app
ENTRYPOINT ["python3"]
# CMD ["inference_realesrgan.py"]
CMD ["loop.py"]