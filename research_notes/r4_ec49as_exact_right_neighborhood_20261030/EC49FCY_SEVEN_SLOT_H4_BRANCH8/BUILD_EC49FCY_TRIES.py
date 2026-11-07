"""Reproducible finite signed-native prefix trie input generation for EC49FCY.
Run next to the EC49FCS frozen_model.py in the original repository tree.
"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
FROZEN = HERE.parent / 'EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256'
sys.path.insert(0, str(FROZEN))
from frozen_model import W, STEPS, ENC, observe, candidates, primpref  # pinned source

CH = {f'{h}:{observe(w)}': w for h, words in W.items() for w in words}
assert len(CH) == 24
PREFIX = {k: set(primpref(w)) for k, w in CH.items()}
assert len(set().union(*PREFIX.values())) == 158

def signed(word):
    return ''.join(ENC[step] for op in word for step in STEPS[op])

def build(keys, output):
    fixed = set().union(*(v for k,v in PREFIX.items() if k not in keys))
    parent, edge, terminal, children, prefixes = [-1], [0], [0], [{}], ['']
    pools = {}
    for label, key in enumerate(keys):
        h, sig = map(int, key.split(':'))
        words = candidates(h)[sig]
        assert CH[key] in words
        pools[key] = len(words)
        for word in words:
            v = 0
            for ch in signed(word):
                if ch not in children[v]:
                    u = len(parent)
                    children[v][ch] = u
                    parent.append(v)
                    prefixes.append(prefixes[v]+ch)
                    edge.append(int(prefixes[u] not in fixed))
                    terminal.append(0)
                    children.append({})
                v = children[v][ch]
            terminal[v] |= (1 << label)
    with output.open('w') as f:
        f.write(f'{len(parent)} {len(keys)} {len(fixed)}\n')
        for p,e,t in zip(parent,edge,terminal):f.write(f'{p} {e} {t}\n')
    return {'slots': keys, 'fixed_edges': len(fixed), 'nodes': len(parent),
            'candidate_counts': pools, 'input_file': output.name}

def run(dest):
    dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for branch in ('A','B'):
        other = (['5:16','6:1','7:1','8:2','8:4','9:16'] if branch=='A' else
                 ['5:32','6:1','7:1','8:1','8:8','9:32'])
        for s in (1,2,4,8):
            rows.append(build([f'4:{s}']+other, dest/f'{branch}_H4_{s}.trie.txt'))
    (dest/'build_summary.json').write_text(json.dumps(rows,indent=2)+'\n')
    return rows
if __name__=='__main__':
    print(json.dumps(run(Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'generated'), indent=2))
