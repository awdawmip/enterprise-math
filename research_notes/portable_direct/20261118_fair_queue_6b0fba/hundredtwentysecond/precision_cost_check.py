"""RP15 fixed-input arithmetic and execution audit. Private source files are read locally."""
from argparse import ArgumentParser
from collections import Counter, deque
from fractions import Fraction
import gc
import gzip
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import platform
import sys
import textwrap
import time

CAPS = tuple(range(4, 25, 2))
WEIGHTS = tuple(2 if i == 2 else 6 if i == 14 else 1 for i in range(21) if i not in (3, 15, 17))
PINS = {
    'rp15_fused/engine.py': '606aa6d3c404f10b131af4c8c4f3faa5cbabf52b0651b452ead8f42887266836',
    'rp15_fused/evidence/MICRO_REAL_FIELDS.json.gz': '38b3576349196874a18fc408dd06d411ea4aa003ce5606eb6457e094562b927f',
    'rp15_fused/micro.py': '040f0bb32bc871328fde176439bf72e06d379b40d53d938d9f40a0a50c4c13ad',
    'rp15_fused/run.py': '0e9b6cde04d2564ba5391f54fc3c85127eb424de0431bcc6bc6557c49c40f6e8',
    'rp15_fused/PLAN.json': 'b0fce9471c53b01c28094e865cc1dadfc1578321c44cfb4622c4c1e8d1f252a7',
    'rp14_budget/engine.py': '3b3306918b3a6daeb21f9fb9850d7db6d857d42282b44119d8f5411663ea3fcc',
}
HIST_PIN = '4f37c9a3de07a3be3e9474d74c2f548211aa3c67f7440ee2313bcdb04e9daf67'


