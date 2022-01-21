from DetectorAPI import DetectorAPI, run_model, visualize, cv


def image_build() -> None:
    api = DetectorAPI(
        r'C:/Users/patry/PycharmProjects/person_detector/config/frozen_inference_graph.pb',
        r'C:/Users/patry/Downloads/test_3.jpg')
    graph = api.read_graph()
    cols, rows, inp, img = api.read_and_preprocess_image()
    out = run_model(graph, inp)
    visualize(out, cols, rows, img)
    cv.imshow('image', img)
    cv.waitKey()
    cv.destroyAllWindows()
