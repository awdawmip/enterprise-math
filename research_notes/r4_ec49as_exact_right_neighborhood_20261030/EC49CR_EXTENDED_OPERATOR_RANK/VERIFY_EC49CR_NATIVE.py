"""Independent whole-path integer DP vs unchanged signed native BRC endpoint kernel."""
import json, time
from collections import defaultdict
from pathlib import Path
from VERIFY_EC49CR import S, suffixes
from native_signed_brc import endpoint_weight, endpoint_multiplicity
Z=(0,)*6
W=((2,3,3,2,1,1),(3,2,3,2,1,1))

def advance(q,a):
    x,y=divmod(q,3)
    def t(v,i,j):return 2 if v==2 or (v==1 and a==j) else (1 if a==i else 0)
    return 3*t(x,1,2)+t(y,2,1)

def lab(q):return 2*(q//3==2)+(q%3==2)

def vec(w):
    d=[0]*6
    for k in w:d[abs(k)-1]+=1 if k>0 else -1
    return tuple(d)

def weight(w):
    out=[1,1,1]
    for x in w:
        if x>0:
            out[0]*=W[0][x-1];out[1]*=W[1][x-1]
    return tuple(out)

def viable(z,rem,targets):
    for t in targets:
        dd=sum(abs(a-b) for a,b in zip(z,t))
        if dd<=rem and (rem-dd)%2==0:return True
    return False

def dp(n,targets):
    state={(Z,0):(1,1,1)}
    for step in range(n):
        nxt=defaultdict(lambda:[0,0,0])
        for (z,q),vals in state.items():
            for k in range(-6,7):
                if k==0:continue
                j=abs(k)-1;s=1 if k>0 else -1
                zz=list(z);zz[j]+=s;zz=tuple(zz)
                if not viable(zz,n-step-1,targets):continue
                qq=advance(q,k);u=nxt[(zz,qq)]
                u[0]+=vals[0]*(W[0][j] if k>0 else 1)
                u[1]+=vals[1]*(W[1][j] if k>0 else 1)
                u[2]+=vals[2]
        state={k:tuple(v) for k,v in nxt.items()}
    return state

def main():
    n=12;sufs=suffixes(1,2)
    tar=sorted(set(tuple(-x for x in vec(w)) for w in sufs.values()))
    t0=time.monotonic();hist=dp(n,tar)
    checks=0;out=[]
    for name,s in sufs.items():
        d=tuple(-x for x in vec(s)); sw=weight(s)
        total=[0,0,0];labels=[[0,0,0] for _ in range(4)]
        for q in range(9):
            val=hist.get((d,q),(0,0,0)); qq=q
            for a in s:qq=advance(qq,a)
            label=lab(qq)
            for k in range(3):
                x=val[k]*sw[k]
                labels[label][k]+=x;total[k]+=x
        native=[int(endpoint_weight(n,d,W[k],(1,)*6))*sw[k] for k in range(2)]
        native.append(endpoint_multiplicity(n,d))
        assert total==native,(name,total,native)
        assert [sum(row[k] for row in labels) for k in range(3)]==native
        out.append({'suffix':name,'target':list(d),'three_total':list(total),'label_channels':labels})
        checks+=3
    rr={'n':n,'suffixes':len(sufs),'native_endpoint_comparisons':checks,
        'typed_states_at_terminal':len(hist),'elapsed_seconds':round(time.monotonic()-t0,4),
        'all_exact_integer_checks_passed':True,'results':out}
    dest=Path(__file__).parent/'NATIVE_REPORT_EC49CR.json'
    dest.write_text(json.dumps(rr,sort_keys=True,indent=2)+'\n')
    print('PASS',checks,'native integer comparisons across',len(sufs),'suffixes; final states',len(hist),'elapsed',rr['elapsed_seconds'])
if __name__=='__main__':main()
