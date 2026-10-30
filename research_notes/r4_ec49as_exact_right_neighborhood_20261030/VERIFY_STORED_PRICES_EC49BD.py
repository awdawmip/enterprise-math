#!/usr/bin/env python3
"""Check the separately published 2156 rational dual multipliers without searching for prices.
Run beside the decoded VERIFY_EC49BD.py and the compressed price-list artifact.
"""
import base64, gzip, hashlib, json
from pathlib import Path
import VERIFY_EC49BD as M

SOURCE = Path(__file__).with_name('EXACT_ONLY_PRICES_EC49BD.json.gz.b64')
raw = gzip.decompress(base64.b64decode(SOURCE.read_bytes()))
assert hashlib.sha256(raw).hexdigest() == '20de2796efa75964b6e18481f3222c271fe966f0e42d605769dc066f5fe49741'
prices = [M.Q(text) for text in json.loads(raw)]
clipped = M.enumerate_polytope()
assert len(prices) == 196*11
idx = 0
least = None
for i,(e0,e1) in enumerate(zip(M.POINTS,M.POINTS[1:])):
    caps=(M.h(M.T_WITNESS[i],e0),M.h(M.T_WITNESS[i+1],e1))
    for edge,(x,y) in clipped.items():
        if M.support(x,y) in M.SPECIAL:
            continue
        lam=prices[idx];idx+=1
        assert lam >= 0
        for et,cap in zip((e0,e1),caps):
            for vertex in (x,y):
                slack=cap-M.dual(M.fibers(vertex,et),lam)
                assert slack>=0, (i,edge,lam,slack)
                least = slack if least is None else min(least,slack)
assert idx==2156
assert least==M.Q(9062167,8412406320000)
print(json.dumps({'result':'PASS','prices_checked':idx,'four_corner_inequalities':4*idx,'minimum_slack':str(least)},sort_keys=True))
