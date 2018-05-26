#  AerialClassifier

Implementation of CNN using Keras for a ImageClassifier. We use a similar model as the one exposed by Yann Le Cun. A triple stack of Conv + MaxPool layers, a Flatten layer previous to the Dense (64) layer, a Dropout of 50% and a final Dense layer with a Softmax function at the end. Conv layers use ReLu activaction functions and we use the last version of the Adam optimizer.

## How does it work?

The idea is to use pre-classified images to train a Convolutional Neural Network (CNN) in order to classify later images.
### Prerequisites

In order to run the project you need:

```
- Python 2.7 or 3.5
- Tensorflow
- Keras
```
