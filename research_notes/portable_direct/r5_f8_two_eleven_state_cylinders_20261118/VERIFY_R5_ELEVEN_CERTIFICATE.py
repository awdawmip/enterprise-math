#!/usr/bin/env python3
"""Frozen R5 exact 11-state/8-error two-family certificate."""
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path

INPUT_SHA256 = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
SCIENCE_COMMIT = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
L = 25845652773852463277015040000
U = 58182461585441404127941754880
BASE = (18, 24, 82, 34, 17)
EXTENSIONS = {
 'A': (0, 16, 32, 144, 208, 240),
 'B': (0, 16, 48, 144, 208, 240),
}

def maximal(masks):
 s = set(masks)
 return tuple(sorted(m for m in s if not any(m != n and (m & n) == m for n in s)))

def by_windows(centers, tau):
 return maximal(sum(1 << i for i,c in enumerate(centers) if x <= c <= x+tau)
                for x in centers)

def by_sweep(centers, tau):
 endpoints = sorted(set(z for c in centers for z in (2*c-tau,2*c+tau)))
 at = [sum(1 << i for i,c in enumerate(centers) if abs(z-2*c) <= tau)
       for z in endpoints]
 between = [sum(1 << i for i,c in enumerate(centers) if abs(a+b-4*c) <= 2*tau)
            for a,b in zip(endpoints,endpoints[1:])]
 return maximal(at+between)

def full_actions(counts, ids, tau):
 cheapest = {}
 for k in range(214,315):
  centers = [int(counts[str(k)]['counts'][h]) for h in ids]
  w=by_windows(centers,tau)
  s=by_sweep(centers,tau)
  assert w==s, ('support_disagreement',ids,k,tau,w,s)
  cheapest[w] = min(k,cheapest.get(w,10**8))
 return sorted((cost,support) for support,cost in cheapest.items())

def solve(exe, actions, n):
 raw = '\n'.join([f'{n} 8', str(len(actions))]+
    [f'{cost} {len(support)} '+' '.join(map(str,support))
     for cost,support in actions])+'\n'
 p=subprocess.run([str(exe)],input=raw,encoding='utf-8',capture_output=True,check=True)
 d=dict(z.split('=',1) for z in p.stdout.split() if '=' in z)
 return {'cost':int(d['cost']),'memo_states':int(d['states']),
         'distinct_action_families':len(actions),'stdout':p.stdout.strip()}

def main():
 if len(sys.argv)!=3:
  sys.exit('usage: python3 VERIFY_R5_ELEVEN_CERTIFICATE.py INPUT_JSON EXACT_ELEVEN_SUBSET.cpp')
 raw=Path(sys.argv[1]).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==INPUT_SHA256
 counts=json.loads(raw)['counts_and_cohorts']
 rows=[]
 with tempfile.TemporaryDirectory() as wd:
  exe=Path(wd)/'solver'
  subprocess.run(['g++','-std=c++17','-O3',sys.argv[2],'-o',str(exe)],check=True)
  for label,added in EXTENSIONS.items():
   ids=BASE+added
   row={'label':label,'ids':ids}
   for phase,tau in [('left',L),('right_integer',U-1)]:
    actions=full_actions(counts,ids,tau)
    row[phase]=solve(exe,actions,len(ids))
    assert row[phase]['cost']==8335,(label,phase,row[phase])
   rows.append(row)
 assert len(set(EXTENSIONS['A'])&set(EXTENSIONS['B']))==5
 print(json.dumps({'schema':'R5_TWO_ELEVEN_STATE_F8_INTERVALS_V1',
      'status':'PASS_R5_TWO_ELEVEN_STATE_F8_BOTH_ENDPOINTS',
      'scientific_pin':SCIENCE_COMMIT,'input_sha256':INPUT_SHA256,
      'f':8,'base':BASE,'tau_left':str(L),'tau_right_exclusive':str(U),
      'family_count_unique':96,
      'coverage':'2*2*101 exact support-family comparisons and 4 exact roots',
      'rows':rows},indent=2,sort_keys=True))
if __name__=='__main__':main()
