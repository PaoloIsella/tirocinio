'''
format of json file:

[string ext] : {
  signs: [sign]
  mime: string
}
A sign is a string in this format (without any space):

[int o],[hex s]
where o is x byte offset (Commonly zero)
'''


import binascii
import json
import base64

def getFormatMimeMagic(nomeFile):
    with open(nomeFile, 'rb') as f:
        fileContent = f.read()
        blob = base64.b64encode(fileContent)
        hexdata = binascii.hexlify(fileContent)
        #print(f'il blob in base64 è: {blob}')
        #print(f'il file in hex è: {hexdata}')

    with open('./file_prova/extensions.json') as json_data:
        jsonMagicNumber = json.load(json_data)

    lista = []

    for k in jsonMagicNumber.keys():
        fileFormat = k
        magicCod = jsonMagicNumber[k]['signs'][0][2:]
        mimeType = jsonMagicNumber[k]['mime']
        if(hexdata.find(bytes(magicCod, 'utf-8')) != -1):
            #we have find the magic number :)
            lista.append((fileFormat, mimeType, magicCod))
    return lista, blob

def stampaHTML(tag, mime, blob):
    TEMPLATE = f'<!DOCTYPE html><html><head><title>render</title></head><body><{tag} src="data:{mime};base64,{blob}"/></body></html>'
    with open('render.html', 'w') as f:
        f.write(TEMPLATE)

if __name__=='__main__':
    listaCodici, blob = getFormatMimeMagic('./file_prova/imm2.png')
    stampaHTML('img', listaCodici[0][-2], blob.decode('utf-8'))
    print(listaCodici[0][-2])
    #print(blob)
