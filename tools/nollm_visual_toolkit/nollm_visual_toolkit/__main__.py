from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .core import VERSION, demo_hex, demo_x6, html, read_data, write_data, fingerprint, collision_groups, profile, legacy_html
from .web import build_site, demo_site, serve_preview


def _preview_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('--preview', action='store_true', help='serve the generated HTML/site on localhost after writing')
    parser.add_argument('--no-open', action='store_true', help='do not ask the default browser to open')


def main() -> int:
    p = argparse.ArgumentParser(description=f'Nollm Visual Toolkit {VERSION} — offline research workbench + static web preview')
    s = p.add_subparsers(dest='command', required=True)

    d = s.add_parser('demo', help='generate a self-contained demo workbench')
    d.add_argument('--kind', choices=['hex','x6'], default='hex')
    d.add_argument('--count', type=int, default=65536)
    d.add_argument('--out', type=Path, required=True)
    d.add_argument('--data', type=Path)
    _preview_args(d)

    r = s.add_parser('render', help='render JSON/CSV data as one self-contained HTML workbench')
    r.add_argument('input', type=Path)
    r.add_argument('--out', type=Path, required=True)
    _preview_args(r)

    site = s.add_parser('site', help='generate a static preview site with landing page and workbench pages')
    site.add_argument('inputs', type=Path, nargs='*', help='optional JSON/CSV datasets; without inputs built-in demos are used')
    site.add_argument('--out', type=Path, required=True)
    site.add_argument('--title', default='Nollm Visual Preview')
    site.add_argument('--hex-count', type=int, default=65536, help='built-in hex demo size when no inputs are supplied')
    site.add_argument('--no-x6', action='store_true', help='omit the built-in X6 demo when no inputs are supplied')
    _preview_args(site)

    pv = s.add_parser('preview', help='serve one generated HTML file or a static-site directory locally')
    pv.add_argument('target', type=Path)
    pv.add_argument('--host', default='127.0.0.1')
    pv.add_argument('--port', type=int, default=0, help='0 chooses a free port')
    pv.add_argument('--allow-remote', action='store_true', help='explicitly allow binding a non-loopback host')
    pv.add_argument('--no-open', action='store_true')

    v = s.add_parser('validate'); v.add_argument('input', type=Path)
    c = s.add_parser('convert'); c.add_argument('input', type=Path); c.add_argument('--out', type=Path, required=True)
    l = s.add_parser('import-legacy'); l.add_argument('input', type=Path); l.add_argument('--out', type=Path, required=True)
    pr = s.add_parser('profile'); pr.add_argument('input', type=Path); pr.add_argument('--axis', required=True); pr.add_argument('--out', type=Path, required=True)

    a = p.parse_args()
    try:
        if a.command == 'demo':
            data = demo_hex(a.count) if a.kind == 'hex' else demo_x6()
            html(data, a.out)
            if a.data: write_data(data, a.data)
            print(a.out)
            if a.preview: serve_preview(a.out, open_browser=not a.no_open)
        elif a.command == 'render':
            print(html(read_data(a.input), a.out))
            if a.preview: serve_preview(a.out, open_browser=not a.no_open)
        elif a.command == 'site':
            if a.inputs:
                datasets = [(path.stem, read_data(path)) for path in a.inputs]
                manifest = build_site(datasets, a.out, title=a.title)
            else:
                manifest = demo_site(a.out, hex_count=a.hex_count, include_x6=not a.no_x6, title=a.title)
            print(a.out / 'index.html')
            print(json.dumps(manifest, ensure_ascii=False, indent=2))
            if a.preview: serve_preview(a.out, open_browser=not a.no_open)
        elif a.command == 'preview':
            serve_preview(a.target, host=a.host, port=a.port, allow_remote=a.allow_remote, open_browser=not a.no_open)
        elif a.command == 'convert': write_data(read_data(a.input), a.out); print(a.out)
        elif a.command == 'import-legacy': write_data(legacy_html(a.input), a.out); print(a.out)
        elif a.command == 'profile':
            axis = 's' if a.axis == 's' else int(a.axis)
            a.out.parent.mkdir(parents=True, exist_ok=True)
            a.out.write_text(json.dumps(profile(read_data(a.input),axis),ensure_ascii=False),encoding='utf-8'); print(a.out)
        elif a.command == 'validate':
            data = read_data(a.input)
            print(json.dumps({'valid':True,'records':len(data['records']), 'kind':data['kind'],
                'sha256':fingerprint(data), 'coincident_projection_groups':len(collision_groups(data))},ensure_ascii=False,indent=2))
        return 0
    except (ValueError, KeyError, OSError, TypeError) as exc:
        p.exit(2, f'error: {exc}\n')

if __name__ == '__main__':
    sys.exit(main())
