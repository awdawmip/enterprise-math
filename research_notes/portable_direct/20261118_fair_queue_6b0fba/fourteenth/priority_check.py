"""U27F-05: four finite-prefix observations, stopped and partly continued.

Uses the independently audited B4 macro solver in the preceding wave. The
source-archive option additionally checks the actual interrupted frames.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import zipfile

HERE=Path(__file__).resolve().parent
WAVES=HERE.parent
PREV_SHA='8caeae71d2276c28c502e1ce5819d1e44600a46b4cf456d38d73cee10d6327ad'
PINS={'ninth/OPERATIVE_RELATION_SPEC.json':'6e289d4f0f89cd75f54bc24f076bf794c500d41e53eb9ea072428fb5b6c368ee',
      'tenth/recovery_traces.json':'e60aab979013bb8a9af2644ab1309955d02b0c565f76c7419121ea2c572511c6'}
GOALS=('base','Q_reverse','old_edge_after_BC','BC_released_after_BC','unresolved')
EDGES={4:(0,1),2:(0,3),1:(2,3),8:(1,2)}
ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'


def sha(data):return hashlib.sha256(data).hexdigest()


def import_old():
    path=WAVES/'thirteenth/priority_check.py'
    assert sha(path.read_bytes())==PREV_SHA
    spec=importlib.util.spec_from_file_location('u27f10_audited',path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


old=import_old()
N=old.N


def frozen_inputs(repo):
    inputs={}
    for name,digest in PINS.items():
        raw=(WAVES/name).read_bytes();assert sha(raw)==digest
        inputs[name]=json.loads(raw)
    source=repo/'research_inputs/U27F_20261012/fixtures'
    for name in ('carry_P','carry_Q','interrupted_after_carry','base_case','recorded_oracles'):
        inputs[name]=json.loads((source/(name+'.json')).read_bytes())
    docs=inputs['tenth/recovery_traces.json']
    costs=[]
    for row in docs['runs']:
        route=row['routes']['reverse']
        end=docs['states'][route[-1][1]]
        assert end['edges']==[[0,1],[0,3],[1,2]] and end['free']=={'2':[0]*6}
        assert end['held']=={} and route[-1][0]=='STABLE'
        assert [a for a,k in route].count('fresh_birth_BC_side1')==1
        if row['stage']==3:
            stop=inputs['interrupted_after_carry']['data']
            data=docs['states'][route[0][1]]
            assert all(stop[k]==data[k] for k in ('body_cells','held','free','bound','modes'))
        costs.append(len(route)-1)
    assert costs==[4,5,6,7,7]
    return inputs,costs


def allowed(geom,mask):
    block={'O':0,'B':4,'C':1}[geom]
    return frozenset(i for i in (4,2,1) if (mask & ~block)&i)


def macros(x):
    g,b=x
    h=allowed(g,b)
    rows=[]
    for i in (4,2,1):
        nh=allowed(g,b^i)
        rows.append(('mode',(g,b^i),588,(h,h,nh,nh),0))
    if g=='O':
        for leaf,d in [('B',1),('C',2)]:
            rows.append(('grow_'+leaf,(leaf,b),1,(h,)*(d+1)+(allowed(leaf,b),)*3,d+2))
            rows.append(('capture_'+leaf,'base',8,(h,)*(d+2)+(h|{8},)*2,0))
    else:
        d=1 if g=='B' else 2
        rows.append(('shrink_'+g,('O',b),48,(h,)+(allowed('O',b),)*(d+3),1))
    rows.append(('wait',x,N-sum(r[2] for r in rows),(h,),0))
    assert Counter((('R' if y=='base' else y),n,tuple(map(len,v))) for _,y,n,v,_ in rows)==Counter(old.branches(*x))
    return rows


def kind(x,label,word,j,edge):
    if x==('O',1) and label=='grow_B' and edge==1:return 'Q_reverse'
    if label.startswith('capture') and j>len(word)-2:
        return 'BC_released_after_BC' if edge==8 else 'old_edge_after_BC'
    return 'unresolved'


def stopped_successor(source,stable_state,operation,ordered_eligibility,stage,edge,source_item):
    """Return the actual local inventory even when this policy has no continuation.

    A caller with a particular identified physical history uses its own source
    frame here. The finite probability quotient is applied only afterwards.
    """
    state=source.freeze_loss(source_item,EDGES[edge])
    return state,kind(stable_state,operation,ordered_eligibility,stage,edge)


def family_rows(P,t,costs,mark_recovery):
    output={}
    for x in old.STATES:
        row={}
        for label,target,n,word,gap in macros(x):
            alive=F(n,N)
            for j,eligible in enumerate(word,1):
                part=P.product(alive,t)
                for edge in eligible:
                    tag=kind(x,label,word,j,edge)
                    extra=0
                    if tag=='Q_reverse':extra=costs[j-1]+49
                    if tag=='old_edge_after_BC':extra=1+(2 if edge==1 else 0)
                    if tag=='BC_released_after_BC':extra=49+3
                    work=j+(extra if mark_recovery else 0)
                    old.accumulate(P,row,tag,(part,P.product(work,part)))
                alive=P.product(alive,1-t*len(eligible))
            old.accumulate(P,row,target,(alive,P.product(len(word),alive)))
        assert sum(v[0] for v in row.values())==1
        if x[0]=='O':
            h=x[1].bit_count()
            c=F(8,N)*((1-h*t)**3+(1-h*t)**4)*(1-(1-(h+1)*t)**2)
            q=F(1,N)*(1-(1-t)**5) if x[1]==1 else F(0)
            assert sum(row.get(g,(0,0))[0] for g in GOALS[2:4])==c
            assert row.get('Q_reverse',(0,0))[0]==q
        output[x]=row
    return output


def strict_rows(P,t):
    # If no earlier strict gap has occurred, only the 8 unmoved damaged states
    # remain transient. The first native leaf growth necessarily ends that run.
    rows={}
    for x in [('O',m) for m in range(8)]:
        row={}
        for label,target,n,word,gap in macros(x):
            alive=F(n,N)
            for j,eligible in enumerate(word,1):
                if j==gap:
                    old.accumulate(P,row,'hit',(alive,P.product(j,alive)))
                    alive=0;break
                loss=P.product(alive,t*len(eligible))
                tag='safe' if label.startswith('capture') and j>len(word)-2 else 'hit'
                old.accumulate(P,row,tag,(loss,P.product(j,loss)))
                alive=P.product(alive,1-t*len(eligible))
            if alive:
                tag='safe' if target=='base' else target
                old.accumulate(P,row,tag,(alive,P.product(len(word),alive)))
        assert sum(v[0] for v in row.values())==1
        rows[x]=row
    return rows


def result(P,sol,law,goal):
    return old.joint(P,law,{x:r[goal] for x,r in sol.items()})


def combine(P,results,goals):
    val=P.zero
    for g in goals:val=P.plus(val,results[g])
    return val


def print_pair(pair):
    w,m=pair
    return {'probability':str(w),'hit_time_times_indicator':str(m),
            'probability_display':round(float(w),9),
            'conditional_mean_time_display':None if not w else round(float(m/w),8)}


def numeric(P,docs,costs,delta):
    law=old.entry_law(P);t=delta/49
    pre=family_rows(P,t,costs,False)
    post=family_rows(P,t,costs,True)
    sols=[]
    for family in (pre,post):
        H=old.solve(P,family,old.STATES,GOALS)
        sols.append({g:result(P,H,law,g) for g in GOALS})
    before,after=sols
    assert all(before[g][0]==after[g][0] for g in GOALS)
    loss=combine(P,before,GOALS[1:])
    effective=combine(P,before,('Q_reverse','unresolved'))
    rec=combine(P,after,GOALS[:4])
    H=strict_rows(P,t); sr=old.solve(P,H,list(H),('hit','safe'))
    strict=result(P,sr,law,'hit')
    assert rec[0]+after['unresolved'][0]==1
    assert loss[0]-effective[0]==before['old_edge_after_BC'][0]+before['BC_released_after_BC'][0]
    assert strict[0]>=effective[0] and rec[0]>0
    if delta:
        assert strict[0]>effective[0] and loss[0]>effective[0] and rec[0]>before['base'][0]
    else:
        assert strict[0]==F(1,9) and strict[1]/strict[0]==F(8051,6)
        assert effective[0]==loss[0]==0 and rec[0]==1
    target=next(v['values'] for v in docs['recorded_oracles']['cases'].values() if F(v['values']['work_loss_delta'])==delta)
    assert before['base'][0]==F(target['repair_before_new_loss']) and loss[0]==F(target['new_loss_before_completion'])
    assert before['base'][1]+loss[1]==F(target['expected_executed_work_to_stop'])
    return {'base_stable_repair':print_pair(before['base']),
            'first_new_release_L':print_pair(loss),'first_strict_gap_S':print_pair(strict),
            'first_effective_gap_E':print_pair(effective),'certified_final_repair_R':print_pair(rec),
            'branchwise_final_or_unresolved':{g:print_pair(after[g]) for g in GOALS},
            'remaining_live_mass_at_infinite_time':'0','first_step_scalar_equations':2*24*5*2+8*2*2,
            'terminal_time_to_resolved_or_held':str(rec[1]+after['unresolved'][1])}


def incidence(item):
    """Complete-slot multiset for the one missing leaf prefix on the two traces."""
    fr=item['frame']; ref=item['reference']; slots=Counter()
    hmod=incidence.source
    for e,ww in ref.paths.table().items():
        for side,word in enumerate(ww):
            pos=fr['body_cells'][e[side]]
            for port in word:
                slots[(e,side,pos,port)]+=1
                pos=hmod.r.advance(pos,port)
    actual=Counter((r['edge'],r['side'],r['cell'],r['port']) for r in fr['bound'].values())
    assert not actual-slots
    return list((slots-actual).elements())


def replay(path,docs):
    assert sha(path.read_bytes())==ARCHIVE
    with tempfile.TemporaryDirectory() as tmp,zipfile.ZipFile(path) as z:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(tmp); root=Path(tmp)/'em_u27_followup/baseline/cell_u27'
        sys.path.insert(0,str(root))
        import work_exposure as h
        incidence.source=h
        c=h.full_comparison();p,stats=h.build_episodes(c)
        def ident(state):
            geom='B' if state.paths.cells[1][2] else ('C' if state.paths.cells[2][2] else 'O')
            return geom,sum(v for v,m in zip((4,2,1),state.modes) if m=='D')
        ix={i:ident(c['states'][i]) for i in c['damaged']}
        checked=Counter()
        for idx,br in p.items():
            x=ix[idx]; full=Counter()
            for dest,w,lab,tag,frames in br:
                target=ix.get(dest,'base')
                if dest==idx:name='wait'
                elif lab[0]=='mode':name='mode'
                elif lab[0]=='body':name=('grow_' if lab[-1] else 'shrink_')+('B' if lab[1]==1 else 'C')
                else:name='capture_'+('B' if lab[2]==0 else 'C')
                word=tuple(frozenset(k for k,e in EDGES.items() if e in item['eligible']) for item in frames)
                gaps=[]
                for j,item in enumerate(frames,1):
                    connected=h.connected(item['complete'])
                    if not connected:
                        gaps.append(j)
                        missing=incidence(item)
                        assert len(missing)==1
                        edge,side,pos,port=missing[0];fr=item['frame']
                        assert edge in ((0,1),(2,3)) and len(fr['held'])==1
                        token,head=next(iter(fr['held'].items()))
                        assert head==pos==fr['body_cells'][lab[1]] and h.connected(set(item['complete'])|{edge})
                        if lab[-1]:
                            prev=frames[j-2]['frame']
                            assert prev['kind']=='RESERVE_OR_DETACH' and prev['held'][token]==h.r.advance(head,port)
                            delivered=[f['frame'] for f in frames[:j-2] if f['frame']['kind']=='FREE_NATIVE_HOP']
                            assert delivered[-1]['token']==token and delivered[-1]['to_cell']==prev['held'][token]
                        else:
                            led=h.v.Ledger(c['states'][idx],4)
                            rr=led.validate(stable=True)[token]
                            assert (rr['edge'],rr['side'],rr['cell'],rr['port'])==missing[0]
                        checked['real_single_slot_bridges']+=1
                    for key in word[j-1]:
                        edge=EDGES[key]
                        stop,case=stopped_successor(h,x,name,word,j,key,item)
                        token=stop['released_token'];released=stop['released_at']
                        assert stop['free'][token]==released and token not in stop['bound']
                        actual=set(item['complete'])-{edge}
                        postcycle=name.startswith('capture') and j>len(word)-2
                        assert h.connected(actual)==postcycle
                        checked['all_actual_freezes']+=1
                        if case=='Q_reverse':checked[case]+=1
                        if case in ('old_edge_after_BC','BC_released_after_BC'):
                            assert not stop['held'] and set(stop['free'])=={token}
                            if case=='old_edge_after_BC':
                                assert len(h.m.straight_word(released,stop['body_cells'][0]))==(2 if key==1 else 0)
                            else:
                                tab=item['reference'].paths.table()
                                side=next(i for i,ww in enumerate(tab[edge]) if ww)
                                absent=h.m.make(tuple(stop['body_cells']),{e:words for e,words in tab.items() if e!=edge})
                                born=h.c.toggle(absent,edge,side)
                                assert born==item['reference'].paths
                                md=dict(item['modes']);md.pop(edge)
                                geo=h.z.state(absent,md)
                                lab=('contact',edge,side)
                                accepted,weight=h.v.accepted(h.K,geo,lab)
                                assert accepted.paths==born and accepted.mode_table()[edge]=='D'
                                assert weight.total/h.K.q[lab].total==F(1,49)
                                assert released==stop['body_cells'][edge[side]]
                            checked[case]+=1
                assert len(gaps)<=1
                full[(name,target,word,gaps[0] if gaps else 0)]+=w.total
            expected=Counter()
            for name,target,n,word,gap in macros(x):
                expected[name,target,word,gap]+=F(n,N)
            assert full==expected
        successes={}
        for case in ('carry_P','carry_Q'):
            source=json.loads((Path(tmp)/'em_u27_followup/fixtures'/(case+'.json')).read_text())['data']
            assert source==docs[case]['data']
        # Actual source stopping/work calculation on both canonical grow witnesses.
        for mode in ((0,1),(2,3)):
            l=h.v.Ledger(h.f.root_state(),4);budget=h.v.Capped(4,F(1,16))
            for lab in [('mode',(1,2)),('contact',(1,2),0),('mode',mode)]:
                y,w=h.v.accepted(budget,l.s,lab);l.commit(lab,y)
            lab=('body',1,4,True);s=l.s;y,w=h.v.accepted(budget,s,lab);i=len(l.log);l.commit(lab,y)
            fr=list(h.references(s,y,l.log[i:]))
            surv,*rest=h.exposure_transfer(fr,F(1,256))
            assert surv.total==(1-F(1,12544))**(2 if mode==(0,1) else 5)
            successes[str(mode)]=str(surv.total)
        # Verification of the one fresh-birth decision clock with the frozen
        # pointed elimination primitive (this is a declared conditional clock).
        R=h.E(F(48,49));A=h.E(F(1,49))
        out,log=h.eliminate_transfers({'try':{'try':(R,R),'ok':(A,A)}},['try'],{'start':{'try':h.ONE}},['ok'])
        assert tuple(w.total for w in out['start']['ok'])==(1,49)
        return dict(archive_sha256=ARCHIVE,**stats,**checked,fresh_BC_attempt_mean=49,
                    original_witness_survivals=successes)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path);ap.add_argument('--archive',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    roots=[Path.cwd(),*HERE.parents,Path('/workspace/enterprise-math')]
    repo=args.repo or next((q for q in roots if (q/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if not repo:ap.error('use --repo with the public enterprise-math checkout')
    src=repo/'src/enterprise_math/brc_weighted.py';raw=src.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='3f205696709e847909958a153f8fe10d3f6b70f0'
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted
    P=old.Pointed(brc_weighted)
    docs,costs=frozen_inputs(repo)
    out={'task_id':'RS-CELL-U27F-05-EVENT-SEPARATION-20261012','predecessor_digests':PINS,
         'loss_free_T03_reverse_actions_including_stable':costs,
         'parameters':{str(d):numeric(P,docs,costs,d) for d in [F(0),F(1,256)]}}
    if args.archive:out['source_comparison']=replay(args.archive,docs)
    text=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')


if __name__=='__main__':main()
