from PIL import Image
import xml.etree.ElementTree as ET
from io import BytesIO
import webbrowser
import json
from jsonpath import jsonpath

with open('json-doc/via_project_6Jul2022_1h18m_json.json') as json_file:
    via_file = json.load(json_file)

# Extract element content from JSON #
filename_value = jsonpath(via_file, "$..filename")
size_value = jsonpath(via_file, "$..size")

name_shape_value = jsonpath(via_file, "$..shape_attributes.name")
x_value = jsonpath(via_file, "$..shape_attributes.x")
y_value = jsonpath(via_file, "$..shape_attributes.y")
width_value = jsonpath(via_file, "$..shape_attributes.width")
height_value = jsonpath(via_file, "$..shape_attributes.height")

region_attributes = jsonpath(via_file, "$..region_attributes")
name_region_value = jsonpath(via_file, "$..region_attributes.name")
type_value = jsonpath(via_file, "$..region_attributes.type")

caption_value = jsonpath(via_file, "$..file_attributes.caption")
public_domain_value = jsonpath(via_file, "$..file_attributes.public_domain")

file_path = 'image/' + filename_value[0]

img = Image.open(file_path)
w = img.width
h = img.height

# Build ElementTree #
root = ET.Element("table")

# Body left table #
body_left = ET.SubElement(root, "table")
body_left.set('class', 'left')
nav = ET.SubElement(body_left, "nav")
ul = ET.SubElement(nav, "ul")
li1 = ET.SubElement(ul, "li")
a1 = ET.SubElement(li1, "a")
a1.set('href', 'https://www.robots.ox.ac.uk/~vgg/software/via/')
a1.text = str('VGG Image Annotator (VIA)')
li2 = ET.SubElement(ul, "li")
a2 = ET.SubElement(li2, "a")
a2.set('href', 'https://www.w3schools.com/html/default.asp')
a2.text = str('HTML tutorial w3schools')
li3 = ET.SubElement(ul, "li")
a3 = ET.SubElement(li3, "a")
a3.set('href', 'https://www.w3schools.com/css/default.asp')
a3.text = str('CSS tutorial w3schools')

# Body middle table #
body_middle = ET.SubElement(root, "table")
body_middle.set('class', 'middle')

img_table = ET.SubElement(body_middle, "table")
img_table.set('class', 'img_table')

table1 = ET.SubElement(img_table, "table")
table1.set('class', 'table1')
table1.set('style', 'color: white')
table1.text = str("1")

table2 = ET.SubElement(img_table, "table")
table2.set('class', 'table2')
table2.set('style', 'color: white')
table2.text = str("2")

table3 = ET.SubElement(img_table, "table")
table3.set('class', 'table3')
table3.set('style', 'color: white')
table3.text = str("3")

# Body right table #
body_right = ET.SubElement(root, "table")
body_right.set('class', 'right')

table = ET.SubElement(body_right, "table")
table.set('class', 'table')
table.set('border', '5')

tr0 = ET.SubElement(table, "tr")
th1 = ET.SubElement(tr0, "th")
th1.text = str("number")
th2 = ET.SubElement(tr0, "th")
th2.text = str("name")
th3 = ET.SubElement(tr0, "th")
th3.text = str("type")
th4 = ET.SubElement(tr0, "th")
th4.text = str("image_quality")

tr1 = ET.SubElement(table, "tr")
td1_1 = ET.SubElement(tr1, "td")
td1_1.text = str("1")
td1_2 = ET.SubElement(tr1, "td")
input1 = ET.SubElement(td1_2, "input")
input1.set('class', 'text')
input1.set('value', name_region_value[0])
td1_3 = ET.SubElement(tr1, "td")
select1 = ET.SubElement(td1_3, "select")
option1_1 = ET.SubElement(select1, "option")
option1_1.set('value', 'human')
option1_1.set('selected', 'selected')
option1_1.text = str("human")
option1_2 = ET.SubElement(select1, "option")
option1_2.set('value', 'cup')
option1_2.text = str("cup")
option1_3 = ET.SubElement(select1, "option")
option1_3.set('value', 'unknown')
option1_3.text = str("unknown")
td1_4 = ET.SubElement(tr1, "td")
checkbox1_1 = ET.SubElement(td1_4, "input")
checkbox1_1.set('type', 'checkbox')
checkbox1_1.text = str("Blurred region")
checkbox1_2 = ET.SubElement(td1_4, "input")
checkbox1_2.set('type', 'checkbox')
checkbox1_2.set('checked', '')
checkbox1_2.text = str("Good Illumination")
checkbox1_3 = ET.SubElement(td1_4, "input")
checkbox1_3.set('type', 'checkbox')
checkbox1_3.text = str("Object in Frontal View")

