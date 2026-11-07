#!/usr/bin/env python3
"""Stage510-B: exact K-saturation for rank-select over untouched BRC gaps.
Pure stdlib, exact integer arithmetic. Deterministic 2026-11-08 test.
"""
import itertools
import json
import random
from collections import deque
from pathlib import Path

A = tuple(range(12))
V = tuple(tuple((1 if d == 2 * j else (-1 if d == 2*j + 1 else 0)) for j in range(6)) for d in A)
E = tuple(0 for _ in range(144))
Z = tuple(0 for _ in range(6))
EMPTY = (0, Z, E, None, None)


def summary(ds):
    if not ds:
        return EMPTY
    n = len(ds)
    disp = tuple(sum(V[d][j] for d in ds) for j in range(6))
    edges = [0] * 144
    for a, b in zip(ds, ds[1:]):
        edges[12*a+b] += 1
    return (n, disp, tuple(edges), ds[0], ds[-1])


def compose(x,y):
    if not x[0]: return y
    if not y[0]: return x
    ee = [a+b for a,b in zip(x[2], y[2])]
    ee[12*x[4]+y[3]] += 1
    return (x[0]+y[0], tuple(a+b for a,b in zip(x[1],y[1])),tuple(ee), x[3],y[4])


def pub_count(tags, cap=None):
    p = sum(t == 'P' for t in tags)
    return p if cap is None else min(cap,p)


def route(counts,k):
    """Return index and rank within its piece, or None. Both from right."""
    rem = k
    for i in range(len(counts)-1,-1,-1):
        if rem <= counts[i]:
            return (i,rem)
        rem -= counts[i]
    return None


def ops(s, R,S,choices):
    n = len(s)
    out = []
    if n: out.append(('POP',))
    if n >= 3: out.append(('DELETE2',))
    if n >= 2:
        out += [('INSERT2',a) for a in choices]
    out += [('SET',r,a) for r in R if 0 <= r < n for a in choices]
    out += [('RANK',k) for k in S]
    return out


def raw_apply(s,op):
    s=list(s)
    kind=op[0]
    if kind == 'POP':
        if not s: return None
        s.pop()
    elif kind == 'DELETE2':
        if len(s)<3: return None
        s.pop(-3)
    elif kind == 'INSERT2':
        if len(s)<2: return None
        new_id=min((x[2] for x in s),default=0)-1
        s.insert(len(s)-2,(op[1],'P',new_id))
    elif kind == 'SET':
        r=op[1]
        if r<0 or r>=len(s):return None
        a,t,i=s[-1-r];s[-1-r]=(op[2],t,i)
    elif kind == 'RANK':
        kk=op[1]
        p=[i for i,x in enumerate(s) if x[1]=='P']
        if len(p)<kk: return None
        s.pop(p[-kk])
    else:raise ValueError(op)
    return tuple(s)


def skeleton_apply(sk, kind, param, newid):
    sk=list(sk)
    if kind == 'POP':
        if not sk:return None,newid,None
        idx=len(sk)-1
        target=sk[idx][0]
        sk.pop()
    elif kind=='DELETE2':
        if len(sk)<3:return None,newid,None
        target=sk[-3][0];sk.pop(-3)
    elif kind=='INSERT2':
        if len(sk)<2:return None,newid,None
        target=None;sk.insert(len(sk)-2,(newid,'P'));newid-=1
    elif kind=='SET':
        r=param
        if r<0 or r>=len(sk):return None,newid,None
        target=sk[-1-r][0]
    elif kind=='RANK':
        pp=[i for i,t in enumerate(sk) if t[1]=='P']
        if len(pp)<param:return None,newid,None
        ix=pp[-param];target=sk[ix][0];sk.pop(ix)
    else: raise ValueError(kind)
    return tuple(sk),newid,target


