# wtprogress
在Windows Terminal中显示进度条的python库

当你在后台运行耗时的python程序（例如训练神经网络），并在前台干其他事情时，你需要打开终端来查看进度。有了这个库，可以将进度条显示在任务栏上，无需切换到终端即可轻松查看进度。

注意：这个库仅支持[Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab1)。系统默认终端不支持进度条显示。

## 示例
```py
import wtprogress,time
def main():
    for i in range(1,101):
            print("\rProgress: {}%".format(i),end="",flush=True)
            wtprogress.show(i)
            time.sleep(0.1)
    print("\nTask finished")
    wtprogress.close()
main()
```
![](example.gif)