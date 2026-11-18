"""Positive return correction on the frozen signed three-port model. Standard library only."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from random import Random, SystemRandom

PINS = {
    'run.py':'7765142879b0798998fbe3253da4fc751a0162d9b81206b4a584d0c0e336889b',
    'SOURCE_BINDINGS.json':'b3df98d16c57d70544205ac7a1f5dbd8d0f23ab88f2a3c7c936e95347b3042e3',
    'THEOREMS.md':'58e24ea97366716c4155f513539306c8695206a49d720e8820b8ac632c01e204',
    'MANIFEST.json':'d0a9c959957a1ada95fe09de15e608a9c41a25aab62973b42ad36872381bcd03',
}
T=6
Q=9**T


def source(root):
    bindings=json.loads((root/'SOURCE_BINDINGS.json').read_text())['files']
    for name, pin in dict(PINS, **{k:v for k,v in bindings.items() if k.startswith('inherited/source/')}).items():
        assert sha256((root/name).read_bytes()).hexdigest()==pin
    spec=importlib.util.spec_from_file_location('hbw47_frozen',root/'run.py')
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Threshold:
    """One U in [0,1); keep the same already-known dyadic interval across cuts."""
    def __init__(self,rng,cost,A):
        self.rng,self.cost,self.A=rng,cost,A
        self.left,self.scale=0,1

    def below(self,num,den):
        assert 0<=num<=den and den>0
        A=self.A
        while True:
            cut=A.mul(num,self.scale)
            if A.mul(A.add(self.left,1),den)<=cut:
                return True
            if A.mul(self.left,den)>=cut:
                return False
            self.left=A.add(A.mul(self.left,2),self.rng.getrandbits(1))
            self.scale=A.mul(self.scale,2)
            self.cost['fair_bits']+=1


class Sampler:
    def __init__(self,src,N,T,seed=47,tilted=False,baseline_only=False):
        self.src,self.N,self.T=src,N,T
        self.rng=SystemRandom() if seed is None else Random(seed)
        self.A=src.old.Arithmetic(limit=2000000)
        self.ops=Counter()
        self.acts={}
        self.group={}
        self.pow9=[1]
        for _ in range(T):
            self.pow9.append(self.A.mul(self.pow9[-1],9))
        self.Q=self.pow9[-1]
        # Every final flag is known from the terminal port, and h equals z[1].
        # Repeated modular doubling generates all work labels without needing their order.
        residue=1
        for q in range(0 if baseline_only else 1<<T):
            key=(q.bit_count(),(q>>(T-1))&1,residue)
            self.group[q]=key
            self.acts[key]=self.acts.get(key,0)+1
            residue=self.A.mul(residue,2)
            if residue>=N:
                residue=self.A.sub(residue,N)
        self.M=max(self.acts.values(),default=1)
        self.cache={}
        self.bands={}
        self.tilted=tilted
        self.norm_list=[]
        self.envelope_n=0
        if tilted and self.M>1:
            for q,g in self.group.items():
                d=self.acts[g]-1
                if not d:
                    continue
                n=self.src.norm(self.A,self.one_record(q))
                if n:
                    self.norm_list.append((q,d,n))
                    self.envelope_n=self.A.add(self.envelope_n,self.A.mul(d,n))
        self.prep=self.short_stats()

    def short_stats(self):
        v=self.A.stats()
        return {k:v[k] for k in ('records','scalar_operations','native_address_updates','peak_integer_bits')}

    def coin(self,num,den):
        return Threshold(self.rng,self.ops,self.A).below(num,den)

    def baseline(self):
        self.ops['baseline_trajectories']+=1
        U=Threshold(self.rng,self.ops,self.A)
        left,q=0,0
        state={(self.src.ORIGIN,0):1}
        for t in range(self.T):
            children=self.src.split_step(self.A,state)
            size=self.src.norm(self.A,children[0])
            cut=self.A.add(left,self.A.mul(size,self.pow9[self.T-1-t]))
            bit=int(not U.below(cut,self.Q))
            if bit:
                q|=1<<t
                left=cut
            state=children[bit]
            assert state
        for b,v in sorted(state.items()):
            right=self.A.add(left,self.A.mul(v,v))
            if U.below(right,self.Q):
                return q,b
            left=right
        raise AssertionError('uncovered threshold')

    def one_record(self,q):
        state={(self.src.ORIGIN,0):1}
        for t in range(self.T):
            state=self.src.split_step(self.A,state)[(q>>t)&1]
        return state

    def tilted_proposal(self):
        self.ops['tilted_trajectories']+=1
        U=Threshold(self.rng,self.ops,self.A)
        offset=0
        for q,d,n in self.norm_list:
            high=self.A.add(offset,self.A.mul(d,n))
            if U.below(high,self.envelope_n):
                for b,v in sorted(self.one_record(q).items()):
                    offset=self.A.add(offset,self.A.mul(d,self.A.mul(v,v)))
                    if U.below(offset,self.envelope_n):
                        return b
                raise AssertionError('record endpoint uncovered')
            offset=high
        raise AssertionError('tilted record uncovered')

    def point(self,b):
        """Only paths ending at the requested key. No terminal mass table is read."""
        self.ops['point_requests']+=1
        if b in self.cache:
            self.ops['point_hits']+=1
            return self.cache[b]
        target,last=b
        amps={}
        residual=list(target[:3])
        assert sum(residual)==self.T and residual[last]>0
        residual[last]-=1
        A=self.A
        def visit(t,z,prev,q,v):
            if t==self.T-1:
                dest=A.walk.address(z,last,1)
                assert dest==target
                final=q|((last==1)<<t)
                if self.acts[self.group[final]]>1:
                    term=A.mul(v,-1 if prev==last else 2)
                    amps[final]=A.add(amps.get(final,0),term)
                self.ops['fixed_endpoint_paths']+=1
                return
            for r in range(3):
                if residual[r]:
                    residual[r]-=1
                    visit(t+1,A.walk.address(z,r,1),r,q|((r==1)<<t),A.mul(v,-1 if r==prev else 2))
                    residual[r]+=1
        visit(0,self.src.ORIGIN,0,0,1)
        c0,g=0,0
        work={}
        group_norms={}
        for q,v in amps.items():
            group=self.group[q]
            sq=A.mul(v,v)
            c0=A.add(c0,sq)
            group_norms[group]=A.add(group_norms.get(group,0),sq)
            g=A.add(g,A.mul(self.acts[group]-1,sq))
            work[group]=A.add(work.get(group,0),v)
        cn=self.src.gather(A,(A.mul(v,v) for v in work.values()))
        delta=A.sub(cn,c0)
        assert max(0,delta)<=g and max(0,-delta)<=c0
        rem0,remg,seen=c0,g,0
        bands=[(-rem0,remg)]
        for group in sorted(work):
            n=group_norms[group]
            term=A.sub(A.mul(work[group],work[group]),n)
            seen=A.add(seen,term)
            rem0=A.sub(rem0,n)
            remg=A.sub(remg,A.mul(self.acts[group]-1,n))
            bands.append((A.sub(seen,rem0),A.add(seen,remg)))
        assert bands[-1]==(delta,delta)
        assert all(lo<=delta<=hi for lo,hi in bands)
        self.bands[b]=bands
        self.cache[b]=(c0,g,delta)
        return self.cache[b]

    def band_coin(self,b,den,negative):
        U=Threshold(self.rng,self.ops,self.A)
        A=self.A
        for low,high in self.bands[b]:
            self.ops['certificate_bands_read']+=1
            lo,hi=(-high,-low) if negative else (low,high)
            lo,hi=max(0,lo),max(0,hi)
            if lo==hi:
                return U.below(lo,den)
            while True:
                bottom=A.mul(U.left,den)
                top=A.mul(A.add(U.left,1),den)
                a,c=A.mul(lo,U.scale),A.mul(hi,U.scale)
                if top<=a:
                    return True
                if bottom>=c:
                    return False
                if bottom<a and c<top:
                    U.left=A.add(A.mul(U.left,2),U.rng.getrandbits(1))
                    U.scale=A.mul(U.scale,2)
                    self.ops['fair_bits']+=1
                else:
                    break
        raise AssertionError('exact final interval missing')

    def sample(self,limit=None):
        original_q,original=self.baseline()
        if self.acts[self.group[original_q]]==1:
            return original,original,0
        c0,_,d=self.point(original)
        assert c0>0
        if not self.band_coin(original,c0,True):
            return original,original,0
        self.ops['initial_rewrites']+=1
        attempts=0
        while limit is None or attempts<limit:
            attempts+=1
            if self.tilted:
                b=self.tilted_proposal()
            else:
                q,b=self.baseline()
                factor=self.acts[self.group[q]]-1
                if not self.coin(factor,self.M-1):
                    continue
            _,g,d=self.point(b)
            assert g>0
            if self.band_coin(b,g,False):
                assert b!=original
                return original,b,attempts
        return original,original,attempts


def dyadic_cost(weights):
    """Exact expected fair bits for thresholds in an ordered positive integer partition."""
    den=sum(weights)
    pos=0
    cuts=[]
    for w in weights[:-1]:
        assert w>0
        pos+=w
        cuts.append(pos)
    exponent=den.bit_length()
    cost=F()
    for n in range(exponent):
        div=1<<n
        cells={c*div//den for c in cuts if c*div%den}
        cost+=F(len(cells),div)
    odd=den//(den & -den)
    tail=sum(c%odd!=0 for c in cuts)
    return cost+F(2*tail,1<<exponent)


def bit_coin(a,b):
    if a==0 or a==b:
        return F(0)
    den=F(a,b).denominator
    if den & (den-1):
        return F(2)
    return 2-F(2,den)


def log_bounds(n):
    """Natural log brackets from powers of two and the positive atanh series."""
    def near(r):
        u=(r-1)/(r+1)
        k=16
        lo=sum(2*u**(2*j+1)/(2*j+1) for j in range(k))
        return lo,lo+2*u**(2*k+1)/((2*k+1)*(1-u*u))
    power=n.bit_length()-1
    a,b=near(F(2))
    c,d=near(F(n,1<<power))
    return power*a+c,power*b+d


def entropy_bracket(weights):
    den=sum(weights)
    lq,uq=log_bounds(den)
    for n in weights:
        a,b=log_bounds(n)
        lq-=F(n,den)*b
        uq-=F(n,den)*a
    low,high=log_bounds(2)
    lo=(lq*10**6)//high
    hi=-((-uq*10**6)//low)
    return {'scale':1000000,'lower':lo,'upper':hi}


def all_records_val(src,T):
    A=src.old.Arithmetic(limit=500000)
    level=[(0,{(src.ORIGIN,0):1})]
    for t in range(T):
        nxt=[]
        for q,state in level:
            children=src.split_step(A,state)
            assert sum(src.norm(A,c) for c in children)==9*src.norm(A,state)
            for i,child in enumerate(children):
                if child:
                    nxt.append((q|(i<<t),child))
        level=nxt
    return level,A.stats()


def law_validation(src,root,N,records):
    # Separate object: exhaustive testing cannot fill the production sampler's cache.
    val=Sampler(src,N,T)
    zero=Counter()
    joint=[]
    beta_mass={}
    for record,state in records:
        weights=[]
        for b,v in sorted(state.items()):
            sq=val.A.mul(v,v)
            zero[b]+=sq
            weights.append(sq)
        joint.extend(weights)
        beta_mass[record]=sum(weights)
    raw=json.loads((root/'inherited/INPUTS.json').read_text())['moduli'][str(N)]['truth'][str(T)]['items']
    reference={(tuple(x['key'][0]),x['key'][1]):x['mass'] for x in raw if x['mass']}
    fresh=src.unsnap(json.loads((root/'runs/density/results.json').read_text())['result']['frames'][str(T)]['diag'])
    assert dict(zero)==fresh and sum(zero.values())==sum(reference.values())==val.Q
    theta_n=sum(n for q,n in beta_mass.items() if val.acts[val.group[q]]>1)
    gamma_n=sum(n*(val.acts[val.group[q]]-1) for q,n in beta_mass.items())
    neg=pos=g0=c0sum=0
    initial_bits=retry_bits=group_bits=F(0)
    minratio=F(0)
    delta_at={}
    for b in zero.keys()|reference.keys():
        c0,g,d=val.point(b)
        assert zero[b]+d==reference.get(b,0)
        assert c0<=zero[b] and 0<=reference.get(b,0)<=val.M*zero[b]
        if zero[b]:
            minratio=max(minratio,F(reference.get(b,0),zero[b]))
        neg+=max(0,-d);pos+=max(0,d);g0+=g;c0sum+=c0
        if c0:
            initial_bits+=F(c0,Q)*bit_coin(max(0,-d),c0)
        if g:
            retry_bits+=F(g,Q)*bit_coin(max(0,d),g)
        delta_at[b]=d
    assert neg==pos and g0==gamma_n and c0sum==theta_n
    # Each intermediate pruned point distribution is checked, not just the global L1.
    for b in zero:
        c0,g,d=val.cache[b]
        kept=zero[b]-max(0,-d)
        surplus=F()
        if pos:
            for q,state in records:
                factor=val.acts[val.group[q]]-1
                if factor and g:
                    surplus+=F(state.get(b,0)**2*factor,g)*max(0,d)
        assert F(kept)+surplus==reference.get(b,0)
    M=val.M
    if M>1:
        group_bits=sum(F(n,Q)*(M-1)*bit_coin(val.acts[val.group[q]]-1,M-1) for q,n in beta_mass.items())
    L0=dyadic_cost(joint)
    tilted_weights=[]
    for q,state in sorted(records,key=lambda x:x[0]):
        d=val.acts[val.group[q]]-1
        if d:
            tilted_weights.extend(d*v*v for b,v in sorted(state.items()))
    LG=dyadic_cost(tilted_weights) if tilted_weights else F(0)
    # Independent pointwise constant computed for the joint (visible key,work).
    exact_joint={}
    for q,state in records:
        g=val.group[q]
        for b,v in state.items():
            num,den=exact_joint.get((b,g),(0,0))
            exact_joint[b,g]=num+v,den+v*v
    joint_star=max(F(v*v,n) for v,n in exact_joint.values())
    assert (joint_star,minratio)=={21:(F(169,49),F(129,65)),35:(2,F(97,65)),77:(1,1)}[N]
    assert not pos or abs(gamma_n)>=pos
    checked_truncations=0
    if pos:
        for total in ((M-1)*Q,gamma_n):
            for cap in (0,1,2,4):
                fail=(1-F(pos,total))**cap
                distances=[]
                mass=F()
                for b,d in delta_at.items():
                    v=min(reference[b],zero[b])+fail*max(0,-d)+(1-fail)*max(0,d)
                    mass+=v
                    distances.append(abs(v-reference[b]))
                assert mass==Q and sum(distances)/2==fail*pos
                checked_truncations+=1
    tilted_expected=L0+F(gamma_n,Q)*LG+initial_bits+retry_bits
    return dict(modulus=N,positive_keys=len(reference),positive_joint_atoms=len(joint),
                scalar_M=M,sharp_joint_ratio_validation_only=str(joint_star),actual_max_likelihood_ratio_validation_only=str(minratio),
                tilted_proposal_bits=str(LG),tilted_sampler_expected_bits=str(tilted_expected),
                TV=str(F(pos,Q)),surplus_numerator=pos,
                theta=str(F(theta_n,Q)),Gamma=str(F(gamma_n,Q)),
                expected_uncached_point_requests=str(F(theta_n+gamma_n,Q)),
                proposal_baseline_joint_bits=str(L0),
                correction_expected_bits=str((M if pos else 1)*L0+initial_bits+group_bits+retry_bits),
                corrected_bits_breakdown={'initial_keep':str(initial_bits),'class_filter':str(group_bits),'point_thinning':str(retry_bits)},
                direct_ordered_visible_expected_bits=str(dyadic_cost([reference[k] for k in sorted(reference)])),
                entropy_baseline_visible_bits=entropy_bracket(list(fresh.values())),
                entropy_target_bits=entropy_bracket(list(reference.values())),
                entropy_record_visible_bits=entropy_bracket(joint),
                finite_retry_full_laws_checked=checked_truncations,rejected_mass_equals_surplus=neg==pos,exact_visible_atoms_checked=len(zero.keys()|reference.keys()),
                capped_retry_TV={str(k):str(F(pos,Q)*(1-F(pos,Q*(M-1)))**k if pos else F(0)) for k in (0,1,2,4)},
                tilted_capped_retry_TV={str(k):str(F(pos,Q)*(1-F(pos,gamma_n))**k if pos else F(0)) for k in (0,1,2,4)},
                validation_point_stats=val.short_stats())


def production(src,N,trials,tilted=False,seed=47,limit=None):
    s=Sampler(src,N,T,seed=seed,tilted=tilted)
    first=None
    eighth=None
    events=[]
    for i in range(trials):
        before,after,steps=s.sample(limit)
        events.append([list(before[0][:3]),before[1],list(after[0][:3]),after[1],steps])
        if i==0:
            first=s.short_stats()
        if i==7:
            eighth=s.short_stats()
    return dict(n=N,samples=trials,seed=seed,retry_limit=limit,mode="norm-tilt" if tilted else "baseline-filter",prep=s.prep,
                retained_scalar_frequency_rows=len(s.norm_list),after_one=first,after_eight=eighth,after_all=s.short_stats(),
                rng_and_request_counters=dict(s.ops),paid_point_cache_size=len(s.cache),
                sample_trace=events)


def baseline_comparison(src):
    s=Sampler(src,21,T,baseline_only=True)
    after8=None
    for i in range(16):
        s.baseline()
        if i==7:
            after8=s.short_stats()
    return dict(samples=16,seed=47,prep=s.prep,after_eight=after8,after_all=s.short_stats(),cost=dict(s.ops))


def direct_tree(src,N,root):
    # An authentic existing implicit event oracle. Initial atom is made at the origin.
    A=src.old.Arithmetic()
    prefix=A.walk.snapshot({(src.ORIGIN,0,(1,)):A.atom(1)})
    loc=root/'inherited/source/two_layer_collapse/run.py'
    spec=importlib.util.spec_from_file_location('hbw47_two_layer_tree',loc)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    oracle=module.Block2(N,T,0,prefix)
    tree=src.old.Tree(oracle)
    rng=src.old.Arithmetic()
    ranks,report=src.old.ranks(rng,Q,20260928+N*100+T*10)
    first=None
    for i,j in enumerate(ranks):
        tree.sample(j)
        if i==0:
            first=oracle.A.stats()['records']
    return dict(outputs=8,rank_seed=20260928+N*100+T*10,initial_atom_primitive=A.stats()['records'],
                oracle_setup_primitives=oracle.setup['records'],first_primitive=first,
                eight_primitives=oracle.A.stats()['records'],nodes=len(tree.nodes),
                rank_generation_primitive=rng.stats()['records'],rank_bits=report['bit_count'],
                rank_expected_bits=str(F(Q.bit_length()*(1<<Q.bit_length()),Q)),
                output_keys=[[list(b[0][:3]),b[1]] for b in [tuple(route['output']) for route in tree.routes]])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-dir',type=Path,required=True)
    ap.add_argument('--tilted',action='store_true',help='use paid scalar norms for surplus proposals')
    ap.add_argument('--draw',type=int,default=0,help='production only: number of samples')
    ap.add_argument('--modulus',type=int,choices=(21,35,77),default=21)
    ap.add_argument('--seed',type=int,help='replay only; production defaults to OS entropy')
    ap.add_argument('--max-retries',type=int,help='on exhaustion retain the first baseline output')
    args=ap.parse_args()
    if args.max_retries is not None and args.max_retries<0:
        ap.error('max-retries must be nonnegative')
    src=source(args.source_dir)
    if args.draw:
        assert args.draw>0
        result=production(src,args.modulus,args.draw,args.tilted,seed=args.seed,limit=args.max_retries)
    else:
        demos=[production(src,n,16,tilted) for n in (21,35,77) for tilted in ((False,True) if n!=77 else (False,))]
        direct=[direct_tree(src,n,args.source_dir) for n in (21,35,77)]
        records,stats=all_records_val(src,T)
        laws=[law_validation(src,args.source_dir,n,records) for n in (21,35,77)]
        result=dict(T=T,a=2,Q=Q,source_pins=PINS,production_demos=demos,
                    comparison_original_event_tree=direct,pure_baseline=baseline_comparison(src),complete_law_certificates=laws,
                    validation_only_record_replay_cost=stats,seed_role='reproducible finite examples only')
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
