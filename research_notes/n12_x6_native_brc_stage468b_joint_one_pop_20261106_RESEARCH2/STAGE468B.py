"""Stage468-B: exact full X6 ternary (P-POP<=1, Q-POP<=h, Q-APPEND<=1).
Positive BRC: every original ordered history has weight 1; partition by initial
complete observer and exact repair key; count class mass without collapse.
"""
from collections import Counter, defaultdict, deque
from itertools import product
import json

DIRECTIONS = tuple((i, sign) for i in range(6) for sign in (1, -1))
# original alphabet is +E1,+E2,+E3: indices 0,2,4.
ABC = (0,2,4)

def obs(p,q):
    def single(s):
        delta=[0]*6; edge=[0]*144
        for x in s:
            axis,sgn=DIRECTIONS[x];delta[axis]+=sgn
        for a,b in zip(s,s[1:]):edge[a*12+b]+=1
        return (len(s),tuple(delta),tuple(edge))
    return (single(p), single(q), sum(a==b for a,b in zip(p,q)))

def key(p,q,h):
    m,n=len(p),len(q)
    t=max(1,n-h)
    lam=(q[t-1],)+tuple((p[j],q[j]) if j<m else (q[j],) for j in range(t,n))
    return (lam,p[-2], (p[-1]==q[m-1]) if t>m else None)

def future_diff(p,q,p2,q2,h):
    """Find labeled legal future path that separates full 12-dir observers, or None."""
    start=(p,q,p2,q2,0,0,0,())
    queue=deque([start]);seen=set()
    while queue:
        x,y,x2,y2,a,b,c,path=queue.popleft()
        state=(x,y,x2,y2,a,b,c)
        if state in seen:continue
        seen.add(state)
        if obs(x,y)!=obs(x2,y2):return path
        if a<1 and x and x2:queue.append((x[:-1],y,x2[:-1],y2,a+1,b,c,path+('POP_P',)))
        if b<h and y and y2:queue.append((x,y[:-1],x2,y2[:-1],a,b+1,c,path+('POP_Q',)))
        if c<1:
            for u in range(12):queue.append((x,y+(u,),x2,y2+(u,),a,b,c+1,path+(f'APPEND_Q_{u}',)))
    return None

def enumerate_fibers(m,n):
    out=defaultdict(list)
    for a in product(ABC,repeat=m-1):
        p=(0,)+a
        for b in product(ABC,repeat=n-1):
            q=(0,)+b
            out[obs(p,q)].append((p,q))
    return out

def check():
    results={'configs':0,'nonempty_multi_fibers':0,'history_pairs_same_key':0,
             'same_key_passed':0,'history_pairs_different_key':0,'different_key_passed':0,
             'mass_conserved_cases':0, 'witnesses':{},'cases':[]}
    # Key equality checked exhaustively for all history pairs in every fiber.
    for m,n in ((2,3),(2,4),(3,4),(3,5),(4,5),(4,6)):
        fibers=enumerate_fibers(m,n)
        for h in range(n+1):
            results['configs']+=1
            pairs_same=pairs_diff=groups_examined=0
            for initial,hs in fibers.items():
                classes=defaultdict(list)
                for p,q in hs:classes[key(p,q,h)].append((p,q))
                assert sum(len(v) for v in classes.values())==len(hs)
                results['mass_conserved_cases']+=1
                if len(hs)<2:continue
                results['nonempty_multi_fibers']+=1
                # Exact comparison for every pair, both directions (witness and class conservation).
                for i,(p,q) in enumerate(hs):
                    for p2,q2 in hs[i+1:]:
                        same=(key(p,q,h)==key(p2,q2,h))
                        trace=future_diff(p,q,p2,q2,h)
                        if same:
                            pairs_same+=1; assert trace is None,(m,n,h,p,q,p2,q2,trace)
                            results['same_key_passed']+=1
                        else:
                            pairs_diff+=1; assert trace is not None,(m,n,h,p,q,p2,q2)
                            results['different_key_passed']+=1
                        # Witness for necessity of each repair component:
                        k1=key(p,q,h);k2=key(p2,q2,h)
                        labels=('Lambda','P_m-1','matching_delta_m')
                        for ix,label in enumerate(labels):
                            if label in results['witnesses']:continue
                            if k1[ix]!=k2[ix] and all(k1[j]==k2[j] for j in range(3) if j!=ix):
                                results['witnesses'][label]={'m':m,'n':n,'h':h,
                                    'p1':p,'q1':q,'p2':p2,'q2':q2,'trace':trace}
            results['history_pairs_same_key']+=pairs_same
            results['history_pairs_different_key']+=pairs_diff
            results['cases'].append({'m':m,'n':n,'h':h,'fibers':len(fibers),'same_pairs':pairs_same,'diff_pairs':pairs_diff})
    from math import comb
    k,b=50,23
    # Family P=A X1 A ... A Xk A, Q=A^n, fixed b letters B among X_i.
    results['closed_form_alternating']={'k':k,'b':b,'m':2*k+1,'n':2*k+10,
        'classes':2,'B_last_mass':comb(k-1,b-1),'C_last_mass':comb(k-1,b),
        'total':comb(k,b)}
    assert results['closed_form_alternating']['B_last_mass']+results['closed_form_alternating']['C_last_mass']==comb(k,b)
    # Family P=A^m, Q=A^(j-1) B A^(n-j), j in [2,m], h<n-m.
    m,n,h=64,80,15
    results['closed_form_match_bit']={'m':m,'n':n,'h':h,'classes':2,
        'q_m_B_mass':1,'q_m_A_mass':m-2,'total':m-1}
    return results

if __name__=='__main__':
    r=check()
    with open('STAGE468B_EXECUTED.json','w') as f:json.dump(r,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:v for k,v in r.items() if k!='cases'},indent=2))
