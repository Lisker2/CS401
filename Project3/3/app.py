import json
import redis
import os
import importlib
import time

REDIS_HOST = os.getenv('REDIS_HOST', "localhost")
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_INPUT_KEY = os.getenv('REDIS_INPUT_KEY', None)
REDIS_OUTPUT_KEY = os.getenv('REDIS_OUTPUT_KEY', None)

INTERVAL_TIME = int(os.getenv('INTERVAL', 5))

r_server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, 
                       charset="utf-8", decode_responses=True)
                       
module_loader = importlib.util.find_spec('usermodule')
        
import usermodule as lf


from context import Context
context = Context(host=REDIS_HOST, port=REDIS_PORT,
                  input_key=REDIS_INPUT_KEY, output_key=REDIS_OUTPUT_KEY)

while True:
    data = None
    output = None
    data = r_server.get(REDIS_INPUT_KEY)
    if data:
        data = json.loads(data)
        output = lf.handler(data, context)
        if output and REDIS_OUTPUT_KEY:
            r_server.set(REDIS_OUTPUT_KEY, json.dumps(output))
        context.confirm_execution()
    time.sleep(INTERVAL_TIME)