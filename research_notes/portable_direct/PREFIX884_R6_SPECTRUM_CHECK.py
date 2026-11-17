from math import gcd
from itertools import product
from collections import Counter
import json
import random

def F(t,z):
    h=1<<t;P=2*h;q,r=divmod(z,P)
    return q*h+max(0,r-h)

def count_bit(L,R,i,shift,want):
    n=F(i,R+shift)-F(i,L+shift)
    return n if want==1 else R-L-n

def prefix_two(r,a,i,di,j,ej):
    # i associated to x+0, j associated to x+a
    if i>=j: high=(i,0,di);low=(j,a,ej)
    else:high=(j,a,ej);low=(i,0,di)
    h=1<<high[0]; P=2*h
    st=(high[2]*h-high[1])%P
    end=st+h; regions=[(st,min(P,end))]
    if end>P:regions.append((0,end-P))
    ans=0
    for lo,hi in regions:
        A=lo;B=min(r,hi)
        if B>A:ans+=count_bit(A,B,low[0],low[1],low[2])
    return ans

def count_w(p,a,d,e):
    N=1<<p
    L=max(0,-a,-d,-a-e)
    U=min(N-1,N-1-a,N-1-d,N-1-a-e)
    if U<L:return 0
    infos=[]
    if d:infos.append(((abs(d).bit_length()-1),0, 0 if d>0 else 1))
    if e:infos.append(((abs(e).bit_length()-1),a,0 if e>0 else 1))
    if not infos:return U-L+1
    if len(infos)==1:
        i,shift,want=infos[0]
        return count_bit(L,U+1,i,shift,want)
    i,_,want_i=infos[0];j,_,want_j=infos[1]
    P=1<<(max(i,j)+1)
    full=prefix_two(P,a,i,want_i,j,want_j)
    def H(z):
        t,r=divmod(z,P)
        return t*full+prefix_two(r,a,i,want_i,j,want_j)
    return H(U+1)-H(L)

def D(p):return [0]+[s*(1<<i) for i in range(p) for s in (+1,-1)]

def collision_count(p,q1,q2):
    N=1<<p;ds=D(p);K=(N-1)//q1
    g=gcd(q1,q2);m=q2//g
    inv=pow(q1//g,-1,m) if m>1 else None
    c=0
    for d in ds:
        for e in ds:
            delta=d-e
            if delta%g:continue
            if m>1:
                root=((delta//g)*inv)%m
                k=root if root else m
            else:k=1
            while k<=K:
                c+=count_w(p,k*q1,d,e)
                k+=m
    c0=0
    for d in ds:
        for e in ds:
            if d!=e and (e-d)%q2==0:
                c0+=count_w(p,0,d,e)
    assert c0%2==0
    return c+c0//2

def direct(p,q1,q2):
    N=1<<p
    counts=Counter()
    for x in range(N):
        for y in [x]+[x^(1<<i) for i in range(p)]:
            counts[x%q1,y%q2]+=1
    return sum(v*(v-1)//2 for v in counts.values()),counts

def symmetry(p,q1,q2,counts):
    N=1<<p
    for (r,s),n in counts.items():
        if counts[((N-1-r)%q1,(N-1-s)%q2)]!=n:
            return False
    return True

def central_fiber(p,q1,q2):
    N=1<<p
    assert q1%2 and q2%2
    r=((N-1)*pow(2,-1,q1))%q1
    s=((N-1)*pow(2,-1,q2))%q2
    count=0
    for x in range(r,N,q1):
        count+=(x%q2==s)
        for i in range(p):
            count+=((x^(1<<i))%q2==s)
    return count

def occupancy_floor(p,q1,q2):
    N=1<<p; t,r=divmod(N,q1)
    def f(z):
        M=z*(p+1);v,s=divmod(M,q2)
        return q2*v*(v-1)//2+s*v
    return r*f(t+1)+(q1-r)*f(t)

if __name__=='__main__':
    tested=0
    for p in range(1,8):
        for q1 in range(1,min(2**p,14),2):
            for q2 in range(1,min(2**p,14),2):
                C,cs=direct(p,q1,q2)
                W=collision_count(p,q1,q2)
                assert C==W,(p,q1,q2,C,W)
                assert symmetry(p,q1,q2,cs),(p,q1,q2)
                assert C>=occupancy_floor(p,q1,q2)
                central=central_fiber(p,q1,q2)
                assert central%2==0 and (C%2)==((central//2)%2)
                tested+=1
    rand=random.Random(884)
    wtests=0
    for p in range(1,9):
        N=1<<p; ds=D(p)
        for _ in range(900):
            a=rand.randrange(N+1);d=rand.choice(ds);e=rand.choice(ds)
            expected=sum(0<=x+d<N and 0<=x+a<N and 0<=x+a+e<N and
                         (d==0 or (x^(x+d))==abs(d)) and
                         (e==0 or ((x+a)^(x+a+e))==abs(e)) for x in range(N))
            assert count_w(p,a,d,e)==expected,(p,a,d,e)
            wtests+=1
    pairs=[(524287,524285),(500383,522777),(523001,523003),(262143,524287),(524287,524287)]
    big=[]
    for q1,q2 in pairs:
        C=collision_count(32,q1,q2)
        lb=occupancy_floor(32,q1,q2)
        center=central_fiber(32,q1,q2)
        assert center%2==0 and C%2==(center//2)%2
        print('BIG',q1,q2,C,lb,center)
        big.append({'q1':q1,'q2':q2,'collisions':C,'occupancy_lower_bound':lb,'central_fiber_multiplicity':center})
    out={'schema':'PREFIX884_R6_RESULTS_V1','model':'p named binary sources, zero or single XOR bit transition; ordered two-port residues','randomized_w_checks':wtests,'random_seed':884,'small_exhaustive_pair_checks':tested,'small_p_range':[1,7],'small_odd_moduli':'1..min(2^p-1,13)','assertions':['collision_count_from_d_e_lattice_equals_direct_multiset_second_moment','complement_observation_fiber_multiplicity_symmetry','fiber_occupancy_lower_bound','odd_q_central_fiber_parity_invariant'], 'large_p':32,'large_pairs':big}
    with open('PREFIX884_R6_SPECTRUM_RESULTS.json','w') as f:json.dump(out,f,indent=2,ensure_ascii=False)
    print('SMALL',tested,'RANDOM',wtests)
