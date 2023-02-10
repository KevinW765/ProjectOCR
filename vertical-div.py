from PIL import Image
import xml.etree.ElementTree as ET
from io import BytesIO
import webbrowser
import json
from jsonpath import jsonpath

with open(
          'json-doc/via_project_19Jul2022_22h46m_json_three_divs_vertical.json'
        ) as json_file:
    via_file = json.load(json_file)

# Extract element content from JSON #
filename_value = jsonpath(via_file, "$..filename")
size_value = jsonpath(via_file, "$..size")

name_shape_value = jsonpath(via_file, "$..shape_attributes.name")
x_value = jsonpath(via_file, "$..shape_attributes.x")
y_value = jsonpath(via_file, "$..shape_attributes.y")
width_value = jsonpath(via_file, "$..shape_attributes.width")
height_value = jsonpath(via_file, "$..shape_attributes.height")
element_region_value = jsonpath(via_file, "$..region_attributes.HTML element")

file_path = 'image/' + filename_value[0]

img = Image.open(file_path)
w = img.width
h = img.height


table = {}
table_css = ""

# Build ElementTree #

container = ET.Element("table")
container.set('class', 'container')

for i in range(len(x_value)):
    table[i] = ET.SubElement(container, "td")
    table[i].set('class', 'table'+str(i+1))
    table[i].text = str(i+1)

# Convert to XML #
tree = ET.ElementTree(container)
io = BytesIO()
tree.write(io)
xml = io.getvalue().decode('UTF8')

index_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        .container {
            position: relative;
            display: flex;
            flex-direction: column;
            background: url(""" + str(file_path) + """) no-repeat center;
            height: """ + str(h) + """px;
            width: """ + str(w) + """px;
            border: 5px solid black;
        }
        .table1 {
             order: 3;
             position: absolute;
             text-align: center;
             font-size: 10px;
             background-color: transparent;
             height: """ + str(height_value[0]) + """px;
             width: """ + str(width_value[0]) + """px;
             left: """ + str(x_value[0]) + """px;
             top: """ + str(y_value[0]-y_value[2]-height_value[2]) + """px;
             outline: 5px solid yellow;

         }
        .table2 {
             order: 1;
             position: absolute;
             text-align: center;
             font-size: 10px;
             background-color: transparent;
             height: """ + str(height_value[1]) + """px;
             width: """ + str(width_value[1]) + """px;
             left: """ + str(x_value[1]) + """px;
             top: """ + str(y_value[1]) + """px;
             outline: 5px solid yellow;

         }
        .table3 {
             order: 2;
             position: absolute;
             text-align: center;
             font-size: 10px;
             background-color: transparent;
             height: """ + str(height_value[2]) + """px;
             width: """ + str(width_value[2]) + """px;
             left: """ + str(x_value[2]) + """px;
             top: """ + str(y_value[2]-y_value[1]-height_value[1]) + """px;
             outline: 5px solid yellow;
        }
    </style>
</head>
<body>
        """ + str(xml) + """
</body>
</html>
"""

GET_HTML = "vertical-table.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()

webbrowser.open("vertical-table.html")
