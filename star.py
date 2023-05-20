


class AHtml:
    def __init__(self):
        self.HTML = '''<!DOCTYPE html>
<html lang="zh">
'''
        self.body = '''    <body>
'''
    def init_head(self,title,cssflies=None):
        self.HTML += '''<head>
    <meta charset="UTF-8">
    <title>%s</title>
</head>
'''%title
    def body_over(self):
        self.body += '''    </body>'''
    def render(self,name):
        with open(name,'w') as f:
            f.write(self.HTML+self.body+'''
</html>''')
    def make_a_h1_text(self,text):
        self.body += '''        <h1>%s</h1>
        '''%text
    def make_a_h2_text(self,text):
        self.body += '''        <h2>%s</h2>
        '''%text
    def make_a_h3_text(self,text):
        self.body += '''        <h3>%s</h3>
        '''%text
    def make_a_h4_text(self,text):
        self.body += '''        <h4>%s</h4>
        '''%text
    def make_a_h5_text(self,text):
        self.body += '''        <h5>%s</h5>
        '''%text
    def make_a_h6_text(self,text):
        self.body += '''        <h6>%s</h6>
        '''%text
    def make_a_normal_text(self,text):
        self.body += '''        <p>%s</p>
        '''%text
        

