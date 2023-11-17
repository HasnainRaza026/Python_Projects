
# Alarm Clock

This is the CLI (Command line interface) based python mini and beginners friendly project. In which the user is asked to provide the minutes and seconds after which the alarm will ring. The program only works with minutes and second but anyone can easily modify it for hours or even for days.


## Modules, Functions and Commands used
### playsound Module
The playsound module is a cross platform module that can play audio files. 

Run the following command to install the packages:
```
pip install playsound
```
The playsound module contains only a single function (also named) `playsound()`.

It requires one argument, the path to the file with the sound we have to play. It can be a local file, or a URL.
```py
from playsound import playsound
playsound('/path/file.mp3')
```
**WAVE** and **MP3** have been tested and are known to work with this module. Other file formats may work as well.

Python has a list of different moudules to play and manipulate audios, each one is used for specific applications.
* [pydub Module](https://www.geeksforgeeks.org/working-with-wav-files-in-python-using-pydub/)
* [tksnack Module](https://www.geeksforgeeks.org/play-sound-in-python/)
* [simpleaudio Module](https://pypi.org/project/simpleaudio/)


### time Module
The time module in Python provides functions for handling time-related tasks. Like representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like pausing the Program during execution and measuring the efficiency of your code etc.

The time module comes with Python’s standard utility module, so there is no need to install it externally. We can simply import it using the `import` statement.
```py
import time
```

Execution can be delayed using `time.sleep()` method. This method is used to halt the program execution for the time specified in the arguments.
```py
time.sleep(1)
# pause for 1 second
```

To learn more about the time module functionalities read Python’s Official [time Module documentation](https://docs.python.org/3/library/time.html)

Read very informative artical posted by geeksforgeeks on Python [time Module](https://www.geeksforgeeks.org/python-time-module/)

Also check out this awesome video by [Bro Code](https://youtube.com/@BroCodez?si=lK6aIAY0xGbpqrGf) on python time Module [here](https://youtu.be/Qj3GlL5ckQA?si=l6jDD0G0DYF8C5-B)
