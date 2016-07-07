# -*- coding: utf-8 -*-
import htmlPy
import json
#from main import app as htmlPy_app

port = None


class HomeClass(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    #def __init__(self):
        #super(HomeClass. self).__init__()
        #return

    @htmlPy.Slot()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        print "Function name"
        return

    @htmlPy.Slot(str, result=str)
    def form_function_name(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        print "Form function name"
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        print "Javascript function"
        return


class Port():

    def __init__(self, portName, bauds, numBits, stopBits, handShake, parity):
        self.portName = portName
        self.bauds = bauds
        self.numBits = numBits
        self.stopBits = stopBits
        self.handShake = handShake
        self.parity = parity

    def openPort(self):
        pass


class ConfigClass(htmlPy.Object):

    @htmlPy.Slot(str, result=str)
    def post(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        # json_data = {"portName":"COM1","bauds":"1200","parity":"n","handShake":"on","numBits":"on","stopBits":"on"}
        import pdb; pdb.set_trace()
        portName = json_data['portName']
        bauds = json_data['bauds']
        parity = json_data['parity']
        handShake = json_data['handShake']
        numBits = json_data['numBits']
        stopBits = json_data['stopBits']
        print "Form function name"
        form_data = json.loads(json_data)
        return json.dumps(form_data)
