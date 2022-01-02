from cefpython3 import cefpython

if __name__ == '__main__':
    cefpython.Initialize()
    cefpython.CreateBrowserSync(url = "https://www.google.com/", window_title = "Dom Garça")
    cefpython.MessageLoop()
    cefpython.Shutdown()