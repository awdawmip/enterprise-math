"""R307 exact BRC defect Newton certificate; Python 3 standard library integers only."""
import argparse, json, hashlib, time

def build_and_check(dmax):
    Q=[ [0,0,0,1], [0,0,0,0,0,0,1] ]
    # Q_d(x)=sum q_k x^k; integer recurrence from R306.
    multipliers=(((1,1),(2,-1),(3,1)),((3,1),(4,-3),(5,2)),((6,-1),(7,2),(8,-1)),((8,1),(9,-3),(10,3),(11,-1)))
    ncoef=0
    min_all=None
    details=[]
    for d in range(2,dmax+1):
        q=[0]*(3*d+4)
        for j,terms in enumerate(multipliers,1):
            if d-j<0: continue
            for k0,c in terms:
                for i,b in enumerate(Q[d-j]):
                    if b: q[i+k0]+=c*b
        if d==2: q[6]-=1; q[7]+=1
        if d==3: q[8]+=1; q[9]-=2; q[10]+=1
        while q and q[-1]==0: q.pop()
        assert len(q)-1<=3*d+3
        Q.append(q)
        # K_s=Delta^(d-1-s)P_d(T) = [u^s](1+u)^(T+d-1) Q_d(1/(1+u)).
        # Thus K_s = sum_k q_k*binom(5*d+3-k,s).
        # Accumulate K_s for all 0<=s<d by binomial update, with exact division.
        kv=[0]*d
        for k,a in enumerate(q):
            if not a: continue
            m=5*d+3-k
            assert m>=d-1
            v=1
            for s in range(d):
                kv[s]+=a*v
                if s+1<d:
                    v=(v*(m-s))//(s+1)
        if not all(z>0 for z in kv):
            bad=[(s,z) for s,z in enumerate(kv) if z<=0]
            raise AssertionError(('negative Newton',d,bad[:3]))
        # Universal top-diagonal closed forms (for d>=s+1).
        if d>=2: assert kv[1]==2*d-1
        if d>=3: assert kv[2]==2*d*d-3*d-1
        if d>=4: assert 3*kv[3]==2*(2*d**3-6*d*d+d-6)
        if d>=5: assert 6*kv[4]==(2*d+1)*(2*d**3-11*d*d+17*d-30)
        if d>=6: assert 30*kv[5]==(8*d**5-60*d**4+150*d**3-255*d*d-143*d-240)
        assert kv[0]==1
        assert kv[-1]>0
        ncoef+=d
        localmin=min(kv)
        min_all=localmin if min_all is None else min(localmin,min_all)
        if d in (2,3,4,5,6,100,200,201,250,300,350,400,dmax):
            details.append({'d':d,'T':4*d+4,'K_first_six':[str(c) for c in kv[:6]],'K_lowest_difference':str(kv[-1]),'minimum':str(localmin),'Q_degree':len(q)-1})
        # Keep only last four to cap memory: history list indices retained for clarity under size 400.
    return {'schema':'EM_R307_NEWTON_TOP_DIAGONALS_AND_EXTENSION_V1','status':'PASS',
        'arithmetic':'exact Python 3 arbitrary-precision integers; no floats',
        'source':'R305 rational defect generating function; R306 Q_d recurrence',
        'range_d':[2,dmax], 'all_lengths_n_lower_bound':'n >= 4d+4 for each checked d',
        'checked_newton_coefficients':ncoef,'minimum_newton_coefficient':str(min_all),
        'top_diagonals_checked':'s=0..min(5,d-1); explicit formulas (in proof)',
        'selected_exact_values':details,
        'scope':'Bounded d parameter certificate yields infinite n via polynomial Newton identity; all-d top-six theorem is separately proved algebraically',
        'native_cell_transfer':'NOT_ESTABLISHED','independent_review':'NOT_PERFORMED'}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--dmax',type=int,default=300);args=p.parse_args()
    assert 6<=args.dmax<=500
    started=time.monotonic()
    result=build_and_check(args.dmax)
    result['wall_seconds_rounded']=round(time.monotonic()-started,2)
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    print(text)