tr2 = ET.SubElement(table, "tr")
td2_1 = ET.SubElement(tr2, "td")
td2_1.text = str("2")
td2_2 = ET.SubElement(tr2, "td")
input2 = ET.SubElement(td2_2, "input")
input2.set('class', 'text')
input2.set('value', name_region_value[1])
td2_3 = ET.SubElement(tr2, "td")
select2 = ET.SubElement(td2_3, "select")
option2_1 = ET.SubElement(select2, "option")
option2_1.set('value', 'human')
option2_1.set('selected', 'selected')
option2_1.text = str("human")
option2_2 = ET.SubElement(select2, "option")
option2_2.set('value', 'cup')
option2_2.text = str("cup")
option2_3 = ET.SubElement(select2, "option")
option2_3.set('value', 'unknown')
option2_3.text = str("unknown")
td2_4 = ET.SubElement(tr2, "td")
checkbox2_1 = ET.SubElement(td2_4, "input")
checkbox2_1.set('type', 'checkbox')
checkbox2_1.text = str("Blurred region")
checkbox2_2 = ET.SubElement(td2_4, "input")
checkbox2_2.set('type', 'checkbox')
checkbox2_2.set('checked', '')
checkbox2_2.text = str("Good Illumination")
checkbox2_3 = ET.SubElement(td2_4, "input")
checkbox2_3.set('type', 'checkbox')
checkbox2_3.set('checked', '')
checkbox2_3.text = str("Object in Frontal View")

tr3 = ET.SubElement(table, "tr")
td3_1 = ET.SubElement(tr3, "td")
td3_1.text = str("3")
td3_2 = ET.SubElement(tr3, "td")
input3 = ET.SubElement(td3_2, "input")
input3.set('class', 'text')
input3.set('value', name_region_value[2])
td3_3 = ET.SubElement(tr3, "td")
select3 = ET.SubElement(td3_3, "select")
option3_1 = ET.SubElement(select3, "option")
option3_1.set('value', 'human')
option3_1.text = str("human")
option3_2 = ET.SubElement(select3, "option")
option3_2.set('value', 'cup')
option3_2.set('selected', 'selected')
option3_2.text = str("cup")
option3_3 = ET.SubElement(select3, "option")
option3_3.set('value', 'unknown')
option3_3.text = str("unknown")
td3_4 = ET.SubElement(tr3, "td")
checkbox3_1 = ET.SubElement(td3_4, "input")
checkbox3_1.set('type', 'checkbox')
checkbox3_1.text = str("Blurred region")
checkbox3_2 = ET.SubElement(td3_4, "input")
checkbox3_2.set('type', 'checkbox')
checkbox3_2.text = str("Good Illumination")
checkbox3_3 = ET.SubElement(td3_4, "input")
checkbox3_3.set('type', 'checkbox')
checkbox3_3.text = str("Object in Frontal View")


# Convert to XML #
tree = ET.ElementTree(root)
io = BytesIO()
tree.write(io)
xml = io.getvalue().decode('UTF8')
# print(xml)

index_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>""" + str(caption_value[0]) + """</title>
    <style>
        header {
            background-color: #999;
            padding: 10px;
            text-align: center;
            font-size: 25px;
            color: black;
        }
        footer {
            background-color: #999;
            padding: 10px;
            text-align: center;
            font-size: 25px;
            color: black;
        }
        .left {
            float: left;
            background-color: transparent;
            height: 80%;
            width: 30%;
            padding: 0;
            border: 0px solid black;
            display: inline-block;
        }
        .middle {
            background-color: transparent;
            height: 80%;
            width: 40%;
            left: 30%;
            padding: 0;
            border: 0px solid black;
            display: inline-block;
        }
        .right {
            float: right;
            background-color: transparent;
            height: 80%;
            width: 30%;
            left: 70%;
            padding: 0;
            border: 0px solid black;
            display: inline-block;
        }
        .img_table {
            width: """ + str(w) + """px;
            height: """ + str(h) + """px;
            background: url(""" + str(file_path) + """) no-repeat center;
            border: 3px solid black;
            margin: 0 auto;
        }
        .table1 {
            position: absolute;
            background-color: transparent;
            height: """ + str(height_value[0]) + """px;
            width: """ + str(width_value[0]) + """px;
            margin-left: """ + str(x_value[0]) + """px;
            margin-top: """ + str(y_value[0]) + """px;
            padding: 0;
            border: 3px solid yellow;
            display: block;
        }
        .table2 {
            position: absolute;
            background-color: transparent;
            height: """ + str(height_value[1]) + """px;
            width: """ + str(width_value[1]) + """px;
            margin-left: """ + str(x_value[1]) + """px;
            margin-top: """ + str(y_value[1]) + """px;
            padding: 0;
            border: 3px solid yellow;
            display: block;
        }
        .table3 {
            position: absolute;
            background-color: transparent;
            height: """ + str(height_value[2]) + """px;
            width: """ + str(width_value[2]) + """px;
            margin-left: """ + str(x_value[2]) + """px;
            margin-top: """ + str(y_value[2]) + """px;
            padding: 0;
            border: 3px solid yellow;
            display: block;
        }
    </style>
</head>
<body>
    <header>
        <h2>""" + str(caption_value[0]) + """</h2>
    </header>
        """ + str(xml) + """
    <footer>
        <ul>
            <li style="display: inline-block">
                <a href="https://www.robots.ox.ac.uk/~vgg/software/via/">
                    VGG Image Annotator (VIA)
                </a>
            </li>
            <li style="display: inline-block">
                <a href="https://www.w3schools.com/html/default.asp">
                    HTML tutorial w3schools
                </a>
            </li>
            <li style="display: inline-block">
                <a href="https://www.w3schools.com/css/default.asp">
                    CSS tutorial w3schools
                </a>
            </li>
        </ul>
    </footer>
</body>
</html>
"""

GET_HTML = "table.html"
f = open(GET_HTML, 'w')
f.write(index_page)
f.close()

webbrowser.open("table.html")
