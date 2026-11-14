#!/usr/bin/env python3
"""EC49FOO exact independent root-prefix union check (stdlib only)."""
import itertools, json

A = {7:{7:"0701",13:"070203"}, 6:{7:"060102",13:"060103"}}
B = {7:{7:"070102",13:"070103"}, 6:{7:"060203",13:"0601"}}

def prefixes(code):
    assert len(code)>=4 and len(code)%2==0
    return {code[:i] for i in range(4,len(code)+1,2)}

def cost(config,root,S):
    return len(set().union(*(prefixes(config[root][l]) for l in S)))

def tab(config):
    return {str(r):{",".join(map(str,S)):cost(config,r,S)
                    for j in range(3) for S in itertools.combinations((7,13),j)}
            for r in (6,7)}

def terminal(config,x,y):
    return sum(cost(config,r,(l for l,s in ((7,x),(13,y)) if r==s))
               for r in (6,7))

tables={"A":tab(A),"B":tab(B)}
tA={f"{x},{y}":terminal(A,x,y) for x,y in itertools.product((6,7),repeat=2)}
tB={f"{x},{y}":terminal(B,x,y) for x,y in itertools.product((6,7),repeat=2)}
assert tA==tB=={"6,6":3,"6,7":4,"7,6":3,"7,7":3}
delta={str(r):{S:tables["B"][str(r)][S]-tables["A"][str(r)][S]
               for S in tables["A"][str(r)]} for r in (6,7)}
assert delta["7"]=={"":0,"7":1,"13":0,"7,13":0}
assert delta["6"]=={"":0,"7":0,"13":-1,"7,13":0}
shared={str(r):[len(prefixes(config[r][7])&prefixes(config[r][13]))
                for config in (A,B)] for r in (6,7)}
assert shared=={"6":[1,0],"7":[0,1]}

# EC49FON hub-gauge coefficients: +unary_13 -interaction_{06,7,13}.
for ha,hb in itertools.product((0,1),repeat=2):
    H=int(not hb)-int(not ha and not hb)
    R=-int(not hb)+int(not ha and not hb)
    keyH=",".join(str(l) for l,v in ((7,ha),(13,hb)) if v)
    keyR=",".join(str(l) for l,v in ((7,ha),(13,hb)) if not v)
    assert delta["7"][keyH]==H
    assert delta["6"][keyR]==R
out={"schema":"EC49FOO_TWO_ROOT_PREFIX_NATIVE_GAUGE_V1",
     "science_pin_preserved":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
     "fixture":{"A":A,"B":B}, "root_cost_tables":tables,
     "terminal_costs":tA,"terminal_equal":True,
     "root_delta":delta,"shared_prefix_depths":shared,
     "kernel_basis":{"unary_13":1,"nonlinear_06_7_13":-1},
     "maximum_postroot_depth":2,
     "scope":"Constructed native prefix-operator key pair; outside frozen 94-key repertoire"}
print(json.dumps(out,sort_keys=True,indent=2))
