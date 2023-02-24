

import os
os.environ["CUDA_VISIBLE_DEVICES"]="5"
kernal_size = 4
num_filters = 20
muti_layer_Conv_filters = [20, 40, 60, 80]

# num_conv_layers = 4
# pool_size = 4
# strides = 1
# kernal_size = 10
type = "VAN_OneHot_withConv40Only"
from model import get_model
import numpy as np
from sklearn.metrics import roc_auc_score,average_precision_score, f1_score, precision_score, recall_score, confusion_matrix
import tensorflow as tf
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

# config = ConfigProto()
# config.gpu_options.allow_growth = True
# session = InteractiveSession(config=config)


model_dir = "./model/specificModel"

models=['GM12878', 'HUVEC', 'HeLa-S3', 'IMR90', 'K562', 'NHEK']
m=models[0]
model=None
model=get_model()
model.load_weights(model_dir + "/GM12878Model14.h5")

cell_line = 'GM12878'

print("\nrun test\n")
data_path_test='./data/%s/test/'%cell_line

print('Loading test ' + cell_line + ' data from ' + data_path_test)
X_enhancers_test = np.load(data_path_test + cell_line + '_enhancers_test.npy')
X_promoters_test = np.load(data_path_test + cell_line + '_promoters_test.npy')
labels_test = np.load(data_path_test + cell_line + '_labels_test.npy')

print("****************Testing %s cell line specific model on %s cell line****************" % (cell_line, cell_line))
y_pred = model.predict([X_enhancers_test, X_promoters_test], batch_size=50, verbose=1)

auc = roc_auc_score(labels_test, y_pred)
print("AUC : ", auc)
aupr = average_precision_score(labels_test, y_pred)
print("AUPR : ", aupr)

# c_mat = confusion_matrix(labels_test, y_pred)
# # sn = c_mat[1, 1] / np.sum(c_mat[1, :])  # 预测正确的正样本
# # sp = c_mat[0, 0] / np.sum(c_mat[0, :])  # 预测正确的负样本
# pr = c_mat[1,1] / (c_mat[1,1] + c_mat[0,1])  # TP / TP + FP
# re = c_mat[1,1] / (c_mat[1,1] + c_mat[1,0])  # TP / TP + FN
# f1 = (2 * pr * re) / (pr + re)  # f1-score for binary classification
# print("F1_Score: ", f1)
