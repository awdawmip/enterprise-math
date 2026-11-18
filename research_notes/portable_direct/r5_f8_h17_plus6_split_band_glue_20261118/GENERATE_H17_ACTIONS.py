#!/usr/bin/env python3
"""Reconstruct H17 integer maximal supports from frozen table, fail on incorrect checksum."""
import hashlib,json,sys
from pathlib import Path
H=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5,6)
K=(214,215,216,223,296)
TAU=58182461585441404127941754879
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
def maximal_supports(values):
    centers={}
    for i,value in enumerate(values):centers[value]=centers.get(value,0)|(1<<i)
    supports={sum(mask for value,mask in centers.items() if start<=value<=start+TAU) for start in centers}
    return sorted(s for s in supports if not any(s!=other and s&other==s for other in supports))
def run(path):
    b=Path(path).read_bytes(); assert hashlib.sha256(b).hexdigest()==SHA
    table=json.loads(b)['counts_and_cohorts']
    rows=[f'{len(H)} {len(K)}']
    for k in K:
       vals=[int(table[str(k)]['counts'][i]) for i in H]
       masks=maximal_supports(vals)
       rows.append(f'{k} {len(masks)} '+' '.join(map(str,masks)))
    return '\n'.join(rows)+'\n'
if __name__=='__main__':
    if len(sys.argv) not in (2,3):raise SystemExit('Usage: python script.py input.json [output.txt]')
    data=run(sys.argv[1]);print(data,end='')
    if len(sys.argv)==3:
       path=Path(sys.argv[2]);assert data==path.read_text()
       print('PASS_R5_H17_MAXIMAL_SUPPORTS_EXACT',file=sys.stderr)
