import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')
root = tree.getroot()

# chcemy zmeinić rok filmu 'Batman Returns'

Batman_Returns_year = root.find("*//movie[@title='Batman Returns']/year")

print(Batman_Returns_year.text)
Batman_Returns_year.text = '2000'

new_Batman_Returns_year = root.find("*//movie[@title='Batman Returns']/year")

print("po zmienie roku\n")
print(new_Batman_Returns_year.text)
