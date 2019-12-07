# given a location to model and image
# look_for_birds() ... looks for birds


import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image


# model is the path to an h5 file
# image is the path to a jpg file

def look(model, img):

    model = load_model(model)
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    img = image.load_img(img, target_size = (150, 150))
    img = image.img_to_array(img)
    img = img*(1./256)  # rescale
    img = np.expand_dims(img, axis = 0)

    # confident_bird is a percent likelyness of bird
    confident_bird = model.predict(img, batch_size = 1)[0][0]
    
    # 0 for bird, 1 for no bird
    if confident_bird < 0.1:
        return 'Bird spotted!'
    elif confident_bird < 0.4:
        return 'hmmm, maybe a bird.'
    elif confident_bird < 0.6:
        return 'I need my glasses.'
    elif confident_bird < 0.9:
        return 'I dont see any birds.'
    else:
        return 'No birds for sure!'
