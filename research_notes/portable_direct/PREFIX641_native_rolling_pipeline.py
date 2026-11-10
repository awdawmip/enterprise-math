#!/usr/bin/env python3
"""PREFIX641: exact integer BRC jet vector pipeline and sliding benchmarks.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reuses frozen PREFIX638 native labelled 576-action BRC+AC and PREFIX640 integer products.
"""
import json,time,hashlib,sys,statistics,math
from pathlib import Path
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import PREFIX640_fraction_free_rolling_jet as ff
native=ff.native
ZERO=ff.Z

def initial_integer():
    """Native four-phase probe r0, exact common-denominator integer representation."""
    v=native.embed()
    den=math.lcm(*(x.denominator for x in v))
    out=[int(x*den) for x in v]
    return out,den

def integer_port_step(v,den,g):
    """Native 96-port BRC propagation, no division in intermediate step."""
    f=Q(g);a,b=f.numerator,f.denominator
    nxt=[0]*96
    for src,edges in enumerate(native.BY):
        val=v[src]
        if val==0:continue
        for aid,d,w,gated in edges:
            wt=a if gated else b*w.numerator
            if wt:nxt[d]+=val*wt
    return nxt,den*b

def integer_vec_apply(v,M):
    out={}
    for src,x in v.items():
        for d,y in M.rows.get(src,{}).items():
            z=ff.jetmul(x,y)
            out[d]=ff.add(out.get(d,ZERO),z)
    return out

def integer_query(v,den,Qq):
    state={s*native.S:(x,0,0,0,0,0) for s,x in enumerate(v) if x}
    denominator=den
    matrices=([Qq.front[-1][1]] if Qq.front else [])+([Qq.back[-1][1]] if Qq.back else [])
    for M in matrices:
        state=integer_vec_apply(state,M)
        denominator*=M.den
    totals=ZERO
    for x in state.values():totals=ff.add(totals,x)
    return tuple(Q(x,denominator) for x in totals)

def max_integer_queue_bits(q):
    return max((ff.worst_bits(x[1]) for x in q.front+q.back),default=0)

def fraction_query(r,front,back):
    state={s*native.S:(x,Q(0),Q(0),Q(0),Q(0),Q(0)) for s,x in enumerate(r) if x}
    for agg in ([front[-1][1]] if front else [])+([back[-1][1]] if back else []):
        state=native.jet_apply(state,agg)
    tot=native.ZERO
    for x in state.values():tot=native.add(tot,x)
    return tot

class FractionQueue:
    def __init__(self):self.front=[];self.back=[];self.compositions=0
    def append(self,step):
        M=native.jet_product(self.back[-1][1],step) if self.back else step
        if self.back:self.compositions+=1
        self.back.append((step,M))
    def pop_left(self):
        if not self.front:
            while self.back:
                step,_=self.back.pop()
                M=native.jet_product(step,self.front[-1][1]) if self.front else step
                if self.front:self.compositions+=1
                self.front.append((step,M))
        self.front.pop()
    def result(self,r):return fraction_query(r,self.front,self.back)

def gates_for(kind,N):
    if kind=='one':return [Q(1)]*N
    if kind=='rational':return [Q(1+(i*7)%8,2+(i*3)%7) for i in range(N)]
    if kind=='zeros':return [Q(0) if i%5==2 else Q(1+(i*7)%8,2+(i*3)%7) for i in range(N)]
    raise AssertionError(kind)

def calculate(kind,L,W,mode):
    gates=gates_for(kind,4+L+W)
    begun=time.perf_counter()
    vals=[];stats={}
    if mode=='integer_queue':
        v,den=initial_integer()
        for g in gates[:4]:v,den=integer_port_step(v,den,g)
        q=ff.Queue()
        for g in gates[4:4+L]:q.append(ff.fstep(g))
        for j in range(W):
            if j:
                q.pop_left();q.append(ff.fstep(gates[4+j+L-1]));v,den=integer_port_step(v,den,gates[4+j-1])
            vals.append(integer_query(v,den,q))
        stats.update(compositions=q.compositions,max_numerator_bits=max_integer_queue_bits(q),prefix_bits=max((abs(x).bit_length() for x in v),default=0),prefix_den_bits=den.bit_length())
    elif mode=='fraction_queue':
        r=native.embed()
        for g in gates[:4]:r=native.native_step(r,g)
        q=FractionQueue()
        for g in gates[4:4+L]:q.append(native.jet_step(g))
        for j in range(W):
            if j:
                q.pop_left();q.append(native.jet_step(gates[4+j+L-1]));r=native.native_step(r,gates[4+j-1])
            vals.append(q.result(r))
        stats['compositions']=q.compositions
    elif mode=='native_dp':
        r=native.embed()
        for g in gates[:4]:r=native.native_step(r,g)
        for j in range(W):
            if j:r=native.native_step(r,gates[4+j-1])
            vals.append(native.oracle(r,gates[4+j:4+j+L]))
    else:raise AssertionError(mode)
    secs=time.perf_counter()-begun
    return vals,dict(kind=kind,L=L,windows=W,mode=mode,seconds=round(secs,6),**stats)

