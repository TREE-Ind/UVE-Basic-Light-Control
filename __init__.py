from adapt.intent import IntentBuilder
from adapt.tools.text.tokenizer import EnglishTokenizer
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import LOG, getLogger
from mycroft.util.parse import fuzzy_match, extract_datetime, extract_number
from mycroft.audio import wait_while_speaking
from mycroft import intent_handler
from mycroft import intent_file_handler
from mycroft.skills.context import *

import requests
import json
import time

class Ue4LightsControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        #self.register_entity_file("name.entity")
        #ip_address = self.settings.get('ip_address', 'http:/localhost')
        ip_address = "http://192.168.1.68"
        self.object_path = self.settings.get('bp_location', '/Game/CyberpunkIndustries/Maps/Demo_Map.Demo_Map:PersistentLevel.Lights_VC_2')
        self.prop_url = ip_address + ":8080/remote/object/property"
        self.call_url = ip_address + ":8080/remote/object/call"


        
    @intent_file_handler('spotlights.intent')
    def handle_spotlights(self, message):
        state = message.data.get("state")
        #length = extract_number(length)
        #length = int(length)
        self.log.info(state)
        data = {'objectPath': self.object_path, 'functionName': 'Spotlights', 'parameters': { 'State':  state}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        LOG.info(r.status_code)
        if r.status_code == 200:
            self.speak('All spotlights have been turned {}'.format(state))
        elif r.status_code == 404:
            self.speak('Sorry, I could not turn the spotlights {}'.format(state))
        else:
            pass
        
    @intent_file_handler('pointlights.intent')
    def handle_pointlights(self, message):
        state = message.data.get("state")
        #length = extract_number(length)
        #length = int(length)
        self.log.info(state)
        data = {'objectPath': self.object_path, 'functionName': 'Pointlights', 'parameters': { 'State':  state}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        LOG.info(r.status_code)
        if r.status_code == 200:
            self.speak('All point lights have been turned {}'.format(state))
        elif r.status_code == 404:
            self.speak('Sorry, I could not turn the spotlights {}'.format(state))
        else:
            pass

    @intent_file_handler('spotlights.color.intent')
    def handle_spotlights_color(self, message):
        color = message.data.get("color")
        #length = extract_number(length)
        #length = int(length)
        self.log.info(color)
        if color == 'blue':
            self.R = '0'
            self.G = '0'
            self.B = float('1.0')
            #data = {'objectPath': self.object_path, 'functionName': 'SpotlightColor', 'parameters': { 'R':  self.R, 'G': self.G, 'B': self.B}}
            #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            #r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        elif color == 'red':
            self.R = float('1.0')
            self.G = '0'
            self.B = '0'
        else:
            pass
        self.log.info(self.B)
        data = {'objectPath': self.object_path, 'functionName': 'SpotlightColor', 'parameters': { 'R':  self.R, 'G': self.G, 'B': self.B}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        LOG.info(r.status_code)
        if r.status_code == 200:
            self.speak('All spotlights have been turned {}'.format(color))
        elif r.status_code == 404:
            self.speak('Sorry, I could not turn the spotlights {}'.format(color))
        else:
            pass

    @intent_file_handler('pointlights.color.intent')
    def handle_pointlights_color(self, message):
        color = message.data.get("color")
        #length = extract_number(length)
        #length = int(length)
        self.log.info(color)
        if color == 'blue':
            self.R = '0'
            self.G = '0'
            self.B = float('1.0')
            #data = {'objectPath': self.object_path, 'functionName': 'SpotlightColor', 'parameters': { 'R':  self.R, 'G': self.G, 'B': self.B}}
            #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            #r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        elif color == 'red':
            self.R = float('1.0')
            self.G = '0'
            self.B = '0'
        else:
            pass
        self.log.info(self.B)
        data = {'objectPath': self.object_path, 'functionName': 'PointlightColor', 'parameters': { 'R':  self.R, 'G': self.G, 'B': self.B}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(self.call_url, data=json.dumps(data), headers=headers)
        LOG.info(r.status_code)
        if r.status_code == 200:
            self.speak('All point lights have been turned {}'.format(color))
        elif r.status_code == 404:
            self.speak('Sorry, I could not turn the spotlights {}'.format(color))
        else:
            pass

#json.loads(r.text)


def create_skill():
    return Ue4LightsControl()
