# Json to PHP Array

__将Json转为等价的PHP array表示__

## Usage

### 1. 使用可执行文件

Release中提供了用pyinstaller打包的适用于macOS的可执行文件，直接下载即可使用

```shell
# 查看帮助
./json2array -h
```

### 2. 源码运行

1. 安装Python3，此项目仅使用了Python标准库，所以无需安装依赖
2. 在当前目录新建文件`input.json`，向其中写入要转换json
3. 执行`python3 main.py`，即可打印出输入json对应的PHP array表示