def test_native_contractions():
    checks=[]
    for kind in ('one','rational','zeros'):
        for L in (1,2,3,4,7,10):
            for W in (1,3):
                ints,irow=calculate(kind,L,W,'integer_queue')
                dp,drow=calculate(kind,L,W,'native_dp')
                assert ints==dp,(kind,L,W,ints,dp)
                checks.append((kind,L,W))
    return checks

def main():
    verified=test_native_contractions()
    rows=[]
    for kind,L,W,modes in [
        ('one',4,12,('integer_queue','fraction_queue','native_dp')),
        ('rational',4,12,('integer_queue','fraction_queue','native_dp')),
        ('zeros',4,12,('integer_queue','fraction_queue','native_dp')),
        ('one',8,16,('integer_queue','fraction_queue','native_dp')),
        ('rational',8,16,('integer_queue','fraction_queue','native_dp')),
        ('one',16,12,('integer_queue','native_dp')),
        ('rational',16,12,('integer_queue','native_dp')),
        ('one',32,16,('integer_queue','native_dp')),
        ('rational',32,16,('integer_queue','native_dp')),
    ]:
        group={}
        for mode in modes:
            vals,row=calculate(kind,L,W,mode)
            group[mode]=vals;rows.append(row)
        for mode in modes:assert group[mode]==group['integer_queue'],(kind,L,W,mode)
        print('CASE',kind,L,W,' '.join('%s=%.4fs'%(r['mode'],r['seconds']) for r in rows if r['kind']==kind and r['L']==L and r['windows']==W),flush=True)
    report={
      'schema':'PREFIX641_NATIVE_BRC_INTEGRAL_STATE_AND_JET_ROLLING_V1',
      'scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'observer':'six-jet AC for (485,316,52,174) and (52,174); 96 native ports, 576 action labels',
      'algorithm':'integer common-denominator BRC prefix state and integer two-stack second moment transfer; vector contraction in integer jet algebra; one final Fraction normalization per component',
      'verified_split_cases':len(verified),'verified_splits':[list(x) for x in verified],
      'benchmark_scope':'single-run Python 3 stdlib; all methods include native prefix propagation from 4 original gate steps, step construction, sliding queue update, vector contraction, exact Fraction output; native_dp uses direct labelled action recurrence for each window; no terminal 48-phase inversion; no controlled timing distribution',
      'cases':rows,'status':'ALL_ASSERTIONS_PASS','review':'AUTHOR_UNREVIEWED'
    }
    p=HERE/'PREFIX641_native_rolling_pipeline_results.json'
    p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_ASSERTIONS_PASS',len(verified),'split cases',len(rows),'performance records',flush=True)
    print('JSON_SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
def extend_large():
    p=HERE/'PREFIX641_native_rolling_pipeline_results.json'
    d=json.loads(p.read_text())
    for kind,L,W in [('one',64,64),('rational',64,64),('one',128,32),('rational',128,32)]:
        present={(r['kind'],r['L'],r['windows'],r['mode']) for r in d['cases']}
        if all((kind,L,W,mode) in present for mode in ('integer_queue','native_dp')):
            print('ALREADY_VERIFIED',kind,L,W,flush=True);continue
        a,ra=calculate(kind,L,W,'integer_queue')
        b,rb=calculate(kind,L,W,'native_dp')
        assert a==b,(kind,L,W)
        d['cases'].extend((ra,rb))
        p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
        print('VERIFIED_AND_SAVED',kind,L,W,ra['seconds'],rb['seconds'],flush=True)
    print('ALL_ASSERTIONS_PASS',len(d['cases']),'complete performance records',flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--large':extend_large()
    else:main()
