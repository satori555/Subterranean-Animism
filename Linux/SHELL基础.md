# SHELL

Bash是大多数Linux系统默认的shell：

```bash
#!/bin/bash
echo "Hello World!"
```

第一行 `#!` 是一个约定的标记，告诉系统这个脚本需要什么解释器来执行，然后 `./test.sh` 来执行。

也可以用 `bash test.sh` 执行，这种方式不需要在第一行指定解释器信息，写了也没用。



变量：变量名和等号之间不能有空格。使用的时候在前面加一个 `$` 符号。也可以再加一个花括号，告诉解释器变量的边界。



### 各种括号的作用

1. 单小括号 ()

   可以用来初始化数组，如 `array=(a b c d)` 

2. 双小括号 (())

   可以在双括号里使用C语言的语法，比如

   ```bash
   #for循环
   for((i=0;i<5;i++))
   for i in `seq 0 4`  
   for i in {0..4}
   #if判断
   if (($i<5))
   if [ $i -lt 5 ]
   ```

3. 单中括号 []
4. 双中括号 [[]]
5. 大括号 {}



参考：

1. shell中各种括号的作用()、(())、[]、[[]]、{}_乌托邦-CSDN博客
   https://blog.csdn.net/taiyang1987912/article/details/39551385

2. Shell 教程 | 菜鸟教程
   https://www.runoob.com/linux/linux-shell.html