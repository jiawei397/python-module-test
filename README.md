## python ##

### 常用命令 ###

  python -m -pip install XX

使用pip的时候在后面加上-i参数，指定pip的下载源

  pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

上面命令每次运行需要指定网址，可进行永久修改：

windows下: 在user目录中创建一个pip目录，如：C:\Users（用户）\xx\pip，新建文件pip.ini，内容如下

  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple

linux下: 修改 ~/.pip/pip.conf （如果没有自己创建一个）， 内容如下：

  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple

参考：https://blog.csdn.net/yamadeee/article/details/80178996

## 安装模块 ##

    python setup.py build
    python setup.py sdist

    python -m pip install twine
    $ https://pypi.org/manage/projects/

可以配置到$HOME/.pypirc文件中，就不用多次输入了

    [pypi]
    username = <username>
    password = <password>


再使用twine发布到服务器：

    twine upload dist/*
