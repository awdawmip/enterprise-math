#!/usr/bin/env python3
"""Exact 256x101 split-band scalar fiber-product verification."""
import hashlib,json,sys
from pathlib import Path
from collections import defaultdict
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
LOW=tuple(range(214,222));HIGH=tuple(range(222,315));ALL=LOW+HIGH
U=58182461585441404127941754880
def check(filename):
 raw=Path(filename).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
 src=json.loads(raw);assert tuple(src['effective_cuts'])==(3,8,9,10,15,17,25,27)
 t=src['counts_and_cohorts'];assert len(t)==101
 counts={k:tuple(int(v) for v in t[str(k)]['counts']) for k in ALL}
 assert all(len(v)==256 for v in counts.values())
 low={};high={}
 for h in range(256):
  u=h&0x8F;v=h&0xF0
  a=tuple(counts[k][h] for k in LOW)
  b=tuple(counts[k][h] for k in HIGH)
  assert u not in low or low[u]==a
  assert v not in high or high[v]==b
  low[u]=a;high[v]=b
 assert len(low)==32 and len(high)==16
 assert len(set(low.values()))==32 and len(set(high.values()))==16
 assert len({counts[214][u] for u in low})==32
 assert len({(counts[223][v],counts[294][v]) for v in high})==16
 fibers=defaultdict(list)
 for h in range(256):fibers[(h&0x8F,h&0xF0)].append(h)
 possible={(u,v) for u in low for v in high if (u&0x80)==(v&0x80)}
 assert len(possible)==256 and possible==set(fibers)
 assert all(len(fibers[x])==1 and fibers[x][0]==(x[0]|(x[1]&0x70)) for x in possible)
 assert len([u for u in low if u&0x80])==16 and len([v for v in high if v&0x80])==8
 assert all(counts[k][5]==counts[k][6] for k in HIGH)
 gaps={k:abs(counts[k][5]-counts[k][6]) for k in LOW}
 assert all(z>=U for z in gaps.values())
 assert min(gaps,key=gaps.get)==221
 assert min(gaps.values())==217549739175592676504371200000
 assert len({tuple(counts[k][h] for k in ALL) for h in range(256)})==256
 return dict(verified_entries=256*101,low_classes=32,high_classes=16,shared_bit=7,compatible_pairs=len(possible),components='two K_16,8',low_decoder=[214],high_decoder=[223,294],high_5_6_equal=len(HIGH),low_5_6_separable=len(LOW),min_5_6_gap=str(min(gaps.values())))
if __name__=='__main__':
 if len(sys.argv)!=2:raise SystemExit('Usage: script.py frozen_table.json')
 print(json.dumps(check(sys.argv[1]),sort_keys=True,indent=2))
 print('PASS_R5_SPLIT_BAND_FIBER_PRODUCT_256_BY_101',file=sys.stderr)
