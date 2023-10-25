# 环境安装

```bash
conda create --name face_recognition python=3.8.10
conda activate face_recognition
python -m pip install deepface
python -m pip install --upgrade numpy
```

# 预训练模型下载

在[Release pre-trained-weights · serengil/deepface_models (github.com)](https://github.com/serengil/deepface_models/releases/tag/v1.0)手动下载[vgg_face_weights.h5](https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5)到~/.deepface/weights/目录下，因为正常情况下github下载大文件会中途失败。