import logging
import random

from flask import Flask

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/debug-influx')
def trigger_error():
    power_plant_level = random.randint(0, 100)
    if power_plant_level < 30:
        app.logger.error("The power plant level is low: {}".format(power_plant_level))
    return {'power_plant_level': power_plant_level}
