"""Original Hart score, exact shell, exact run enumeration and prime certificates."""
import argparse
import json
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, prod
from pathlib import Path

ROWS=[[12, 0, 1, 3, 22906492243], [12, 1, 6, 3, 22909288559], [24, 0, 1, 11, 429306043897240473923], [24, 1, 6, 11, 429306056691557724251], [24, 1, 128, 11, 429306044496974089399], [24, -1, 128, 11, 429306043297506859091], [36, 0, 1, 23, 14109502332975075077528522633657], [36, 1, 6, 23, 14109502333077735218460720426293], [48, 0, 1, 67, 332846943261651091664712213024602410536913]]
PRATT={22906492243: (2, {2: 1, 3: 1, 79: 1, 3359: 1, 14387: 1}), 22909288559: (11, {2: 1, 13: 1, 881126483: 1}), 881126483: (2, {2: 1, 19: 1, 3361: 1, 6899: 1}), 429306043897240473923: (2, {2: 1, 7: 1, 53: 1, 42960613: 1, 13467675007: 1}), 42960613: (5, {2: 2, 3: 1, 43: 1, 83257: 1}), 13467675007: (3, {2: 1, 3: 3, 7069: 1, 35281: 1}), 429306056691557724251: (2, {2: 1, 5: 3, 11: 1, 13: 1, 67: 1, 73: 1, 127: 1, 19332569747: 1}), 19332569747: (2, {2: 1, 7: 1, 2411: 1, 572749: 1}), 429306044496974089399: (3, {2: 1, 3: 2, 43: 1, 31601: 1, 17551943679577: 1}), 17551943679577: (10, {2: 3, 3: 1, 571: 1, 1280789819: 1}), 1280789819: (6, {2: 1, 7: 1, 11: 1, 59: 1, 73: 1, 1931: 1}), 429306043297506859091: (2, {2: 1, 5: 1, 13513: 1, 3176985445848493: 1}), 3176985445848493: (5, {2: 2, 3: 1, 331: 1, 1367: 1, 585109933: 1}), 585109933: (2, {2: 2, 3: 1, 11: 1, 113: 1, 39227: 1}), 14109502332975075077528522633657: (3, {2: 3, 67: 1, 241: 1, 1867: 1, 445433: 1, 131341858343127871: 1}), 131341858343127871: (3, {2: 1, 3: 1, 5: 1, 101: 1, 2469041: 1, 17556269: 1}), 2469041: (3, {2: 4, 5: 1, 7: 1, 4409: 1}), 17556269: (2, {2: 2, 23: 1, 190829: 1}), 14109502333077735218460720426293: (2, {2: 2, 769: 1, 5881: 1, 779963330650319725402357: 1}), 779963330650319725402357: (5, {2: 2, 3: 1, 271: 1, 1031: 1, 232629604836274663: 1}), 232629604836274663: (3, {2: 1, 3: 1, 29: 1, 613: 1, 5227: 1, 417256163: 1}), 417256163: (2, {2: 1, 208628081: 1}), 208628081: (3, {2: 4, 5: 1, 17: 1, 179: 1, 857: 1}), 332846943261651091664712213024602410536913: (5, {2: 4, 3: 1, 2089: 1, 9227: 1, 359752959175115531062448703549973: 1}), 359752959175115531062448703549973: (2, {2: 2, 3: 2, 11: 1, 13: 1, 12269: 1, 5695825430096046438770431: 1}), 5695825430096046438770431: (6, {2: 1, 3: 2, 5: 1, 7: 2, 1291570392312028670923: 1}), 1291570392312028670923: (3, {2: 1, 3: 3, 73: 1, 1637: 1, 200148703592443: 1}), 200148703592443: (3, {2: 1, 3: 1, 11: 1, 103: 1, 2837: 1, 10377967: 1}), 10377967: (3, {2: 1, 3: 1, 409: 1, 4229: 1})}


