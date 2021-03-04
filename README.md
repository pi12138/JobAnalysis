# JobAnalysis
IT行业毕业生的就业分布数据分析与可视化系统的设计与实现  

## 配置环境

### 开发环境

- Ubuntu 20.04.2 LTS

### 安装mysql 8.0

- Ubuntu 20 默认源版本是mysql8.0
- 安装完成后通过系统root用户先进入，然后修改mysql用户密码
- `ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'yourpasswd';`
- `FLUSH PRIVILEGES;`
- 网上找了一圈，全都不能用，然后去stackoverflow上找到的[https://stackoverflow.com/questions/50691977/how-to-reset-the-root-password-in-mysql-8-0-11]
- ps: 国内都是一群啥歪瓜裂枣在哪写文章，醉了


### 安装 mysqlclient

```shell
sudo apt-get install libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient
```

### 创建数据库

- `create database if not exists job_analysis default character set = 'utf8';` 