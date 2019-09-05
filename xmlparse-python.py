import xml.etree.ElementTree as ET
import subprocess
from pymongo import MongoClient
import pymongo

path = ET.parse('C:\\Users\\munoz\\Desktop\\test-library.xml')
plist = path.getroot()
top = path.find('dict')
tracks = top.find('dict')
for trackrow in tracks.findall('dict'):
    trackID=trackrow.text
    props = trackrow.findall('*')
    #name = trackrow.find('string').text
    fields = trackrow.findall('key')
    name = fields[1].text
    trackname = trackrow.findall('string')[0].text
    artist = fields[2].text
    artisttext = trackrow.findall('string')[1].text
    album = fields[3].text
    albumtext = trackrow.findall('string')[2].text
    genre = fields[4].text
    genretext = trackrow.findall('string')[3].text
    filetype= fields[5].text
    filetypetext = trackrow.findall('string')[4].text
    size = fields[6].text
    sizenum = trackrow.findall('integer')[1].text
    time = fields[7].text
    tracktime = trackrow.findall('integer')[2].text
    year = fields[8].text
    trackyear = trackrow.findall('integer')[3].text
    bpmfield = fields[9].text
    bpm = trackrow.findall('integer')[4].text
    datemodfield = fields[10].text
    datemod = trackrow.findall('date')[0].text
    dateaddfield = fields[11].text
    dateadd = trackrow.findall('date')[1].text
    bitratefield = fields[12].text
    bitrate = trackrow.findall('integer')[5].text
    commentfield = fields[14].text
    comments = trackrow.findall('string')[5].text
    #unplayedfield = fields[21].text
    #unplayedflag = 
    locationfield = fields[22].text
    location = trackrow.findall('string')[9].text
    filefoldercount = fields[23].text
    ffcount = trackrow.findall('integer')[9].text

    #This will find text for the 
    print(ffcount)
    #
"""     vclient = MongoClient('localhost',27017)
    db=vclient.myDB
    result = db.data.insert_one({name:trackTitle})
    print (result.inserted_id) """

    

""" 
for dicT in plist:
    # print (dicT.tag, dicT.attrib)
    for key in dicT:
        #print(key.tag,key.attrib)
        for child in key:
            # print(child.tag, child.attrib)
            for secondChild in child:
                data = secondChild
                data = data.iter()
                datatype = type(data)
    print(dicT[3][0].text)
                # print(data,datatype)
print(plist.tag, plist.attrib, find) """