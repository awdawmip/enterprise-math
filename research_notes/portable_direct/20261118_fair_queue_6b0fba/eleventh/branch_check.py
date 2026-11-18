"""Five-state finite-horizon control, exact positive rational masses."""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import prod
from pathlib import Path
import sys

CORE="7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26"


def load_core(root):
    path=root/'src/enterprise_math/brc_weighted_recurrent.py'
    assert sha256(path.read_bytes()).hexdigest()==CORE
    spec=spec_from_file_location('frozen_rational_positive_brc',path)
    obj=module_from_spec(spec);sys.modules[spec.name]=obj;spec.loader.exec_module(obj)
    return obj


def segment(p,l,eta,n,initial_bias,core):
    # Positive BRC transfer on hidden live states; submass missing here is failure.
    kernel=((p*(1-eta),p*eta),(l*eta,l*(1-eta)))
    rows=core.recurrent_mass_power(kernel,n)
    return ((1+initial_bias)*sum(rows[0])+(1-initial_bias)*sum(rows[1]))/2


def formula(T,B,p,l,eta,core):
    W=max(0,T-1);n=max(0,W-2*B)
    if n==0:
        return F(1),F(1),[]
    r=B+1;z,s=divmod(n,r)
    f=segment(p,l,eta,z,1,core)**(r-s)
    if s:f*=segment(p,l,eta,z+1,1,core)**s
    return segment(p,l,eta,n,0,core),f,[z]*(r-s)+[z+1]*s


def advance(u,v,choice,p,l,eta):
    if choice==0:x,y=u*p,v*l
    else:x,y=u*l,v*p
    return x*(1-eta)+y*eta,x*eta+y*(1-eta)


def open_loop_optima(T,B,p,l,eta):
    # Every surviving m=0 path sees the same H at a choice, hence a schedule;
    # its score includes all hidden paths, and repair pauses the hidden chain.
    count=0
    def search(w,b,u,v):
        nonlocal count
        if w<=0:
            count+=1
            return u+v
        values=[search(w-1,b,*advance(u,v,a,p,l,eta)) for a in (0,1)]
        if b:values.append(search(max(0,w-2),b-1,u,v))
        return max(values)
    best=search(max(0,T-1),B,F(1,2),F(1,2))
    return best,count


def all_history_optimum(T,B,p,l,eta):
    # Complete deterministic observation trees; the two children of a public C
    # can optimize independently. This upper bounds every finite-memory policy.
    @lru_cache(None)
    def visit(w,b,u,v):
        if w<=0 or not u+v:return u+v
        opts=[visit(w-1,b,*advance(u,v,a,p,l,eta)) for a in (0,1)]
        if b:
            if w<=2:opts.append(u+v)
            else:opts.append(visit(w-2,b-1,u,0)+visit(w-2,b-1,0,v))
        return max(opts)
    w=max(0,T-1)
    return (visit(w,B,F(1),F(0))+visit(w,B,F(0),F(1)))/2


def trace_one_bit(memory,p,l,eta,core):
    # The fixed policy on W=4 is ordinary,repair,C-read,ordinary.
    states=[(typ,b,c) for typ in ('C','H') for b in (0,1) for c in range(1+memory)]+[('F',0,0)]
    fail=states.index(('F',0,0))
    cur=[F(0)]*len(states)
    cur[states.index(('C',0,0))]=cur[states.index(('C',1,0))]=F(1,2)
    result=[]
    for step in range(1,6):
        mat=[[F(0)]*len(states) for st in states]
        for i,(typ,b,c) in enumerate(states):
            if typ=='F':mat[i][fail]=1
            elif typ=='C':
                mat[i][states.index(('H',b,b if memory else 0))]=1
            elif step==3:
                mat[i][states.index(('C',b,c))]=1
            else:
                live=p if b==c else l
                mat[i][states.index(('H',b,c))]=live*(1-eta)
                mat[i][states.index(('H',1-b,c))]=live*eta
                mat[i][fail]=1-live
        assert all(sum(row)==1 for row in mat)
        bank=core.recurrent_mass_power(mat,1)
        edges={f'{i}>{j}':str(cur[i]*prob) for i,row in enumerate(bank)
               for j,prob in enumerate(row) if cur[i]*prob}
        cur=[sum(cur[i]*row[j] for i,row in enumerate(bank)) for j in range(len(states))]
        assert sum(cur)==1
        result.append({'step':step,'branch_masses':edges,'state_masses':list(map(str,cur))})
    return dict(states=states,history=result,survival=str(1-cur[fail]))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path('.'))
    parser.add_argument('--output',type=Path)
    opts=parser.parse_args();core=load_core(opts.repo)
    p,l,eta=F(15,16),F(1,2),F(1,8)
    target=[trace_one_bit(m,p,l,eta,core) for m in (0,1)]
    z,n=open_loop_optima(5,1,p,l,eta)
    y=all_history_optimum(5,1,p,l,eta)
    f0,f1,gaps=formula(5,1,p,l,eta,core)
    assert n==36 and f0==z==F(2263,4096) and f1==y==F(225,256)
    assert [t['survival'] for t in target]==list(map(str,(z,y)))
    rows=[]
    for pp,ll in [(p,l),(F(4,5),F(1,3))]:
        for flip in (F(0),F(1,8),F(1,3),F(1,2)):
            for t in range(1,9):
                for b in range(5):
                    a,m,g=formula(t,b,pp,ll,flip,core)
                    ar,num=open_loop_optima(t,b,pp,ll,flip)
                    mr=all_history_optimum(t,b,pp,ll,flip)
                    assert (a,m)==(ar,mr)
                    assert (a<m)==(t-1>2*b)
                    rows.append([str(pp),str(ll),str(flip),t,b,str(a),str(m),num])
    out={'core_sha256':CORE,'comparison_cases':len(rows),
         'total_open_loop_schedules_across_cases':sum(r[-1] for r in rows),
         'comparison_rows_sha256':sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
         'mandated_case':{'T':5,'B':1,'epsilon':'1/16','q':'1/2','eta':'1/8',
                          'ordinary_run_lengths':gaps,'memoryless_schedules':n,
                          'memoryless_optimum':str(z),'unrestricted_history_optimum':str(y),
                          'positive_branch_traces':target}}
    contents=json.dumps(out,indent=2,sort_keys=True)+'\n'
    print(contents,end='')
    if opts.output:opts.output.write_text(contents)


if __name__=='__main__':
    main()
