"""Two five-stage attempts on the actual interrupted Q state. No network I/O."""
import argparse
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
import tempfile
import zipfile

TASK='RS-CELL-U27F-04-OVERLAP-CONFLICT-20261012'
PINS={'interrupted_after_carry':'31012bcbfa2cfb0bdfbbfa073616ac9244130e429a6f166f927968d2ad68847e',
      'carry_Q':'acd915da997e0703ae72395e805126b29d841d47a68a435e75af379e40f76708',
      'source_Q':'c2c12cc616c33d269b190345a950683cda5068215279fae2372cd6a115683790'}
ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
CASES={'record':('to_D','to_old_B'),'endpoint':('reverse','to_body_B'),
       'one_grant':('bind','to_D'),'independent':('bind','to_D')}
STAGES=('observe','reserve','advance','commit','release')
BRC='3f205696709e847909958a153f8fe10d3f6b70f0'
SCHED=('X','Y')


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def blobid(blob):
    return hashlib.sha1(b'blob '+str(len(blob)).encode()+b'\0'+blob).hexdigest()


def step(pos,port):
    x=list(pos)
    x[port//2]+=1 if port%2==0 else -1
    return tuple(x)


def route(x,y):
    path=[]
    for i,(a,b) in enumerate(zip(x,y)):
        for _ in range(abs(a-b)):
            x=step(x,2*i+int(b<a))
            path.append(x)
    return path


def load_inputs(repo):
    root=repo/'research_inputs/U27F_20261012/fixtures'
    docs={}
    for k,pin in PINS.items():
        raw=(root/(k+'.json')).read_bytes()
        assert sha(raw)==pin
        docs[k]=json.loads(raw)['data']
    s=docs['interrupted_after_carry']
    seq=docs['carry_Q']
    original=seq[2]['frame']
    assert s['body_cells']==original['body_cells'] and s['held']==original['held']
    assert original['bound']=={**s['bound'],'3':seq[2]['complete']['(2, 3)'][0][1]}
    assert seq[2]['eligible']=={'(2, 3)':[0,3,s['body_cells'][2]]}
    assert s['free']=={'3':s['body_cells'][2]} and s['automatic_cached_commit_permitted'] is False
    assert s['modes']=={'(0, 1)':'A','(0, 3)':'A'} and s['lost_edge']==[2,3]
    assert s['bound']['0']=={'cell':s['body_cells'][0],'edge':[0,1],'side':0,'port':0}
    assert s['bound']['1']=={'cell':s['body_cells'][0],'edge':[0,3],'side':0,'port':2}
    assert tuple(s['body_cells'][1])==step(step(s['body_cells'][0],0),4)
    assert s['held']=={'2':s['body_cells'][1]}
    assert [x['weight'] for x in docs['source_Q']['preparation']]==['1/32','1/784','1/32']
    return docs


@dataclass
class World:
    cells:list
    old_b:tuple
    new_b:tuple
    role2:str
    pos2:tuple
    pos3:tuple
    uses:int=0

    @classmethod
    def from_stop(cls,s):
        cells=list(map(tuple,s['body_cells']))
        return cls(cells,step(cells[0],0),cells[1],'held',tuple(s['held']['2']),tuple(s['free']['3']))

    def validate(self):
        assert len(self.cells)==len(set(self.cells))==4
        assert self.cells[1] in (self.old_b,self.new_b) and self.pos2==self.cells[1]
        assert self.role2 in ('held','bound','free') and (self.role2!='bound' or self.pos2==self.new_b)
        assert self.uses in (0,1)
        assert self.pos3 in (self.cells[2],self.cells[3],self.old_b,self.new_b)

    def view(self):
        return {'B':self.cells[1],'ID2':[self.role2,self.pos2],'ID3':['free',self.pos3],
                'grant_uses':self.uses}

    def lookup(self,key):
        return {'ID2':(self.role2,self.pos2),'ID3':self.pos3,'B':self.cells[1],'grant':self.uses}[key]


@dataclass
class Attempt:
    op:str
    shared_grant:bool
    phase:int=0
    outcome:str='OPEN'
    seen:dict=field(default_factory=dict)
    path:list=field(default_factory=list)

    def keys(self):
        if self.op in ('reverse','bind'): result={'ID2','B'}
        elif self.op=='to_body_B': result={'ID3','B'}
        else: result={'ID3'}
        if self.shared_grant: result.add('grant')
        return result

    def observe(self,w):
        self.seen={k:w.lookup(k) for k in self.keys()}
        if self.op in ('reverse','bind'):
            ok=w.role2=='held' and w.pos2==w.cells[1]==w.new_b
        else:
            ok=w.pos3==w.cells[2]
            dest={'to_D':w.cells[3],'to_old_B':w.old_b,'to_body_B':w.cells[1]}[self.op]
            self.path=route(w.pos3,dest)
            assert 1<=len(self.path)<=2
        if not ok or (self.shared_grant and w.uses):
            self.outcome='INELIGIBLE'

    def advance(self,w):
        if self.op=='reverse':
            assert w.cells[1]==w.pos2==w.new_b
            w.cells[1]=w.pos2=step(w.new_b,5)
        elif self.op not in ('bind',):
            assert w.pos3==w.cells[2]
            w.pos3=self.path[0]

    def commit(self,w):
        if self.op=='reverse':
            assert w.pos2==w.old_b
            w.role2='free'
        elif self.op=='bind':
            assert w.role2=='held' and w.pos2==w.new_b
            w.role2='bound'
        else:
            if len(self.path)>1:
                assert w.pos3==self.path[0]
                w.pos3=self.path[1]
            if self.op=='to_body_B' and w.pos3!=w.cells[1]: return 'STALE_BODY_TARGET'
        if self.shared_grant:
            w.uses+=1
            if w.uses>1:return 'DOUBLE_GRANT_USE'
        self.outcome='DONE'
        return None


def run(stop,case,word,drop='',detailed=False):
    w=World.from_stop(stop)
    attempts={z:Attempt(op,case=='one_grant') for z,op in zip(SCHED,CASES[case])}
    locks={}
    journal=[]
    def frame(actor,event):
        if detailed: journal.append({'actor':actor,'stage':event,'state':w.view(),'locks':dict(locks),
                                     'outcomes':[attempts[z].outcome for z in SCHED]})
    frame(None,'interrupted')
    for idx,z in enumerate(word):
        t=attempts[z]; phase=t.phase;t.phase+=1
        # Negative controls drop one lock only. Revalidation still checks it.
        keys=t.keys()-{drop}
        failure=None
        if phase==0:
            t.observe(w)
        elif phase==1 and t.outcome=='OPEN':
            if keys.intersection(locks):
                t.outcome='WAIT'
            elif any(w.lookup(k)!=v for k,v in t.seen.items()):
                t.outcome='STALE'
            else:
                locks.update({k:z for k in keys})
                t.outcome='ACTIVE'
                other=attempts['Y' if z=='X' else 'X']
                if drop=='ID3' and other.outcome=='ACTIVE' and 'ID3' in other.keys() & t.keys():
                    failure='DOUBLE_ID3_RESERVATION'
        elif phase==2 and t.outcome=='ACTIVE':
            t.advance(w)
        elif phase==3 and t.outcome=='ACTIVE':
            failure=t.commit(w)
        elif phase==4 and t.outcome=='DONE':
            for k in keys:
                assert locks.pop(k)==z
        frame(z,STAGES[phase])
        if failure: return {'failure':failure,'prefix':word[:idx+1],'trace':journal}
        # A dropped endpoint is allowed to race in its negative control.
        w.validate()
    assert not locks and all(t.phase==5 and t.outcome in ('DONE','WAIT','STALE','INELIGIBLE')
                             for t in attempts.values())
    return {'outcomes':[attempts[z].outcome for z in SCHED],'state':w.view(),'trace':journal}


def words(length):
    for xs in combinations(range(2*length),length):
        chosen=set(xs)
        yield ''.join('X' if i in chosen else 'Y' for i in range(2*length))


def inversions(word):
    ys=n=0
    for c in word:
        if c=='Y':ys+=1
        else:n+=ys
    return n


@lru_cache(maxsize=None)
def gaussian_poly(n,k):
    if k in (0,n): return Counter({0:1})
    a=gaussian_poly(n-1,k).copy()
    a.update({i+n-k:v for i,v in gaussian_poly(n-1,k-1).items()})
    return a


def schedule_law(brc):
    for L in range(1,8):
        seq=list(words(L))
        for a in range(1,L+1):
            actual=Counter()
            for word in seq:
                x=[i for i,v in enumerate(word) if v=='X']
                y=[i for i,v in enumerate(word) if v=='Y']
                if x[-1]<y[a-1] or y[-1]<x[a-1]:
                    actual[inversions(word)]+=1
            base=gaussian_poly(L+a-1,a-1)
            expected=base.copy()
            expected.update({i+L*(L-a+1):c for i,c in base.items()})
            assert actual==expected and actual.total()==2*comb(L+a-1,a-1)
    rr=Counter(inversions(x) for x in words(5))
    res={}
    for q in (Fraction(1,2),Fraction(1),Fraction(2)):
        tot=brc.cwm_from_positive_weights(q**i for i,ct in rr.items() for _ in range(ct))
        ok=brc.cwm_from_positive_weights(q**i for i in [*range(6),*range(20,26)])
        res[str(q)]={'all_CWM':[tot.count,str(tot.total),str(tot.dominant)],
                     'nonoverlap_CWM':[ok.count,str(ok.total),str(ok.dominant)],
                     'normalized_nonoverlap':str(ok.total/tot.total)}
    return res


def sweep(stop,brc):
    runs={};summary={}; controls={}
    for case in CASES:
        buckets=[];codes=[];outcomes=Counter()
        for seq in words(5):
            res=run(stop,case,seq)
            sig=(res['outcomes'],res['state'])
            if sig not in buckets: buckets.append(sig)
            codes.append('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[buckets.index(sig)])
            outcomes['/'.join(res['outcomes'])]+=1
        assert len(codes)==252
        runs[case]={'signatures':buckets,'codes':''.join(codes)}
        summary[case]={'outcomes':dict(sorted(outcomes.items())),'distinct_terminal_records':len(buckets)}
    end_poly=Counter(inversions(seq) for seq,code in zip(words(5),runs['endpoint']['codes'])
                     if runs['endpoint']['signatures'][int(code,36)][0]==['DONE','DONE'])
    assert end_poly==Counter([0,1,2,*range(20,26)])
    summary['endpoint']['both_success_inversion_polynomial']=dict(sorted(end_poly.items()))
    for case,key in [('record','ID3'),('endpoint','B'),('one_grant','grant')]:
        bad=[run(stop,case,seq,key) for seq in words(5)]
        counter=Counter(z['failure'] for z in bad if 'failure' in z)
        mn=min((z['prefix'] for z in bad if 'failure' in z),key=lambda s:(len(s),s))
        controls[case]={'deleted_lock':key,'faults':dict(counter),'shortest_bad_prefix':mn}
    assert len(runs['independent']['signatures'])==1
    assert all(x['outcomes'].get('DONE/DONE',0)==0 for k,x in summary.items() if k in ('record','one_grant'))
    assert [len(controls[k]['shortest_bad_prefix']) for k in ('record','endpoint','one_grant')]==[4,7,8]
    return summary,controls,runs


def prior_t03(path,stop):
    raw=path.read_bytes()
    assert sha(raw)=='e60aab979013bb8a9af2644ab1309955d02b0c565f76c7419121ea2c572511c6'
    old=json.loads(raw)
    row=old['runs'][2];assert row['kind']=='LOCAL_CARRY' and row['stage']==3
    checked=0
    for key,case,selection in [('reverse','endpoint',[(0,0),(1,3),(2,4)]),
                               ('forward','independent',[(0,0),(1,4)])]:
        trace=run(stop,case,'XXXXXYYYYY',detailed=True)['trace']
        for a,b in selection:
            state=old['states'][row['routes'][key][a][1]]
            role=next(k for k in ('free','held','bound') if '2' in state[k])
            rec=state[role]['2']
            head=rec['cell'] if role=='bound' else rec
            assert trace[b]['state']['B']==tuple(state['body_cells'][1])
            assert trace[b]['state']['ID2']==[role,tuple(head)]
            assert trace[b]['state']['ID3']==['free',tuple(state['free']['3'])]
            checked+=1
    return {'sha256':sha(raw),'matched_selected_stage_observations':checked}


def archived(path,docs):
    assert sha(path.read_bytes())==ARCHIVE
    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(path) as z:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(tmp)
        pkg=Path(tmp)/'em_u27_followup'
        baseline=pkg/'baseline/cell_u27'
        for k in PINS:
            assert json.loads((pkg/'fixtures'/(k+'.json')).read_bytes())['data']==docs[k]
        sys.path.insert(0,str(baseline))
        h=importlib.import_module('work_exposure')
        l=h.v.Ledger(h.f.root_state(),4)
        budget=h.v.Capped(4,Fraction(1,16))
        prep=h.ONE
        for row in docs['source_Q']['preparation']:
            bare=row['label']
            lab=tuple(tuple(i) if isinstance(i,list) else i for i in bare)
            y,w=h.v.accepted(budget,l.s,lab)
            assert str(w.total)==row['weight']
            l.commit(lab,y);prep=h.r.serial(prep,w)
        assert prep.total==Fraction(1,802816)
        s=l.s;l.validate(stable=True);n=len(l.log)
        lab=('body',1,4,True)
        y,w=h.v.accepted(budget,s,lab)
        l.commit(lab,y);data=list(h.references(s,y,l.log[n:]))
        freeze=h.freeze_loss(data[2],(2,3))
        assert json.loads(json.dumps(h.v.encode(freeze)))==docs['interrupted_after_carry']
        assert w.total==Fraction(1,18816)
        # Obtain a stable geometry by completing only held AB, keeping CD absent.
        fr=docs['interrupted_after_carry'];cx=tuple(tuple(q) for q in fr['body_cells'])
        table={(0,1):((0,),(5,)),(0,3):((2,),())}
        other=object.__new__(h.v.Ledger)
        other.s=h.z.state(h.m.make(cx,table),{k:'A' for k in table})
        other.B=4;other.ids=frozenset(range(4));other.tokens={(0,1):[[0],[2]],(0,3):[[1],[]]}
        other.free={3:cx[0]};other.log=[]
        bound=other.validate(stable=True)
        assert bound[0]['edge']==(0,1) and bound[1]['edge']==(0,3) and bound[2]['port']==5
        w0=World.from_stop(fr)
        for dest in (cx[3],w0.old_b,cx[1]):
            other.deliver(3,cx[2]);start=len(other.log)
            other.deliver(3,dest)
            assert [row['to_cell'] for row in other.log[start:]]==route(cx[2],dest)
        return {'released_after_stage':3,'source_preparation_weight':str(prep.total),
                'growth_weight':str(w.total),'source_coordinate_courier_routes':3,
                'archive_sha256':ARCHIVE,'stable_comparison_inventory_passed':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path)
    ap.add_argument('--archive',type=Path)
    ap.add_argument('--t03',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--interleavings',type=Path)
    ap.add_argument('--case',choices=CASES)
    ap.add_argument('--word')
    a=ap.parse_args()
    roots=[Path.cwd(),*Path(__file__).resolve().parents,Path('/workspace/enterprise-math')]
    repo=a.repo or next((d for d in roots if (d/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if not repo: ap.error('supply --repo path to enterprise-math')
    docs=load_inputs(repo);stop=docs['interrupted_after_carry']
    if a.word or a.case:
        if a.case not in CASES or not a.word or sorted(a.word)!=list('XXXXXYYYYY'):
            ap.error('supply --case and a word containing five X and five Y')
        print(json.dumps(run(stop,a.case,a.word,detailed=True),indent=2));return
    assert blobid((repo/'src/enterprise_math/brc_weighted.py').read_bytes())==BRC
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    summary,control,runs=sweep(stop,brc)
    out={'task_id':TASK,'pins':PINS,'schedules_per_case':252,'total_schedules':1008,
         'negative_control_schedules':756,'summary':summary,'omitted_lock_controls':control,
         'q_weighting':schedule_law(brc),'gaussian_polynomial_pairs_checked':28}
    trace=a.t03 or Path(__file__).resolve().parent.parent/'tenth/recovery_traces.json'
    if trace.is_file():out['prerequisite_T03']=prior_t03(trace,stop)
    elif a.t03:ap.error('--t03 file does not exist')
    if a.archive:out['source_replay']=archived(a.archive,docs)
    if a.interleavings:
        a.interleavings.write_text(json.dumps({'order':'Choose the five X positions in lexicographic combination order from 0..9. At each index the corresponding base36 character points to one [outcomes, final_state] entry. The checker reconstructs every intervening observation.', 'cases':runs},separators=(',',':'))+'\n')
    data=json.dumps(out,indent=2)+'\n'
    if a.output:a.output.write_text(data)
    else:print(data,end='')


if __name__=='__main__': main()
