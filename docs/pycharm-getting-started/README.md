# Getting Started with PyCharm Community Edition

An easy way to get started on this project is to use the 
[PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/).

Launch PyCharm and if it opens into a default project, go to File -> Close until you see the project selector
window:

![PyCharm - Project Selection](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/01%20-%20project%20selection.png)

From this option, select "Get from VCS" (VCS is 
[Version Control System](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)), and then enter
the details of this project:

```
https://github.com/kws/django-starter
```

![PyCharm - Checkout from VCS](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/01%20-%20checkout%20from%20VCS.png)

PyCharm should now download and open the project:

![PyCharm - Checkout and download](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/01%20-%20checkout%20from%20VCS.gif)

You may see a couple of error messages cause by me editing this project in the Professional Edition which has
a few extra features compared to the Community Edition. These can safely be ignored. 

You now have a local copy of the project you can edit and work on. The original is still on GitHub, and 
if you break something, you can always revert to the original versions, so don't worry about playing around.

## Installing Dependencies

The next thing we need to do is make sure we have the right version of Python and Django installed. 

At the bottom of the screen, you should now see a message that there is `<No interpreter>`:

![PyCharm - Add Intepreter](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/02%20-%20add%20interpreter.png)

Click on this text, and you should get a menu where you can select "Add Interpreter".

You can select any of the options here, but I would recommend using Conda as it what we use for most projects at SF.

![PyCharm - Create Environment](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/02%20-%20create%20environment.png)

Hit OK to configure the environment. Whilst that is downloading the necessary, explore the Projects tab on the left
hand side of the screen and open the file `requirements.txt` that declares the additional dependencies we need.

![PyCharm - Select requirements.txt](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/02%20-%20select%20requirements.png)

Once the environment is configured, you should see an option to install additional requirements. It may take a little
bit of time before this appears:

![PyCharm - Install requirements](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/02%20-%20install%20requirements.png)

Click install requirements and wait while it installs.

![PyCharm - Install requirements](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/02%20-%20environment.gif)

## Running the Django Management Tool

Once that has completed, you are ready to run Django. Most Django operations are done through the management tool,
and you can launch this from the terminal. Click "Terminal" at the bottom of the screen, and when the prompt opens, 
type:

```shell
python manage.py
```

You should then see a list of management commands. You can now head back to the
[main tutorial](https://github.com/kws/django-starter#creating-the-database-and-a-superuser).

![PyCharm - Launch terminal](https://github.com/kws/django-starter/blob/main/docs/pycharm-getting-started/03%20-%20launch%20terminal.gif)

