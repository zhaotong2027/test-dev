# test-dev
1、更新最新插件
插件名写入requirements.txt，
在terminal执行：pip install -r requirements.txt
验证：pytest --version
2、分组执行
在用例上用标签注释打标
同时执行冒烟测试和用户管理测试命令：pytest -vs -m "smoke or usermanege"
3、自动生成简单测试报告
新建report目录，执行命令：pytest -vs --html ./report/report.html
