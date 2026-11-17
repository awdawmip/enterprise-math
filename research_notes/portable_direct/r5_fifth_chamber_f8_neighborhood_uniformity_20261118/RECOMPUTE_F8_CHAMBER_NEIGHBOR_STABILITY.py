#!/usr/bin/env python3
"""Recalculate exact 1255 five-state replacements and 251 six-state extensions at U-1.
Supply the immutable earlier R5 files in the same directory:
 EXACT_R5_ALL_101_BUDGETS.json (original 101x256 integer table)
 RESULTS_COMPACT.json (left-endpoint root costs, prior one-exchange certificate)
 VERIFY_EXACT_SMALL_MINIMAX.cpp (prior exact C++17 Bellman engine)
The solver uses exact integer center distances and counter states, no float noise.
"""
import base64, collections, hashlib, itertools, json, subprocess, zlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
H0=(18,24,82,34,17)
L=25845652773852463277015040000
U=58182461585441404127941754880
T1=39667188909509775772876800000
T2=42621568083499305947627520000
PIN_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'

raw=(HERE/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()==PIN_SHA
table=json.loads(raw)['counts_and_cohorts']
assert set(map(int,table))==set(range(214,315))
assert all(len(table[str(k)]['counts'])==256 for k in range(214,315))
prior=json.loads((HERE/'RESULTS_COMPACT.json').read_text())
indices=zlib.decompress(base64.b64decode(prior['per_neighbor_level_indices_zlib_base64']))
old=[prior['value_levels'][j] for j in indices]
assert len(old)==1255 and prior['original_V']==8335

binary=HERE/'_exact_neighbor_solver'
subprocess.run(['g++','-O3','-DNDEBUG','-std=c++17',str(HERE/'VERIFY_EXACT_SMALL_MINIMAX.cpp'),'-o',str(binary)],check=True)
def cost(H,tau):
    cheapest={}
    for k in range(214,315):
        counts=table[str(k)]['counts']
        vals={}
        for j,h in enumerate(H):
            c=int(counts[h]);vals[c]=vals.get(c,0)|(1<<j)
        supports={sum(bits for c,bits in vals.items() if lo<=c<=lo+tau) for lo in vals}
        maximal=tuple(sorted(x for x in supports if not any(x!=y and (x&y)==x for y in supports)))
        cheapest.setdefault(maximal,k)
    lines=[f'{len(H)} {len(cheapest)}']
    lines += [f'{k} {len(f)} '+' '.join(map(str,f))
              for f,k in sorted(cheapest.items(),key=lambda x:x[1])]
    tmp=HERE/'_neighbor_actions.tmp'
    tmp.write_text('\n'.join(lines)+'\n')
    result=subprocess.run([str(binary),str(tmp),'8'],text=True,capture_output=True,check=True)
    d=dict(part.split('=',1) for part in result.stdout.split() if '=' in part)
    return int(d['V']),int(d['states']),len(cheapest)

hs=[h for h in range(256) if h not in H0]
right5=[];exceptions=[]
for i in range(5):
    for j,h in enumerate(hs):
        v,states,actions=cost(H0[:i]+(h,)+H0[i+1:],U-1)
        before=old[i*251+j]
        assert before<=v<=8326,(i,h,before,v)
        if before!=v:exceptions.append((i,h,before,v))
        right5.append({'index':i,'h':h,'V':v,'states':states,'actions':actions})
assert exceptions==[(2,144,6328,6337),(2,208,6328,6337)],exceptions
assert sum(x['states'] for x in right5)==33758805
assert len(collections.Counter(x['V'] for x in right5))==18

right6=[]
for h in hs:
    v,states,actions=cost(H0+(h,),U-1)
    assert v==8335,(h,v)
    right6.append({'h':h,'V':v,'states':states,'actions':actions})
assert len(right6)==251 and sum(x['states'] for x in right6)==29387425
assert cost(H0,L)[0]==cost(H0,U-1)[0]==8335

for h in (144,208):
    H=H0[:2]+(h,)+H0[3:]
    gaps=set()
    for k in range(214,315):
        centers=[int(table[str(k)]['counts'][m]) for m in H]
        for a,b in itertools.combinations(centers,2):
            d=abs(a-b)
            if L<d<U: gaps.add(d)
    assert gaps=={T1,T2},(h,gaps)
    assert cost(H,L)[0]==6328
    assert cost(H,T1)[0]==6328
    assert cost(H,T2-1)[0]==6328
    assert cost(H,T2)[0]==6337

for name,rows in [('RIGHT_ONE_EXCHANGE_F8.jsonl',right5),
                  ('RIGHT_SIX_EXTENSION_F8.jsonl',right6)]:
    (HERE/name).write_text(''.join(json.dumps(row,separators=(',',':'))+'\n' for row in rows))
print('PASS_R5_F8_UNIFORM_NEIGHBORHOOD_EXCEPT_TWO_THRESHOLD_SWAPS')
print('five',len(right5),'six',len(right6),'exceptions',exceptions)
(HERE/'_neighbor_actions.tmp').unlink(missing_ok=True)
binary.unlink(missing_ok=True)
