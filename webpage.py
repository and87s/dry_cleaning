class webPage():
    def __init__(self,cleaner=None):
        pass
    def __top(self):
        return """
        <!doctype html>
            <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
                    <link href="/static/css/bootstrap-reboot.min.css" rel="stylesheet">
                    <link href="/static/css/style.css" rel="stylesheet">
                </head>
            <body>
                <div class="container">
                    """
    def __foot(self):
        return """
                </div>
                <script src="/static/js/bootstrap.min.js">
            </body>
        </html>"""
    def middle(self):
        return ""
    def index(self):
        return self.__top()+self.middle()+self.__foot()
    index.exposed=True