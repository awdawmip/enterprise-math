"""Demand projection on one fixed BRC snapshot family, using original physical words.
Run from any cwd with sibling parent bundle directories at the workspace root.
"""
from collections import Counter
from functools import cache
from itertools import combinations
from pathlib import Path
import argparse, json, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
sys.path.insert(0,str(ROOT))
from copylife.kernel_checks import Physical,core

POINT=range(1,8); DIG=(10,9,8)    # high, middle, low digit markers
SLOTS=15; FULL=255; BACK=11
def mask(j): return 1<<j if j<=7 else sum(1<<h for h in range(8) if h>>(j-8)&1)
def members(u): return tuple(h for h in range(8) if u>>h&1)
def output(u,T):
    return tuple({h if h in T else 0 for h in members(u)})
def solve(T,kind):
    tests=tuple(T) if kind=='own' else (DIG+tuple(POINT) if kind=='open' else DIG)
    @cache
    def opt(u):
        if len(output(u,T))<=1: return (0,0,None)
        choices=[]
        for order,j in enumerate(tests):
            p=u&mask(j);q=u&~mask(j)
            if not p or not q: continue
            a=opt(q);b=opt(p)
            choices.append((1+max(a[0],b[0]),u.bit_count()+a[1]+b[1],order,j))
        if not choices: return (1000,1000,None)
        d,l,_,j=min(choices)
        return (d,l,j)
    return opt
# Counting bound and first-split obstruction are independent of the solver.
def fixed_formula(k):
    return min(k,3)
def plan(backend,T,policy):
    # Backend exposes only a probe of a public marker. No full current matching, time,
    # prefix record, branch address, audit/ledger, or old guard is passed through.
    u=FULL; traces=[]
    while True:
        d,l,j=policy(u)
        if j is None:break
        bit=backend(j)
        v=u&(mask(j) if bit else ~mask(j))
        assert v and v!=u
        traces.append(dict(marker=j,answer=bit,before=list(members(u)),after=list(members(v))))
        u=v
    labels=output(u,T);assert len(labels)==1
    occupied=labels[0]
    return tuple(BACK if j==occupied else j for j in T),u,traces

def initial(h):
    return tuple((h>>j)&1 for j in range(3))+tuple(range(1,11))+(0,0)
def marker_slot(j): return 2+j
def least_one(j): return (j&-j).bit_length()-1
class Recorder(Physical):
    """Only on two selected checked traces: retain actual executed raw words."""
    def __init__(self,C,prep):
        super().__init__(C,prep)
        self.stream=[];self.dictionary={};self.boundaries=[]
    def record(self,w,op):
        for raw in w:
            if raw not in self.dictionary:self.dictionary[raw]=len(self.dictionary)
            self.stream.append(self.dictionary[raw])
        self.boundaries.append((op,len(self.stream)))
    def runword(self,J,w):
        res=super().runword(J,w);self.record(w,'word');return res
    def addressed(self,J,op):
        res=super().addressed(J,op);self.record(res[2]['word'],op);return res
    def packed(self):
        assert len(self.stream)==self.cost
        return dict(dictionary=list(self.dictionary),command_ids=self.stream,boundaries=self.boundaries)
def prefix(C,prep,route=mask,record=False):
    p=(Recorder if record else Physical)(C,prep);observed=0
    for s in range(3):
        p.drop(s);observed|=int(C.observe_result(p.J))<<s
    writes=[]
    for j in range(1,11):
        a=marker_slot(j);temp=13;waste=14
        assert p.copy(temp,a)==j
        p.drop(a)
        assert p.copy(waste,temp)==j
        on=bool(route(j)&(1<<observed))
        assert p.copy(a if on else waste,temp)==j
        p.drop(temp);p.drop(waste)
        writes.append((j,on))
    # Computed for the audit, never passed to plan.
    assert p.codes()==(0,0,0)+tuple(j if yes else 0 for j,yes in writes)+(0,0)
    assert p.probes==0 and p.copies==30
    return p

