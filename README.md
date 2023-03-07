# EPI-HAN ( Identification of Enhancer Promoter Interaction using Hierarchical Attention Network)
Enhancer-Promoter Interaction (EPI) recognition is crucial for understanding human development. In transcriptional regulation, EPI in the genome plays a significant role. In genome-wide association studies (GWAS), EPIs can help enhance statistical strength and improve the mechanistic understanding of disease- or trait-associated genetic variants. However, in terms of time, effort, and resources, experimental methods to classify EPIs cost too much. Therefore, increasing research efforts are focusing on the development of computational methods that use deep learning and other machine learning methods to solve these problems. Unfortunately, one of the main challenges when dealing with EPI prediction is the long sequences of the enhancers and promoters, and most existing computational approaches suffer from this problem.

To address the above challenge, this paper proposes a Hierarchical Attention Network for EPI detection, which is called EPI-HAN. The proposed model has two distinct features: (i) the hierarchy structure captures the hierarchy structure of the enhancer/promoter sequence; (ii) The model has two layers of attention mechanisms that operate at the level of individual tokens and smaller sequences, allowing it to selectively focus on important features when creating the overall representation of the sequence. On some cell lines, benchmarking comparisons reveal that EPI-HAN is doing better than state-of-the-art methods.

# File Description 
- Data_Augmentation.R

  A tool of data augmentation provided by Mao et al. (2017). The details of the tool can be seen in https://github.com/wgmao/EPIANN.

  We used this tool to amplify the positive samples in the training set to 20 times to achieve class balance.
  
  - sequence_processing.py

  Perform pre-processing of DNA sequences:

  1.	Convert the enhancer and promoter gene sequences into sequences consisting of words (6-mers), and if a word contains a ‘N’, the word is marked as ‘NULL’.
  2.	Construct a dictionary containing 4^6+1 words.
  3.	Convert each gene sequence into a sequence of word indexes according to the dictionary (each word has its own unique in-dex).
 
- embedding_matrix.npy

  The weight of the embedding layer converted from the pre-trained DNA vector provided by Ng (2017).

- train.py

  Perform model training.

  You can find the weight of the model mentioned in our paper under the directory model/.
  
  
  Directory| Content
  ---|---
  model/specificModel/| the weight of EPIVAN-specific on each cell line.
  model/generalModel/| the weight of EPIVAN-general.
  model/retrainModel/| the weight of EPIVAN-best on each cell line.
  model/transferModel/| the weight of EPIVAN-general transferred to the new cell line.


- test.py

  Evaluate the performance of model.
  



References:

  Mao, W. et al. (2017) Modeling Enhancer-Promoter Interactions with Attention-Based Neural Networks. bioRxiv, 219667.

  Ng, P. (2017) dna2vec: Consistent vector representations of variable-length k-mers. arXiv:1701.06279.