def sparse_digits(a, width, last):
    """Yield only nonzero right-aligned changes, from low to high significance."""
    head = (a << (last-width)) if last >= width else a >> (width-last)
    while head:
        bit = (head & -head).bit_length()-1
        cap = max(4, last-2*(bit//2))
        offset = last-cap
        digit = (head >> offset) & (15 if cap == 4 else 3)
        head -= digit << offset
        delta = digit << (width-cap) if width >= cap else digit >> (cap-width)
        oldshift = width if cap == 4 else max(width-cap+2, 0)
        yield cap, delta, oldshift


class Index:
    def __init__(self, rows, weights, largest):
        self.buckets = {k: [] for k in CAPS if k < largest}
        self.dj = Counter()
        self.floor = Counter()
        self.queue = deque()
        self.j = self.lower_z = 0
        self.built = self.paid = self.activated = 0
        self.setup_slots = self.peak_queue = self.tests = self.peak_bits = 0
        if not self.buckets:
            return
        last = max(self.buckets)
        for _, _, numbers, width, offset in sorted(rows,key=lambda row:row[0]):
            for a, w in zip(numbers, weights):
                self.setup_slots += 1
                for cap, delta, oldshift in sparse_digits(a, width, last):
                    weight_delta = w*delta << offset
                    self.dj[cap] += weight_delta*a
                    self.floor[cap] += weight_delta
                    self.buckets[cap].append((a, oldshift, delta, weight_delta))
                    self.built += 1

    def advance(self, cap, mass, bound):
        """Emit an integral lower certificate iff at least one active entry is unread."""
        events = self.buckets.pop(cap)
        self.queue.extend(events)
        self.activated += len(events)
        self.peak_queue = max(self.peak_queue, len(self.queue))
        self.j += self.dj[cap]
        self.lower_z += self.floor[cap]
        j = self.j
        rhs_factor = (bound.denominator-bound.numerator)*mass
        lhs = 2*j*j*bound.denominator
        while self.queue:
            twice_lower_c = j+self.lower_z
            rhs = rhs_factor*twice_lower_c
            self.tests += 1
            self.peak_bits = max(self.peak_bits, lhs.bit_length(), rhs.bit_length())
            if lhs < rhs:
                return None, j, (j, twice_lower_c, mass, len(self.queue))
            a, oldshift, delta, weight_delta = self.queue.popleft()
            old = (a >> oldshift) << oldshift
            self.lower_z += weight_delta*(4*old+2*delta-a-1)
            self.paid += 1
        twice_c = j+self.lower_z
        assert twice_c % 2 == 0
        return twice_c//2, j, None


class GroupIndex:
    """Only the next cap of each still-live magnitude is kept; no future dot products."""
    def __init__(self, rows, weights, largest):
        self.rows=rows
        self.weights=weights
        self.buckets={k:[] for k in CAPS if k<largest}
        self.energy=Counter()
        self.dot=Counter()
        self.exact_slots=self.bin_visits=self.scheduled=self.active=self.setup_slots=0
        self.peak_bits=self.peak_live=self.live=0
        if not self.buckets:
            return
        self.last=max(self.buckets)
        for _,_,numbers,width,offset in rows:
            for a,w in zip(numbers,weights):
                self.setup_slots+=1
                if not a: continue
                weight=w<<offset
                gap=width-a.bit_length()
                self.energy[gap]+=weight*a*a
                head=a<<(self.last-width) if self.last>=width else a>>(width-self.last)
                if head:
                    self.push(head,width,weight*a,gap)

    def push(self,head,width,weighted_a,gap):
        cap=max(4,self.last-2*((head.bit_length()-1)//2))
        self.buckets[cap].append((head,width,weighted_a,gap))
        self.scheduled+=1
        self.live+=1
        self.peak_live=max(self.live,self.peak_live)

    def advance(self,cap,mass,bound):
        events=self.buckets.pop(cap)
        self.live-=len(events)
        for head,width,weighted_a,gap in events:
            pos=self.last-cap
            digit=head>>pos
            delta=digit<<(width-cap) if width>=cap else digit>>(cap-width)
            self.dot[gap]+=weighted_a*delta
            rest=head-(digit<<pos)
            if rest: self.push(rest,width,weighted_a,gap)
        self.active+=len(events)
        j=sum(self.dot.values())
        low=sum((jg*jg+ag-1)//ag for gap,ag in self.energy.items() if (jg:=self.dot.get(gap,0)))
        self.bin_visits+=len(self.energy)
        lhs=bound.denominator*j*j
        rhs=(bound.denominator-bound.numerator)*mass*low
        self.peak_bits=max(self.peak_bits,lhs.bit_length(),rhs.bit_length())
        if lhs<rhs:
            return None,j,(j,2*low,mass,len(self.weights)*len(self.rows))
        c=0
        for _,_,numbers,width,offset in self.rows:
            shift=max(width-cap,0)
            c+=sum(w*(n>>shift)**2 for w,n in zip(self.weights,numbers))<<(2*shift+offset)
        self.exact_slots+=len(self.weights)*len(self.rows)
        return c,j,None


def selected_rows(rows, cap, canonical):
    out = {}
    for label, x, numbers, width, _ in rows:
        shift = max(width-cap, 0)
        if shift:
            signed = tuple(-(v >> shift) if n < 0 else v >> shift for n,v in zip(x.n,numbers))
            x = canonical(signed, x.e+shift)
        out[label] = x
    return out


def bind(baseline, strategy=Index):
    """Replace only the candidate phase of the source-verified host."""
    src = textwrap.dedent(inspect.getsource(baseline.finish_budget))
    begin = src.index('    attempts=[];selected=None')
    end = src.index('    fallback=selected is None', begin)
    part = '''
    if tuple(self.caps) != CAPS:
        return original(self,h,raw,remaining,A)
    attempts=[]; selected=None
    table=Index(rows, weights, largest)
    for K in self.caps:
        self.counts['candidate_tests']+=1
        if K>=largest:
            selected=(raw,K,A,A,F(),F())
            attempts.append(dict(cap=K,gamma2=F(),passed=True))
            self.performance['unchanged_field_shortcuts']+=1
            break
        cn,jn,proof=table.advance(K,ai,bound2)
        if proof is not None:
            attempts.append(dict(cap=K,passed=False,unread_proof=proof))
            continue
        g2=F(ai*cn-jn*jn,ai*cn)
        passes=g2<=bound2
        attempts.append(dict(cap=K,passed=passes,gamma2=g2))
        if passes:
            out=selected_rows(rows,K,canonical)
            assert all(not x.zero() and maxbits(x.n)<=K for x in out.values())
            selected=(out,K,F(cn)*scale,F(jn)*scale,g2,F(ai+cn-2*jn)*scale)
            break
'''
    ns = dict(baseline.finish_budget.__globals__, CAPS=CAPS, Index=strategy,
              original=baseline.finish_budget, selected_rows=selected_rows)
    exec(src[:begin]+part+src[end:],ns)
    return type('DigitBudget',(baseline,),{'finish_budget':ns['finish_budget']})


def compare(ref, got, counts, allow=None):
    if isinstance(got,dict):
        if 'unread_proof' in got:
            assert set(got)=={'cap','passed','unread_proof'}
            j, lower, mass, unread = got['unread_proof']
            lower_angle = 1-Fraction(2*j*j,mass*lower)
            assert ref['cap']==got['cap'] and not ref['passed'] and not got['passed']
            assert unread>0 and allow**2 < lower_angle <= ref['gamma2']
            counts['true_unread_rejections']+=1
            return
        assert ref.keys()==got.keys()
        for k,v in got.items():
            compare(ref[k],v,counts,got.get('allowance',allow))
    elif isinstance(got,(list,tuple)):
        assert len(ref)==len(got)
        for u,v in zip(ref,got):
            compare(u,v,counts,allow)
    else:
        assert ref==got


def old_method():
    path = Path(__file__).resolve().parent.parent/'seventyseventh/valuation_check.py'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==HIST_PIN
    spec = importlib.util.spec_from_file_location('rp15_w77',path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tuple_rows(records):
    base=min(e for _,e in records)
    return [(i,None,tuple(map(abs,vec)),max(map(abs,vec)).bit_length(),2*(e-base))
            for i,(vec,e) in enumerate(records)],base


def direct(rows, cap):
    mass=cn=jn=0
    for _,_,numbers,width,offset in rows:
        s=max(0,width-cap)
        for a,w in zip(numbers,WEIGHTS):
            y=(a>>s)<<s
            mass+=w*a*a<<offset
            cn+=w*y*y<<offset
            jn+=w*a*y<<offset
    return mass,cn,jn


def small():
    total=0
    for width in range(1,12):
        for a in range(1,1<<width):
            actual={c:d for c,d,s in sparse_digits(a,width,24)}
            old=0
            for cap in CAPS:
                s=max(0,width-cap)
                y=(a>>s)<<s
                assert actual.get(cap,0)==y-old
                if y>old:
                    z=(y-old)*(4*old+2*(y-old)-a)
                    assert z>=(y-old)*(3*old+y-old-(1<<s)+1) >= y-old
                old=y
                total+=1
    fields=0
    for hi,lo in [(31,17),(85,51),(983041, 245889),((1<<90)+3,(1<<85)+1)]:
        rows,_=tuple_rows([([lo,-hi]+[0]*16,-39),([-3,7]+[0]*16,51)])
        b=max(row[3] for row in rows)
        for target in CAPS:
            if target>=b: continue
            mass,c,j=direct(rows,target)
            g=1-Fraction(j*j,mass*c)
            for q in {g,max(Fraction(),g-Fraction(1,1<<400)),g+Fraction(1,1<<400),Fraction(1)}:
                tab=Index(rows,WEIGHTS,b)
                group_table=GroupIndex(rows,WEIGHTS,b)
                for cap in CAPS:
                    if cap>=b: break
                    got,jj,proof=tab.advance(cap,mass,q)
                    _,cc,jref=direct(rows,cap)
                    gc,gj,gproof=group_table.advance(cap,mass,q)
                    assert jref==jj==gj
                    if gproof: assert gproof[1]<=2*cc and 1-Fraction(jj*jj,mass*cc)>q
                    else: assert gc==cc
                    if proof:
                        assert proof[1]<=2*cc and 1-Fraction(jj*jj,mass*cc)>q
                    else:
                        assert got==cc
                    fields+=1
    nonmono=[]
    rows,_=tuple_rows([([51,85]+[0]*16,0)])
    for k in (4,6):
        a,c,j=direct(rows,k)
        nonmono.append(str(1-Fraction(j*j,a*c)))
    assert nonmono==['0','1/81226']
    return dict(digit_cells=total,threshold_comparisons=fields,nonmonotone=nonmono)


def audit(records,history):
    total=Counter(); peaks=Counter(); cross=Counter(); block=Counter(); percap={}; grouped=Counter(); gcross=Counter()
    for packet in records:
        cert=packet['certificate']
        attempts=cert.get('candidates',[])
        total['fields']+=1
        if not attempts:
            total['terminal']+=1
            continue
        data=[vec for _,vec in sorted(packet['raw'].items(),key=lambda kv:int(kv[0]))]
        rows,base=tuple_rows(data)
        spec,_,_=history.classify(data)
        m=sum(spec.values())
        q=Fraction(cert['allowance'])**2
        b=max(v[3] for v in rows)
        tab=Index(rows,WEIGHTS,b)
        group_table=GroupIndex(rows,WEIGHTS,b)
        total['base_setup_slots']+=tab.setup_slots
        total['built']+=tab.built
        total['index_fields']+=bool(tab.setup_slots)
        total['index_rows']+=len(rows) if tab.setup_slots else 0
        peaks['built_events']=max(peaks['built_events'],tab.built)
        assert m*Fraction(2)**(2*base)==Fraction(cert['A'])
        for at in attempts:
            k=at['cap']
            percap.setdefault(str(k),Counter())['tested']+=1
            total['attempts']+=1
            if k>=b:
                assert at['passed'] and Fraction(at['gamma2'])==0
                total['shortcut']+=1
                break
            paid_before=tab.paid
            cc,j,proof=tab.advance(k,m,q)
            cg,jg,gproof=group_table.advance(k,m,q)
            mass,c,correct=direct(rows,k)
            angle=1-Fraction(correct**2,mass*c)
            assert angle==Fraction(at['gamma2']) and (angle<=q)==at['passed']
            assert m==mass and j==jg==correct
            if gproof:
                assert gproof[1]<=2*c and not at["passed"]
                grouped["early"]+=1
                grouped["dense_rows_saved"]+=len(rows)
            else: assert cg==c
            total['dense_rows']+=len(rows)
            total['dense_slots']+=18*len(rows)
            if not at['passed']:
                old=history.relax(history.intervals(spec,k))[0]>q*m
                cross['old'+str(int(old))+'_new'+str(int(proof is not None))]+=1
                gcross['old'+str(int(old))+'_new'+str(int(gproof is not None))]+=1
                real_low=sum(Fraction(z*z,group_table.energy[g]) for g,z in group_table.dot.items())
                grouped['real_bucket_rejects']+=j*j<(1-q)*m*real_low
                parity_low=0
                for gg,ag in group_table.energy.items():
                    dot=group_table.dot[gg]
                    rounded=(dot*dot+ag-1)//ag
                    parity_low+=rounded+((dot-rounded)%2)
                assert parity_low<=c
                grouped['parity_bucket_rejects_audit_only']+=j*j<(1-q)*m*parity_low
                prefix_e=prefix_j=0
                prefix=False
                for g,ag in sorted(group_table.energy.items()):
                    prefix_e+=ag; prefix_j+=group_table.dot[g]
                    prefix |= (1-q)*(m*prefix_j-prefix_e*j)**2 > q*j*j*prefix_e*(m-prefix_e)
                grouped['two_group_prefix_rejects']+=prefix
            if proof is not None:
                assert cc is None and proof[1]<=2*c and 1-Fraction(2*j*j,proof[1]*m)>q
                total['early']+=1
                percap[str(k)]['early']+=1
                if tab.paid==paid_before: total['early_without_new_debt_reads']+=1
                total['unread_at_early_decisions_sum']+=proof[3]
            else:
                assert cc==c
                total['nonraw_accept' if at['passed'] else 'exact_reject']+=1
            if at['passed']:
                total['returned_nonraw_rows']+=len(rows)
                total['returned_rows_shifted']+=sum(row[3]>k for row in rows)
                break
        group='raw_shortcut' if k>=b else ('fallback' if cert['fallback'] else 'nonraw_accept')
        block[group+'_fields']+=1
        block[group+'_unpaid']+=tab.activated-tab.paid
        block[group+'_future']+=tab.built-tab.activated
        total['paid']+=tab.paid
        total['activated']+=tab.activated
        total['bound_tests']+=tab.tests
        grouped['slots_read_setup']+=group_table.setup_slots
        grouped['dot_event_products']+=group_table.active
        grouped['next_cap_insertions']+=group_table.scheduled
        grouped['untested_lookahead_at_stop']+=group_table.live
        grouped['full_norm_slots_read']+=group_table.exact_slots
        grouped['energy_bucket_visits']+=group_table.bin_visits
        peaks['lookahead_records']=max(peaks['lookahead_records'],group_table.peak_live)
        peaks['energy_buckets']=max(peaks['energy_buckets'],len(group_table.energy))
        peaks['group_test_bits']=max(peaks['group_test_bits'],group_table.peak_bits)
        peaks['integer_comparison_bits']=max(peaks['integer_comparison_bits'],tab.peak_bits)
        peaks['queue_events']=max(peaks['queue_events'],tab.peak_queue)
    return dict(counts=total,maxima=peaks,decisions_vs_W77=cross,settlement=block,by_cap=percap,grouped=grouped,grouped_vs_W77=gcross)


def host_audit(root, measured, full):
    sys.path.insert(0,str(root))
    from rp15_fused import run,micro,engine
    baseline=engine.FusedBudget
    candidate=bind(baseline)
    grouped=bind(baseline,GroupIndex)
    names={baseline:'baseline',candidate:'digits',grouped:'grouped'}
    start=time.perf_counter_ns()
    bank,rep,_=run.build()
    measured['bank_setup_ns']=time.perf_counter_ns()-start
    assert rep.weights==WEIGHTS and tuple(run.PLAN['caps'])==CAPS
    cases=list(map(tuple,run.PLAN['benchmark_cases']))
    records=run.load(root/'rp15_fused/evidence/MICRO_REAL_FIELDS.json.gz')
    streams=[]
    post=run.DemandDriver(run.DemandFactory(16)).classical_postprocess
    for i,case in enumerate(cases):
        for j in range(2):
            host=micro.Capture(run.make_program(case,bank),bank,rep)
            seed=run.PLAN['seed_base']+10000*i+j
            host.sample(run.Tape(seed),post,1)
            streams.extend((case,seed,*s) for s in host.packets)
    assert len(records)==len(streams)==98
    for p,(case,seed,h,raw,rem,mass,out) in zip(records,streams):
        assert (list(case),seed,list(h),rem,mass)==(p['case'],p['seed'],p['h'],p['remaining'],Fraction(p['A']))
        assert {str(w):[list(x.n),x.e] for w,x in raw.items()}==p['raw']
        assert run.encode(out[2])==p['certificate']
    counts=Counter(); gcounts=Counter()
    for trial in range(5):
        methods=(baseline,candidate,grouped)
        for typ in methods[trial%3:]+methods[:trial%3]:
            name=names[typ]
            hosts={case:typ(run.make_program(case,bank),bank,rep) for case in cases}
            gc.collect()
            start=time.perf_counter_ns()
            results=[hosts[c].finish_budget(h,raw,rem,mass) for c,_,h,raw,rem,mass,out in streams]
            measured.setdefault('fields_'+name+'_ns',[]).append(time.perf_counter_ns()-start)
            for res,source in zip(results,streams):
                compare(source[-1],res,(counts if typ==candidate else gcounts) if typ!=baseline and trial==0 else Counter())
    solves=[]
    for i,case in enumerate(cases):
        for j,seed in enumerate([run.PLAN['seed_base']+10000*i,20261119122000+i]):
            result={}
            methods=(baseline,candidate,grouped)
            for typ in methods[(i+j)%3:]+methods[:(i+j)%3]:
                try:
                    run.FusedBudget=typ
                    gc.collect()
                    start=time.perf_counter_ns()
                    result[typ],_=run.solve(case,'fused',bank,rep,seed)
                    name=names[typ]
                    measured.setdefault('solves_'+name+'_ns',[]).append(time.perf_counter_ns()-start)
                finally:
                    run.FusedBudget=baseline
            cmp=Counter()
            compare(result[baseline],result[candidate],cmp)
            pair2=Counter()
            compare(result[baseline],result[grouped],pair2)
            ref=result[baseline]
            assert ref['success']
            if j==0:
                assert run.encode(ref)==run.load(root/f'rp15_fused/evidence/SOLVES_{case[0]}_r0_fused.json.gz')[0]['result']
            solves.append(dict(N=case[0],seed=seed,outputs=len(ref['outputs']),grouped_rejects=pair2['true_unread_rejections'],**cmp))
    laws={}
    if full:
        for N,a,t,policy,eps in run.PLAN['diagnostics']:
            case=(N,a,t); hosts=[typ(run.make_program(case,bank),bank,rep,policy=policy,epsilon=Fraction(eps)) for typ in (baseline,candidate,grouped)]
            nodes=iter(run.load(root/f'rp15_fused/evidence/REPLAY_BRANCHES_{N}.json.gz'))
            leaves=[Fraction()]*(1<<t)
            audit_counts=Counter()
            def walk(h,raw,rem,prob):
                if len(h)==t:
                    leaves[sum(bit<<i for i,bit in enumerate(h))]=prob
                    audit_counts['reachable_leaves']+=1
                    return
                arms,masses,total=hosts[0].prepare(h,raw)
                assert all((arms,masses,total)==host.prepare(h,raw) for host in hosts[1:])
                for bit,mass in enumerate(masses):
                    if mass:
                        nh=h+(bit,)
                        pair=[host.finish_budget(nh,arms[bit],rem,mass) for host in hosts]
                        compare(pair[0],pair[1],audit_counts)
                        group_counts=Counter()
                        compare(pair[0],pair[2],group_counts)
                        audit_counts['grouped_rejects']+=group_counts['true_unread_rejections']
                        field,left,cert=pair[0]
                        child=next(nodes)
                        pr=prob*mass/total
                        assert child['h']==list(nh) and Fraction(child['probability'])==pr and run.encode(cert)==child['certificate']
                        audit_counts['branches']+=1
                        walk(nh,field,left,pr)
            walk((),{1:hosts[0].one},hosts[0].ticks,Fraction(1))
            assert next(nodes,None) is None
            assert run.encode(leaves)==run.load(root/f'rp15_fused/evidence/REPLAY_LAW_{N}.json.gz')
            assert all(hosts[0].stats==host.stats and hosts[0].counts==host.counts for host in hosts[1:])
            laws[str(N)]=audit_counts
    return dict(streams=len(streams),same_selector_calls=5*3*len(streams),native_comparison=counts,grouped_comparison=gcounts,solves=solves,laws=laws)


if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('--source',type=Path,help='locally supplied RP14_Run directory in the RP15 archive')
    parser.add_argument('--native',action='store_true')
    parser.add_argument('--full-laws',action='store_true')
    parser.add_argument('--measure',type=Path,help='optional machine-specific timing, separate from stable stdout')
    args=parser.parse_args()
    result={'portable':small()}
    if args.source:
        for path,expected in PINS.items():
            assert hashlib.sha256((args.source/path).read_bytes()).hexdigest()==expected
        frozen=json.loads(gzip.decompress((args.source/'rp15_fused/evidence/MICRO_REAL_FIELDS.json.gz').read_bytes()))
        result['source_pins']=PINS
        result['audit']=audit(frozen,old_method())
    if args.native:
        if not args.source: parser.error('--native requires --source')
        measured={'python':platform.python_version(),'cpu':platform.machine()}
        result['native']=host_audit(args.source,measured,args.full_laws)
        if args.measure:
            args.measure.write_text(json.dumps(measured,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2))
