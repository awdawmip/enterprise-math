"""Stage506-B: exact original-token exposure mask and piece-monoid checker.
Pure Python 3 standard library; fixed X6 signed directions and 144 directed edges.
This verifies POP, DELETE2, INSERT2(c), SET_END(r,c) for finite horizon h.
"""
from itertools import product
import json, random

A = tuple(range(12))
V = tuple(tuple((1 if d == 2*k else -1 if d == 2*k+1 else 0)
                for k in range(6)) for d in A)
ZERO = (0, (0,)*6, (0,)*144, None, None)

def atom(d):
    return (1, V[d], (0,)*144, d, d)

def join(a, b):
    if not a[0]: return b
    if not b[0]: return a
    e = [x+y for x,y in zip(a[2], b[2])]
    e[12*a[4]+b[3]] += 1
    return (a[0]+b[0], tuple(x+y for x,y in zip(a[1], b[1])),
            tuple(e), a[3], b[4])

def observe(w):
    z=ZERO
    for d in w: z=join(z,atom(d))
    return z

def ops(R, letters):
    return [('pop',None,None), ('del2',None,None)] + [
        ('ins2',None,c) for c in letters] + [
        ('set',r,c) for r in R for c in letters]

def eligible(L,op):
    kind,r,_=op
    return ((kind=='pop' and L>=1) or (kind=='del2' and L>=3)
            or (kind=='ins2' and L>=2) or (kind=='set' and L>r))

def transition(L,q,kind):
    """Surviving original token's new (length, end-offset), None if erased."""
    if kind=='pop':
        return None if q==0 else (L-1,q-1)
    if kind=='del2':
        return None if q==2 else (L-1,q-(q>2))
    if kind=='ins2':
        return (L+1,q+(q>=2))
    return (L,q)

def broad(n,h,R):
    p=set(range(min(n,h+3)))
    for r in R:
        p.update(range(max(0,r-h),min(n,r+h+1)))
    return sorted(p)

def exact_mask(n,h,R):
    """All initial offsets whose original tokens may be directly exposed.
    Explore position/length reachability, not alphabet words or operation trees.
    """
    out=set()
    for rho in broad(n,h,R):
        states={(n,rho)}
        for _ in range(h):
            next_states=set()
            for L,q in states:
                if L>=1:
                    if q==0: out.add(rho)          # POP target
                    z=transition(L,q,'pop')
                    if z is not None: next_states.add(z)
                if L>=3:
                    if q==2: out.add(rho)          # DELETE2 target
                    z=transition(L,q,'del2')
                    if z is not None: next_states.add(z)
                if L>=2:
                    if q in (1,2): out.add(rho)    # INSERT2 neighbors
                    next_states.add(transition(L,q,'ins2'))
                for r in R:
                    if L>r:
                        if q==r: out.add(rho)      # SET target
                        next_states.add((L,q))
            states=next_states
    return sorted(out)

def make_pieces(w,mask):
    n=len(w); indices={n-1-r for r in mask}
    out=[]; i=0
    while i<n:
        if i in indices:
            out.append(('tok',w[i])); i+=1
        else:
            j=i
            while j<n and j not in indices: j+=1
            out.append(('gap',observe(w[i:j]))); i=j
    return out

def piece_len(p):
    return 1 if p[0]=='tok' else p[1][0]

def piece_F(p):
    return atom(p[1]) if p[0]=='tok' else p[1]

def get_total(ps):
    z=ZERO
    for p in ps: z=join(z,piece_F(p))
    return z

def at(ps,index,insertion=False):
    """Find explicit token at index, or allowable boundary for insertion."""
    pos=0
    for j,p in enumerate(ps):
        next_pos=pos+piece_len(p)
        if insertion and index==pos: return j
        if pos<=index<next_pos:
            if p[0]=='gap': raise AssertionError(('opaque_gap_access',index,pos,next_pos))
            return j
        pos=next_pos
    if insertion and index==pos: return len(ps)
    raise AssertionError(('index_missing',index,pos))

def change_plain(w,op):
    if not eligible(len(w),op): return None
    kind,r,c=op; x=list(w)
    if kind=='pop': x.pop()
    elif kind=='del2': x.pop(-3)
    elif kind=='ins2': x.insert(len(x)-2,c)
    else: x[len(x)-1-r]=c
    return tuple(x)

def change_piece(ps,op):
    L=sum(map(piece_len,ps))
    if not eligible(L,op): return None
    kind,r,c=op; x=list(ps)
    if kind=='pop': x.pop(at(x,L-1))
    elif kind=='del2': x.pop(at(x,L-3))
    elif kind=='ins2': x.insert(at(x,L-2,True),('tok',c))
    else: x[at(x,L-1-r)]=('tok',c)
    return x

def test_tree(w,h,R,letters):
    mask=exact_mask(len(w),h,R)
    ps=make_pieces(w,mask)
    q=[(tuple(w),ps,0)]
    nodes=transitions=0
    actions=ops(R,letters)
    while q:
        raw,cmp,depth=q.pop()
        assert observe(raw)==get_total(cmp)
        nodes+=1
        if depth==h: continue
        for op in actions:
            a=change_plain(raw,op)
            b=change_piece(cmp,op)
            transitions+=1
            assert (a is None)==(b is None)
            if a is not None:
                assert observe(a)==get_total(b), (w,op,raw,mask)
                q.append((a,b,depth+1))
    return nodes,transitions

def main():
    assert len(V)==12 and len(V[0])==6
    assert exact_mask(1000000,4,(2,100000))==[0,1,2,3,4,5,99997,99998,99999,100000,100001,100002,100003]
    tests=0; nodes=0; edges=0
    for n in range(6):
        for w in product(range(3),repeat=n):
            a,b=test_tree(w,2,(2,4),(0,1,2))
            tests+=1; nodes+=a; edges+=b
    rng=random.Random(506)
    for j in range(65):
        n=rng.randrange(0,35)
        w=tuple(rng.randrange(12) for _ in range(n))
        a,b=test_tree(w,3,(2,5),(0,1))
        tests+=1; nodes+=a; edges+=b
    # Distinct words collide exactly under K but need no future expansion.
    x=(0,0,1,0)+(0,)*15
    y=(0,1,0,0)+(0,)*15
    mask=exact_mask(len(x),3,(2,5))
    assert x!=y
    assert make_pieces(x,mask)==make_pieces(y,mask)
    a,b=test_tree(x,3,(2,5),(0,1))
    c,d=test_tree(y,3,(2,5),(0,1))
    tests+=2; nodes+=a+c; edges+=b+d
    print(json.dumps({'kind':'stage506b_exact_finite', 'tests':tests,
       'visited_nodes':nodes, 'checked_transitions':edges,
       'million_n':1000000, 'million_h':4,'million_R':[2,100000],
       'million_exact_mask':exact_mask(1000000,4,(2,100000)),
       'million_exact_tokens':len(exact_mask(1000000,4,(2,100000))),
       'million_broad_tokens':len(broad(1000000,4,(2,100000))),
       'collision_19_mask':mask,
       'all_assertions':'PASS'},sort_keys=True))
if __name__=='__main__': main()
