# -*- coding: utf-8 -*-
import htmlPy
import os
from back_end import HomeClass, ConfigClass

# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initializations
app = htmlPy.AppGUI(title=u"Application", maximized=False, plugins=True)

# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)
#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

app.template = ("index.html", {"username": "htmlPy_user"})

# Register back-end functionalities
app.bind(HomeClass())
app.bind(ConfigClass())

if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()
