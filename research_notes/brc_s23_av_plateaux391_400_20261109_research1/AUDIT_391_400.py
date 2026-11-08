#!/usr/bin/env python3
"""Independent exact endpoint identity audit; not a replacement for critical-cell coverage."""
import hashlib,importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'brc_s23_av_plateau20_20261108_r1'/'VERIFY_PLATEAUX20_200.py'
b=p.read_bytes()
assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()=='261d7e22da0e62d667009cb50acfe77ac4e35c3f'
spec=importlib.util.spec_from_file_location('checker',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[(391,148713867,811715196,74154),(392,149094241,813790480,74477),
(393,149474615,815865685,74802),(394,149854910,817940380,75495),
(395,150235284,820015664,75822),(396,150615579,822090359,76150),
(397,150995953,824165643,76478),(398,151376327,826240848,76806),
(399,151756622,828315543,77135),(400,152136996,830390827,77467)]
prev=148333572
for i,H,M,cells in rows:
    ww=m.get_witnesses(i)
    ix,ai,V,K,dl,du=ww[-1]
    assert ix==i
    assert ai*m.EU<i*m.DL and i*m.DU<(ai+1)*m.EL
    assert H==V+510 and M==K+V-ww[-2][2]-1
    assert H==prev+380295+79*(ai-ww[-2][1])
    prev=H
assert sum(t[3] for t in rows)==758786
print('PASS_10_EXACT_ENDPOINT_AND_FLOOR_AUDIT',prev,rows[-1][2],
      'sum_critical_cells',sum(t[3] for t in rows))