def direct_mask(tags,h,R,S):
    n=len(tags)
    init=tuple((i,t) for i,t in enumerate(tags))
    q=deque([(init,-1,0)])
    seen={(init,-1,0)}
    touched=set()
    states=0
    while q:
        s,newid,depth=q.popleft();states+=1
        if depth>=h:continue
        moves=[('POP',None),('DELETE2',None),('INSERT2',None)]
        moves += [('SET',r) for r in R]
        moves += [('RANK',k) for k in S]
        for kind,param in moves:
            nxt,nn,target=skeleton_apply(s,kind,param,newid)
            if nxt is None:continue
            if target is not None and target >=0: touched.add(target)
            st=(nxt,nn,depth+1)
            if st not in seen:seen.add(st);q.append(st)
    return touched,states


def build_pieces(root,mask,cap=None):
    out=[];i=0
    while i<len(root):
        if i in mask:
            a,t,_=root[i]
            out.append(('tok',(a,t,root[i][2]),summary([a]),int(t=='P')))
            i+=1
        else:
            j=i
            while j<len(root) and j not in mask:j+=1
            run=root[i:j]
            out.append(('gap',None,summary([a for a,t,_ in run]),pub_count([t for a,t,_ in run],cap)))
            i=j
    return tuple(out)


def piece_summary(ps):
    v=EMPTY
    for typ,item,f,c in ps:v=compose(v,f)
    return v


def piece_rank(ps,k):
    return route([p[3] for p in ps],k)


def piece_pos(ps,idx):
    if idx<0 or idx>=sum(p[2][0] for p in ps):return None
    cur=0
    for j,p in enumerate(ps):
        if cur <= idx < cur+p[2][0]:
            return j,idx-cur
        cur+=p[2][0]
    assert False


def compact_apply(ps,op):
    """Return None for illegal operation. Raises if source mask would expose a hidden token."""
    ps=list(ps)
    n=sum(p[2][0] for p in ps)
    kind=op[0]
    if kind == 'POP':
        if not n:return None
        ix=n-1
    elif kind == 'DELETE2':
        if n<3:return None
        ix=n-3
    elif kind == 'SET':
        r=op[1]
        if not 0<=r<n:return None
        ix=n-1-r
    elif kind == 'RANK':
        loc=piece_rank(ps,op[1])
        if loc is None:return None
        jj,rank=loc
        if ps[jj][0]!='tok':
            raise AssertionError('selected target inside opaque gap: D_h missing')
        ix=sum(p[2][0] for p in ps[:jj])
    elif kind == 'INSERT2':
        if n<2:return None
        pos=n-2
        if pos==0: insert_piece_at=0
        else:
            pos_loc=piece_pos(ps,pos-1)
            assert pos_loc is not None
            jj,offset=pos_loc
            if offset+1!=ps[jj][2][0]:
                raise AssertionError('insertion splitting opaque gap')
            insert_piece_at=jj+1
        new=('tok',(op[1],'P',-100000),summary([op[1]]),1)
        ps.insert(insert_piece_at,new)
        return tuple(ps)
    else:raise ValueError(kind)
    j, offset=piece_pos(ps,ix)
    if ps[j][0]!='tok':
        raise AssertionError('positional edit touched opaque gap: D_h missing')
    if kind=='SET':
        old=ps[j][1]; assert offset==0
        ps[j]=('tok',(op[2],old[1],old[2]),summary([op[2]]),ps[j][3])
    else:ps.pop(j)
    return tuple(ps)


def check_root(root,h,R,S,choices,c):
    mask,numstates=direct_mask([t for a,t,i in root],h,R,S)
    exact=build_pieces(root,mask,None)
    cap=build_pieces(root,mask,max(S) if S else 1)
    assert piece_summary(exact) == summary([a for a,t,i in root])
    assert piece_summary(cap) == piece_summary(exact)
    q=deque([(root,exact,cap,0)])
    while q:
        raw,ex,ca,depth=q.popleft()
        c['future_nodes']+=1
        expected=summary([a for a,t,i in raw])
        assert piece_summary(ex)==piece_summary(ca)==expected
        if depth==h:continue
        for op in ops(raw,R,S,choices):
            nr=raw_apply(raw,op)
            ne=compact_apply(ex,op)
            nc=compact_apply(ca,op)
            c['transitions']+=1
            assert (nr is None)==(ne is None)==(nc is None), (raw,op)
            if nr is None:continue
            assert piece_summary(ne)==piece_summary(nc)==summary([a for a,t,i in nr]),(op,raw)
            q.append((nr,ne,nc,depth+1))
    c['roots']+=1
    c['abstract_states']+=numstates
    c['opaque_gaps']+=sum(p[0]=='gap' for p in cap)
    c['gaps_with_P_saturation']+=sum(p[0]=='gap' and p[3] < q[3] for p,q in zip(cap,exact))


