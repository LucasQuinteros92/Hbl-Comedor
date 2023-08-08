import json
import os

file_path_JSON_aux = '/home/pi/Desktop/hbl.json'
file_path_JSON_new = '/usr/programas/hbl/modulos/hbl.json'

file_path_JSON_final = '/usr/programas/hbl/modulos/hbl.json'
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
with open(os.path.join(__location__ , file_path_JSON_aux), "r") as f:
    data = json.load(f)
    f.close()
    #print("data : ",json.JSONEncoder(indent=2).encode(data))

#print("\n\n\n\n\n")

with open(os.path.join(__location__ , file_path_JSON_new), "r") as f2:
    data2 = json.load(f2)
    f2.close()
    #print("data2 : ",json.JSONEncoder(indent=2).encode(data2))

aux = {'Test':'Test'}
for key in data:
    if key in data2:
        if type(aux) == type(data2[key]):
            for key_key in data[key]:
                if key_key in data2[key]:
                    if type(aux) == type(data2[key][key_key]):
                        for key_key_key in data[key][key_key]:
                            if key_key_key in data2[key][key_key]:
                                if type(aux) == type(data2[key][key_key][key_key_key]):
                                    for key_key_key_key in data[key][key_key][key_key_key]:
                                        if key_key_key_key in data2[key][key_key][key_key_key]:
                                            data2[key][key_key][key_key_key][key_key_key_key]=data[key][key_key][key_key_key][key_key_key_key]
                                else:
                                    data2[key][key_key][key_key_key]=data[key][key_key][key_key_key]
                    else:
                        data2[key][key_key]=data[key][key_key]
        else:
            try:
                data2[key]=data[key]
            except:
                a=0
            a=0 
    #else:
        #print(key," no pertenece a data2") ### Si no pertenece, tiene que aregarlo?




#print(json.JSONEncoder(indent=2).encode(data2))
myFile = open(file_path_JSON_final, 'w')
with myFile:
    myFile.write(json.JSONEncoder(indent=2).encode(data2))
