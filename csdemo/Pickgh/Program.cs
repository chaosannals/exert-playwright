using Serilog;
using Serilog.Events;
using Serilog.Sinks.File;

using Microsoft.Playwright;

Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .WriteTo.File
    (
        path: "logs/logserver-.log",
        rollingInterval: RollingInterval.Day,
        rollOnFileSizeLimit: true,
        fileSizeLimitBytes: 2000000,
        flushToDiskInterval: TimeSpan.FromSeconds(10),
        outputTemplate: "[{Timestamp:yy-MM-dd HH:mm:ss} {Level:u3}] {Message:lj}{NewLine}{Exception}"
        )
    .WriteTo.Console(restrictedToMinimumLevel: LogEventLevel.Information)
    .CreateLogger();

using var playwright = await Playwright.CreateAsync();
var target = "https://github.com";
await using var browser = await playwright.Chromium.LaunchAsync(new BrowserTypeLaunchOptions()
{
    Headless = false,
    //Devtools: true,
    Proxy = new Proxy
    {
        Server="socks5://127.0.0.1:1080",
    }
});
//var page = await browser.NewPageAsync();
var context = await browser.NewContextAsync(new BrowserNewContextOptions
{
    StorageStatePath = "D:\\auth.json",
});
var page = await context.NewPageAsync();
await page.GotoAsync(target);

try
{
    while (true)
    {
        var r = await page.WaitForNavigationAsync(new PageWaitForNavigationOptions
        {
            Timeout = 0,
        });
        Log.Information(r?.Url);
    }
}
catch (PlaywrightException e)
{
    Log.Error(e, "playwright exception.");
}
// 等待导航事件（地址改变）
//await page.RunAndWaitForNavigationAsync(async () =>
//{
//    await Task.CompletedTask;
//});
//await page.ScreenshotAsync(new PageScreenshotOptions
//{
//    Path = "screenshot.png",
//});