'''
using the JSON provided, 
1. read it into a python script as a python dictionary (of dictionaries)
2. drill down and edit ["image"]["name"] "sun1"
    to be: ["image"]["name"] "moon1"
3. drill down and edit ["image"]["src"] "Images/Sun.png"
    to be ["image"]["src"] "Images/Moon.png"

4. this will also requre an edit in ["text"]["onmouseup"]
5. write the modified widget to a NEW JSON file modified-widget.json

you will use the methods json.load (without an S)
you will use the methods json.dump (without an S)
'''

import json 
with open("widget.json") as widget_file:
    # read contents into a Python dictionary:
    print(widget := json.load(widget_file))#version of load for file handling

# 2 and 3 edit dict data
widget["widget"]["image"]["name"] = "moon1"
widget["widget"]["image"]["src"] = "Images/Moon.png"
# print(widget["widget"]["text"]["onMouseUp"])#testing
widget["widget"]["text"]["onMouseUp"] = 'moon1.opacity = (moon1.opacity / 100) * 90;'

# 5. write to new file (serialised back into json)
with open("modified-widget.json", mode="w") as modified_widget_file:
    json.dump(widget, modified_widget_file)
