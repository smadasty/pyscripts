import os, glob
from lxml import etree as ET 

def scandirs(path):
	for currentFile in glob.glob(os.path.join(path, '*')):
		if os.path.isdir(currentFile):
			print 'got a directory: ' + currentFile
			scandirs(currentFile)
		print "processing file: " + currentFile

scandirs('/Users/')

root = ET.Element('background')
starttime = ET.SubElement(root, 'starttime')
hour = ET.SubElement(starttime, 'hour')
hour.text = '00'
minute = ET.SubElement(starttime, 'minute')
minute.text = '00'
second = ET.SubElement(starttime, 'second')
second.text = '01'

print ET.tostring(root, pretty_print=True, xml_declaration=True)
