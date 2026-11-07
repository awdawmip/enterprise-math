#!/usr/bin/env python3
"""EC49EXR reproducible exact signed-native BRC E<80 screen.
Requires the adjacent EC49EXQ/EC49EXJ directories from the same PR branch,
Python 3 standard library, g++ C++17. No numeric floating point is used.
"""
import json, re, subprocess, sys, tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
EXQ=ROOT/'EC49EXQ_H8_M5_ADJACENT_PREFIX_MATCHING'/'SCREEN_ALL_EC49EXQ.cpp'
EXJ=ROOT/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
sys.path.insert(0,str(EXJ))
from SCREEN_H5_EC49EXJ import build_input, words

OLD='append(group,bound(ks,hs));\n   }'
NEW='''Cost v=bound(ks,hs);append(group,v);
    if(v.newb<80){cerr<<"SURVIVE "<<v.newb<<" "<<a<<","<<b<<","<<c;
      for(auto &k:ks)cerr<<" "<<k.u<<","<<k.v<<","<<k.w;
      cerr<<"\\n";}
   }'''

def residual_cases(work):
    source=EXQ.read_text()
    assert source.count(OLD)==2, "Expected one triple and one double loop"
    patched=work/'screen.cpp';patched.write_text(source.replace(OLD,NEW,1))
    subprocess.run(['g++','-std=c++17','-O3',str(patched),'-o',str(work/'screen')],check=True)
    r=subprocess.run([str(work/'screen')],capture_output=True,text=True,check=True)
    assert json.loads(r.stdout)['triple']['new_survivors_lt80']==946
    lines=[x for x in r.stderr.splitlines() if x.startswith('SURVIVE ')]
    assert len(lines)==946
    entries=[]
    for index,line in enumerate(lines):
        f=line.split()
        b=int(f[1]); tri=tuple(map(int,f[2].split(',')))
        ks=[tuple(map(int,z.split(','))) for z in f[3:]]
        assert len(ks)==5 and len(set(ks))==5
        rem=[h for h in range(2,9) if h not in tri]
        mapping={h:ks[0] for h in tri}
        mapping.update({h:k for h,k in zip(rem,ks[1:])})
        schedule=tuple((mapping[h],4 if mapping[h][0]+mapping[h][1]-h-1>=1 else 2) for h in range(2,9))
        counts=[len(words(h,k,t)) for h,(k,t) in enumerate(schedule,2)]
        assert all(counts)
        entries.append((sum(counts),max(counts),index,b,tri,schedule))
    entries.sort()
    assert sum(x[0]<=400 for x in entries)==92
    return entries

def main():
    records=[]
    with tempfile.TemporaryDirectory() as tmp:
        work=Path(tmp)
        cases=residual_cases(work)
        subprocess.run(['g++','-std=c++17','-O3',str(EXJ/'EXACT_OR_MASK_DP.cpp'),'-o',str(work/'dp')],check=True)
        for eligible,maximum,index,b,tri,assignment in cases[:92]:
            inp,nodes,nwords=build_input(assignment)
            assert eligible==nwords
            r=subprocess.run([str(work/'dp'),'80'],input=inp,capture_output=True,text=True,check=True)
            assert re.fullmatch(r'BOUND_PASS minimum_total_at_least=80 nodes=\d+ colors=\d+',r.stdout.strip()),(index,r.stdout)
            records.append({'index':index,'EXQ_B':b,'triple':tri,'eligible_words':eligible,'trie_nodes':nodes,'receipt':r.stdout.strip()})
    assert len(records)==92
    print(json.dumps({'status':'PASS','checked':92,'new_excluded_E_lt80':92,
                      'triple_remaining':854,'double_remaining':63665,
                      'all_remaining':64519,'cases':records},separators=(',',':')))

if __name__=='__main__':main()
