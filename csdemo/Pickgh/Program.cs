using Microsoft.Playwright;

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
//await page.RunAndWaitForNavigationAsync(async () =>
//{
//    await Task.CompletedTask;
//});
//await page.ScreenshotAsync(new PageScreenshotOptions
//{
//    Path = "screenshot.png",
//});