def emit(p,keys):
    """Existing original source check -> create -> addressed bind -> release -> drop.
    No ledger selects the key; the abstract policy above must supply it.
    """
    C=p.C;events=[]
    for k in keys:
        prior=p.cost
        assert k not in p.codes()   # assertion only: a conflicting choice fails, never retries
        w=C.free_reads[0];J,m,_=p.runword(p.J,w)
        out=int(C.observe_result(J));assert out==1 and m.count==1 and J==p.encoded(p.table,True,p.cache)
        col=k-C.key(0,0);cw=C.create_words[0,col,out]
        K,m,_=p.runword(J,cw);p.checked(('reserve',0),K,m,dict(color=col,answer=bool(C.observe_result(K))))
        op=('bind',0,0);K,m,data=p.addressed(p.J,op);p.checked(op,K,m)
        assert data['code']==k and len(data['observations'])==1+C.color_bits
        p.ledger.bind(0,data['code']) # independent, verification only
        op=('release',C.targets[0][0]);rw=C.programs[op];K,m,_=p.runword(p.J,rw);p.checked(op,K,m)
        p.observation_audit()
        parts=[len(w),len(cw),len(data['word']),len(rw)]
        p.cost+=sum(parts)
        p.drop(0)
        assert p.C.observe_result(p.J) and p.events[-1]['present']
        parts.append(p.events[-1]['commands'])
        assert p.cost-prior==sum(parts)
        events.append(dict(preferred_delivery=k,source_free=out,bind_delivered=data['code'],drop_reply=True,words=parts,cumulative=p.cost))
    return events

def physical(C,T,kind,h):
    p=prefix(C,initial(h),record=(h==0 and kind=='open' and T==(4,5,6,7)));pre=p.cost
    start=p.codes()
    obs=lambda j:p.probe(marker_slot(j),least_one(j))
    if kind=='remember':
        # Measured benchmark: actual prefix physical marker report recomputed from actual guard
        # drop booleans in the prefix events, never from the initial table.
        old=sum(int(p.events[i]['present'])<<i for i in range(3))
        advice=old if old in T else 0
        ks=tuple(BACK if j==advice else j for j in T);u=sum(1<<t for t in range(8) if (t if t in T else 0)==advice);tr=[]
    else:
        ks,u,tr=plan(obs,T,solve(T,kind))
    after_read=p.cost;assert p.probes==len(tr) and after_read-pre==8*len(tr)
    assert all(a['marker'] in T for a in tr) if kind=='own' else True
    jobs=emit(p,ks)
    assert p.probes==len(tr) and p.codes()==start
    assert ks==tuple(BACK if h==j else j for j in T)
    assert u>>h&1
    for j,k in zip(T,ks):assert (k==BACK)==(j in start)
    return dict(guard=h,mode=kind,writes=ks,prefix=pre,traces=tr,paid_reads=len(tr),read_commands=after_read-pre,
                survivors=members(u),business=p.cost-after_read,total=p.cost,original_service=jobs,**({'original_word':p.packed()} if isinstance(p,Recorder) else {}))

def conceptual():
    rows=[];tab={}
    for k in range(1,8):
        bag=Counter()
        for T in combinations(POINT,k):
            a=solve(T,'own')(FULL);b=solve(T,'open')(FULL);c=solve(T,'digit')(FULL)
            assert a[0]==k and b[0]==fixed_formula(k)
            bag[str((a[0],b[0],c[0]))]+=1
            rows.append(dict(demand=T,own_depth=a[0],open_depth=b[0],digit_depth=c[0],own_external_path=a[1],open_external_path=b[1]))
        tab[k]=dict(bag)
    return dict(subsets=len(rows),counts_by_size=tab,exhaustive=rows)
