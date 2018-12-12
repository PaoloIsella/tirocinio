import html_page

class FactoryHTML:
    def __init__(self):
        pass

    def getHTML(self, mime, blob):
        if(mime.startswith('image')):
            m = mime.split('/')[1]
            if(m == 'png' or m == 'jpeg' or m == 'gif'):
                return html_page.HtmlImage(mime, blob).TEMPLATE
        elif(mime == 'application/pdf'):
           return html_page.HtmlPdf(mime, blob).TEMPLATE
        elif(mime.startswith('video')):
            m = mime.split('/')[1]
            if(m == 'mp4' or m == 'webm' or m == 'ogg'):
                return html_page.HtmlVideo(mime, blob).TEMPLATE
        elif(mime.startswith('audio')):
            m = mime.split('/')[1]
            if(m == 'mpeg' or m == 'ogg' or m == 'wav'):
                return html_page.HtmlAudio(mime, blob).TEMPLATE
        else:
            return None
