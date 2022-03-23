# test-dev
**1、更新最新插件**
插件名写入requirements.txt，
在terminal执行：pip install -r requirements.txt
验证：pytest --version

**2、分组执行**
在用例上用标签注释打标
同时执行冒烟测试和用户管理测试命令：pytest -vs -m "smoke or usermanege"

**3、自动生成简单测试报告**
新建report目录，执行命令：pytest -vs --html ./report/report.html

**4、生成allure报告**
a、下载 https://github.com/allure-framework/allure2/releases
b、解压并运行 /bin/allure
c、配置环境变量 PATH=${PATH}:/Applications/allure-2.17.3/bin
d、验证：allure --version
ps：命令1 pytest -vs 命令2 allure serve temp
