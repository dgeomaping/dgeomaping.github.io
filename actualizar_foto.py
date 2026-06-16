import base64, re, io
from PIL import Image

with open(r'C:\Users\lenovo\Desktop\Diego Gutierrez\DIEGO\1. EMPRESA\DGeoMaping\Fotos\deon.jpeg', 'rb') as f:
    img = Image.open(io.BytesIO(f.read()))

w, h = img.size
new_h = int(w / (16/9))
top = int(h * 0.18)
bottom = min(top + new_h, h)
top = max(0, bottom - new_h)
cropped = img.crop((0, top, w, bottom)).resize((1200, 675), Image.LANCZOS)
buf = io.BytesIO()
cropped.save(buf, format='JPEG', quality=72)
b64 = base64.b64encode(buf.getvalue()).decode()
nuevo = 'src="data:image/jpeg;base64,' + b64 + '"'

with open('index_dgeomap.html', 'r', encoding='utf-8') as f:
    html = f.read()

html2 = re.sub(r'src="data:image/jpeg;base64,[^"]+"', nuevo, html, count=1)

with open('index_dgeomap.html', 'w', encoding='utf-8') as f:
    f.write(html2)

print('FOTO ACTUALIZADA CORRECTAMENTE')