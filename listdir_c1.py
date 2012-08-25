import os, glob
import inspect
from lxml import etree as ET 

def scandirs(path):
	for currentFile in glob.glob(os.path.join(path, '*')):
		if os.path.isdir(currentFile):
			write2file('<' + currentFile[currentFile.rfind('/')+1:len(currentFile)] + '>')
			scandirs(currentFile)
		else:
			write2file('<' + currentFile[currentFile.rfind('/')+1:len(currentFile)] + '>')
		write2file('</' + currentFile[currentFile.rfind('/')+1:len(currentFile)] + '>')


def write2file(xml_string):
	fo = open('foo.xml', 'ab+')
	fo.write(xml_string)
	fo.close()

#str = '/Users/smadishetti/FTP_Sandviks/kathy/dbu/project2'
#lstr = '/'

#print str
#print str[str.rfind('/')+1:len(str)]

write2file('<?xml version="1.0"?><path>')
scandirs('/Users/smadishetti/FTP_Sandviks')
write2file('</path>')

#root = ET.Element('background')
#starttime = ET.SubElement(root, 'starttime')
#hour = ET.SubElement(starttime, 'hour')
#hour.text = '00'
#minute = ET.SubElement(starttime, 'minute')
#minute.text = '00'
#second = ET.SubElement(starttime, 'second')
#second.text = '01'

#print ET.tostring(root, pretty_print=True, xml_declaration=True)
