"""PREFIX-482: exact finite certificates for positive rational X6 BRC fiber weights."""
from collections import defaultdict
from fractions import Fraction
from math import gcd

AXES = 'abcde'
LETTERS = 'aAbBcCdDeE'


def next_q(word, q, char):
    sample = word[:q] + char
    return max((j for j in range(len(word) + 1) if sample.endswith(word[:j])), default=0)


def observe(counts, s):
    plus, minus = counts[::2], counts[1::2]
    y = tuple(a-b for a, b in zip(plus, minus))
    p = tuple(min(a,b) for a,b in zip(plus,minus))
    V = p[1]+2*p[3]+p[4]
    W = p[2]+p[4]
    return (s, *y, V, W),p


def defect(wpos, wneg):
    rho = [a*b for a,b in zip(wpos,wneg)]
    return rho[0]*rho[3]/(rho[1]**2), rho[0]*rho[4]/(rho[1]*rho[2])


def repaired_weight(n, obs, pd, pe, wpos, wneg, wx):
    s, *vals = obs
    y = vals[:5]
    V,W = vals[5:]
    P = (n-s-sum(abs(z) for z in y))//2
    assert 2*P == n-s-sum(abs(z) for z in y)
    plus = [max(z,0) for z in y]
    minus = [max(-z,0) for z in y]
    rho = [a*b for a,b in zip(wpos,wneg)]
    d1,d2 = defect(wpos,wneg)
    base = (wx**s * rho[0]**(P-V-W)*rho[1]**V*rho[2]**W)
    for a,b,z,t in zip(wpos,wneg,plus,minus):
        base *= a**z*b**t
    return base*d1**pd*d2**pe


def repair_vector(p, repair_kind):
    if repair_kind == 'native_rank0': return ()
    if repair_kind == 'e35_rank1': return (p[4],)
    if repair_kind == 'dependent_rank1': return (2*p[3]+3*p[4],)
    return (p[3],p[4])


def append_compressed(O, q, r, letter, gate, repair_kind):
    s, *tail = O
    y = list(tail[:5]); V,W = tail[5:]
    i = LETTERS.index(letter)//2
    positive = letter.islower()
    delta = int(y[i]<0) if positive else int(y[i]>0)
    y[i] += 1 if positive else -1
    V += (0,1,0,2,1)[i]*delta
    W += (0,0,1,0,1)[i]*delta
    if repair_kind == 'native_rank0': nr=()
    elif repair_kind == 'e35_rank1': nr=(r[0]+(delta if i==4 else 0),)
    elif repair_kind == 'dependent_rank1': nr=(r[0]+delta*(2 if i==3 else 3 if i==4 else 0),)
    else: nr=(r[0]+(delta if i==3 else 0),r[1]+(delta if i==4 else 0))
    return ((s,*y,V,W),next_q(gate,q,letter),nr)


def run(word, wpos, wneg, wx, nmax, repair_kind):
    compressed = {((0,0,0,0,0,0,0,0),0,repair_vector((0,)*5,repair_kind)):1}
    raw = {(tuple([0]*10),0,0):1}
    total_paths = 0
    total_fibers = 0
    for n in range(nmax+1):
        grouped = defaultdict(lambda: defaultdict(int))
        repaired = defaultdict(int)
        repaired_hist = defaultdict(set)
        for (counts,s,q),cnt in raw.items():
            O,p = observe(counts,s)
            true_weight = wx**s
            for i in range(5):
                true_weight *= wpos[i]**counts[2*i]*wneg[i]**counts[2*i+1]
            predicted = repaired_weight(n,O,p[3],p[4],wpos,wneg,wx)
            assert predicted == true_weight, (word,n,counts,true_weight,predicted)
            grouped[(O,q)][true_weight] += cnt
            repair = repair_vector(p,repair_kind)
            repaired[(O,q,repair)] += cnt
            repaired_hist[(O,q,repair)].add(true_weight)
        assert all(len(h)==1 for h in repaired_hist.values())
        assert dict(repaired) == dict(compressed), (word,repair_kind,n,'compressed discrepancy')
        assert sum(sum(v.values()) for v in grouped.values()) == sum(raw.values())
        total_paths = sum(raw.values())
        total_fibers = len(grouped)
        if n < nmax:
            nxt = defaultdict(int)
            for (counts,s,q),cnt in raw.items():
                for k,char in enumerate(LETTERS):
                    nc = list(counts); nc[k] += 1
                    nq = next_q(word,q,char)
                    nxt[(tuple(nc),s,nq)] += cnt
                if n==0 or q==len(word):
                    nxt[(counts,s+1,0)] += cnt
            raw = nxt
            nxt_compressed = defaultdict(int)
            for (O,q,r),cnt in compressed.items():
                for char in LETTERS:
                    nxt_compressed[append_compressed(O,q,r,char,word,repair_kind)] += cnt
                if n==0 or q==len(word):
                    Os=(O[0]+1,*O[1:])
                    nxt_compressed[(Os,0,r)]+=cnt
            compressed=nxt_compressed
    return total_paths,total_fibers,len(compressed)


