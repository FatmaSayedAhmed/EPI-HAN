# EPI-HAN ( Identification of Enhancer Promoter Interaction using Hierarchical Attention Network)
Enhancer-Promoter Interaction (EPI) recognition is crucial for understanding human development. In transcriptional regulation, EPI in the genome plays a significant role. In genome-wide association studies (GWAS), EPIs can help enhance statistical strength and improve the mechanistic understanding of disease- or trait-associated genetic variants. However, in terms of time, effort, and resources, experimental methods to classify EPIs cost too much. Therefore, increasing research efforts are focusing on the development of computational methods that use deep learning and other machine learning methods to solve these problems. Unfortunately, one of the main challenges when dealing with EPI prediction is the long sequences of the enhancers and promoters, and most existing computational approaches suffer from this problem.

To address the above challenge, this paper proposes a Hierarchical Attention Network for EPI detection, which is called EPI-HAN. The proposed model has two distinct features: (i) the hierarchy structure captures the hierarchy structure of the enhancer/promoter sequence; (ii) The model has two layers of attention mechanisms that operate at the level of individual tokens and smaller sequences, allowing it to selectively focus on important features when creating the overall representation of the sequence. On some cell lines, benchmarking comparisons reveal that EPI-HAN is doing better than state-of-the-art methods.

# File Description 
- Data_Augmentation.R

  A tool of data augmentation provided by Mao et al. (2017). The details of the tool can be seen in https://github.com/wgmao/EPIANN.

  To amplify the positive samples in the training set to 20 times to achieve class balance, we used this tool.
  
- fasta2oneHot.py

  Perform pre-processing of DNA sequences:
  1. convert the enhancer and promoter sequences into one-hot vectors by using this oneHot Map:
     A -> [1,0,0,0]
     T -> [0,1,0,0]
     C -> [0,0,1,0]
     G -> [0,0,0,1]
  2. save the one-hot embeddings into .npy files

- dna2vec_sequence_processing.py

  Perform pre-processing of DNA sequences:

  1. Convert the enhancer and promoter gene sequences into sequences consisting of words (6-mers), and if a word contains a ‘N’, the word is marked as ‘NULL’.
  2. Construct a dictionary containing 4^6+1 words.
  3. Convert each gene sequence into a sequence of word indexes according to the dictionary (each word has its own unique index).
  4. save the dna2vec embeddings into .npz files
  
- embedding_matrix.npy

  The weight of the embedding layer converted from the pre-trained DNA vector provided by Ng (2017).

- model.py

    It contains the implementation of our proposed model

- layers.py

    It contains custom layer implementation for self-attention mechanisms in TensorFlow

- train_dna2vec.py

  Perform model training with using the dna2vec embedding

- train_OneHot.py

    Perform model training with using the one-hot embedding

- train_dna2vec_oneHot.py

  Perform model training with using the combination between dna-vec and one-hot embeddings

- test.py

  Evaluate the performance of model.
  
You can find the weight of the model mentioned in our paper under the directory ./model

Directory| Content
  ---|---
  model/EPI-HAN_dna2vec_SelfSoftAttention/| the weight of EPI-HAN with using the dna2vec embedding on each cell line.
  model/EPI-HAN_OneHot_SelfSoftAttention/ | the weight of EPI-HAN with using the one-hot embedding on each cell line.
  model/EPI-HAN_dna2vec_OneHot_SelfSoftAttention/| the weight of EPI-HAN with using the combination between the dna2vec and one-hot embedding on each cell line.

References:

  Mao, W. et al. (2017) Modeling Enhancer-Promoter Interactions with Attention-Based Neural Networks. bioRxiv, 219667.

  Ng, P. (2017) dna2vec: Consistent vector representations of variable-length k-mers. arXiv:1701.06279.
