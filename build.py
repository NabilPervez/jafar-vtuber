import base64, pathlib
root = pathlib.Path(__file__).parent
art = base64.b64encode((root/'art/jafar.png').read_bytes()).decode()
html = (root/'src/app.html').read_text().replace('__ART__', 'data:image/png;base64,' + art)
(root/'index.html').write_text(html)
print('index.html', len(html)//1024, 'KB')
