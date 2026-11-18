"""Actual native two-arm run, with directed rational observer-error certificates."""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
from math import isqrt
from itertools import product
import os
from pathlib import Path
import sys

BANK='79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'


def sqrt_interval(value,bits=52):
    """Only for certifying scalar inequalities after exact BRC observations."""
    if value<0:
        raise ValueError('nonnegative rational required')
    a,b=value.as_integer_ratio()
    n=isqrt((a<<(2*bits))//b)
    lo=F(n,1<<bits)
    hi=lo if lo*lo==value else F(n+1,1<<bits)
    assert lo*lo<=value<=hi*hi
    return lo,hi


def h2_interval(p,q):
    vals=[sqrt_interval(p*q),sqrt_interval((1-p)*(1-q))]
    return max(F(0),1-sum(v[1] for v in vals)),1-sum(v[0] for v in vals)


def two_round_certificate(program,j,theta):
    """Constant number of typed columns; the declared row recipe is part of the certificate."""
    from lazy_streaming import LazyStreamingProgram
    from certified_word_compiler import PositivePathObserver
    if type(program) is not LazyStreamingProgram or program.dim!=61 or program.t<4:
        raise ValueError('admitted full program with at least four rounds required')
    if j not in (0,1,2) or (j==2 and theta!=0) or theta.denominator & (theta.denominator-1):
        raise ValueError('unsupported row recipe')
    a=program.tables[0][1];b=program.tables[1][1]
    if b==1 or program.tables[1][b]!=a or program.tables[1][a]!=1:
        raise ValueError('first nontrivial three-cycle unavailable')
    quarter=program.bank[2]
    for k,(target,sgn) in enumerate(((1,-1),(0,1),(2,1))):
        basis=tuple(int(i==k) for i in range(61))
        actual=quarter.apply_numer(basis)
        assert tuple(actual)==tuple(quarter.den*sgn*int(i==target) for i in range(61))
    o=PositivePathObserver()
    square=o.evaluate('public dyadic perturbation square',[(theta,theta)])
    contrast=F(1) if j==2 else square/(1+square)
    error=(square if j==0 else square+2)/2
    return dict(recipe=['row direction at prefix 1',j,str(theta)],typed_front=[a,b],
                actual_input=[program.N,program.a,program.t],beta=[F(0)]*program.t,
                epsilon=[F(0),error]+[F(0)]*(program.t-2),history_mass=F(1,2),
                history_and_collision_mass=F(1,4),local_zero_probability=(1-contrast)/2,
                exact_terminal_joint_tv=contrast/8,full_rows_queried=0)


def execute(repo,stage,compact=None):
    rec=repo/'research_notes/directed_recovery'
    pkg=rec/'20260926_C6438C'; prev=rec/'20260926_0C08F0'
    pins={
        rec/'20260927_C6438C/qft_row_queries/gram_research/single_walker.py':'19ec66c4453d8ca5168d0f8fe7950ff85b297562e8625bfb73c9b40142ac3f74',
        pkg/'optimization/streaming/lazy_streaming.py':'635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257',
        pkg/'new_word_compiler/certified_word_compiler.py':'e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d',
        pkg/'optimization/lazy_modular/lazy_modular.py':'08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4',
        stage/'stage80/fixed_phase.py':'d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254'}
    for file,pin in pins.items():
        assert hashlib.sha256(file.read_bytes()).hexdigest()==pin
    os.environ.update(BRC_STAGE87_SOURCE=str(stage),BRC_STREAMING_PREVIOUS=str(prev),
                      BRC_ZERO_ENDPOINT_SOURCE=str(prev/'adversarial/zero_endpoint_extension.py'))
    for path in (stage,pkg/'new_word_compiler',pkg/'optimization/streaming',
                 rec/'20260927_C6438C/qft_row_queries/gram_research'):
        sys.path.insert(0,str(path))
    from compiled_streaming import bank_from_compilation
    from single_walker import PointRowOracle,RawRow,normalize_row
    from lazy_streaming import LazyStreamingProgram
    from certified_word_compiler import PositivePathObserver
    from stage45.brc_loop_recheck import CALLS,verify_vendor
    from stage80.fixed_phase import apply_word
    vendor=verify_vendor()
    first=len(CALLS)
    raw=gzip.decompress((pkg/'direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==BANK
    bank=bank_from_compilation(json.loads(raw)['phase_compilation'],t=4,epsilon=F(1))['bank']
    if compact is not None:
        modulus,base,j,theta=compact
        return two_round_certificate(LazyStreamingProgram(modulus,base,4,bank,61),j,theta)
    program=LazyStreamingProgram(57,8,4,bank,61)
    other,one=program.tables[0][1],1
    r=program.tables[1][one]
    assert r!=one and program.tables[1][r]==other and program.tables[1][other]==one
    observer=PositivePathObserver()

    def obs(name,terms):
        terms=[tuple(x) for x in terms if all(x)]
        return observer.evaluate(name,terms) if terms else F(0)

    @lru_cache(None)
    def ora(h):
        return PointRowOracle(program,tuple(int(x) for x in h))

    def rotated(row,k):
        if not k:
            return row
        vals,den=apply_word(row.values,row.den,[('swap',0,k)])
        return RawRow(tuple(vals),den)

    # A mode is (planar basis index, dyadic perturbation, public zero rule).
    exact=(0,F(0),False)

    @lru_cache(None)
    def approx(mode,h,w):
        o=ora(h)
        j,theta,zero_layer=mode
        if zero_layer and len(h)==2:
            return RawRow((0,)*61,1)
        if h!='1' or mode==exact:
            return o.query(len(h),w)
        # Closed-form two labels from actual typed columns. The public approximation
        # does not need an exact row query at this prefix.
        row=RawRow(tuple((int(w==1)-int(w==other))*int(k==0) for k in range(61)),2)
        # Independent audit only; the small certificate generator never calls this oracle.
        check=o.query(1,w)
        assert all(a*check.den==b*row.den for a,b in zip(row.values,check.values))
        base=rotated(row,j)
        if not theta:
            return base
        v=rotated(row,2)
        offset=normalize_row([u*theta.numerator for u in v.values],v.den*theta.denominator)
        return o.combine(base,offset,halve=False)

    @lru_cache(None)
    def probability(mode,h,z):
        o=ora(h); depth=len(h)
        x=approx(mode,h,z)
        y=o.apply_feedback(depth,approx(mode,h,o.inverse_table(depth)[z]))
        total=obs('norm pair',[(o.norm_observation(x),),(o.norm_observation(y),)])
        if not total:
            return F(1,2)
        plus=o.combine(x,y,halve=False)
        return o.norm_observation(plus)/(2*total)

    @lru_cache(None)
    def fields(mode):
        layers=[{('',1):F(1)}]
        for depth in range(4):
            masses=defaultdict(list)
            for (h,w),mass in layers[-1].items():
                for z in (w,program.tables[depth][w]):
                    q=probability(mode,h,z)
                    for bit,weight in (('0',q),('1',1-q)):
                        if weight:
                            masses[h+bit,z].append((mass,F(1,2),weight))
            layers.append({key:obs('positive joint update',terms) for key,terms in masses.items()})
            assert sum(layers[-1].values())==1
        return layers

    source=fields(exact)
    def evaluate(mode):
        approx_law=fields(mode)
        tv_by_layer=[]
        for a,b in zip(source,approx_law):
            tv_by_layer.append(sum(abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys())/2)
        score_charges=[];h2=[]
        for i,parent in enumerate(source[:-1]):
            charge=alo=ahi=F(0)
            for (h,w),mass in parent.items():
                for z in (w,program.tables[i][w]):
                    p,q=probability(exact,h,z),probability(mode,h,z)
                    charge+=mass*abs(p-q)/2
                    lo,hi=h2_interval(p,q)
                    alo+=mass*lo/2;ahi+=mass*hi/2
            score_charges.append(charge);h2.append((alo,ahi))
        assert tv_by_layer[-1]<=sum(score_charges)
        A=sum(v[1] for v in h2)
        if A:
            assert tv_by_layer[-1]<=sqrt_interval(4*A)[1]+4*A
        raw=F(0);inner=F(0);unorm=F(0)
        for w in (1,other):
            u=approx(mode,'1',w);v=approx(exact,'1',w); o=ora('1')
            diff=o.combine(v,u,sign=-1,halve=False)
            raw+=o.norm_observation(diff)
            inner+=obs('whole prefix overlap',[(F(x,v.den),F(y,u.den)) for x,y in zip(v.values,u.values)])
            unorm+=o.norm_observation(u)
        projective=F(1,2)-inner*inner/unorm
        return dict(tv=tv_by_layer,score_charges=score_charges,h2_intervals=h2,
                    h1_raw_error=raw,h1_projective_error=projective,
                    collision_true=probability(exact,'1',1),collision_approx=probability(mode,'1',1))

    examples={}
    for key,j,theta in [('near',0,F(1,4)),('in_plane',1,F(0)),('tilted',1,F(1,2)),
                         ('spectator',2,F(0))]:
        mode=j,theta,False
        record=evaluate(mode)
        loss=F(1,8) if j==2 else theta*theta/(8*(1+theta*theta))
        assert record['tv']==[0,0,loss,loss,loss]
        assert record['score_charges']==[0,loss,0,0]
        assert record['h1_raw_error']==(theta*theta if j==0 else 2+theta*theta)/2
        small=two_round_certificate(program,j,theta)
        assert small['epsilon'][1]==record['h1_raw_error']
        assert small['exact_terminal_joint_tv']==record['tv'][-1]
        assert small['local_zero_probability']==record['collision_approx']
        record['compact_certificate']=small
        examples[key]=record
    assert examples['in_plane']['h1_projective_error']==examples['spectator']['h1_projective_error']==F(1,2)
    # Another consistent oracle changes two stages. Include the exact fair fallback and zero approximate score.
    mode=2,F(0),True
    example=evaluate(mode)
    def stopped(bound):
        current=[('',1,F(1),F(1))]
        leaves=[]
        for i in range(4):
            nxt=[]
            for h,w,pm,qm in current:
                if not pm or qm>bound*bound*pm:
                    leaves.append((pm,qm,True))
                    continue
                for z in (w,program.tables[i][w]):
                    p,q=probability(exact,h,z),probability(mode,h,z)
                    for bit,a,b in [('0',p,q),('1',1-p,1-q)]:
                        pp,qq=pm*a/2,qm*b/2
                        if pp or qq: nxt.append((h+bit,z,pp,qq))
            current=nxt
        leaves.extend((p,q,False) for _,__,p,q in current)
        assert sum(p for p,_,__ in leaves)==sum(q for _,q,__ in leaves)==1
        crossed=sum((p for p,_,stop in leaves if stop),F(0))
        stop_tv=sum(abs(p-q) for p,q,_ in leaves)/2
        bc=[sqrt_interval(p*q) for p,q,_ in leaves]
        hilo=(1-sum(v[1] for v in bc),1-sum(v[0] for v in bc))
        assert hilo[1]<=bound*sum(v[0] for v in example['h2_intervals'])
        assert example['tv'][-1]<=stop_tv+crossed
        return dict(bound=bound,stopped_tv=stop_tv,true_threshold_hits=crossed,stopped_h2=hilo)
    example['stopping_audits']=[stopped(F(5,4)),stopped(F(2))]
    examples['two_stages_with_zeros']=example
    # A distinct arithmetic fixture: n=3*2^(t-2) with a one-hot work label.
    n,t=12,4
    pg=LazyStreamingProgram((1<<n)-1,2,t,bank,61)
    @lru_cache(None)
    def mo(h):
        return PointRowOracle(pg,tuple(map(int,h)))
    b=1<<(t-2)
    zero=RawRow((0,)*61,1)
    def recover(h,w):
        i=len(h)
        if w<=0 or w&(w-1) or w.bit_length()>n: return zero
        e=w.bit_length()-1
        if e% (1<<(t-i)): return zero
        parent=1<<((e//b)*b)
        row=mo(h[:2]).query(2,parent)
        for j in range(2,i):
            if (e>>(t-1-j))&1:
                row=mo(h[:j]).apply_feedback(j,row)
                row=mo(h[:j]).combine(zero,row,sign=1 if h[j]=='0' else -1)
            else:
                row=normalize_row(row.values,row.den*2)
        return row
    checks=active=0
    for i in (2,3,4):
        for bits in product('01',repeat=i):
            h=''.join(bits)
            for w in [0,3]+[1<<e for e in range(n)]:
                actual=mo(h).query(i,w); via=recover(h,w)
                assert all(a*via.den==b*actual.den for a,b in zip(actual.values,via.values))
                checks+=1
                if i==t-1 and h[0]=='1' and any(actual.values): active+=1
    assert active==3*(1<<(2*t-5))
    return dict(mersenne=dict(input=[(1<<n)-1,2,t],full_rows_checked=checks,
                             last_parent_active_cells_starting_one=active),typed_input=[57,8,4],coordinates=61,first_multipliers=[other,r],
                bank_sha256=BANK,vendor_blob=vendor['git_blob'],actual_BRC_calls=len(CALLS)-first,
                native_observer_records=len(observer.operations),examples=examples)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path('/workspace/enterprise-math'))
    ap.add_argument('--stage',type=Path,required=True,help='frozen RP14_Run native stage source')
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--certificate-only',action='store_true')
    ap.add_argument('--modulus',type=int,default=57)
    ap.add_argument('--base',type=int,default=8)
    ap.add_argument('--direction',type=int,choices=[0,1,2],default=0)
    ap.add_argument('--amplitude',type=F,default=F(1,4))
    args=ap.parse_args()
    compact=(args.modulus,args.base,args.direction,args.amplitude) if args.certificate_only else None
    result=execute(args.repo.resolve(),args.stage.resolve(),compact)
    output=json.dumps(result,sort_keys=True,indent=2,default=str)+'\n'
    if args.verify:
        assert args.verify.read_text()==output
        print('PASS',hashlib.sha256(output.encode()).hexdigest())
    else:
        print(output,end='')


if __name__=='__main__':
    main()