def synergy(C):
    # All eight guard words occur; 6,7 intentionally have the same physical marker
    # vector as 0,1 respectively. Output labels are (requested) 0,1,2,3,4.
    rows=((0,0,0),(1,0,0),(2,0,1),(3,0,1),(2,1,0),(4,1,0),(0,0,0),(1,0,0))
    T=(1,2,3,4)
    def route(j):
        def f(row):
            label,a,b=row
            return (label==j) if j<=4 else (a if j==8 else b if j==9 else False)
        return sum(1<<i for i,r in enumerate(rows) if f(r))
    def labels(u):return sorted({rows[h][0] for h in members(u)})
    def form(tests):
        @cache
        def f(u):
            if len(labels(u))==1:return (0,0,None)
            scores=[]
            for i,j in enumerate(tests):
                a=u&route(j);b=u&~route(j)
                if not a or not b:continue
                x=f(a);y=f(b)
                scores.append((1+max(x[0],y[0]),u.bit_count()+x[1]+y[1],i,j))
            d,s,i,j=min(scores);return d,s,j
        return f
    def policy(query,f):
        u=FULL;tr=[]
        while True:
            d,_,j=f(u)
            if not d:break
            reply=query(j)
            old=u;u &=route(j) if reply else ~route(j)
            assert u and u!=old
            tr.append(dict(marker=j,answer=reply,before=members(old),after=members(u)))
        lab=labels(u);assert len(lab)==1
        return tuple(BACK if j==lab[0] else j for j in T),u,tr
    tests={'own':T,'a':(8,)+T,'b':(9,)+T,'both':(8,9)+T}
    opt={mode:form(js) for mode,js in tests.items()}
    depth={k:f(FULL)[0] for k,f in opt.items()}
    assert depth=={'own':4,'a':4,'b':4,'both':3}
    # Even allowing every other physical marker never improves on the two-helper optimum.
    assert form(tuple(range(1,11)))(FULL)[0]==depth['both']
    runs={}
    for h in range(8):
        item={}
        for mode in ('remember',*tests):
            p=prefix(C,initial(h),route,record=(h==3 and mode=='both'));pre=p.cost;start=p.codes()
            if mode=='remember':
                old=sum(int(p.events[i]['present'])<<i for i in range(3))
                label=rows[old][0];ks=tuple(BACK if j==label else j for j in T)
                u=sum(1<<i for i,r in enumerate(rows) if r[0]==label);tr=[]
            else:
                ks,u,tr=policy(lambda j:p.probe(marker_slot(j),least_one(j)),opt[mode])
                assert all(t['marker'] in tests[mode] for t in tr)
            mid=p.cost
            assert mid-pre==8*len(tr) and p.probes==len(tr)
            ev=emit(p,ks)
            assert p.probes==len(tr) and p.codes()==start and u>>h&1
            assert ks==tuple(BACK if j==rows[h][0] else j for j in T)
            assert all(start[marker_slot(j)]==0 for j in (5,6,7,10))
            assert all((k==BACK)==(j in start) for j,k in zip(T,ks))
            item[mode]=dict(prefix=pre,delivered=ks,final_possible=members(u),paid_reads=len(tr),traces=tr,
                            read_commands=mid-pre,business=p.cost-mid,total=p.cost,original_service=ev,**({'original_word':p.packed()} if isinstance(p,Recorder) else {}))
        baseline=item['remember']
        assert all(r['prefix']==baseline['prefix'] and r['business']==baseline['business'] and r['total']==baseline['total']+r['read_commands'] for r in item.values())
        runs[str(h)]=item
    assert all(d==max(g[k]['paid_reads'] for g in runs.values()) for k,d in depth.items())
    return dict(guard_rows=rows,demand=T,helper_keys=[8,9],unused_always_empty=[5,6,7,10],readable_by_mode=tests,worst_depth=depth,
                common_prefix=runs['0']['remember']['prefix'],physical_count=8*(1+len(tests)),original_runs=runs,
                worst_total={mode:max(g[mode]['total'] for g in runs.values()) for mode in ('remember',*tests)})

