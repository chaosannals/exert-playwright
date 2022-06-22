# exert-playwright

注： Playwright 的 await 无法取消，直接关闭页面会抛出异常。不过问题不大，一般此种情况就是要关闭程序了。顶多一条日志，这可能是为什么现在官方没有提供处理这个问题的解决方案。

```bash
# 安装 （指定了清华的镜像，指定镜像可能会拉到的版本不是最新）
pip install playwright -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装浏览器驱动
playwright install
```


```bash
# 打开并保存所有 cookie 和 localStorage
playwright open --save-storage=auth.json

# 打包，加载存储的信息
playwright open --load-storage=auth.json

# 指定初始页面录制代码
playwright codegen www.baidu.com

# 保存所有 cookie 和 localStorage 到文件
playwright codegen --save-storage=auth.json

# 通过保存的 auth.json 文件打开录制
playwright codegen --load-storage=auth.json www.baidu.com
```
