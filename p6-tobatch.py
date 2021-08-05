import math
import numpy as np

#thisis p6-1 np implementation

layer_outputs = [[4.8, 1.21,2.385],
                [8.9 ,-1.81,0.2],
                [1.41,1.051,0.026]]



exp_values = np.exp(layer_outputs)

print(np.sum(layer_outputs, axis=1,keepdims=True))#suma wierszy; 0 byłoby sumą kolumn, a bez arg/arg=None byłby to zwykly skalar

#keepdims makes matrix the same dimentions as input matrix

# norm_values = exp_values / np.sum(exp_values)

# print(norm_values)
# print(sum(norm_values))