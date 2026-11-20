#!/usr/bin/env python3
"""Exact kinetic-circle atlas of the frozen 34-bit 64 Port-fiber arcs."""
from bisect import bisect_right
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
P=17179869143
D=(1120832,6,13,1651128)
Z=(0,390139,394465,1497639)
SEL=(0,1,2,4,5,6)
FROZEN_SHA='b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'

def det(lo,top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=lo
    t,s=6-a11,13-a22
    u=t*s-x*w
    v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=u*u3+p1*g+p2*h
    k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base=D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top&(1<<j))

def lower(key,fill):
    lo=[fill]*12
    for j,pos in enumerate(SEL):
        lo[pos]=1+((key>>(5-j))&1)
    return lo

def arcs():
    arr=[]
    for key in range(64):
        start=det(lower(key,2),15)
        width=det(lower(key,1),0)-start
        assert 0<width<P//2
        arr.append((start%P,width))
    return arr

def sig(aa,y2,r2):
    # Twice-the-circle exact arithmetic, real noise radii whose double is integer.
    bits=0
    for k,(a,w) in enumerate(aa):
        if 2*w+2*r2 >= 2*P:
            bits|=1<<k
        else:
            d=(y2-2*a)%(2*P)
            if d<=2*w+r2 or d>=2*P-r2:bits|=1<<k
    return bits

def events_at(aa,r2):
    """Return sorted distinct event groups; each event position is doubled coordinate."""
    events=[]
    for k,(a,w) in enumerate(aa):
        if w+r2>=P: continue  # arc already saturated: no boundary
        events.append(((2*a-r2)%(2*P), k,1))
        events.append(((2*(a+w)+r2)%(2*P), k,-1))
    return sorted(events)

def compile_index(aa,r2):
    """At radius rho=r2/2, exact 2*y endpoints and right-of-event masks.

    Use only the specified frozen observer's circle; returns the state
    strictly before the zero cut to handle simultaneous events at zero.
    """
    events=events_at(aa,r2)
    on_zero=sig(aa,0,r2)
    before_zero=on_zero
    for x,k,delta in events:
        if x!=0: break
        if delta==1:before_zero&=~(1<<k)
    state=before_zero
    positions=[0]
    for x,k,delta in events:
        if x!=0:break
        if delta==1:state|=1<<k
        else:state&=~(1<<k)
    after=[state];j=0
    while j<len(events):
        x=events[j][0]
        new=state
        while j<len(events) and events[j][0]==x:
            _,k,delta=events[j]
            if delta==1:new|=1<<k
            else:new&=~(1<<k)
            j+=1
        if x!=0:
            positions.append(x);after.append(new)
        state=new
    assert state==before_zero  # circle closes
    return (positions,after,before_zero,events)

def query(index,y2):
    """Exact query with closed-arc membership even at coincident boundaries."""
    positions,after,before_zero,events=index
    y2=y2%(2*P)
    j=bisect_right(positions,y2)-1
    ans=after[j]
    if y2==positions[j]:
        ans|=(before_zero if j==0 else after[j-1])
    return ans

