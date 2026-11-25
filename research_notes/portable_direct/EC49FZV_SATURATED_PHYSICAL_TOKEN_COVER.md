# EC49FZV — Saturated physical-token set cover

2026-11-25. Parent EC49FZU at 9d691a3acf1fa3cf97735ae0593ff83147597a55:research_notes/portable_direct/EC49FZU_FORCED_HOLE_ROW_DOMINANCE.md; parent artifact commit 4f5a05824539773c05bf0805b5340dcc955444fc. Frozen BRC16943: 10 rows, m=25, h=14; fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923, parent archive manifest verified locally. Current topic receipt r4-20261125-1828-ec49as-read SUCCEEDED at ad9c7c76b748ff3b3115cc41aa53f5d0b621c3a6: NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. Independent portable science; historical author EM-DIRECT-23537B, current private binding unconfirmed; no shared CLAIM, Result, Review or identity adoption.

## Theorem and proof

Use FZU's genuine AND-query history, common positive anchor, target x=(U,H), |H|=h, B=B_U, O=H minus B. All free holes O require an observation, since the same-support state H minus {j} exists. FZU eliminates optional forced holes through historical zero witness row domination. Let Q be the rivals V!=U with |B_V union O|<=h; each clause is excluded by a row in U xor V or a normal column in B_V minus H. Write R_r={V in Q:r in U xor V} and L_j={V in Q:j in B_V minus H} for j outside H.

Define the physical-token family
  K={R_r union L_j : r in U,j outside H} union {R_r:r outside U}.
Then the minimum saturated path certificate cost is exactly |O|+sc(Q,K), where sc is ordinary unit-cost set cover. The proof has two directions. For an optimal FZU certificate with selected rows T and normal columns P, pair positive rows T intersect U and P arbitrarily, padding the shorter list by the common positive anchor row or column. Each pair is a physical query with positive target answer and excludes the union R_r union L_j of the two clauses. Negative rows are paid separately using the anchor normal column; the free holes are tested using the anchor row. The number of extra observations is |T minus U|+max(|T intersect U|,|P|), exactly the FZU cost. Conversely a cover by physical tokens yields T and P from its representatives, with |T minus U|+max(|T intersect U|,|P|) at most the number of tokens; observing O first excludes all rivals with excessive capacity, then the tokens exclude every remaining support and saturation identifies H uniquely in U. FZU thus gives the reverse inequality. Both U and the normal-column set are nonempty by the positive anchor. The argument also covers Q empty with cost |O|. Tokens with contained signatures may be dropped for this fixed-target path certificate, retaining an actual representative; this is not a global adaptive-query deletion. The decision predicate for residual e, remaining d, chooses any v in e and recurses on e minus t for tokens t containing v, with empty e true and nonempty e at d=0 false. It is exact by induction; selecting a least-frequency clause affects work only. This removes the separate row-subset enumeration in the FZU certificate optimizer. A stronger runtime claim is not made. The same theorem applies after actual first-query contraction via FZT/FZU.

## Local implementation and verification

New generator build_v.py below inserts the exact bounded predicate in tight.cpp before candidate enumeration. Gate: k<=5, b=h-|B_U| within [0,p], p<=5, b>=k-1; enumerate every free-hole subset o of size b in this selected support; one impossible certificate prunes the adaptive node. Other targets are skipped, never excluded by this gate. C++ still replays all YES physical states. The independent Python token_check.py below tests the full optimizer without this gate against the explicit physical-query cover and FZU optimizer. 80 small histories, 1280 fixed-first comparisons; 185 frozen roots (indices 0,13,...), unconditioned and one seeded conditioned target each, 370 exact cost comparisons, all agree. Aggregate 3793 distinct nonempty token masks before dominance, 654 maximal masks after dominance. No speed claim. Frozen arithmetic uses exact integer masks and parent BRC16943 coordinate input, not a native heartbeat evolution experiment.

