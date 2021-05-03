# %%
import os
from sklearn.metrics import plot_confusion_matrix
from sklearn.mixture import GaussianMixture
BIRDS = os.listdir("./train_short_audio")


# %%
# returns mfcc matrinx from given recording as numpy array
def process(Recording):
    pass


# %%
# returns recording as numpy array
def readRecording(path):
    pass


# %%
models = {}
for bird in BIRDS:
    model = GaussianMixture()
    for path in PATH_LIST_FOR_EACH_BIRD:
        recording = readRecording(path)
        mfcc = process(recording)
        model.fit(mfcc)
    models[bird] = model

# %%
