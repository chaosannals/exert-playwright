# CSharp Playwright

```pwsh
# 创建项目
dotnet new console -n PlaywrightDemo
cd PlaywrightDemo

# 添加依赖
dotnet add package Microsoft.Playwright
# 构建项目，为了生成下面的 ps1 脚本
dotnet build

# 上3个步骤可以通过 IDE 等完成。

# 安装需要的浏览器 - netX 代表框架, 比如 net6.0，所以路径是一个例子，视具体情况。
# playwright.ps1 有多种功能，功能类似 python 版的 playwright 命令。
pwsh bin\Debug\netX\playwright.ps1 install

# 如果上面的脚本无法工作 (throws TypeNotFound), 尝试更新 PowerShell.
dotnet tool update --global PowerShell
```

```pwsh
pwsh bin\Debug\netX\playwright.ps1 open --save-storage=auth.json github.com

# open 和 codegen 的参数基本一致。

# 脚本采集生成
pwsh bin\Debug\netX\playwright.ps1 codegen github.com

# 仿真 iPhone 11.
pwsh bin\Debug\netX\playwright.ps1 codegen --device="iPhone 11" wikipedia.org

# 仿真屏幕大小和颜色.
pwsh bin\Debug\netX\playwright.ps1 codegen --viewport-size=800,600 --color-scheme=dark twitter.com

# 仿真时区，语言和定位
# Once page opens, click the "my location" button to see geolocation in action
pwsh bin\Debug\netX\playwright.ps1 codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com
```


```pwsh
# 测试库
dotnet add package Microsoft.Playwright.NUnit
```