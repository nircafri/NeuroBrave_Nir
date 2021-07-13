# Pseudo-code
from deepexplain.tensorflow import DeepExplain

# Option 1. Create and train your model within a DeepExplain context

with DeepExplain(session=...) as de:  # < enter DeepExplain context
    model = init_model()  # < construct the model
    model.fit()           # < train the model

    attributions = de.explain(...)  # < compute attributions

# Option 2. First create and train your model, then apply DeepExplain.
# IMPORTANT: in order to work correctly, the graph to analyze
# must always be (re)constructed within the context!

model = init_model()  # < construct the model
model.fit()           # < train the model

with DeepExplain(session=...) as de:  # < enter DeepExplain context
    new_model = init_model()  # < assumes init_model() returns a *new* model with the weights of `model`
    attributions = de.explain(...)  # < compute attributions