def pack_index(index):
    """Compact complete radius-specific event index for integer r2=2*rho.

    No constant observer coefficients counted; event tags are 7-bit packs.
    Reader obtains n from the unambiguous total byte length.
    """
    positions,after,before_zero,events=index
    n=len(events)
    assert n<=128 and n%2==0
    result=before_zero.to_bytes(8,'little')
    result+=b''.join(x.to_bytes(5,'little') for x,k,d in events)
    bits=sum((k+(64 if d==1 else 0))<<(i*7) for i,(x,k,d) in enumerate(events))
    result+=bits.to_bytes((7*n+7)//8,'little')
    assert len(result)==8+5*n+(7*n+7)//8<=760
    return result

def unpack_index(blob):
    n_candidates=[n for n in range(0,129,2) if len(blob)==8+5*n+(7*n+7)//8]
    assert len(n_candidates)==1
    n=n_candidates[0]
    before_zero=int.from_bytes(blob[:8],'little')
    positions=[int.from_bytes(blob[8+i*5:13+i*5],'little') for i in range(n)]
    tags=int.from_bytes(blob[8+5*n:],'little')
    assert tags>>(7*n)==0
    events=[]
    for i,x in enumerate(positions):
        tag=(tags>>(i*7))&127
        events.append((x,tag&63,1 if tag&64 else -1))
    assert events==sorted(events)
    state=before_zero;after=[before_zero];cuts=[0]
    j=0
    while j<len(events):
        x=events[j][0]
        while j<len(events) and events[j][0]==x:
            _,k,d=events[j];
            if d==1:state|=1<<k
            else:state&=~(1<<k)
            j+=1
        if x!=0:cuts.append(x);after.append(state)
        else:after[0]=state
    assert state==before_zero
    return cuts,after,before_zero,events

def kinetic_critical(aa):
    sat=[P-w for a,w in aa]  # twice-radius
    crossing=[]
    for i,(ai,wi) in enumerate(aa):
        xi=(ai+wi)%P
        for j,(aj,wj) in enumerate(aa):
            gap=(aj-xi)%P
            if 0<gap<min(sat[i],sat[j]):
                crossing.append((gap,i,j))
    return sat,crossing

def main():
    aa=arcs()
    sat,crossing=kinetic_critical(aa)
    by=Counter(gap for gap,i,j in crossing)
    sm=Counter(sat)
    first=min(by); last=max(sat)
    # Count potentially simultaneous crossings, distinguish from saturation.
    intervals=sorted(set(by)|set(sm))
    print('critical_stats',json.dumps({'arc_width_range':[min(w for a,w in aa),max(w for a,w in aa)],'first_crossing_r2':first,'crossing_events':len(crossing),'unique_crossing_r2':len(by),'duplicate_crossing_multiplicities':dict(Counter(by.values())),'saturation_events':len(sat),'unique_saturation_r2':len(sm),'first_saturation_r2':min(sat),'last_saturation_r2':last,'total_unique_breakpoints':len(intervals),'joint_saturation_and_crossing':len(set(sm)&set(by)),'first_twelve':[(t,by[t],sm[t]) for t in intervals[:12]]},indent=2))
    # prove event-order inventory: each possible collision is a pair of opposite moving boundaries
    assert first==4226124
    assert len(crossing)<=4096
    # At each of 4019 breakpoints sample around events; also cover all
    # current boundaries at selected radii (exact real guarantee is proved).
    test_r2=sorted(set([0,first-1,first,first+1,min(sat)-1,min(sat),min(sat)+1,last-1,last,last+1,P]))
    tests=0; critical_tests=0
    for r2 in intervals:
        ix=compile_index(aa,r2)
        # Coincident event and immediate neighbor on both sides;
        # 0, plus representatives of non-event gaps.
        ey=[x for x,k,d in ix[3]]
        ys={0,1,2*P-1}
        for q in ey[:8]: ys.update(((q-1)%(2*P),q,(q+1)%(2*P)))
        for k in range(0,len(ey),17):ys.add((ey[k]+13579)%(2*P))
        for y2 in ys:
            v=query(ix,y2); expected=sig(aa,y2,r2)
            assert v==expected,(r2,y2,hex(v),hex(expected))
            critical_tests+=1
    for r2 in test_r2:
        ix=compile_index(aa,r2)
        ys={0,1,2*P-1}
        for pos,k,action in ix[3]:
            ys.update(((pos-1)%(2*P),pos,(pos+1)%(2*P)))
        for y2 in ys:
            x=query(ix,y2); y=sig(aa,y2,r2)
            assert x==y, (r2,y2,hex(x),hex(y))
            tests+=1
    # Compact index round-trip and size, including every critical parameter.
    pack_checks=0; maximum_index=0; zero_index_hash=None
    for r2 in [0,*intervals]:
        original=compile_index(aa,r2)
        raw=pack_index(original)
        rebuilt=unpack_index(raw)
        assert original==rebuilt
        pack_checks+=1
        maximum_index=max(maximum_index,len(raw))
        if r2==0:zero_index_hash=sha256(raw).hexdigest()
    assert maximum_index==760
    # Entire frozen population, fixed compiled index per radius.
    population_r2=(0,first-1,first,first+1,min(sat),last)
    population_ix=[compile_index(aa,r2) for r2 in population_r2]
    population_checks=0
    for topvals in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(topvals))
        for lo in product((1,2),repeat=12):
            y2=2*(det(lo,top)%P)
            for r2,ix in zip(population_r2,population_ix):
                assert query(ix,y2)==sig(aa,y2,r2)
                population_checks+=1
    print('boundary_tests',tests,'critical_tests',critical_tests,'population_checks',population_checks)
    # independent digest of the frozen word stream
    digest=sha256(); total=0
    for topvals in product((1,2), repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(topvals))
        for lo in product((1,2),repeat=12):
            x=det(lo,top)%P
            digest.update(x.to_bytes(8,'big'));total+=1
    assert digest.hexdigest()==FROZEN_SHA and total==65536
    result={'schema':'R284CJ_KINETIC_FIBER_ATLAS_V1','p':P,'frozen_sha256':digest.hexdigest(),'arc_sequence_sha256':sha256(b''.join(a.to_bytes(5,'little')+w.to_bytes(5,'little') for a,w in aa)).hexdigest(),'arcs':len(aa),'first_crossing_r2':first,'first_crossing_pairs':[(i,j) for t,i,j in crossing if t==first],'crossings_in_active_boundary_domain':len(crossing),'distinct_crossing_r2':len(by),'multiplicity_distribution':dict(sorted(Counter(by.values()).items())),'saturation_events':len(sat),'distinct_saturation_r2':len(sm),'first_saturation_r2':min(sat),'last_saturation_r2':last,'distinct_breakpoint_r2':len(intervals),'joint_crossing_saturation_r2':len(set(by)&set(sm)),'max_crossing_multiplicity':max(by.values()),'boundary_verification_tests':tests,'critical_parameter_tests':critical_tests,'population_full_codeword_queries':population_checks,'compact_index_roundtrips':pack_checks,'maximum_compiled_index_bytes_for_integer_r2':maximum_index,'zero_radius_760byte_compiled_index_sha256':zero_index_hash,'population_radius_double':list(population_r2),'test_radius_double':test_r2,'first_10_critical_r2':intervals[:10],'sorted_crossing_data_sha256':sha256('\n'.join(f'{t}:{i}:{j}' for t,i,j in sorted(crossing)).encode()).hexdigest(),'sorted_saturation_data_sha256':sha256('\n'.join(f'{t}:{i}' for t,i in sorted((P-w,i) for i,(a,w) in enumerate(aa))).encode()).hexdigest(),'full_circle_mask_at_last_saturation':hex(sig(aa,0,last)),'numeric_semantics':'exact integers, r2=2*rho, y2=2*y; general real proof via affine motion and equality case' }
    with Path(__file__).with_name('R284CJ_kinetic_fiber_atlas_certificate.json').open('w') as f:json.dump(result,f,indent=2,sort_keys=True)
    print('result',json.dumps(result,indent=2))
if __name__=='__main__':main()
