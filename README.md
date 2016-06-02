# 运维脚本

运维常用的一些脚本,大部分使用python27，所以请确保本地已经有[python](https://www.python.org/downloads/)环境。

另外附送一些在线工具，

#### [crontab-gui](http://www.corntab.com/pages/crontab-gui)


## MySQLBackup
依赖安装

```
pip install PyYAML
```

复制配置文件

```bash
cd MySQLBackup
cp mysql.conf.yaml.sample mysql.conf.yaml
```

根据需要修改 mysql.conf.yaml 文件。

加入到crontab中，

```bash
crontab -e
```

```
# 每天执行一次
* */12 * * * /usr/bin/python /usr/local/script/useful-script/MySQLBackup/mysql.py
```