#!/usr/bin/env python3
"""PREFIX-642: original BRC integer six-jet single-base periodic compiler.
Exact native action semantics: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires unmodified PREFIX640_fraction_free_rolling_jet.py and PREFIX638/PREFIX638_native_jet_support.py,
both available in the PREFIX-640 full author archive. Python 3 standard library only.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,time
from typing import Optional
from PREFIX640_fraction_free_rolling_jet import Matrix, fprod, fstep, fresult, Queue, rt_from, native

# None represents identity; avoids allocating the dense 672x672 identity.
def prod(A:Optional[Matrix],B:Optional[Matrix]):
    if A is None:return B
    if B is None:return A
    return fprod(A,B)

def take_product(xs):
    A=None
    for x in xs:A=prod(A,x)
    return A

def power(A,n):
    assert n>=0
    out=None
    while n:
        if n&1:out=prod(out,A)
        n//=2
        if n:A=prod(A,A)
    return out

def phase_direct(steps,r,L):
    p=len(steps)
    return take_product(steps[(r+i)%p] for i in range(L))

class PeriodCompiler:
    def __init__(self,gates):
        self.gates=tuple(F(g) for g in gates)
        assert self.gates and all(g>=0 for g in self.gates)
        self.steps=[fstep(g) for g in self.gates]
        self.p=len(self.steps)
        self.P=[None]*(self.p+1)
        self.S=[None]*(self.p+1)
        for i in range(self.p):self.P[i+1]=prod(self.P[i],self.steps[i])
        for i in range(self.p-1,-1,-1):self.S[i]=prod(self.steps[i],self.S[i+1])
        self.Q=self.P[-1]

    def class_at(self,r,L):
        assert L>=1
        r%=self.p
        if r==0:
            q,s=divmod(L,self.p)
            return prod(power(self.Q,q),self.P[s])
        if L<self.p-r:
            return take_product(self.steps[r:r+L])
        m=L-(self.p-r)
        q,s=divmod(m,self.p)
        return prod(prod(self.S[r],power(self.Q,q)),self.P[s])

    def compile_all(self,L):
        assert L>=1
        p=self.p
        if L<p:
            q=Queue()
            for i in range(L):q.append(self.steps[i%p])
            ans=[]
            for r in range(p):
                front=q.front[-1][1] if q.front else None
                back=q.back[-1][1] if q.back else None
                ans.append(prod(front,back))
                if r+1<p:
                    q.pop_left()
                    q.append(self.steps[(r+L)%p])
            return ans,{'branch':'short_swag','queue_compositions':q.compositions}
        whole,s=divmod(L,p)
        low=power(self.Q,whole-1)
        high=prod(low,self.Q)
        out=[prod(high,self.P[s])]
        for r in range(1,p):
            x=r+s
            op=high if x>=p else low
            out.append(prod(prod(self.S[r],op),self.P[x%p]))
        return out,{'branch':'single_base','power_levels':[whole-1,whole],
                     'full_block_Q_reused':True}

    def eventual_operator(self,transient,t,L):
        assert t>=0 and L>=1
        h=len(transient)
        if t>=h:return self.class_at((t-h)%self.p,L)
        before=take_product(fstep(g) for g in transient[t:min(h,t+L)])
        if t+L<=h:return before
        return prod(before,self.class_at(0,t+L-h))

def matrix_equals(x,y):
    if x is None or y is None:return x is None and y is None
    return x==y

def main():
    periodic=[('p1',[F(1)]),('p2',[F(2,3),F(5,4)]),
              ('p3-zeros',[F(0),F(3,2),F(5,3)]),
              ('p4-rational',[F(1),F(2,3),F(7,5),F(0)])]
    tests=0;oracle_checks=0;eventual_tests=0;obs=[];bench=[]
    initial=rt_from([F(1)]*4)
    for name,gates in periodic:
        c=PeriodCompiler(gates);p=c.p
        for L in sorted({1,2,3,p,p+1,2*p+1,16,32,64}):
            st=time.perf_counter();all_ops,meta=c.compile_all(L)
            compiler_s=time.perf_counter()-st
            for r,precompiled in enumerate(all_ops):
                a=phase_direct(c.steps,r,L)
                assert matrix_equals(precompiled,a),(name,L,r,'matrix')
                tests+=1
                if L<=8 and r<2:
                    g=[gates[(r+i)%p] for i in range(L)]
                    assert fresult(initial,precompiled)==native.oracle(initial,g),(name,L,r,'oracle')
                    oracle_checks+=1
            if L in (16,32,64):
                st=time.perf_counter();old=[]
                for r in range(p):
                    q,s=divmod(L,p)
                    oldQ=phase_direct(c.steps,r,p)
                    old.append(prod(power(oldQ,q),phase_direct(c.steps,r,s)) if s else power(oldQ,q))
                old_s=time.perf_counter()-st
                assert old==all_ops
                bench.append({'family':name,'p':p,'L':L,
                  'single_base_s':round(compiler_s,6),'per_phase_power_s':round(old_s,6),
                  'timing_scope':'all phase matrices prepared, same original scaled operators, one run'})
            obs.append({'family':name,'p':p,'L':L,'phase_classes':p,
              'branch':meta['branch'],'full_operator_equality':'PASS'})
        h=5;trans=[F(0),F(1,2),F(5,3),F(1),F(0)]
        for t in [0,2,3,4,5,6,9,14]:
            for L in [1,2,4,7,16]:
                base=c.eventual_operator(trans,t,L)
                def gate(i):return trans[i] if i<h else gates[(i-h)%p]
                comparison=take_product(fstep(gate(t+i)) for i in range(L))
                assert matrix_equals(base,comparison),(name,'eventual',t,L)
                eventual_tests+=1
    report={'schema':'ENTERPRISE_MATH_PREFIX642_SINGLE_BASE_PERIODIC_JET_V1',
      'science_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'native_actions':len(native.ACTIONS),'ac_states':native.S,'port_states':96,
      'patterns':[list(i) for i in native.PATTERNS],
      'matrix_comparisons':tests,'oracle_six_moment_checks':oracle_checks,
      'eventually_periodic_operator_checks':eventual_tests,'benchmark_samples':bench,
      'families_and_lengths':obs,'test_status':'ALL_ASSERTIONS_PASS',
      'review_status':'AUTHOR_SIDE_UNREVIEWED',
      'limitation':'Python times include matrices only, exclude source state/period verification. Exact tested finite cases.'}
    fp=Path(__file__).with_name('PREFIX642_check_results.json')
    fp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('ALL_ASSERTIONS_PASS',tests,oracle_checks,eventual_tests)
    print('RESULT_SHA256',hashlib.sha256(fp.read_bytes()).hexdigest())
    for a in bench:print(a)
if __name__=='__main__':main()
