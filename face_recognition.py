from deepface import DeepFace
import os


def face_recognition(src, dataset_path: str = "./data", threshhold: float = 0.4):
    """
    Args:
        src : 路径或者是numpy数组格式的图片(BGR顺序). 我建议用numpy数组, 以免将数据写入磁盘, 效率比较低.
        dataset_path (str): 存放已知身份的人脸的目录, 目录中图片的命名为{id}_{index}.[jpg|jpeg|png]
        threshhold : 用余弦距离来计算向量之间的距离, 范围是[0,1), 越接近0越好, 大于等于阈值会被判断为陌生人

    Return Vlue:
        bool: 是否识别成功
        identity: 用户id
    """
    result = DeepFace.find(src, dataset_path)
    target = result[0].iloc[0]
    identity = os.path.basename(target['identity']).split("_")[0]
    cosine_distance = target['VGG-Face_cosine']
    if cosine_distance <= threshhold:
        return True, identity
    else:
        return False, None


if __name__ == "__main__":
    src_img = "./17.jpg"
    dataset_path = "./data"
    res = face_recognition(src_img, dataset_path)
    print(res)
