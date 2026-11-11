import json, glob, re, sys

raw = json.load(open('data/raw.json'))
uniq = json.load(open('data/unique.json'))
uid = {n: i for i, n in enumerate(uniq)}

steps = [None] * len(uniq)
for f in sorted(glob.glob('data/steps/*.txt')):
    for line in open(f):
        line = line.rstrip('\n')
        if not line:
            continue
        i, a, b, c = line.split('|')
        steps[int(i)] = [a, b, c]
assert all(steps)

# Channel allocation by category (edit here to move a category to another channel)
CH = {
    'sports': ['Olympic & Paralympic Sports', 'Team Ball Sports', 'Bat & Ball Sports', 'Stick & Goal Sports',
               'Racket Sports', 'Athletics', 'Combat Sports & Martial Arts', 'Aquatic Sports',
               'Winter & Ice Sports', 'Motorsports', 'Cycling', 'Equestrian & Animal Sports',
               'Target & Precision Sports', 'Gymnastics & Strength', 'Extreme & Adventure Sports',
               'Air Sports', 'Cue Sports & Table Games'],
    'guess': ['Guessing Games'],
    'quiz': ['Trivia & Quiz', 'Educational Games'],
    'mind': ['Board Games', 'Card Games', 'Dice Games', 'Tile & Domino Games', 'Abstract Strategy',
             'Paper & Pencil', 'Word Games', 'Puzzle Games', 'Memory & Brain', 'Mind Sports'],
}
cat2ch = {}
for ch, cs in CH.items():
    for c in cs:
        cat2ch[c] = ch

def slug(s):
    s = s.lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

cats = []
cidx = {}
for c in raw['cats']:
    ch = cat2ch.get(c['n'], 'gaming')
    cidx[c['n']] = len(cats)
    cats.append({'n': c['n'], 'g': c['g'], 'd': c['d'], 's': slug(c['n']), 'ch': ch, 'src': c['src']})

SET = ['Indoor', 'Outdoor', 'Water', 'Ice/Snow', 'Digital', 'Air', 'Any']
items = []
for x in raw['items']:
    items.append([x['name'], cidx[x['cat']], x['origin'] or '', str(x['players'] or ''), x['equip'] or '',
                  SET.index(x['setting']), x['how'] or '', uid[x['name']]])

data = {'cats': cats, 'items': items, 'steps': steps}
js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
tpl = open('src/template.html').read()
out = tpl.replace('/*__DATA__*/null', js)
head, body = out.split('<header class="top">', 1)
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="How to play 1,716 games and sports from around the world, by category. From Pujiverse.">\n'
       '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
       + head + '</head>\n<body>\n<header class="top">' + body + '\n</body>\n</html>\n')
open('index.html', 'w').write(out)
from collections import Counter
print(len(cats), len(items), len(out) // 1024, 'KB', Counter(c['ch'] for c in cats))
