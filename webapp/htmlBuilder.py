import re

class htmlBuilder:

    htmlString = ""
    def __init__(self):
        self.htmlString += \
        """
            <!DOCTYPE html>
            <html lang="en">

	        <head>
		        <meta charset="utf-8"/>
		        <title></title>
		    </head>
		    
		    <body>
		        <h1>
		    </body>
        """

    # def setTitle(self, title):
    #     titleTagStart = self.getIndicesOf(self, '<title>')
    #     titleTagEnd = titleTagStart + 8
    #
    #     newString = self.htmlString[:titleTagEnd] + title + self.htmlString[titleTagEnd:]
    #     self.htmlString = newString
    #
    # def setBody
    # def getIndicesOf(self, key):
    #     return [m.start() for m in re.finditer(key, self.htmlString)]


