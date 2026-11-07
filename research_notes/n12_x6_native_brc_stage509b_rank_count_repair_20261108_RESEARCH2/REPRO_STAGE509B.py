#!/usr/bin/env python3
"""Stage509-B: minimum opaque-gap safe singleton mask for X6 BRC future grammar.
All scientific observations use the native signed six-axis vectors and the full
144-element directed edge tensor F; integer arithmetic only, no scalar projection.
"""
from collections import defaultdict
from itertools import product
import json

Q = 12
V = [tuple((1 if a % 2 == 0 else -1) if j == a // 2 else 0 for j in range(6)) for a in range(Q)]

def F(word):
    e = [0]*(Q*Q); d=[0]*6
    for a in word:
        for j in range(6):d[j]+=V[a][j]
    for a,b in zip(word,word[1:]):e[a*Q+b]+=1
    return (len(word),tuple(d),tuple(e),word[0] if word else None,word[-1] if word else None)

def product_F(x,y):
    if not x[0]:return y
    if not y[0]:return x
    e=[a+b for a,b in zip(x[2],y[2])]
    e[x[4]*Q+y[3]]+=1
    return (x[0]+y[0],tuple(a+b for a,b in zip(x[1],y[1])),tuple(e),x[3],y[4])

def observe(w):return F([a for a,t in w])[:3]

def constraints(tags,h,R,S):
    """Enumerate only direction-free tag+identity skeleton, not 12-way SET options.
    Return directly addressed original tokens and insertion edges in original path.
    """
    n=len(tags);mandatory=set();edges=set();frontier={tuple((i,int(t)) for i,t in enumerate(tags))}
    visited=0;transitions=0
    for depth in range(h):
        nxt=set()
        for word in frontier:
            visited+=1;m=len(word)
            def mark(j):
                if word[j][0]>=0:mandatory.add(word[j][0])
            if m>=1:
                mark(m-1);nxt.add(word[:-1]);transitions+=1
            if m>=3:
                mark(m-3);nxt.add(word[:m-3]+word[m-2:]);transitions+=1
            if m>=2:
                left=word[m-3][0] if m>=3 else None
                right=word[m-2][0]
                if left is not None and left>=0 and right>=0 and right==left+1:
                    edges.add(left)
                # New public token has negative unique ID based on its insertion depth.
                nxt.add(word[:m-2]+((-depth-1,1),)+word[m-2:]);transitions+=1
            for r in R:
                if r<m:
                    mark(m-1-r);nxt.add(word);transitions+=1
            p=[j for j in range(m-1,-1,-1) if word[j][1]]
            for k in S:
                if k<=len(p):
                    j=p[k-1];mark(j);nxt.add(word[:j]+word[j+1:]);transitions+=1
        frontier=nxt
    return frozenset(mandatory),frozenset(edges),{'abstract_prefixes':visited,'abstract_transitions':transitions}

def mask_optimal(n,mandatory,edges):
    # Exact minimum cardinality vertex cover on the original linear order.
    if n==0:return frozenset()
    dp=[{0:(0,(0,)),1:(1,(1,))}]
    if 0 in mandatory:dp[0].pop(0)
    for i in range(1,n):
        d={}
        for v in (0,1):
            if i in mandatory and v==0:continue
            choices=[]
            for prev,(cost,bits) in dp[-1].items():
                if i-1 in edges and prev==v==0:continue
                choices.append((cost+v,bits+(v,)))
            if choices:d[v]=min(choices)
        dp.append(d)
    best=min(dp[-1].values())[1]
    out=frozenset(i for i,b in enumerate(best) if b)
    assert mandatory<=out and all(i in out or i+1 in out for i in edges)
    return out

def old_mask(tags,h,R,S):
    n=len(tags);offs=set(range(h+3))
    for r in R:offs.update(range(r-h,r+h+1))
    selected={n-1-k for k in offs if 0<=k<n}
    m=max(S)+h-1 if S else 0
    selected.update(i for i in [j for j in range(n-1,-1,-1) if tags[j]][:m])
    return frozenset(selected)

def old_exact_touch(tags,h,R,S):
    n=len(tags);frontier={tuple((i,int(t)) for i,t in enumerate(tags))};touch=set()
    for depth in range(h):
        nxt=set()
        for word in frontier:
            m=len(word)
            def mark(j):
                if word[j][0]>=0:touch.add(word[j][0])
            if m>=1:mark(m-1);nxt.add(word[:-1])
            if m>=3:mark(m-3);nxt.add(word[:m-3]+word[m-2:])
            if m>=2:
                if m>=3:mark(m-3)
                mark(m-2)
                nxt.add(word[:m-2]+((-depth-1,1),)+word[m-2:])
            for r in R:
                if r<m:mark(m-1-r);nxt.add(word)
            pubs=[j for j in range(m-1,-1,-1) if word[j][1]]
            for k in S:
                if k<=len(pubs):
                    j=pubs[k-1];mark(j);nxt.add(word[:j]+word[j+1:])
        frontier=nxt
    return frozenset(touch)

def compact(w,mask):
    z=[];i=0;n=len(w)
    while i<n:
        if i in mask:
            z.append(('E',w[i][0],w[i][1]));i+=1
        else:
            j=i
            while j<n and j not in mask:j+=1
            z.append(('G',F([a for a,t in w[i:j]]),sum(t for a,t in w[i:j])));i=j
    return tuple(z)

def summ(p):
    f=F(())
    for x in p:f=product_F(f,F([x[1]]) if x[0]=='E' else x[1])
    return f[:3]

def ln(x):return 1 if x[0]=='E' else x[1][0]

def at(p,j):
    pos=0
    for i,x in enumerate(p):
        if pos<=j<pos+ln(x):
            assert x[0]=='E',('OPAQUE_TARGET',p,j)
            return i
        pos+=ln(x)
    raise AssertionError(('NOT_FOUND',j,pos))

def boundary(p,j):
    pos=0
    for i,x in enumerate(p):
        if pos==j:return i
        pos+=ln(x)
        if pos>j:raise AssertionError(('OPAQUE_INSERT_BOUNDARY',j,p))
    if pos==j:return len(p)
    raise AssertionError(('OUTSIDE',j,pos))

def step_raw(w,op):
    kind,arg=op;z=list(w);n=len(z)
    if kind=='POP' and n>=1:z.pop()
    elif kind=='DELETE2' and n>=3:z.pop(n-3)
    elif kind=='INSERT2' and n>=2:z.insert(n-2,(arg,1))
    elif kind=='SET' and n>arg[0]:
        i=n-1-arg[0];z[i]=(arg[1],z[i][1])
    elif kind=='PUBLIC':
        p=[i for i in range(n-1,-1,-1) if z[i][1]]
        if len(p)<arg:return None
        z.pop(p[arg-1])
    else:return None
    return tuple(z)

def step_compact(p,op):
    kind,arg=op;z=list(p);n=sum(ln(x) for x in z)
    if kind=='POP' and n>=1:del z[at(z,n-1)]
    elif kind=='DELETE2' and n>=3:del z[at(z,n-3)]
    elif kind=='INSERT2' and n>=2:z.insert(boundary(z,n-2),('E',arg,1))
    elif kind=='SET' and n>arg[0]:
        i=at(z,n-1-arg[0]);z[i]=('E',arg[1],z[i][2])
    elif kind=='PUBLIC':
        count=arg;hit=None
        for i in range(len(z)-1,-1,-1):
            a=z[i];q=int(a[2]) if a[0]=='E' else a[2]
            if q<count:count-=q
            else:
                assert a[0]=='E',('HIDDEN_RANK_TARGET',arg,i,a)
                hit=i;break
        if hit is None:return None
        del z[hit]
    else:return None
    return tuple(z)

def acts(R,S):
    return [('POP',None),('DELETE2',None),('INSERT2',0),('INSERT2',7)]+[('SET',(r,c)) for r in R for c in (0,7)]+[('PUBLIC',k) for k in S]

CHECK={'roots':0,'all_future_prefix_nodes':0,'all_future_transitions':0,'abstract_prefix_states':0,'abstract_transitions':0,'optimal_lt_stage508':0,'optimal_lt_right_mask':0,'max_saved_stage508':0,'bruteforce_min_covered':0,'all_insert_edges_already_mandatory':0,'rank_count_regressions':0}

def verify(w,h,R,S,deep=True):
    n=len(w);tags=tuple(t for a,t in w)
    mandatory,edges,stats=constraints(tags,h,R,S)
    opt=mask_optimal(n,mandatory,edges)
    assert all(i in mandatory for i in edges)
    assert opt==mandatory
    CHECK['all_insert_edges_already_mandatory']+=len(edges)
    old_touch=old_exact_touch(tags,h,R,S)
    right=frozenset(set(mandatory)|{i+1 for i in edges})
    assert opt<=old_touch or len(opt)<=len(old_touch)
    assert mandatory<=old_touch and all(i in old_touch or i+1 in old_touch for i in edges)
    assert mandatory<=right and all(i in right or i+1 in right for i in edges)
    assert len(opt)<=len(old_touch) and len(opt)<=len(right)
    assert len(old_touch)<=len(old_mask(tags,h,R,S))
    CHECK['roots']+=1;CHECK['abstract_prefix_states']+=stats['abstract_prefixes'];CHECK['abstract_transitions']+=stats['abstract_transitions']
    CHECK['optimal_lt_stage508']+=(len(opt)<len(old_touch));CHECK['optimal_lt_right_mask']+=(len(opt)<len(right))
    CHECK['max_saved_stage508']=max(CHECK['max_saved_stage508'],len(old_touch)-len(opt))
    if n<=7:
        # Independent exhaustive certificate for this exact set-cover problem.
        feasible=[]
        for bits in product((0,1),repeat=n):
            chosen={i for i,b in enumerate(bits) if b}
            if mandatory<=chosen and all(i in chosen or i+1 in chosen for i in edges):feasible.append(len(chosen))
        assert len(opt)==min(feasible)
        CHECK['bruteforce_min_covered']+=1
    if not deep:return opt,old_touch,right,mandatory,edges
    p=compact(w,opt)
    assert observe(w)==summ(p)
    layer=[(w,p)]
    for depth in range(h+1):
        nxt=[]
        for raw,cp in layer:
            CHECK['all_future_prefix_nodes']+=1
            assert observe(raw)==summ(cp)
            if depth==h:continue
            for act in acts(R,S):
                CHECK['all_future_transitions']+=1
                a,b=step_raw(raw,act),step_compact(cp,act)
                assert (a is None)==(b is None),(w,act,'LEGALITY')
                if a is not None:
                    assert observe(a)==summ(b),(w,act,'OBSERVER')
                    nxt.append((a,b))
        layer=nxt
    return opt,old_touch,right,mandatory,edges

def run():
    for h,nmax,R,S in [(1,4,(2,5),(1,2)),(2,3,(2,4),(1,2))]:
        for n in range(nmax+1):
            for letters in product(range(6),repeat=n):
                w=tuple(((0,1,2)[x//2],x%2) for x in letters)
                verify(w,h,R,S)
    for n in (9,12,19,28):
        for pat in range(5):
            w=tuple(((7*i+i*i+3*n+pat)%12,int((i+2*pat)%5<2)) for i in range(n))
            verify(w,3 if n<20 else 2,(2,11 if n>=19 else 6),(1,2,3))
    n=19;h=3;R=(2,11);S=(1,3)
    w=tuple(((3*i+i*i+7)%12,int(i in (0,3,6,12,15,18))) for i in range(n))
    optimal,stage508,right,mandatory,edges=verify(w,h,R,S)
    witness={'n':n,'h':h,'R':list(R),'S':list(S),
      'stage507_count':len(old_mask(tuple(t for a,t in w),h,R,S)),
      'stage508_count':len(stage508),'right_only_count':len(right),'optimal_count':len(optimal),
      'stage508':sorted(stage508),'optimal':sorted(optimal),'mandatory':sorted(mandatory),
      'insertion_original_adjacency_edges':[[i,i+1] for i in sorted(edges)]}
    # An adversarial sparse public-label case missed by the preceding Stage508 tests.
    ww=tuple((i%12,int(i in (1,4,7))) for i in range(12))
    verify(ww,1,(2,11),(1,3))
    CHECK['rank_count_regressions']+=1
    # Genuine Stage508 uncounted-F fiber collision with different rank legality.
    xx=tuple((i%12,int(i in (1,4,7))) for i in range(12))
    yy=tuple((i%12,int(i in (1,7))) for i in range(12))
    rr=(2,10,11);ss=(1,3)
    mx=old_exact_touch(tuple(t for a,t in xx),1,rr,ss)
    my=old_exact_touch(tuple(t for a,t in yy),1,rr,ss)
    assert mx==my
    px=compact(xx,mx);py=compact(yy,my)
    def strip_hidden_public_counts(p):
        return tuple(x[:2] if x[0]=='G' else x for x in p)
    assert strip_hidden_public_counts(px)==strip_hidden_public_counts(py)
    assert px!=py
    assert step_raw(xx,('PUBLIC',3)) is not None
    assert step_raw(yy,('PUBLIC',3)) is None
    verify(xx,1,rr,ss);verify(yy,1,rr,ss)
    CHECK['rank_count_regressions']+=2
    # Find nontrivial difference vs right-side-only selection on small tag families.
    first_right=None
    for n in range(3,11):
        for bits in product((0,1),repeat=n):
            m,e,_=constraints(bits,1,(2,),(1,2))
            opt=mask_optimal(n,m,e)
            right=frozenset(set(m)|{i+1 for i in e})
            if len(opt)<len(right):
                first_right={'length':n,'tags':''.join('P' if t else 'O' for t in bits),
                  'h':1,'R':[2],'S':[1,2],'mandatory':sorted(m),'edges':[[i,i+1] for i in sorted(e)],
                  'optimal':sorted(opt),'right_only':sorted(right)}
                ww=tuple((i%12,bits[i]) for i in range(n))
                verify(ww,1,(2,),(1,2));break
        if first_right:break
    assert first_right is not None
    return {'stage':'509-B','status':'ALL_ASSERTIONS_PASS',
        'native_directions':12,'directed_X6_relations':144,
        'theorem':'DIRECT_TOUCH_MASK_WITH_F_AND_GAP_PUBLIC_COUNTS_IS_FUTURE_LOSSLESS',
        'complexity_post_constraints':'O(n+number_of_edges)',
        'rank_count_fiber_counterexample':{'n':12,'h':1,'R':[2,10,11],'S':[1,3], 'P_positions_x':[1,4,7],'P_positions_y':[1,7], 'same_stage508_uncounted_compact':True,'same_direct_touch_mask':True,'rank_3_legal_x':True,'rank_3_legal_y':False},'tests':CHECK,'stage508_witness':witness,'first_right_opt_gap':first_right}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
