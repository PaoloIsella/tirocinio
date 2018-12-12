import magic
import base64
import factory_html

class DumpRender:
    def __init__(self, nomeFile):
        try:
            self.mime = magic.from_file(nomeFile, mime=True)
            with open(nomeFile, 'rb') as f:
                self.blob = base64.b64encode(f.read())
        except FileNotFoundError as e:
            raise e.strerror

        self.factory = factory_html.FactoryHTML()

    def printHTML(self, nomepagina):
        contenuto = self.factory.getHTML(self.mime, self.blob.decode('utf-8'))
        with open(nomepagina, 'w') as f:
            f.write(contenuto)

if __name__=='__main__':
    renderPdf = DumpRender('./file_prova/montacarichi.pdf')
    renderImm = DumpRender('./file_prova/imm.jpg')
    renderImm2 = DumpRender('./file_prova/imm2.png')
    renderAudio = DumpRender('./file_prova/hangouts_incoming_call.ogg')
    renderVideo = DumpRender('./file_prova/video.mp4')
    renderPdf.printHTML('renderPDF.html')
    renderImm.printHTML('renderIMM.html')
    renderImm2.printHTML('renderIMM2.html')
    renderAudio.printHTML('renderaudio.html')
    renderVideo.printHTML('renderVideo.html')
