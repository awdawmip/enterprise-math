"""Exact finite audit of R155B adjacent 01->10 signature-preservation criterion."""
from fractions import Fraction
from collections import defaultdict
from pathlib import Path
import json

def signature(w):
    m=len(w); s=[0]
    for x in w: s.append(s[-1]+int(x))
    ln, ld, hn, hd=0,1,1,1
    for i in range(m):
        for j in range(i+1,m+1):
            n,d=s[j]-s[i],j-i
            if (n-1)*ld>ln*d: ln,ld=n-1,d
            if (n+1)*hd<hn*d: hn,hd=n+1,d
            if ln*hd>=hn*ld: return None
    alpha,beta=Fraction(ln,ld),Fraction(hn,hd)
    a,b=alpha.numerator,alpha.denominator
    c,d=beta.numerator,beta.denominator
    U=min(b*(v+1)-a*j for j,v in enumerate(s))
    V=max(d*v-c*j for j,v in enumerate(s))
    return alpha,beta,U,V

def predicts_same_signature(w, sig, t):
    """Input has w[t-1:t+1]=='01'; target swaps it to '10'."""
    m=len(w); s=[0]
    for x in w:s.append(s[-1]+int(x))
    alpha,beta,U,V=sig
    a,b=alpha.numerator,alpha.denominator
    c,d=beta.numerator,beta.denominator
    if any((s[t]-s[i])*b>a*(t-i) for i in range(t)):return False
    if any((s[j]-s[t])*d<c*(j-t) for j in range(t+1,m+1)):return False
    all_pairs=((i,j) for i in range(m) for j in range(i+1,m+1) if i!=t and j!=t)
    base_lower= a==0 or any((s[j]-s[i]-1)*b==a*(j-i) for i,j in all_pairs)
    left_lower=any((s[t]-s[i])*b==a*(t-i) for i in range(t))
    all_pairs=((i,j) for i in range(m) for j in range(i+1,m+1) if i!=t and j!=t)
    base_upper= c==d or any((s[j]-s[i]+1)*d==c*(j-i) for i,j in all_pairs)
    right_upper=any((s[j]-s[t])*d==c*(j-t) for j in range(t+1,m+1))
    if not (base_lower or left_lower) or not (base_upper or right_upper):return False
    if not any(b*(s[j]+1)-a*j==U for j in range(m+1) if j!=t):return False
    if d*s[t]-c*t+d>V:return False
    return True

by_length={}; total_swaps=total_same=0
for m in range(2,15):
    sigs={}; classes=defaultdict(list)
    for x in range(1<<m):
        w=f'{x:0{m}b}'
        q=signature(w)
        sigs[w]=q
        if q is not None:classes[q].append(w)
    swaps=same=0
    for w,q in sigs.items():
        if q is None:continue
        for t in range(1,m):
            if w[t-1:t+1]!='01': continue
            target=w[:t-1]+'10'+w[t+1:]
            prediction=predicts_same_signature(w,q,t)
            actual=(sigs[target]==q)
            assert prediction==actual,(m,w,t,target,q,sigs[target])
            swaps+=1; same+=actual
    for group in classes.values():
        assert len(group)<=2
        if len(group)==2:
            a,b=group
            changes=[j for j in range(m) if a[j]!=b[j]]
            assert len(changes)==2 and changes[1]==changes[0]+1
            assert {a[j] for j in changes}=={'0','1'}
    doubled=sum(len(v)==2 for v in classes.values())
    assert doubled==same,(m,doubled,same)
    by_length[str(m)]={'candidate_words':1<<m,'admissible_words':sum(len(v) for v in classes.values()),'01_to_10_admissible_source_swaps':swaps,'exact_signature_preserving_swaps':same,'doubleton_signatures':doubled}
    total_swaps+=swaps;total_same+=same
result={'status':'R155B_ADJACENT_SWAP_CRITERION_PASS','finite_lengths':[2,14], 'swaps_checked':total_swaps,'preserving_swaps':total_same, 'all_collisions_adjacent_in_range':True,'by_length':by_length}
print(json.dumps(result,indent=2))
with Path(__file__).with_name('R155B_verification.json').open('w',encoding='utf-8') as f: json.dump(result,f,indent=2); f.write('\n')