def floor_cube(n):
    a,b=0,1<<((n.bit_length()+2)//3)
    while b-a>1:
        m=(a+b)//2
        if m**3<=n:
            a=m
        else:
            b=m
    return b if b**3==n else a


@cache
def certify_prime(p):
    if p<10**6:
        assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
        return
    a,factors=PRATT[p]
    assert prod(l**e for l,e in factors.items())==p-1 and pow(a,p-1,p)==1
    for l in factors:
        certify_prime(l)
        assert gcd(pow(a,(p-1)//l,p)-1,p)==1


def shell(N):
    a=floor_cube(N)
    return a+int(a**3<N),floor_cube(8*N)


def pair(N,k):
    s=4*N*k
    x=isqrt(s-1)+1
    return x*x-s,2*x-1


def runs(N,lo,hi,a,b):
    assert lo<=hi and 0<a<b
    size=hits=count=best=0
    first=None
    for k in range(lo,hi+1):
        v,w=pair(N,k)
        if b*v<=a*w:
            hits+=1
            if size==0:
                count+=1
            size+=1
            if size>best:
                best=size
                first=k-size+1
        else:
            size=0
    answer={'interval':[lo,hi],'hits':hits,'runs':count,'longest_length':best,
            'longest_first_start':first}
    if first is not None:
        mx=max(Fraction(*pair(N,k)) for k in range(first,first+best))
        assert b*mx.numerator<=a*mx.denominator
        answer['largest_score_in_witness']=[mx.numerator,mx.denominator]
    return answer


def last_true(upper,condition):
    a,b=0,upper+1
    while b-a>1:
        v=(a+b)//2
        if condition(v):
            a=v
        else:
            b=v
    return a


def sample(t,off_num,off_den,p,q):
    certify_prime(p);certify_prime(q)
    T=Fraction(2**t)+Fraction(off_num,off_den)
    N=p*q
    assert p!=q and p%2==q%2==1 and 0<=T**3-N
    assert p**8>=T and p**8<=256*T
    low,high=shell(N); K0=floor_cube(N)
    # 2g'(k) >= j2 on the right of K, checked without a radical.
    threeK=floor_cube(27*N)
    j2=threeK+int(threeK**3<27*N)
    def upper(k):
        return k>=j2 or 4*N>=k*(j2-k)**2
    a=low-1;b=high
    assert upper(b)
    while b-a>1:
        m=(a+b)//2
        if upper(m):
            b=m
        else:
            a=m
    x0=b
    grid=2**100
    h=floor_cube(27*N*grid**3)
    dd=Fraction(h-threeK*grid+1,2*grid)
    radius=last_true(K0,lambda r:r**3+(x0-K0)*r*r<=K0)
    radius2=last_true(K0,lambda r:r**3*dd.denominator+K0*r*dd.numerator<=K0*dd.denominator)
    assert radius>=1 and radius2>=1
    rows={}
    for key,start,R in [('upper_half_integer',x0,radius),('lower_half_integer',low,radius2)]:
        rows[key]=runs(N,start,min(high,start+12*R),3,10)
    eps0=Fraction(h,grid)-threeK
    return {'T':str(T),'p':p,'q':q,'N':N,'shell': [low,high],
            'threeK_fractional_part_outward_10pow9':
            [int(eps0*10**9),int((eps0+Fraction(1,grid))*10**9)+1],
            'upper_stationary_ceiling':x0,'upper_scan_radius':radius,'lower_scan_radius':radius2,
            'alpha':[3,10],'certified_subwindow_runs':rows,
            'full_shell_if_computed':runs(N,low,high,3,10) if high-low<=5000 else None}


def main():
    output=[]
    for N in [7,11,29,77,609,1009*1013,10007*10177,1000003*1000033,10**9]:
        low,high=shell(N)
        for a,b in [(1,4),(3,10),(1,3),(1,2),(3,4)]:
            row=runs(N,low,high,a,b)
            if a*4<=b:
                assert row['longest_length']<=4
            if a*3<b and a*4>b and row['longest_length']>=8:
                start=row['longest_first_start']
                xs=[(pair(N,k)[1]+1)//2 for k in range(start,start+row['longest_length'])]
                second=[z-2*y+x for x,y,z in zip(xs,xs[1:],xs[2:])]
                assert set(second)<={0,-1}
            output.append({'N':N,'alpha':[a,b],**row})
    for n in range(1,129):
        lo,hi=shell(n)
        for k in range(lo,hi+1):
            v,w=pair(n,k);x=0
            while x*x<4*n*k:
                x+=1
            assert (v,w)==(x*x-4*n*k,2*x-1)
    return {'method':'Exact isqrt and rational thresholds. Only full-shell rows claim a global maximum.',
            'ordered_small_grid_n':[1,128],
            'full_shell_results':output,
            'pratt_nontrivial_nodes':len(PRATT),
            'resonance_samples':[sample(*args) for args in ROWS]}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    data=json.dumps(main(),ensure_ascii=False,indent=2)+'\n'
    if args.out:
        args.out.write_text(data,encoding='utf-8')
    else:
        print(data,end='')
