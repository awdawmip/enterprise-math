#!/usr/bin/env python3
"""R284EZ: exact bounded Hamming-jump checks, Python stdlib only."""
import itertools, json
from pathlib import Path

def ms(n,k):
    for r in range(k+1):
        for comb in itertools.combinations(range(n),r):
            yield sum(1<<b for b in comb)

def enc(u,q,h):
    t=min(q,h//2);v=u+q
    if v==0: return (0,1,3,2),[[0,1],[1,3],[3,2],[2,0]],2
    a,b,c=v,3*u+2*q+t+1,v+1
    A=(1<<a)-1; B=((1<<b)-1)<<a;C=((1<<c)-1)<<(a+b)
    codes=(0,B|C,A|C,A|B)
    rows=[]
    for i in range(4):
        Bpos=list(range(a,a+b)); seq=[]
        if i%2==0:
            K=2*u+q+t;seq.extend(Bpos[:K])
            for x,y in zip(range(a+b,a+b+c),Bpos[K:]):seq.extend([x,y])
        else:
            K=2*u+q+t+1;seq.extend(Bpos[:K])
            for x,y in zip(range(a),Bpos[K:]):seq.extend([x,y])
        cur=codes[i]; row=[cur]
        for p in seq:
            cur^=1<<p;row.append(cur)
        assert cur==codes[(i+1)%4]
        assert len(seq)==(codes[i]^codes[(i+1)%4]).bit_count()
        rows.append(row)
    return codes,rows,a+b+c

def bridge(x,endpoint,n,u,v):
    bits=[j for j in range(n) if (x^endpoint)>>j&1]
    assert len(bits)<=u+v
    z=x
    for j in bits[:min(u,max(0,len(bits)-v))]:z^=1<<j
    assert (z^x).bit_count()<=u and (z^endpoint).bit_count()<=v
    return z

def witness(u,q,h):
    t=min(q,h//2);c=q-t;v=u+q;T=2*u+q; d=4*u+3*q+t
    if v==0:return {"u":u,"q":q,"h":h,"obstruction":"distinct labels","edge_required":1}
    assert d>=2*v+1
    # A=j, B=c, C=d-j-c; pick j meeting all constraints
    j=max(t,d-c-t-T)
    assert j<=min(d-c-t,T+t)
    k=j+c
    F1=sum(1<<p for p in range(j,j+c))+sum(1<<p for p in range(k,k+t))
    F2=sum(1<<p for p in range(j,j+c))+sum(1<<p for p in range(j-t,j))
    assert F1.bit_count()<=q and F2.bit_count()<=q
    assert (F1^F2).bit_count()<=h
    xj=(1<<j)-1; xk=(1<<k)-1; old=0;new=(1<<d)-1
    act1=xj^F1;act2=xk^F2
    y1=bridge(act1,new,d,u,v);y2=bridge(act2,old,d,u,v)
    assert (y1^new).bit_count()<=v and (y2^old).bit_count()<=v
    return {"u":u,"q":q,"h":h,"t":t,"edge_distance":d,"j":j,"k":k,"F_before":hex(F1),"F_after":hex(F2),"read_new":hex(y1),"read_old":hex(y2),"result":"ROLLBACK_AT_EDGE_BELOW_THRESHOLD"}

def verify(u,q,h):
    v=u+q;t=min(q,h//2);A=4*u+3*q+t+1; B=2*v+1
    codes,rows,n=enc(u,q,h)
    assert n==5*u+4*q+t+2
    for i in range(4):
        for j in range(i+1,4):
            dij=(codes[i]^codes[j]).bit_count()
            assert dij >= (A if (j-i)%4 in (1,3) else B)
    nread=0;npairs=0
    faults=list(ms(n,q));err=list(ms(n,u))
    for i,row in enumerate(rows):
        new=(i+1)%4
        # All observations at a prefix; record potential labels for each fixed F.
        avail=[]
        for p,x in enumerate(row):
            labels={}
            for f in faults:
                seen=set()
                for e in err:
                    y=x^f^e
                    hits=[j for j,z in enumerate(codes) if (y^z).bit_count()<=v]
                    assert len(hits)<=1
                    label=hits[0] if hits else None
                    assert label in (None,i,new)
                    if p==0:assert label==i
                    if p==len(row)-1:assert label==new
                    seen.add(label); nread+=1
                labels[f]=seen
            avail.append(labels)
        # compare any two read times (ordered prefix) with <=h mask change
        for j,states_1 in enumerate(avail):
            new_masks=[f for f,s in states_1.items() if new in s]
            for k in range(j,len(row)):
                old_masks=[f for f,s in avail[k].items() if i in s]
                for f in new_masks:
                    for g in old_masks:
                        npairs+=1
                        assert (f^g).bit_count()>h,(u,q,h,i,j,k,f,g)
    return {"u":u,"q":q,"h":h,"t":t,"n":n,"observations":nread,"potential_rollback_pairs_examined":npairs,"result":"PASS"}

if __name__=='__main__':
    cases=[];wit=[]
    for u in range(2):
        for q in range(3):
            for h in range(2*q+1):
                cases.append(verify(u,q,h));wit.append(witness(u,q,h))
    out={"record":"R284EZ_BOUNDED_ONE_MASK_JUMP","theorem":"n_min=5*u+4*q+min(q,floor(h/2))+2", "model":"at most one mask change per edge; each pre/post mask weight <=q; Hamming jump <=h; each read transient mask weight <=u; unique-radius-(u+q) decoder; no rollback even at same prefix", "checks":cases,"edge_sharpness_witnesses":wit,"review":"NOT_REVIEWED"}
    p=Path('/mnt/data/R284EZ_bounded_single_mask_jump_certificate.json')
    p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({"cases":len(cases),"reads":sum(z['observations'] for z in cases),"pairs":sum(z['potential_rollback_pairs_examined'] for z in cases),"file":str(p)},ensure_ascii=False))
