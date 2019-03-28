import tensorflow as tf

x = tf.placeholder(tf.float32,shape=(None,2))
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print "the result of tf3 is:\n",sess.run(y,feed_dict={x:[[0.1,0.2],[0.2,0.3],[0.3,0.4],[0.4,0.5]]})
	print "w1:\n",sess.run(w1)
	print "w2:\n",sess.run(w2)
