"""Independent B=18 forced-key two-H9 exact finite certificate; native ordered signed prefixes."""
from ec49fjd_shared import *
from collections import Counter,defaultdict
from pathlib import Path
import json, hashlib,time
P=Path(__file__).parent
lines=(P/'B18_CASES.tsv').read_text().splitlines()
# Independent of the C++ trie algorithm: enumerate all pairs of native signed words at H9 16/32.
results=[];stats=Counter();t0=time.monotonic()
for i,line in enumerate(lines):
 pr,q,labels,options,zero=line.split('\t')
 if len(options.split('|'))!=1:continue  # independently classified key-reallocation exceptions
 assert options.count('|')==0
 keyset=[tuple(map(int,k.split(','))) for k in options.split(';')]
 assert len(keyset)==7
 F={bytes.fromhex(p) for p in zero.split(';')}
 assert len(F)==75
 choices=[]
 for lab in [(9,16),(9,32)]:
  o=set()
  for k in keyset:
   for w in bykey[k][lab]:
    p=pref(w)
    o.add(tuple(x for x in p if x not in F))
  choices.append(o)
 union={p for cand in choices for opt in cand for p in opt}
 ind={p:j for j,p in enumerate(union)}
 a={sum(1<<ind[p] for p in x) for x in choices[0]}
 b={sum(1<<ind[p] for p in x) for x in choices[1]}
 opt=min((u|v).bit_count() for u in a for v in b)
 results.append({'profile':pr,'Q':q,'minimum_H9_pair_new_prefixes':opt,'H9_16_options':len(a),'H9_32_options':len(b)})
 stats[opt]+=1
print('EXACT_TWO_H9',len(results),'min_hist',dict(stats),'elapsed',round(time.monotonic()-t0,3),flush=True)
assert len(results)==832
assert min(stats)>=19
b=(json.dumps({'science_pin':PIN,'method':'complete two-label word-pair native signed prefix union, allowed original seven keys','results':results},sort_keys=True,separators=(',',':'))+'\n').encode()
(P/'EXACT_H9_PAIR_REPORT_B18.json').write_bytes(b)
print('PAIR_H9_B18_PASS','sha256',hashlib.sha256(b).hexdigest(),flush=True)
