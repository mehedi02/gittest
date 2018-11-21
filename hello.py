import tensorflow as tf
a = tf.placeholder(tf.float32, shape=(1,))
b = tf.placeholder(tf.float32, shape=(1,))
c = a + b

with tf.Session() as sess:
	c_eval = sess.run(c, {a:[1.], b:[2.]})
	print(c_eval)