Eight common 150000-node roots: same 1 YES / 1 NO / 6 UNKNOWN; only one saturated prune, node totals unchanged because the last affected root reached cap. Concurrent timing 14.39 vs 14.48 sec (not a controlled wall-clock speed estimate). Eight further 200000-node roots: 5 YES / 2 NO / 1 UNKNOWN, 7.18 sec. Combined 1695183 search nodes, 1229 saturated checks, 2 saturation prunes, 9218 actual-label YES replays. All 3 NO independently crosschecked with unchanged parent tight.cpp; no classification conflict. Raw rows (id,n,status,calls,envelopePrunes,satChecks,satPrunes):
```csv
1773,1451,0,150001,4515,143,0
1813,1495,0,150001,2598,168,0
1815,1499,0,150001,3897,88,0
1818,1511,-1,116568,4312,188,0
1819,1511,0,150001,1804,95,0
1821,1514,0,150001,4084,147,0
1825,1524,1,109809,2187,50,0
1826,1524,0,150001,7645,114,1
1827,1525,-1,179090,9113,147,1
1828,1526,0,200001,7351,44,0
1829,1535,1,33413,289,18,0
1830,1537,1,26674,251,21,0
1833,1540,1,13895,114,0,0
1834,1541,1,34362,367,2,0
1835,1541,1,34362,367,2,0
1836,1541,-1,47003,614,2,0
```
Baseline first eight:
```csv
1773,1451,0,150001,4515
1813,1495,0,150001,2598
1815,1499,0,150001,3897
1818,1511,-1,116568,4312
1819,1511,0,150001,1804
1821,1514,0,150001,4084
1825,1524,1,109809,2187
1826,1524,0,150001,7646
```
Remaining NO baseline:
```csv
1827,1525,-1,179091,9114
1836,1541,-1,47003,614
```
Totals 1863 YES, 23 NO, 507 UNKNOWN of 2393. Ordered 3761 YES, 40 NO, 894 UNKNOWN of 4695. 25<=M14<=27 unchanged. Next: investigate cheaper saturation-gate selection, and conditional first-query token covers for tight paths; preserve all prior closed roots. AUTHOR_PROVED / EXACT_FINITE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.

## Reproduction source

Use parent archive (FZU) unchanged, including tight.cpp, gen.py, fourth.py, forced_hole.py, retry_u.py. Derive retry_v.py by replacing 't.csv' with 't.csv','u.csv' and ==521 with ==516 in retry_u.py. Generate v.in and v2.in with python retry_v.py 0 8 150000 and python retry_v.py 8 16 200000. Compile g++ -O3 -std=c++17 sat_token.cpp. The following generator reproduces the actual source.
```python
from pathlib import Path
s=Path('tight.cpp').read_text().replace('int cap,calls=0,envelopePrunes=0;', 'int cap,calls=0,envelopePrunes=0,satChecks=0,satPrunes=0;')
a=''' // Saturated support-token cover (FZU + FZV).
 if(k<=5){
 for(int i=0;i<(int)ids.size();i++){
   int p=free[i],u=F[ids[i]],f=A[i]^B[i],b=H-pc(B[i]);
   if(b<0||b>p||p>5||b<k-1)continue;
   for(int o=f;;o=(o-1)&f){
     if(pc(o)==b){
       ++satChecks;
       int h=B[i]|o;W all=0;
       array<W,10> row{};array<W,M> col{};
       for(int j=0;j<(int)ids.size();j++)if(i!=j&&pc(B[j]|o)<=H){
         W bit=W(1)<<j;all|=bit;int diff=u^F[ids[j]],holes=B[j]&~h;
         for(int t=diff;t;t&=t-1)row[__builtin_ctz(t)]|=bit;
         for(int t=holes;t;t&=t-1)col[__builtin_ctz(t)]|=bit;
       }
       vector<W> tokens;
       for(int r=0;r<10;r++)if(u>>r&1){
         for(int j=0;j<M;j++)if(!(h>>j&1))tokens.push_back(row[r]|col[j]);
       }else tokens.push_back(row[r]);
       sort(tokens.begin(),tokens.end(),[](W a,W b){return make_pair(-pc(a),a)<make_pair(-pc(b),b);});
       vector<W> maximal;for(W t:tokens){if(!t)continue;bool dom=false;for(W v:maximal)if(!(t&~v)){dom=true;break;}if(!dom)maximal.push_back(t);}
       auto can=[&](auto&& self,W e,int rem)->bool{
         if(!e)return true;if(rem<=0)return false;
         int best=INT_MAX;vector<W> choices;
         for(W v=e;v;v&=v-1){W bit=v&-v;vector<W> g;for(W t:maximal)if(t&bit)g.push_back(t);if((int)g.size()<best){best=g.size();choices=move(g);}}
         for(W t:choices)if(self(self,e&~t,rem-1))return true;
         return false;
       };
       if(!can(can,all,k-b)){++satPrunes;return mem.emplace(key,-1).first->second;}
     }
     if(!o)break;
   }
 }
 }
'''
s=s.replace(' struct O{long long score,bal;',a+' struct O{long long score,bal;').replace('<<v.envelopePrunes<<endl','<<v.envelopePrunes<<","<<v.satChecks<<","<<v.satPrunes<<endl')
Path('sat_token.cpp').write_text(s)
```