def weighted_check(cases,mix):
    # Independent command-price recursion. The leaf charges were observed on the
    # remembered physical preparation. An output determines every mandatory
    # suffix key, and all business words are independent of unresolved history.
    out=[]
    for index,x in enumerate([*cases,mix]):
        T=x['demand'];auxiliary=index==len(cases)
        R=x.get('guard_rows',[(h,0,0) for h in range(8)])
        worlds=x['original_runs'] if auxiliary else x['worlds']
        label=[row[0] if row[0] in T else 0 for row in R]
        terminal=[worlds[str(w)]['remember']['total'] for w in range(8)]
        assert len({(lab,price) for lab,price in zip(label,terminal)})==len(set(label))
        tests=x.get('readable_by_mode',{'own':tuple(T),'open':tuple(range(1,11))})
        values={}
        for mode,js in tests.items():
            def feature(j,h):
                if not auxiliary:return bool(mask(j)&(1<<h))
                if j<=4:return R[h][0]==j
                return R[h][j-7] if j in (8,9) else 0
            @cache
            def value(U):
                if len({label[h] for h in U})==1:return max(terminal[h] for h in U)
                candidates=[]
                for j in js:
                    yes=tuple(h for h in U if feature(j,h))
                    no=tuple(h for h in U if not feature(j,h))
                    if yes and no:candidates.append(8+max(value(yes),value(no)))
                return min(candidates)
            values[mode]=value(tuple(range(8)))
            assert values[mode]==x['worst_total'][mode]
        out.append(dict(family='helpers' if auxiliary else 'cube',demand=T,measured_preparation_plus_business=terminal,
                        minimum_worst_original_commands=values))
    return out

def run():
    ctrl=conceptual()
    C=core.prior.Compiler(slots=SLOTS)
    phys=[];same=set()
    for T in [(1,2,3),(4,5,6,7),tuple(POINT)]:
        by={}
        for h in range(8):
            items={mode:physical(C,T,mode,h) for mode in ('remember','own','open')}
            base=items['remember']
            for mode,v in items.items():
                assert v['writes']==base['writes'] and v['business']==base['business'] and v['total']==base['total']+8*v['paid_reads']
                same.add(v['prefix'])
            by[str(h)]=items
        for mode in ['open','own']:
            assert max(d[mode]['paid_reads'] for d in by.values())==solve(T,mode)(FULL)[0]
        phys.append(dict(demand=T,worlds=by,worst_reads={s:max(d[s]['paid_reads'] for d in by.values()) for s in ('open','own')},
                         worst_total={s:max(d[s]['total'] for d in by.values()) for s in ('remember','open','own')}))
    mix=synergy(C);assert len(same)==1 and mix['common_prefix'] in same
    return dict(status='PASS',physical_preparations=72+mix['physical_count'],physical_word_unit='original command',
                scope='all physical runs are sequential bodies without admission; lower bounds count nonmutating slot-bit reads; joins have no retained guard except remember baseline',
                common_prefix=sorted(same)[0],inventory=dict(slots=C.slots,colors=C.colors,identity_bits=C.bits,members=C.members,candidates=len(C.H)),
                common_route=dict(guard_slots=[0,1,2],requested_marker_slots=list(range(3,10)),digit_marker_slots=[10,11,12],work=[13,14],fallback_key=BACK),
                physical=phys,controller=ctrl,synergy=mix,weighted_minimax=weighted_check(phys,mix))

if __name__=='__main__':
    ps=argparse.ArgumentParser();ps.add_argument('--out',type=Path,default=HERE/'subset_kernel_results.json');a=ps.parse_args()
    data=run();a.out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');print(data['inventory'],data['common_prefix'],data['physical_preparations'])
    for row in data['physical']:print(row['demand'],row['worst_reads'],row['worst_total'])
