# Network Login
Automates login for the LNMIIT Login Portal

#### Dependencies:
> [`selenium`](https://pypi.org/project/selenium/)
> [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.41/)
> [`pynotify`](https://github.com/adarshpunj/pynotify)


#### Note that you need to set your login credentials in line 14 and 17 of the [login.py](https://github.com/adarshpunj/Network-Login/blob/master/login.py) file.

#### Is it safe to enter my password?
It can be easily concluded from the script that none of your details are being sent outside your the LNMIIT Login Portal. The script simply puts your login ID and password into a browser - the same thing you would do manually.

---   
### For  users:
There's more for macOS users. Turn this .py file into an app using Script Editor. Here's what you can do:

1. Move the login.py file to Macintosh HD (/).
2. Open Script Editor > New Script (⌘+N)

3. Paste the following two lines of codes:

   `do shell script "networksetup -setairportpower en0 on"`
   
   `do shell script "python login.py"`

4. Go to File > Export > File Format > app
5. Save to Desktop

Now, you have an app that logs you into the network. The app also turns on the WiFi in case, you haven't.

![ezgif-1-86561a3119](https://user-images.githubusercontent.com/30762976/45983322-c1374200-c079-11e8-94b0-07cb0d0504d8.gif)

##### The browser is headless in the real code. 

###### Made with ❤️ using Python
