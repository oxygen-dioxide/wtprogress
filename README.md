# wtprogress
A python library for showing progress in windows terminal.

When you are running a long-running task in python in background, such as training a neural network, you may switch to your terminal frequently to check the progress. With this library, your python script can show progress in your taskbar, and you can easily see it without switching to your terminal.

Note: this library only supports [windows terminal](https://www.bing.com/search?q=windows+termina&cvid=449bb659a5224c3bba78d71a7b8f7545&aqs=edge..69i57j0l2j69i59j69i61j69i60j69i61.128398j0j1&pglt=131&FORM=ANNTA1&PC=U531). Conhost doesn't have this feature.

## Example
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