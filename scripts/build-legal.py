#!/usr/bin/env python3
"""Génère les pages juridiques HTML de proposition/ à partir des .md à la racine.

Les .md restent la source : modifier le .md puis relancer
    python3 scripts/build-legal.py
Les encadrés « ⚠️ » (notes de travail) ne sont pas publiés ; les champs
entre crochets restant à compléter ([DATE…]) sont surlignés.
"""
import html, re, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = [
    ('mentions-legales.md', 'mentions-legales.html', 'Mentions légales'),
    ('cgvu-lokentia.md', 'cgvu.html', 'CGVU'),
    ('politique-confidentialite.md', 'confidentialite.html', 'Confidentialité'),
    ('dpa-sous-traitance.md', 'sous-traitance.html', 'Sous-traitance (DPA)'),
]

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\[([^\]]+)\]', r'<mark>[\1]</mark>', t)
    t = re.sub(r'\b([\w.+-]+@[\w-]+\.[\w.]+)\b', r'<a href="mailto:\1">\1</a>', t)
    return t

def convertir(md):
    out, para, lignes = [], [], md.splitlines()
    def flush():
        if para:
            out.append('<p>' + '<br>'.join(inline(l) for l in para) + '</p>')
            para.clear()
    i = 0
    while i < len(lignes):
        l = lignes[i].rstrip()
        if l.startswith('>'):            # note de travail : non publiée
            flush(); i += 1; continue
        if not l.strip() or l.strip() == '---':
            flush(); i += 1; continue
        m = re.match(r'(#{1,3}) (.*)', l)
        if m:
            flush(); n = len(m.group(1))
            out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if l.startswith('|'):
            flush(); rows = []
            while i < len(lignes) and lignes[i].startswith('|'):
                cells = [c.strip() for c in lignes[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            t = ['<div class="table"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>']
            t += ['<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:]]
            out.append(''.join(t) + '</tbody></table></div>'); continue
        para.append(l.strip()); i += 1
    flush()
    return '\n'.join(out)

GABARIT = (RACINE / 'scripts' / 'legal-template.html').read_text()

for src, dst, court in PAGES:
    corps = convertir((RACINE / src).read_text())
    titre = re.search(r'<h1>(.*?)</h1>', corps).group(1)
    titre_txt = re.sub('<[^>]+>', '', titre)
    nav = ''.join(f'<a href="{d}"{" aria-current=\"page\"" if d == dst else ""}>{c}</a>' for _, d, c in PAGES)
    page = (GABARIT.replace('{{TITRE}}', html.escape(titre_txt))
                   .replace('{{NAV}}', nav).replace('{{CORPS}}', corps))
    (RACINE / 'proposition' / dst).write_text(page)
    print('écrit', dst)
