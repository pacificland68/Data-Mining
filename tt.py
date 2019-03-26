from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec1 = np.array([[1,1,0,1,1]])
vec2 = np.array([[0,1,0,1,1]])
#print(cosine_similarity([vec1, vec2]))
print(cosine_similarity(vec1, vec2))