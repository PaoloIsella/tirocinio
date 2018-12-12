import abc

class HTML(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, mime, blob):
        pass

class HtmlImage(HTML):
    def __init__(self, mime, blob):
        self.TEMPLATE = f'<!DOCTYPE html><html><head>' \
                        f'<title>render</title>' \
                        f'</head>' \
                        f'<body><img src="data:{mime};base64,{blob}"/>' \
                        f'</body>' \
                        f'</html>'

class HtmlPdf(HTML):
    def __init__(self, mime, blob):
        self.TEMPLATE = f'<!DOCTYPE html><html><head>' \
                        f'<title>render</title>' \
                        f'</head>' \
                        f'<body><object data="data:{mime};base64,{blob}" type="{mime}" width="100%" height="100%"/>' \
                        f'</body>' \
                        f'</html>'


class HtmlVideo(HTML):
    def __init__(self, mime, blob):
        self.TEMPLATE = f'<!DOCTYPE html><html><head>' \
                        f'<title>render</title>' \
                        f'</head>' \
                        f'<body>' \
                        f'<video width="500" height="250" controls> ' \
                        f'<source src="data:{mime};base64,{blob}" type="{mime}">' \
                        f'</video>' \
                        f'</body>' \
                        f'</html>'

class HtmlAudio(HTML):
    def __init__(self, mime, blob):
        self.TEMPLATE = f'<!DOCTYPE html><html><head>' \
                        f'<title>render</title>' \
                        f'</head>' \
                        f'<body>' \
                        f'<audio controls>  ' \
                        f'<source src="data:{mime};base64,{blob}" type="{mime}">' \
                        f'</audio>' \
                        f'</body>' \
                        f'</html>'

