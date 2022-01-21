
import tensorflow.compat.v1 as tf
import cv2 as cv

tf.disable_v2_behavior()


def run_model(graph_def, inp) -> tf.Session():
    with tf.Session() as sess:
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')
        out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                        sess.graph.get_tensor_by_name('detection_scores:0'),
                        sess.graph.get_tensor_by_name('detection_boxes:0'),
                        sess.graph.get_tensor_by_name('detection_classes:0')],
                       feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})
    return out


def visualize(out, cols, rows, img) -> None:
    persons = 1
    num_detections = int(out[0][0])
    for i in range(num_detections):
        score = float(out[1][0][i])
        bbox = [float(v) for v in out[2][0][i]]
        if score > 0.3:
            x = bbox[1] * cols
            y = bbox[0] * rows
            right = bbox[3] * cols
            bottom = bbox[2] * rows
            cv.rectangle(img, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)
            persons += 1
    cv.putText(img, f'Ilosc osob : {persons - 1}', (300, 25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255),
               2)


class DetectorAPI:

    def __init__(self, model_path: str, image_path: str) -> None:
        self._model_path = model_path
        self._image_path = image_path

    def __str__(self) -> None:
        return "Ścieżka do modelu:{}\nŚcieżka do zdjęcia:{}".format(self._model_path, self._image_path)

    @property
    def model_path(self) -> str:
        return self._model_path

    @model_path.setter
    def model_path(self, value: str) -> None:
        self._model_path = value

    @property
    def image_path(self) -> str:
        return self._image_path

    @image_path.setter
    def image_path(self, value: str) -> None:
        self._image_path = value

    def read_graph(self) -> str:
        graph_def = None
        with tf.gfile.FastGFile(
                self._model_path,
                'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
        return graph_def

    def read_and_preprocess_image(self) -> tuple():
        img = cv.imread(self._image_path)
        rows = img.shape[0]
        cols = img.shape[1]
        inp = cv.resize(img, (300, 300))
        inp = inp[:, :, [2, 1, 0]]
        return cols, rows, inp, img
