#!/usr/bin/env python3
"""EC49FDG exact 800-pair signed-native-prefix census; no floats or heuristic pruning.
Fixed source: frozen_model.py Git Blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
Run: python VERIFY_EC49FDG.py --case 6,5,1 6,4,1
     python VERIFY_EC49FDG.py --all   # 800 complete exact models
Compile: g++ -O3 -std=c++17 DP_EC49FDG.cpp -o exact_solver
"""
import argparse, hashlib, json, subprocess, tempfile
from pathlib import Path
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),
   (4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),
       'f':(1,-1),'g':(2,-2)}
ENC={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),
     7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
FIXED={'2:16':'fe','2:32':'ge','3:16':'feg','3:32':'gef'}
L=(4,2,1); M=(6,4,1)
WITNESS={'4:1':'gefd','4:2':'fegd','4:4':'fegc','4:8':'gefc',
         '5:16':'feggf','5:32':'geffg','6:1':'gefddd','6:2':'fegddd',
         '6:4':'fegccc','6:8':'gefccc','7:1':'gefddgf','7:2':'fegddgf',
         '7:4':'fegccfg','7:8':'gefccfg','8:1':'gefddgfg','8:2':'fegddgfg',
         '8:4':'fegccfgg','8:8':'gefccfgg','9:16':'feggffgfg','9:32':'geffggffg'}

def observe(w):
 s=0
 for c in w:
  s=T[s][OPS.index(c)]
  if s==8:return None
 return SIG[s]

def native(w):
 return ''.join(ENC[x] for c in w for x in STEPS[c])

def prefixes(w):
 s=native(w)
 return {s[:i] for i in range(1,len(s)+1)}

def language(h,key):
 x,y,z=key; b=x+y-h-1
 m0={'a':z-1,'c':0,'d':b,'e':z,'f':h+1-y-2*z,'g':h+1-x}
 out={s:[] for s in REQ[h]}
 if min(m0.values())<0:return out
 for c in range(b+1):
  m=dict(m0);m['c']=c;m['d']=b-c
  def visit(s,w):
   if len(w)==h:
    if SIG[s] in out:out[SIG[s]].append(w)
    return
   for i,op in enumerate(OPS):
    if m[op] and T[s][i]!=8:
     m[op]-=1;visit(T[s][i],w+op);m[op]+=1
  visit(0,'')
 return out

def feasible_keys(h):
 for z in range(1,(h+1)//2+1):
  for x in range(1,h+2):
   for y in range(h+2-2*z):
    if x+y<h+1:continue
    key=(x,y,z);lang=language(h,key)
    if all(lang.values()):yield key,lang

def verify_witness():
 words={**FIXED,**WITNESS}
 assert len(words)==24
 for k,w in words.items():
  h,s=map(int,k.split(':'));key=L if h<=5 else (6,5,1) if h==8 else M
  assert len(w)==h and observe(w)==s
  if h>=4:assert w in language(h,key)[s]
 fixed=set().union(*(prefixes(w) for w in FIXED.values()))
 early_late=set().union(*(prefixes(w) for k,w in words.items() if not k.startswith('8:')))
 total=set().union(*(prefixes(w) for w in words.values()))
 assert len(fixed)==16 and len(early_late)==98 and len(total)==106
 return {'witness_edges':106,'fixed_edges':16,'without_H8_edges':98,
         'words':words,'signed_native_words':{k:native(v) for k,v in words.items()}}

def build(pool,fixed):
 child=[{}];parent=[-1];weight=[0];terminal=[0];pref=['']
 for i,(label,words) in enumerate(pool.items()):
  for w in words:
   v=0
   for c in native(w):
    u=child[v].get(c)
    if u is None:
     u=len(child);child[v][c]=u
     child.append({});parent.append(v)
     pref.append(pref[v]+c);weight.append(int(pref[u] not in fixed));terminal.append(0)
    v=u
   terminal[v]|=1<<i
 return parent,weight,terminal

def exact(k8,k9,solver):
 key_by_h={h:L if h<=5 else M if h<=7 else k8 if h==8 else k9 for h in range(4,10)}
 pool={f'{h}:{s}':ws for h in range(4,10) for s,ws in language(h,key_by_h[h]).items()}
 assert len(pool)==20 and all(pool.values())
 fixed=set().union(*(prefixes(w) for w in FIXED.values()))
 assert len(fixed)==16
 parent,weight,terminal=build(pool,fixed)
 with tempfile.TemporaryDirectory() as tmp:
  p=Path(tmp)/'input.trie'
  with p.open('w') as f:
   f.write(f'{len(parent)} {len(pool)} {len(fixed)}\n')
   for a,b,c in zip(parent,weight,terminal):f.write(f'{a} {b} {c}\n')
  cp=subprocess.run([str(solver),str(p),'500'],capture_output=True,text=True,check=True)
  res=json.loads(cp.stdout)
 assert res['labels']==20 and res['fixed_edges']==16
 return {'H8':list(k8),'H9':list(k9),'total_exact_optimum':res['total_exact_optimum'],
         'candidate_words':sum(map(len,pool.values())),'trie_nodes':len(parent),
         'inspected_pairs':res['inspected_pairs']}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--case',nargs=2)
 ap.add_argument('--all',action='store_true')
 ap.add_argument('--solver',default='./exact_solver');args=ap.parse_args()
 print(json.dumps({'witness':verify_witness()['witness_edges']},sort_keys=True),flush=True)
 if not args.case and not args.all:return
 solver=Path(args.solver).resolve()
 if args.case:
  k8,k9=(tuple(int(x) for x in a.split(',')) for a in args.case)
  print(json.dumps(exact(k8,k9,solver),sort_keys=True));return
 from collections import Counter
 a=list(feasible_keys(8));b=list(feasible_keys(9));assert len(a)==50 and len(b)==16
 rows=[]
 for key8,_ in a:
  for key9,_ in b:rows.append(exact(key8,key9,solver))
 minval=min(row['total_exact_optimum'] for row in rows)
 assert minval==106 and len(rows)==800
 report={'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
         'key_counts':[len(a),len(b)],'models':len(rows),'min_cost':minval,
         'argmins':[(r['H8'],r['H9']) for r in rows if r['total_exact_optimum']==minval],
         'histogram':dict(sorted(Counter(r['total_exact_optimum'] for r in rows).items())),
         'total_checked_dp_pairs':sum(r['inspected_pairs'] for r in rows),
         'rows':rows}
 Path('EXACT_REPLAY_EC49FDG.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='rows'},sort_keys=True))
if __name__=='__main__':main()
