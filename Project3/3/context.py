import os
import datetime
class Context(object):

    host = None
    port = None
    input_key = None
    output_key = None
    last_execution = None
    env = None

    def __init__(self, host='localhost', port=6379, input_key=None, output_key=None):
        self.host = host
        self.port = port
        self.input_key = input_key
        self.output_key = output_key
        tmp = os.path.getmtime("/opt/usermodule.py")
        self.function_getmtime = datetime.datetime.fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S')
        self.last_execution = None
        self.env = {}

    def confirm_execution(self):
        self.last_execution = datetime.datetime.now()

    def set_env(self, new):
        self.env = new
