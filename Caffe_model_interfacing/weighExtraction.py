import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe

caffe.set_mode_cpu()

#net = caffe.Net('conv.prototxt', caffe.TEST)
net = caffe.Net('/home/hafx/VV/adil/deploy.prototxt',
                '/home/hafx/VV/adil/snapshot_iter_21120.caffemodel',
                caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load('/home/hafx/VV/adil/test.npy').mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
#transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)

net.blobs['data'].reshape(1,1,28,28)

im = caffe.io.load_image('/home/hafx/VV/adil/test.png',0)


net.blobs['data'].data[...] = transformer.preprocess('data', im)
out = net.forward()
"""
print "Input Data"
print "Shpae ",net.blobs['data'].data.shape
data =  net.blobs['data'].data[0,0,:,:]
#print data
for i in range(np.shape(data)[0]):
	print data[i]
	

print "Scale Data"
print "Shpae ",net.blobs['scale'].data.shape
data =  net.blobs['scale'].data[0,0,:,:]
#print data
for i in range(np.shape(data)[0]):
	print data[i]


print "conv1 Data "
print "Shape ",net.blobs['conv1'].data.shape
for i in range(0,20):
	print i+1,"th activation map"
	data = net.blobs['conv1'].data[0][i]
	for i in range(24):
		print data[i]

print "conv1 Coefficients"
print "Shape ",net.params['conv1'][0].data.shape
for i in range(0,20):
	print "Filter ", i + 1
	data =  net.params['conv1'][0].data[i][0]
	for i in range(5):
		print data[i]



print "conv1 Bais"
print "Shape ",net.params['conv1'][1].data.shape
for i in range(0,20):
	print "Bais ", i + 1
	data =  net.params['conv1'][1].data[i]
	print data

print "Pool1 Data"
print "Shape ", net.blobs["pool1"].data.shape
for i in range(0,20):
	print i+1,"th pool map"
	data = net.blobs['pool1'].data[0][i]
	for i in range(12):
		print data[0]
"""	
exit(0)

	

#print "ip2"
#print net.blobs['ip2'].data



#print "bias convs1"

#print "Shape ",net.params['conv1'][0].data.shape
#print "Coefficients"
#for i in range(0,20):
#	print "Coefficient matrix ", i + 1
#	print net.params['conv1'][0].data[i]

#print net.params['conv1'][1].data
#print "bias conv2"
#print net.params['conv2'][1].data

print "#####################################################"
#print "Coefficients"
"""
for i in range(0,50):
	print "Coefficient convolutin 2 matrix ", i + 1
	print net.params['conv2'][0].data[i]
"""
"""

print "Activation map values of conv2"
for i in range(0,50):
	print i+1,"th  activation map"
	print net.blobs['conv2'].data[0][i]
"""

print "Conv2 bias"
#for i in range(0,50):
#	print "Bias convolutin 2 matrix ", i + 1
print net.params['conv2'][1].data