def main():
    counts={'schema':'STAGE510B_EXACT_INTEGER_TESTS_V1','date':'2026-11-08','roots':0,'future_nodes':0,'transitions':0,'abstract_states':0,'opaque_gaps':0,'gaps_with_P_saturation':0,'router_vectors':0,'router_queries':0,'monoid_checks':0,'long_example':None}
    # First proof-independent rank selection exhaustive coverage, including illegal queries.
    for length in range(6):
        for cs in itertools.product(range(6), repeat=length):
            counts['router_vectors']+=1
            for K in range(1,7):
                capped=tuple(min(K,c) for c in cs)
                for k in range(1,K+1):
                    assert route(cs,k)==route(capped,k)
                    counts['router_queries']+=1
                for other in range(6):
                    assert min(K,sum(cs)+other)==min(K,sum(capped)+min(K,other))
                    counts['monoid_checks']+=1
    # Exhaustive tagged words (6 alphabet elements, 3 signed directions) through length 4.
    # h=2 for shorter words and h=1 for length 4; K in {1,3}.
    for n in range(5):
        for letters in itertools.product(range(6),repeat=n):
            root=tuple((z//2, 'P' if z%2 else 'O',i) for i,z in enumerate(letters))
            h=2 if n<=3 else 1
            check_root(root,h,{0,2},{1,3},(0,1),counts)
    # Larger native-12-direction roots, mixed provenance, and explicit rank saturation.
    rng=random.Random(51020261108)
    for n in (9,12,19,28):
        for t in range(9):
            root=tuple((rng.randrange(12),'P' if rng.randrange(3)!=0 else 'O',i) for i in range(n))
            check_root(root,2 if n<=12 else 3,{2,11},{1,3},(0,11),counts)
    # Deliberate long gap with many public markers, safely shielded by late public suffix.
    n=80
    root=tuple(((i*7+3)%12,'P' if i<45 or i>=70 else 'O',i) for i in range(n))
    mask,num_states=direct_mask([t for a,t,i in root],2,{2,3},{1,3})
    ex=build_pieces(root,mask)
    ca=build_pieces(root,mask,3)
    gains=[(p[2][0],p[3],q[3]) for p,q in zip(ex,ca) if p[0]=='gap' and p[3]>q[3]]
    assert gains,mask
    assert piece_summary(ex)==piece_summary(ca)==summary([a for a,t,i in root])
    # Two distinct source-provenance assignments with identical capped source state.
    # They are in the same Stage510 finite-future observational equivalence class.
    alt=tuple((a, 'O' if 10<=i<20 else t, i) for i,(a,t,_) in enumerate(root))
    mask_alt,_=direct_mask([t for a,t,i in alt],2,{2,3},{1,3})
    assert mask==mask_alt
    assert build_pieces(alt,mask_alt,3)==ca
    assert build_pieces(root,mask)!=build_pieces(alt,mask_alt)
    check_root(root,2,{2,3},{1,3},(0,11),counts)
    check_root(alt,2,{2,3},{1,3},(0,11),counts)
    counts['long_example']={'n':n,'h':2,'R':[2,3],'S':[1,3],'K':3,'explicit_orig':len(mask),'opaque_gap_saturation':gains,'abstract_states':num_states,'distinct_histories_same_capped_state':True, 'original_prefix_P_counts':[50,40]}
    counts['all_assertions_passed']=True
    path=Path(__file__).with_name('STAGE510B_EXECUTED.json')
    path.write_text(json.dumps(counts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(counts,indent=2))

if __name__=='__main__':main()
