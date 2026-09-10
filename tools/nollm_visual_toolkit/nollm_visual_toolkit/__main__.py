from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .core import demo_hex, demo_x6, html, read_data, write_data, validate, fingerprint, collision_groups, profile, legacy_html

def main() -> int:
    p = argparse.ArgumentParser(description='Nollm Visual Toolkit 0.2.0 — offline research workbench')
    s = p.add_subparsers(dest='command', required=True)
    d = s.add_parser('demo'); d.add_argument('--kind', choices=['hex','x6'], default='hex')
    d.add_argument('--count', type=int, default=65536); d.add_argument('--out', type=Path, required=True)
    d.add_argument('--data', type=Path)
    r = s.add_parser('render'); r.add_argument('input', type=Path); r.add_argument('--out', type=Path, required=True)
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
        elif a.command == 'render': print(html(read_data(a.input), a.out))
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
