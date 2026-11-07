"""Exact one-step lookahead rank and optional native-path h4 witness."""
from VERIFY_EC49CJ import *
from fractions import Fraction

def rational_rank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    r=0
    for c in range(9):
        k=next((i for i in range(r,len(a)) if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        den=a[r][c]
        a[r]=[v/den for v in a[r]]
        for i in range(r+1,len(a)):
            f=a[i][c]
            if f:a[i]=[v-f*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==9:break
    return r

def exact_rank_summary(sufs):
    rows=defaultdict(list)
    for key,word in sufs.items():
        target=tuple(-x for x in displacement(word))
        labels=[label(follow(q,word)) for q in range(9)]
        for a in range(4):rows[target].append([int(k==a) for k in labels])
    return {str(d):rational_rank(r) for d,r in sorted(rows.items())}

if __name__=='__main__':
    base=suffixes(3,True)
    series={}
    for key,word in S.items():
        augmented={**base,**{key+"|"+k:word+w for k,w in base.items()}}
        rank=exact_rank_summary(augmented)
        series[key]={'full_rank':3*sum(rank.values()),'extra_vs_147':3*sum(rank.values())-147,'by_target':rank}
    for h in (3,4):
        for upto in (False,True):
            suf=suffixes(h,upto)
            rat=exact_rank_summary(suf)
            assert sum(rat.values())==sum(len(rows) for rows in row_system(suf).values())
            print('h',h,'upto',upto,'rank_Q',3*sum(rat.values()),'fibers',rat,flush=True)
    print('single_s_lookahead',series,flush=True)
    path=Path(__file__).parent
    (path/'RANKS_EC49CJ.json').write_text(json.dumps({'single_operation_lookahead':series,'S3':exact_rank_summary(suffixes(3,False)),'S_leq3':exact_rank_summary(suffixes(3,True)),'S_leq4':exact_rank_summary(suffixes(4,True))},ensure_ascii=False,indent=2)+'\n')
    if '--witness4' in sys.argv:
        suf=suffixes(4,True);rs=row_system(suf)
        for n in (10,12):
            rec=certify(n,suf,rs)
            recheck_certificate(rec,suf,rs)
            (path/f'CERT_EC49CJ_S1234_n{n}.json').write_text(json.dumps(rec,ensure_ascii=False,separators=(',',':'),sort_keys=True)+'\n')