```python
from functools import lru_cache
from random import Random
from forced_hole import opt, child, explicit, brute, obs
from fourth import fibers
import json
from collections import Counter

def token(f,u,h,nr,nc,hmax):
    b=next(b for v,b,a in f if v==u);o=h&~b
    q=[(v^u,c&~h) for v,c,a in f if v!=u and (c|o).bit_count()<=hmax]
    row=[sum(1<<i for i,(d,l) in enumerate(q) if d>>r&1) for r in range(nr)]
    col=[sum(1<<i for i,(d,l) in enumerate(q) if l>>j&1) for j in range(nc)]
    tokens={row[r]|col[j] for r in range(nr) if u>>r&1 for j in range(nc) if not h>>j&1}
    tokens.update(row[r] for r in range(nr) if not u>>r&1)
    maximal=[]
    for v in sorted(tokens,key=lambda x:(-x.bit_count(),x)):
        if v and not any(not(v&~m) for m in maximal):maximal.append(v)
    by=[[v for v in maximal if v>>i&1] for i in range(len(q))]
    @lru_cache(None)
    def dp(e):
        if not e:return 0
        i=min((i for i in range(len(q)) if e>>i&1),key=lambda i:len(by[i]))
        return min((1+dp(e&~v) for v in by[i]),default=100)
    return o.bit_count()+dp((1<<len(q))-1),len(tokens-{0}),len(maximal)

def main():
    rng=Random(16943);counts=Counter()
    for nr,nc,hmax in [(3,4,2),(4,5,3)]:
        allf=[(u,0,((1<<nc)-1)^1) for u in range(1,1<<nr,2)]
        for _ in range(40):
            x=rng.choice([x for x in explicit(allf,hmax) if x[1].bit_count()==hmax]);f=allf[:]
            for _ in range(rng.randrange(6)):
                r,j=rng.randrange(nr),rng.randrange(nc);f=child(f,r,j,obs(x,r,j),hmax)
            st=explicit(f,hmax)
            for r in range(nr):
                for j in range(nc):
                    g=child(f,r,j,obs(x,r,j),hmax);s=[y for y in st if obs(y,r,j)==obs(x,r,j)]
                    assert token(g,*x,nr,nc,hmax)[0]==brute(s,x,nr,nc)
                    counts['small_fixed_checks']+=1
    roots=json.load(open('fourth.json'))
    for i in range(0,len(roots),13):
        _,key,_,_=roots[i];f=list(fibers(key));st=explicit(f,14);sat=[x for x in st if x[1].bit_count()==14];x=sat[(i*16943)%len(sat)]
        for r,j in [(-1,-1),divmod(rng.randrange(250),25)]:
            g=f if r<0 else child(f,r,j,obs(x,r,j),14)
            cost,n,m=token(g,*x,10,25,14);assert cost==opt(g,*x,10,25,14)[0];counts['frozen_checks']+=1;counts['distinct_tokens']+=n;counts['maximal_tokens']+=m
    print(dict(counts))
if __name__=='__main__':main()
```

Local hashes: build_v.py 209c44ad476b069fd8ca2e0d5295b4d090e7e4bd43c5cb00eb78d4f361233a20; sat_token.cpp f1d819e8447386e7a6a7ae91ac1c6ec7272e4ff6ea908f461955f432ae481fc5; token_check.py a2c6cc78294392061c5c449cbf09d45286eecd82424fdf2e44a31c6c039f685d; v.csv cc3c5fb69663575ef658c4747598a01052ac74d04bc5f9ca64a4f67e3ffc168a; vbase.csv a0c97d3bd5d3d3ec2508e12d6dd2060ee2214fb421e11ed9c8e1e21ad43b6017; v2.csv 0327f3d845545816b23815f0f566576b76a6203c466ef47949227cfed1134dcb; v2no.csv dde7d7d4b9b3deba5ce157facce7988889656fc50aee083905c1c561ec44e36e.
