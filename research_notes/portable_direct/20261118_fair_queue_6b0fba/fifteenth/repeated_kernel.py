"""Two-terminal finite repair process on actual T05 output configurations."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import zipfile

HERE=Path(__file__).resolve().parent
WAVES=HERE.parent
TASK='RS-CELL-U27F-06-MULTICYCLE-LIFETIME-20261012'
ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
PINS={'fourteenth/priority_checked.json':'677a9f54a9a4b19251e1e3670c8cb6b625319a5b06b63b5a79a910dc4dc6f4b1',
      'tenth/recovery_traces.json':'e60aab979013bb8a9af2644ab1309955d02b0c565f76c7419121ea2c572511c6',
      'thirteenth/priority_check.py':'8caeae71d2276c28c502e1ce5819d1e44600a46b4cf456d38d73cee10d6327ad'}
A=(0,0,0,0,0,0); B=(1,0,0,0,0,0); C=(1,1,0,0,0,0); D=(0,1,0,0,0,0)
CELLS=(A,B,C,D)
EDGES={'b':(1,2),'d':(2,3)}
PORTS={'b':3,'d':1}; SIDE={'b':1,'d':0}
ROUTE=(C,D,A,B,C,C,C)
FULL=('',-1); Q_OUT=('d',2)
STATES=[FULL]+[(queue,i) for queue in ('b','d','bd','db') for i in range(7)]
P=Q(1,49)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def input_json(path,expected):
    raw=path.read_bytes()
    if sha(raw)!=expected:raise ValueError('input digest mismatch: '+path.name)
    return json.loads(raw)


def import_solver():
    path=WAVES/'thirteenth/priority_check.py'
    assert sha(path.read_bytes())==PINS['thirteenth/priority_check.py']
    spec=importlib.util.spec_from_file_location('u27_audited_scalar_kernels',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def snapshot(x,assign):
    """The controller coordinates encode a full labelled physical inventory."""
    queue,phase=x
    assert x in STATES and sorted(assign.values())==[2,3]
    def record(cell,edge,side,port):
        return {'cell':list(cell),'edge':list(edge),'side':side,'port':port}
    bound={'0':record(A,(0,1),0,0),'1':record(A,(0,3),0,2)}
    free={};held={}
    modes={'(0, 1)':'A','(0, 3)':'A'}
    for arm,edge in EDGES.items():
        key=str(assign[arm])
        if arm not in queue:
            bound[key]=record(C,edge,SIDE[arm],PORTS[arm])
            modes[str(edge)]='D'
        elif arm==queue[0]:
            (held if phase==6 else free)[key]=list(ROUTE[phase])
        else:
            free[key]=list(C)
    ids=set(bound)|set(held)|set(free)
    assert ids==set('0123') and len(bound)+len(held)+len(free)==len(ids)
    return {'body_cells':list(map(list,CELLS)),'bound':bound,'held':held,'free':free,'modes':modes}


def register_inputs(repo):
    t05=input_json(WAVES/'fourteenth/priority_checked.json',PINS['fourteenth/priority_checked.json'])
    assert Q(t05['parameters']['1/256']['branchwise_final_or_unresolved']['Q_reverse']['probability'])>0
    trace=input_json(WAVES/'tenth/recovery_traces.json',PINS['tenth/recovery_traces.json'])
    row=trace['runs'][2];assert row['kind']=='LOCAL_CARRY'
    endpoint=trace['states'][row['routes']['reverse'][-1][1]]
    assigned={'b':3,'d':2}
    tree=snapshot(Q_OUT,assigned)
    assert all(endpoint[k]==v for k,v in tree.items())
    src=input_json(repo/'research_inputs/U27F_20261012/fixtures/source_Q.json',
                   'c2c12cc616c33d269b190345a950683cda5068215279fae2372cd6a115683790')['data']
    # Same prepared Q, this time choose the clean capture of BC from side C.
    old=src['resource_frames'][-1]
    full=snapshot(FULL,{'b':2,'d':3})
    assert old['body_cells']==full['body_cells'] and old['free']=={'2':list(A)}
    assert {k:v for k,v in full['bound'].items() if k!='2'}==old['bound']
    assert old['held']==full['held']=={} and full['bound']['2']['cell']==list(C)
    return {'T05_Q_tree_assignment':assigned,'T05_full_assignment':{'b':2,'d':3},
            'tree_free_ID2':list(A),'tree_graph_edges':sorted(tree['modes']),
            'full_graph_edges':sorted(full['modes']),'tree_starts_at_phase':2,
            'public_full_capture_source_route':[list(A),list(B),list(C)]}


def branches(x,lam):
    """One total clock tick. A loss consumes the tick before service proceeds."""
    queue,phase=x
    up=[arm for arm in EDGES if arm not in queue]
    for arm in up:
        yield 'lose_'+arm,(queue+arm,phase if queue else 0),lam
    safe=1-len(up)*lam
    if not queue:yield 'idle',FULL,safe
    elif phase==4:
        yield 'birth_decision_accept',(queue,5),safe*P
        yield 'birth_decision_refuse',x,safe*(1-P)
    elif phase==6:
        yield 'bind_'+queue[0],((queue[1:],0) if len(queue)==2 else FULL),safe
    else:
        yield ('reserve' if phase==5 else 'native_hop'),(queue,phase+1),safe


def physical_checks(assignments):
    count=0
    def roles(s):
        return {k:(kind,tuple(row['cell'] if kind=='bound' else row))
                for kind in ('bound','free','held') for k,row in s[kind].items()}
    for assign in assignments:
        for x in STATES:
            old=snapshot(x,assign); rx=roles(old)
            for kind,y,p in branches(x,Q(1,49*16)):
                assert p>0
                new=snapshot(y,assign);ry=roles(new)
                changed=[k for k in rx if rx[k]!=ry[k]]
                assert len(changed)<=1 and not {'0','1'}.intersection(changed)
                for k in rx:
                    assert sum(abs(a-b) for a,b in zip(rx[k][1],ry[k][1]))<=1
                if kind.startswith('lose_'):
                    key=str(assign[kind[-1]])
                    assert rx[key]==('bound',C) and ry[key]==('free',C)
                    if x[0]:
                        assert x[1]==y[1] and x[0]==y[0][0]
                        assert rx[str(assign[x[0][0]])]==ry[str(assign[x[0][0]])]
                if kind.startswith('bind_'):
                    key=str(assign[kind[-1]])
                    assert rx[key]==('held',C) and ry[key]==('bound',C)
                count+=1
        seen={FULL};agenda=[FULL]
        for x in agenda:
            for _,y,p in branches(x,Q(1,49*16)):
                if y not in seen:seen.add(y);agenda.append(y)
        assert seen==set(STATES)
    return count


def grouped(PA,x,lam,goal,mark):
    row={}
    for _,nxt,p in branches(x,lam):
        if p:
            dest=goal(nxt)
            before=row.get(dest,PA.zero)
            row[dest]=PA.plus(before,(p,p*mark(x)))
    assert sum(w for w,_ in row.values())==1
    return row


def first_hitting(M,PA,lam):
    live=[x for x in STATES if len(x[0])<2]
    rows={x:grouped(PA,x,lam,lambda y:'cut' if len(y[0])==2 else y,lambda x:1) for x in live}
    v=M.solve(PA,rows,live,['cut'])
    return rows,{x:v[x]['cut'][1] for x in live}


def one_attempt(M,PA,lam):
    single=[x for x in STATES if len(x[0])==1]
    def end(y):
        if y==FULL:return 'full'
        if len(y[0])==2:return 'cut'
        return y
    rows={x:grouped(PA,x,lam,end,lambda x:1) for x in single}
    v=M.solve(PA,rows,single,['full','cut'])
    return {x:v[x]['cut'][0] for x in single}


def stationary_reward(M,PA,lam,mark):
    # Visits to the same physical full state, including its real self loops.
    active=[x for x in STATES if x!=FULL]
    end=lambda y:'again' if y==FULL else y
    rows={x:grouped(PA,x,lam,end,mark) for x in active}
    v=M.solve(PA,rows,active,['again'])
    excursion=PA.zero
    for y,w in grouped(PA,FULL,lam,end,mark).items():
        tail=PA.one if y=='again' else v[y]['again']
        excursion=PA.plus(excursion,PA.times(w,tail))
    assert excursion[0]==1
    return excursion[1]


def formulas(lam):
    z=1-lam
    s=P*z**7/(1-(1-P)*z)
    s0=P*z**5/(1-(1-P)*z)
    f=1-s
    full=1/lam+1/(2*lam*f)
    tree=1/lam+s0/(2*lam*f)
    down=(55+f-f/lam)/(s/(2*lam)+55+f)
    return {'ordinary_one_repair_cut':f,'T05_Q_immediate_repair_cut':1-s0,
            'full_initial_first_cut_mean':full,'Q_initial_first_cut_mean':tree,
            'invariant_disconnected_fraction':down,'invariant_connected_fraction':1-down}


def pgf_checks(M,PA,lam):
    eligible=[x for x in STATES if len(x[0])<2]
    out={}
    for z in (Q(1,2),Q(9,10),1/(1+lam*lam)):
        rows={}
        for x in eligible:
            row=grouped(PA,x,lam,lambda y:'cut' if len(y[0])==2 else y,lambda x:0)
            rows[x]={y:(PA.product(z,w),0) for y,(w,_) in row.items()}
            rows[x]['discount']=(1-z,0)
        solved=M.solve(PA,rows,eligible,['cut','discount'])
        t=(1-lam)*z
        wait=2*lam*z/(1-(1-2*lam)*z)
        def joint(k):
            safe=P*t**(k+1)/(1-(1-P)*t)
            return safe,lam*z*(1-safe)/(1-t)
        safe,cut=joint(6)
        full=wait*cut/(1-wait*safe)
        safe0,cut0=joint(4)
        tree=cut0+safe0*full
        assert full==solved[FULL]['cut'][0] and tree==solved[Q_OUT]['cut'][0]
        out[str(z)]={'full':str(full),'T05_tree':str(tree)}
    return out


def analyze(M,PA,delta):
    lam=delta/49
    rows,hit=first_hitting(M,PA,lam)
    outcomes=one_attempt(M,PA,lam)
    total=stationary_reward(M,PA,lam,lambda x:1)
    off=stationary_reward(M,PA,lam,lambda x:int(len(x[0])==2))
    pi={s:stationary_reward(M,PA,lam,lambda x,s=s:int(x==s))/total for s in STATES}
    incoming={s:Q(0) for s in STATES}
    for x,mass in pi.items():
        for _,y,p in branches(x,lam):
            incoming[y]=PA.add(incoming[y],PA.product(mass,p))
    assert pi==incoming and sum(pi.values())==1 and sum(pi[x] for x in STATES if len(x[0])==2)==off/total
    direct={'ordinary_one_repair_cut':outcomes[('b',0)],'T05_Q_immediate_repair_cut':outcomes[Q_OUT],
            'full_initial_first_cut_mean':hit[FULL],'Q_initial_first_cut_mean':hit[Q_OUT],
            'invariant_disconnected_fraction':off/total,'invariant_connected_fraction':1-off/total}
    assert direct==formulas(lam)
    assert sum(p for _,y,p in branches(Q_OUT,lam) if len(y[0])==2)==lam
    assert sum(p for _,y,p in branches(FULL,lam) if len(y[0])==2)==0
    return {'lambda':str(lam),'exact':{k:str(v) for k,v in direct.items()},
            'display':{k:float(v) for k,v in direct.items()},
            'total_time_to_actual_full_return':str(total),'down_reward_to_actual_full_return':str(off),
            'stationary_coordinate_equations':len(pi),'exact_PGF_checks':pgf_checks(M,PA,lam)},rows


def rehydrate(h,s):
    cells=tuple(tuple(x) for x in s['body_cells'])
    tab={};tokens={}
    for k,rec in s['bound'].items():
        e=tuple(rec['edge']);side=rec['side']
        tab.setdefault(e,[(),()])[side]=(rec['port'],)
        tokens.setdefault(e,[[],[]])[side]=[int(k)]
    geom=h.z.state(h.m.make(cells,tab),{e:s['modes'][str(e)] for e in tab})
    L=object.__new__(h.v.Ledger)
    L.s,L.B,L.ids,L.log=geom,4,frozenset(range(4)),[]
    L.tokens=tokens;L.free={int(k):tuple(v) for k,v in s['free'].items()}
    return L


def source(path,rows,result):
    assert sha(path.read_bytes())==ARCHIVE
    with tempfile.TemporaryDirectory() as td,zipfile.ZipFile(path) as z:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(td)
        root=Path(td)/'em_u27_followup/baseline/cell_u27';sys.path.insert(0,str(root))
        import work_exposure as h
        l=h.v.Ledger(h.f.root_state(),4);budget=h.v.Capped(4,Q(1,16))
        for label in [('mode',EDGES['b']),('contact',EDGES['b'],0),('mode',EDGES['d'])]:
            y,w=h.v.accepted(budget,l.s,label);l.commit(label,y)
        src=l.s;lab=('body',1,4,True);y,w=h.v.accepted(budget,src,lab)
        n=len(l.log);l.commit(lab,y)
        seq=list(h.references(src,y,l.log[n:]))
        freeze=h.freeze_loss(seq[2],EDGES['d'])
        assert freeze['held']=={2:(1,0,1,0,0,0)} and freeze['free']=={3:C}
        # Original Q full-output route, leaving every identified token in place.
        l=h.v.Ledger(h.f.root_state(),4)
        for label in [('mode',EDGES['b']),('contact',EDGES['b'],0),('mode',EDGES['d']),('contact',EDGES['b'],1)]:
            y,w=h.v.accepted(budget,l.s,label);l.commit(label,y)
        assert json.loads(json.dumps(h.v.encode(l.validate(stable=True))))==snapshot(FULL,{'b':2,'d':3})['bound']
        # The other T05 endpoint, without renumbering, can use the U22 CD gate.
        tree=snapshot(Q_OUT,{'b':3,'d':2});l=rehydrate(h,tree);l.validate(stable=True)
        K=h.z.Kernel(Q(1,4));cap=('contact',EDGES['d'],0)
        y,w=h.v.accepted(K,l.s,cap);assert w.total/K.q[cap].total==P
        start=len(l.log);l.commit(cap,y)
        assert [f['to_cell'] for f in l.log[start:] if f['kind']=='FREE_NATIVE_HOP']==[B,C]
        assert json.loads(json.dumps(h.v.encode(l.validate(stable=True))))==snapshot(FULL,{'b':3,'d':2})['bound']
        for arm in EDGES:
            lab=('contact',EDGES[arm],SIDE[arm])
            y,w=h.v.accepted(K,l.s,lab);n=len(l.log);l.commit(lab,y)
            assert [f['to_cell'] for f in l.log[n:] if f['kind']=='FREE_NATIVE_HOP']==[D,A]
            y,w=h.v.accepted(K,l.s,lab);assert w.total/K.q[lab].total==P
            n=len(l.log);l.commit(lab,y)
            assert [f['to_cell'] for f in l.log[n:] if f['kind']=='FREE_NATIVE_HOP']==[B,C]
            l.validate(stable=True)
        # Two frozen positive elimination interfaces independently see the 15
        # transient connected states, using actual one-tick marks.
        tab={x:{y:(h.E(p),h.E(m)) for y,(p,m) in row.items()} for x,row in rows.items()}
        entries={'full':{FULL:h.ONE},'tree':{Q_OUT:h.ONE}}
        v,_=h.eliminate_transfers(tab,list(tab),entries,['cut'])
        ww,_=h.f.eliminate({x:{y:w for y,(w,_) in row.items()} for x,row in tab.items()},
                           list(tab),entries,['cut'])
        for start,key in [('full','full_initial_first_cut_mean'),('tree','Q_initial_first_cut_mean')]:
            assert tuple(t.total for t in v[start]['cut'])==tuple(t.total for t in ww[start]['cut'])==(1,Q(result['exact'][key]))
        return {'archive_sha256':ARCHIVE,'original_Q_interruption_matched':True,'original_full_T05_endpoint_replayed':True,
                'actual_T05_Q_endpoint_next_birth':'CD/side0/ID2','original_courier_and_binding_round_trips':2,
                'original_positive_eliminators_checked':['work_exposure.eliminate_transfers','release_flux.eliminate'],
                'eliminated_connected_states':len(tab),'delta_for_elimination':'1/256'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path);ap.add_argument('--archive',type=Path);ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    roots=[Path.cwd(),*HERE.parents,Path('/workspace/enterprise-math')]
    repo=a.repo or next((v for v in roots if (v/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if not repo:ap.error('use --repo path to enterprise-math')
    brcsrc=(repo/'src/enterprise_math/brc_weighted.py').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(brcsrc)).encode()+b'\0'+brcsrc).hexdigest()=='3f205696709e847909958a153f8fe10d3f6b70f0'
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted
    M=import_solver();PA=M.Pointed(brc_weighted)
    starts=register_inputs(repo)
    out={'task_id':TASK,'source_T05':starts,'states_per_fixed_identified_assignment':len(STATES),
         'physical_branch_comparisons':physical_checks([starts['T05_Q_tree_assignment'],starts['T05_full_assignment']]),
         'conditional_birth_probability':str(P),'ordinary_mean_no_extra_loss_service':55,
         'susceptible_edges_scheduling':'one at a time, lambda = delta/49 per currently up arm',
         'zero_noise':{'first_cut_mean':'infinite','eventual_connected_fraction':'1'},
         'parameters':{}}
    for delta in (Q(1,16),Q(1,256),Q(1,1024),Q(1)):
        result,rows=analyze(M,PA,delta)
        out['parameters'][str(delta)]=result
        if delta==Q(1,256) and a.archive:
            out['original_source_replay']=source(a.archive,rows,result)
    data=json.dumps(out,indent=2)+'\n'
    if a.output:a.output.write_text(data)
    else:print(data,end='')


if __name__=='__main__':main()
