class webPage():
    def __init__(self,cleaner=None):
        pass
    def __top(self):
        return """
            <html>
                <head>
                <link href="/static/style.css" rel="stylesheet">
                </head>
            <body>"""
    def __foot(self):
        return """
            </body>
        </html>"""
    def middle(self):
        return ""
    def index(self):
        return self.__top()+self.middle()+self.__foot()
    index.exposed=True