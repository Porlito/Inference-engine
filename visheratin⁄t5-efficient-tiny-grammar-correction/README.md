---
language: 
  - en
tags:
- grammar-correction
license: mit
datasets:
- c4_200m
---

# T5-Efficient-TINY for grammar correction

This is a [T5-Efficient-TINY](https://huggingface.co/google/t5-efficient-tiny) model that was trained on a subset of [C4_200M](https://ai.googleblog.com/2021/08/the-c4200m-synthetic-dataset-for.html) dataset to solve the grammar correction task in English. To bring additional errors, random typos were introduced to the input sentences using the [nlpaug](https://github.com/makcedward/nlpaug) library. Since the model was trained on only one task, there are no prefixes needed.

The model was trained as a part of the project during the [Full Stack Deep Learning](https://fullstackdeeplearning.com/course/2022/) course. ONNX version of the model is deployed on the [site](https://edge-ai.vercel.app/models/grammar-check) and can be run directly in the browser.