#  Ammar Qaseem
import sys
import gzip
import os
import xml.etree.ElementTree as ET

cmd = "mkdir corpus/DS3/DS3"
os.system(cmd)

print "splitting..."
context = ET.iterparse(gzip.open('corpus/DS3/test0.txt.gz'), events=('end', ))
index = -1
j = 0
$max_lim = 500
f = gzip.GzipFile("corpus/DS3/DS3/test" + str(j) + ".txt.gz", 'wb')
#gzip.GzipFile(options.output,'w') 
for event, elem in context:
    if elem.tag == 'document':
        index += 1
        #print "doc", index
        sys.stdout.write("Documents progressed: %d\r" % index )
        sys.stdout.flush()
        
        if (index == (max_lim*j)):
            f.write("</corpus>")
            f.close()    
            f = gzip.GzipFile("corpus/DS3/DS3/test" + str(j) + ".txt.gz", 'wb')
            #print "file", j
            j=j+1
            
            #f.write("<corpus source=\"DS3\">\n")
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><corpus source=\"DS3\">\n")
            #with open(filename, 'wb') as f:
        if (index < (max_lim*j)):   
            #print "writing :", index
            #print f 
            f.write(ET.tostring(elem))
            elem.clear()    
            
            #f.write("</corpus>")
            
f.write("</corpus>")            
f.close()

#os.exit(0)
    
            
sys.stdout.write("\n")