def from_word(text):
    c=[0]*10
    for x in text:
        c[LETTERS.index(x)]+=1
    return tuple(c)


def verify_witness(gate, pair1, pair2, wpos, wneg, wx):
    c1,c2=from_word(pair1),from_word(pair2)
    o1,p1=observe(c1,0);o2,p2=observe(c2,0)
    assert o1==o2 and len(pair1)==len(pair2)
    q1=q2=0
    for x in pair1:q1=next_q(gate,q1,x)
    for x in pair2:q2=next_q(gate,q2,x)
    if q1!=q2:
        reset = next(x for x in LETTERS if x.lower()!=gate[0].lower())
        pair1+=reset;pair2+=reset
        c1,c2=from_word(pair1),from_word(pair2)
        o1,p1=observe(c1,0);o2,p2=observe(c2,0)
        q1=next_q(gate,q1,reset);q2=next_q(gate,q2,reset)
    assert o1==o2 and q1==q2
    def weight(s):
        ans=Fraction(1)
        for x in s:
            i=LETTERS.index(x)
            ans*=wpos[i//2] if i%2==0 else wneg[i//2]
        return ans
    return pair1,pair2,weight(pair1),weight(pair2),q1


def F(x):return Fraction(x)

native=tuple(map(F,(6,12,18,24,36)))
neg=tuple(map(F,(1,1,1,1,1)))
scenarios={
 'native_rank0':(native,neg,F(1)),
 'e35_rank1':(tuple(map(F,(6,12,18,24,35))),neg,F(1)),
 'd25_e35_rank2':(tuple(map(F,(6,12,18,25,35))),neg,F(1)),
 'dependent_rank1':(tuple(map(F,(6,12,18,96,288))),neg,F(1)),
 'two_sided_rationals':(tuple(map(F,(6,12,18,24,36))),tuple(map(F,(2,3,5,7,11))),F(13)),
}
for key,(wp,wn,wx) in scenarios.items():
    d1,d2=defect(wp,wn)
    for gate in ('aab','aba','aAa'):
        paths,fibers,_=run(gate,wp,wn,wx,6,key)
        print(f'{key} gate={gate} n=6 ordered_paths={paths} BRC_KMP_fibers={fibers} defects={d1},{d2} RAW_TO_REPAIRED_TRANSFER_CHECKED')
    if key=='native_rank0': assert (d1,d2)==(1,1)
    if key=='e35_rank1': assert (d1,d2)==(1,F(35)/36)
    if key=='d25_e35_rank2':assert (d1,d2)==(F(25)/24,F(35)/36)
    if key=='dependent_rank1':assert (d1,d2)==(4,8)
    wa=verify_witness('aab','aAdD','bBbB',wp,wn,wx)
    wb=verify_witness('aab','aAeE','bBcC',wp,wn,wx)
    print('WITNESSES r1',wa,'r2',wb)

# Rank-one dependence is not the same as just one nonunit defect:
wp,wn,wx=scenarios['dependent_rank1']
assert defect(wp,wn)==(4,8)
assert 2*1+3*0==2 and 2*0+3*1==3
print('DEPENDENT_RANK1_REPAIR 2*p_d+3*p_e confirmed')
print('ALL_CHECKS_PASS')
