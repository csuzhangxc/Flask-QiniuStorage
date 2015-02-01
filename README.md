# Flask-QiniuStorage
[七牛云存储](http://www.qiniu.com/)Flask扩展，Qiniu Storage for Flask

## 安装
```python
pip install Flask-QiniuStorage
```

## 配置
| 配置项 | 说明 |
|:--------------------:|:---------------------------:|
| QINIU_ACCESS_KEY | 七牛 Access Key |
| QINIU_SECRET_KEY | 七牛 Secret Key |
| QINIU_BUCKET_NAME | 七牛空间名称 |
| QINIU_BUCKET_DOMAIN | 七牛空间对应域名 |

## 使用
```python
from flask import Flask
from flask_qiniustorage import Qiniu

QINIU_ACCESS_KEY = '七牛 Access Key'
QINIU_SECRET_KEY = '七牛 Secret Key'
QINIU_BUCKET_NAME = '七牛空间名称'
QINIU_BUCKET_DOMAIN = '七牛空间对应域名'

app = Flask(__name__)
app.config.from_object(__name__)
qiniu_store = Qiniu(app)
# 或者
# qiniu_store = Qiniu()
# qiniu_store.init_app(app)

# 保存文件到七牛
@app.route('/save')
def save():
    data = 'data to save'
    filename = 'filename'
    ret, info = qiniu_store.save(data, filename)
    return str(ret)

# 删除七牛空间中的文件
@app.route('/delete')
def delete():
    filename = 'filename'
    ret, info = qiniu_store.delete(filename)
    return str(ret)

# 根据文件名获取对应的公开URL
@app.route('/url')
def url():
    filename = 'filename'
    return qiniu_store.url(filename)
```
参考*tests.py*

## 返回值
`save`与`delete`返回的`ret`、`info`为[qiniu python-sdk](https://github.com/qiniu/python-sdk)中对应API的返回值，可在成功操作与失败操作时分别打印查看其具体内容
```python
print ret
print info
```

## 测试
```python
$ python tests.py
```

## 许可
The MIT License (MIT). 详情见 __License文件__
