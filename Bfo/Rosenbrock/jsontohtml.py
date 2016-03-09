import pandas as p

df = p.read_json('results.json')
html = df.to_html()

with open('result.html', 'w') as f:
    f.write(html)
