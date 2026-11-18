"""Direct integer-tuple-prefix independent objective audit; same immutable candidate source."""
from pathlib import Path
from itertools import combinations
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import W, STEPS, REQ, observe, candidates

def pref(word):
    trace = []
    for op in word:
        trace.extend(STEPS[op])
    return frozenset(tuple(trace[:j]) for j in range(1,len(trace)+1))

def run():
    selected={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    pool={f'{h}:{s}':ws for h in (4,5,6) for s,ws in candidates(h).items()}
    needed=set(selected.values())|{w for ws in pool.values() for w in ws}
    ps={w:pref(w) for w in needed}
    assert len(set().union(*(ps[w] for w in selected.values())))==158
    entries=[];total=0
    for slots in combinations(early,4):
        rest=set().union(*(ps[w] for k,w in selected.items() if k not in slots))
        cutoff=158-len(rest)
        f=[[(w,ps[w]-rest) for w in pool[k] if len(ps[w]-rest)<cutoff] for k in slots]
        a,b,c,d=sorted(f,key=len)
        count=0;minimum=158
        for wa,pa in a:
            for wb,pb in b:
                p2=pa|pb
                if len(p2)>=cutoff:continue
                for wc,pc in c:
                    p3=p2|pc
                    if len(p3)>=cutoff:continue
                    for wd,pd in d:
                        count+=1
                        minimum=min(minimum,len(rest)+len(p3|pd))
        total+=count
        entries.append([*slots,len(rest),count,minimum])
    assert len(entries)==210 and total==3001 and all(e[-1]==158 for e in entries)
    out=Path(__file__).with_name('DIRECT_REPORT_EC49FBZ.json')
    out.write_text(json.dumps({'schema':'EC49FBZ_NATIVE_TUPLE_AUDIT_V1','groups':len(entries),
       'fourth_evaluations':total,'minimum':158,'per_group':entries},indent=2)+'\n',encoding='utf-8')
    print('PASS DIRECT',len(entries),'quartets',total,'fourth evaluations')
    return entries
if __name__=='__main__':run()
