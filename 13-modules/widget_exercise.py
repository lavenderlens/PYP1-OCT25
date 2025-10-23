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