"""Optional Matplotlib hex-cell export. Floating arithmetic is display-only."""
from __future__ import annotations
import math
from pathlib import Path
from .core import validate, neighborhood

def plot_hex(data, values=None, *, center_id=None, radius=3, out=None, title=None):
    validate(data)
    if data['kind'] != 'hex':
        raise ValueError('plot_hex requires explicit hex data; never pads X6 coordinates')
    try:
        import matplotlib.pyplot as plt
        from matplotlib.collections import PolyCollection
    except ImportError as exc:
        raise ImportError('Install nollm-visual-toolkit[static] for Matplotlib export') from exc
    rows = data['records']
    if center_id is not None:
        ids = set(neighborhood(data, center_id, radius))
        rows = [r for r in rows if r['id'] in ids]
    if values is None:
        values = {r['id']: r.get('n', 0) for r in rows}
    if any(r['id'] not in values for r in rows):
        raise ValueError('One value per selected record ID is required')
    vertices = []
    R = 1/math.sqrt(3)
    for r in rows:
        q, p = r['coord']
        x, y = q+p/2, math.sqrt(3)*p/2
        vertices.append([(x+R*math.cos(math.radians(30+60*k)), y+R*math.sin(math.radians(30+60*k))) for k in range(6)])
    fig, ax = plt.subplots(figsize=(9, 8))
    pc = PolyCollection(vertices, linewidths=0)
    pc.set_array([values[r['id']] for r in rows])
    ax.add_collection(pc); ax.autoscale_view(); ax.set_aspect('equal'); ax.set_axis_off()
    ax.set_title(title or data.get('title', 'Hex implementation carrier'))
    fig.colorbar(pc, ax=ax, shrink=.75)
    fig.tight_layout()
    if out:
        out = Path(out); out.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out, dpi=180, bbox_inches='tight')
    return fig, ax
