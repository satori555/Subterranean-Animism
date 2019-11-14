## tensorflow教程

p9 5 例子2

```python
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 1维，范围从-1到1
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
### create tensorflow structure end ###

sess = tf.Session()
sess.run(init)  # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
```

p10 6 Session会话控制

```python
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])

product = tf.matmul(matrix1, matrix2)  # matrix multiply 类似np.dot(m1, m2)

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
```

p11 7 Variable变量

```python
import tensorflow as tf

state = tf.Variable(0, name='counter')
print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# init = tf.initialize_all_variables()  
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
```

8 placeholder传入值

```python
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.0]}))
```

