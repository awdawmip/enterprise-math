#!/usr/bin/env python3
"""R27: event-select proof-of-concept for exact S23/AV risk epochs.
No loop over future cut count in the generator. Independently compares to R16 and R25.
"""
from fractions import Fraction
from bisect import bisect_right
from pathlib import Path
import csv, random, sys, time, os
D = 10**24
P = 262204504569236716045286
LO, HI = Fraction(P,D), Fraction(P+1,D)
MID = (LO+HI)/2
M = 128
ORDER = sorted(range(M),key=lambda t:(t*MID.numerator)%MID.denominator)
ARCS = [(u, ORDER[(z+1)%M]) for z,u in enumerate(ORDER)]
A = MID.numerator
B = MID.denominator

# Euclidean floor sums; exact signed-offset normalization.
def floor_sum(n,mod,a,b):
    assert n>=0 and mod>0 and a>=0 and b>=0
    out=0
    while True:
        if a>=mod:
            out += n*(n-1)*(a//mod)//2
            a%=mod
        if b>=mod:
            out += n*(b//mod)
            b%=mod
        z=a*n+b
        if z<mod: return out
        n=z//mod
        b=z%mod
        mod,a=a,mod

def shifted(l,r,shift):
    n=r-l
    if n<=0:return 0
    q,rem=divmod((l-shift)*A,B)
    return n*q+floor_sum(n,B,A,rem)

def below(s,l,r):
    return shifted(l,r,0)-shifted(l,r,s)-(r-l)*(s*A//B)

def inarc(s,e,l,r):
    if l>=r:return 0
    z=below(e,l,r)-below(s,l,r)
    if (s*A)%B>(e*A)%B:z+=r-l
    assert 0<=z<=r-l,(s,e,l,r,z)
    return z

def farey(n):
    assert n>=2
    bound=n-1
    a,i,c,j=0,1,1,1
    moves=0
    while i+j<=bound:
        diff1=A*i-B*a
        diff2=B*c-A*j
        assert diff1>0 and diff2>0
        if diff1>diff2:
            z=min((diff1-1)//diff2,(bound-i)//j)
            assert z>0
            a+=z*c; i+=z*j
        else:
            z=min((diff2-1)//diff1,(bound-j)//i)
            assert z>0
            c+=z*a; j+=z*i
        moves+=1
    assert i*c-j*a==1 and i+j>=n and i<n and j<n
    assert Fraction(a,i)<LO and HI<Fraction(c,j),('enclosure-crossing',n)
    return a,i,c,j,moves

def pairmax(x,y):
    vl=lambda z:z[0]+z[1]*LO
    vh=lambda z:z[0]+z[1]*HI
    assert (vl(x)>=vl(y)) == (vh(x)>=vh(y)),(x,y)
    return x if vl(x)>=vl(y) else y

def oracle(n):
    a,i,c,j,_=farey(n)
    gaps=[(-a,i),(c,-j),(c-a,i-j)]
    ranges=[(0,n-i),(j,n),(n-i,j)]
    ans=(1,0)
    for s,e in ARCS:
        count=[inarc(s,e,l,r) for l,r in ranges]
        assert sum(count)>0
        winners=[gaps[k] for k in range(3) if count[k]]
        best_lo=max(winners,key=lambda z:z[0]+z[1]*LO)
        best_hi=max(winners,key=lambda z:z[0]+z[1]*HI)
        assert best_lo==best_hi,('risk winner enclosure crosses',n,s,e,winners,best_lo,best_hi)
        best=best_lo
        ans=(ans[0]-best[0],ans[1]-best[1])
    return ans

def last_witness(s,e,l,j):
    """Largest source t in [l,j) that belongs to historical arc (s,e).
    Return None if no such source. Each rank/select count is O(log B).
    """
    if l>=j or inarc(s,e,l,j)==0:return None
    low,high=l,j-1
    while low<high:
        mid=(low+high+1)//2
        if inarc(s,e,mid,j):low=mid
        else:high=mid-1
    assert inarc(s,e,low,low+1)==1
    return low

def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]

def generator(N,verify_regime=False):
    assert N>=M
    n0=M
    value=(0,0)
    event_map={} # n -> exact delta coefficients
    regimes=[]
    event_count=0
    while n0<=N:
        a,i,c,j,jumps=farey(n0)
        nend=min(N,i+j)
        first=max(M,n0)
        # Verify starting risk when crossing different Farey bracket.
        if verify_regime:
            assert value==oracle(n0),(n0,value,oracle(n0))
        events=[]
        for s,e in ARCS:
            t=last_witness(s,e,first-i,j)
            if t is None:continue
            event=i+t+1
            assert first<event<=i+j,(first,nend,event,t,i,j)
            if event<=nend:
                events.append((event,s,e,t))
        # Unique event position: one global w gap is destroyed per insertion.
        assert len({x[0] for x in events})==len(events)
        if events:
            incr=pairmax((-a,i),(c,-j))
            w=(c-a,i-j)
            gap=(w[0]-incr[0],w[1]-incr[1])
            assert gap[0]+gap[1]*LO>0 and gap[0]+gap[1]*HI>0
        else:
            gap=(0,0)  # only the current observer is needed; u/v comparison is irrelevant
        for event,s,e,t in events:
            assert event not in event_map
            event_map[event]=gap
            event_count+=1
        end_value=add(value,(len(events)*gap[0],len(events)*gap[1]))
        if verify_regime:
            assert end_value==oracle(nend),(n0,nend,end_value,oracle(nend))
        regimes.append((first,nend,i,j,len(events),gap))
        if nend==N:
            value=end_value
            break
        # Each transition is one exact insertion, independently queried.
        next_value=oracle(nend+1)
        trans=sub(next_value,end_value)
        assert trans[0]+trans[1]*LO>=0 and trans[0]+trans[1]*HI>=0
        if trans!=(0,0):
            event_map[nend+1]=trans
            event_count+=1
        value=next_value
        n0=nend+1
    return event_map,regimes,value

def lookup(events,n):
    out=(0,0)
    for pos,d in events.items():
        if pos<=n:out=add(out,d)
    return out

def read_r16(path):
    rows=list(csv.DictReader(open(path),delimiter='\t'))
    rr=[]
    for x in rows:
        rr.append(tuple(int(x[k]) for k in ['n0','n1','A0','B0','dA','dB']))
    return rr

def table_value(rows,n):
    for s,e,A0,B0,dA,dB in rows:
        if s<=n<=e:
            return (A0+(n-s)*dA,B0+(n-s)*dB)
    raise ValueError(n)

def run(N):
    tic=time.monotonic()
    ev,regs,end=generator(N,verify_regime=True)
    dur=time.monotonic()-tic
    positions=sorted(ev)
    # Compute risk by sweepline from sorted jump list.
    cumulative=[]; running=(0,0)
    for pos in positions:
        running=add(running,ev[pos])
        cumulative.append((pos,running))
    assert running==end,(running,end)
    def at(n):
        k=bisect_right(positions,n)-1
        return cumulative[k][1] if k>=0 else (0,0)
    root=Path(__file__).resolve().parent
    outdir=Path(os.environ.get('R27_OUT_DIR',str(root)))
    outdir.mkdir(parents=True,exist_ok=True)
    r16=Path(os.environ.get('R16_FILE',str(root/'AFFINE_RUNS_1T.tsv')))
    rows=read_r16(r16) if r16.is_file() else None
    rng=random.Random(20261110)
    probes=set(range(128,min(N,700)+1))
    if rows is not None:
        for s,e,*_ in rows:
            probes.update(n for n in (s-1,s,s+1,e-1,e,e+1) if 128<=n<=N)
    probes.update(rng.randint(128,N) for _ in range(200))
    for n in sorted(probes):
        if rows is not None:
            assert at(n)==table_value(rows,n),('R16 mismatch',n,at(n),table_value(rows,n))
        else:
            assert at(n)==oracle(n),('oracle mismatch',n,at(n),oracle(n))
    r25=Path(os.environ.get('R25_FILE',str(root/'EPOCHS_R25.tsv')))
    if rows is not None and N<=323000 and r25.is_file():
        with r25.open() as f:
            epos=list(csv.DictReader(f,delimiter='\t'))
        for e in epos:
            for n in (int(e['n_first'])-1,int(e['n_first']),int(e['n_last'])):
                if 128<=n<=N:
                    assert at(n)==table_value(rows,n)
    assert at(N)==oracle(N)
    # Independent direct phase partition (no Farey gaps or floor-sum rank).
    if N>=500:
        for n in range(128,501):
            order=sorted(range(n),key=lambda t:(t*MID.numerator)%MID.denominator)
            rank_hist={t for t in range(M)}
            start=next(k for k,t in enumerate(order) if t in rank_hist)
            mx=Fraction(0); maxima=[]
            for k in range(n):
                u=order[(start+k)%n]
                v=order[(start+k+1)%n]
                z=(((v*MID)%1)-((u*MID)%1))%1
                mx=max(mx,z)
                if v in rank_hist:
                    maxima.append(mx)
                    mx=Fraction(0)
            assert len(maxima)==M
            assert at(n)[0]+at(n)[1]*MID==1-sum(maxima),(n,at(n))
    # Turn sparse positive increments into maximal constant-increment affine runs.
    run_rows=[]
    cursor=M
    cur=(0,0)
    for pos in positions:
        if pos>cursor+1:
            run_rows.append((cursor,pos-1,*cur,0,0))
            cursor=pos-1
        d=ev[pos]
        if run_rows and run_rows[-1][1]==pos-1 and run_rows[-1][4:]==d:
            x=run_rows[-1]
            run_rows[-1]=(x[0],pos,x[2],x[3],*d)
        else:
            run_rows.append((cursor,pos,*cur,*d))
        cur=add(cur,d)
        cursor=pos
    if cursor<N:
        run_rows.append((cursor,N,*cur,0,0))
    assert cur==end
    with (outdir/'AFFINE_RUNS_R27.tsv').open('w') as f:
        f.write('n0\tn1\tA0\tB0\tdA\tdB\n')
        for z in run_rows:f.write('\t'.join(map(str,z))+'\n')
    if rows is not None and N==1000000000128:
        assert run_rows==rows,(len(run_rows),len(rows),next((k for k in range(min(len(rows),len(run_rows))) if rows[k]!=run_rows[k]),None))
    with (outdir/'EVENTS_R27.tsv').open('w') as f:
        f.write('n\tdelta_A\tdelta_B\n')
        for pos in positions:
            f.write(f'{pos}\t{ev[pos][0]}\t{ev[pos][1]}\n')
    with (outdir/'REGIMES_R27.tsv').open('w') as f:
        f.write('n0\tn1\ti\tj\tevents\tdelta_A\tdelta_B\n')
        for s,e,i,j,k,d in regs:
            f.write(f'{s}\t{e}\t{i}\t{j}\t{k}\t{d[0]}\t{d[1]}\n')
    print('PASS_R27_FAREY_REGIME_SELECT_EXACT')
    print('N',N,'regimes',len(regs),'positive_events',len(ev),'crosschecks',len(probes),
          'end',at(N),'affine_runs',len(run_rows),'elapsed_s',round(dur,3),'max_regime_len',max(e-s+1 for s,e,*_ in regs))
    print('First regimes',regs[:8]);print('Last regimes',regs[-8:]);
    if N==1000000000128:
        print('RISK_1T',at(N))

if __name__=='__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 323000)
