from brubeck.request_handling import Brubeck
from brubeck.templating import Jinja2Rendering, load_jinja2_env

class RootHandler(Jinja2Rendering):
    def get(self):
        return self.render_template('index.html')

config = {
    'mongrel2_pair': ('ipc://127.0.0.1:9999', 'ipc://127.0.0.1:9998'),
    'handler_tuples': [(r'^/$', RootHandler)],
    'template_loader' : load_jinja2_env('./templates')
}

app = Brubeck(**config)
app.run()
