"""
predict a number of samples with a pretrained model
1. to predict a given number of batches, using batch_iterator
2. to predict a full dataset array, using a full dataset array
"""

# access test_batches iterator, val_batches iterator
from vgg16_02_from_img_directory_2_iterators import test_batches, val_batches
from vgg16_02_array_from_batches_from_folder import test_img_array, train_img_array

#############################################
# load a pretrained model
from tensorflow.contrib.keras.python.keras.models import load_model

trained_model_path = "/Users/Natsume/Downloads/data_for_all/dogscats/results"
vgg16_ft_epoch3 = load_model(trained_model_path+'/train_vgg16_again_model_3.h5')
# this model modified and trained on dogs and cats


#############################################
# predict_generator:
# 1. generate 3 batches of predictions
# 2. regardless whether 3 batches > an epoch or 3 batches > full_dataset or not
# 2. all batches of predictions will be row-bind, then return as output
preds_test_3_batches = vgg16_ft_epoch3.predict_generator(generator=test_batches,
								steps=3, # predict for 3 batches even though one epoch is less than 2 epochs
								max_q_size=10,
								workers=1,
								pickle_safe=False,
								verbose=2
								)

#############################################
# predict:
# 1. generate (full_num_samples/batch_size) num of batches of predictions
# 2. num_batches * batch_size + final_batch_samples == full number of samples
# 2. all batches of predictions will be row-bind, then return as output
preds_test_full = vgg16_ft_epoch3.predict(test_img_array, verbose=2)

preds_train_full = vgg16_ft_epoch3.predict(train_img_array, verbose=2)
preds_train_full.shape

#############################################
# save large arrays using bcolz
from save_load_large_array import bz_save_array, bz_load_array

bz_save_array(trained_model_path+"/preds_test", preds_test_full)
bz_save_array(trained_model_path+"/preds_train", preds_train_full)
preds_test = bz_load_array(trained_model_path+"/preds_test")

#####################################
# steps = 1 and steps =3 make a differece to predict_generator?
