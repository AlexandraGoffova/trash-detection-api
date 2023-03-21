import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  'ssd_mobilenet_v2_taco_2018_03_29.pb', 'image_tensor', ['num_detections', 'detection_boxes', 'MultipleGridAnchorGenerator/assert_equal/Assert/Assert', 'detection_scores', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/MultiClassNonMaxSuppression/SortByField_1/Assert/Assert', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/MultiClassNonMaxSuppression/SortByField/Assert/Assert', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/Switch', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/Switch_1', 'Preprocessor/map/while/Switch_1', 'Preprocessor/map/while/Switch', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/MultiClassNonMaxSuppression/SortByField_1/TopKV2', 'Postprocessor/BatchMultiClassNonMaxSuppression/map/while/MultiClassNonMaxSuppression/SortByField/TopKV2', 'detection_classes'])
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)