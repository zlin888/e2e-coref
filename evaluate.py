#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
import coref_model as cm
import util
import time

if __name__ == "__main__":
  config = util.initialize_from_env()
  model = cm.CorefModel(config)
  while True:
    try:
      with tf.Session(config=util.gpu_config()) as session:
        model.restore(session)
        model.evaluate(session, official_stdout=True)
    except tf.errors.ResourceExhaustedError:
        print("OOM")
        time.sleep(3)
        continue
    break
