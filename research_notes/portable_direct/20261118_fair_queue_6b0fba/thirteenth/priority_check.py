"""U27F-10 reconstruction of the B=4 transverse stopped TOTAL/work observer.

The public computation generates the comparison rows from the finite geometry.
Optional original-archive replay also checks the positive stage counter and all
four historical row tables. This program does not run the old suite's main.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import gzip
import hashlib
import importlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
import tempfile
import zipfile

N=18816
STATES=[(g,b) for g in ('O','C','B') for b in range(8)]
TAGS=('R','F')
TASK='RS-CELL-U27F-10-INDEPENDENT-AUDIT-20261012'
ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'
PINS={'recorded_oracles':'98c6c3e961f66d4093459c998cee8e14c0d0cdd70d034b8e36090027b52c633c',
      'carry_P':'bfffff71a955af7fba73ec569c47710b470860e2855eb12c89973e3398b77883',
      'carry_Q':'acd915da997e0703ae72395e805126b29d841d47a68a435e75af379e40f76708',
      'order_observer':'5c68ecd1cfe4eeb615856a552fbb6c253e5af7e2ae65c6b1aeb50a100f3c95d7'}
SOURCE_PINS={'NOTE.md':'4859daa4aee5963524a308f28e8787d9f00371a6e328022e1b92fdf8c948de85',
             'work_exposure.py':'53da273a333ff11750d549be1409d5c2f4b5296850d354d57dbb91fd0e7424f3',
             'check_u27.py':'33fed8fc95a32dc5d07b5da85b852ac29326a45a6d4ffc8d63f0f863ba7928de',
             'CHECKPOINT.json':'fd27bbd8009c88836c14b948835b85590f08702ec85ba62839e93a344cbc5985',
             'evidence/results.json':'15e42b310676846282b42d263fdfbe3241ed008f58d96de8e0358451cb944cb7'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def eligible(geometry,mask):
    blocked={'O':0,'B':4,'C':1}[geometry]
    return (mask & ~blocked).bit_count()


def branches(geometry,mask):
    """Outcome, mass numerator, and ordered eligible-contact counts."""
    old=eligible(geometry,mask)
    rows=[]
    for bit in (4,2,1):
        new=eligible(geometry,mask^bit)
        rows.append(((geometry,mask^bit),588,(old,old,new,new)))
    if geometry=='O':
        for leaf,bit,distance in [('B',4,1),('C',1,2)]:
            new=old-int(bool(mask & bit))
            rows.append(((leaf,mask),1,(old,)*(distance+1)+(new,)*3))
            rows.append(('R',8,(old,)*(distance+2)+(old+1,)*2))
    else:
        distance=1 if geometry=='B' else 2
        rows.append((('O',mask),48,(old,)+(mask.bit_count(),)*(distance+3)))
    rows.append(((geometry,mask),N-sum(weight for _,weight,_ in rows),(old,)))
    return rows


def padd(a,b,scale=1):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=scale*x
    while len(out)>1 and out[-1]==0: out.pop()
    return out


def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return padd(out,[])


def peval(a,x):
    result=0
    for c in reversed(a):result=result*x+c
    return result


def polynomial_risks():
    survived={}; first={}
    for x in STATES:
        row=defaultdict(lambda:[0])
        fail=[N]
        for dst,weight,hs in branches(*x):
            term=[weight]
            for h in hs:term=pmul(term,[1,-h])
            row[dst]=padd(row[dst],term)
            fail=padd(fail,term,-1)
        survived[x]=row
        first[x]=fail
    second={x:[0] for x in STATES}
    for x,row in survived.items():
        for y,term in row.items():
            if y in first:
                second[x]=padd(second[x],pmul(term,first[y]))
    return first,second


def separation(rows):
    ties=[]; orders=Counter(); smallest=None
    for x,y in combinations(STATES,2):
        diff=padd(rows[x],rows[y],-1)
        if diff==[0]:
            ties.append([x,y]);continue
        v=next(i for i,c in enumerate(diff) if c)
        orders[v]+=1
        coeff=diff[v:];d=len(coeff)-1
        bern=[sum(Q(c*comb(j,i),49**i*comb(d,i)) for i,c in enumerate(coeff[:j+1])) for j in range(d+1)]
        assert min(bern)>0 or max(bern)<0
        abs_min=min(map(abs,bern))
        smallest=abs_min if smallest is None else min(smallest,abs_min)
    return {'strict_pair_count':sum(orders.values()),'leading_power_counts':dict(orders),
            'identical_pairs':ties,'smallest_abs_Bernstein_coefficient_before_common_normalization':str(smallest)}


class Pointed:
    """TOTAL and its first additive work mark; every positive operation uses BRC."""
    def __init__(self,brc):
        self.brc=brc;self.zero=(Q(0),Q(0));self.one=(Q(1),Q(0))
    def edge(self,x):
        return self.brc.cwm_edge(x) if x else self.brc.CWM_ZERO
    def add(self,x,y):
        if not x:return y
        if not y:return x
        return self.brc.cwm_recoalesce(self.edge(x),self.edge(y)).total
    def product(self,x,y):
        if not x or not y:return Q(0)
        return self.brc.cwm_propagate(self.edge(x),self.edge(y)).total
    def plus(self,a,b):
        return self.add(a[0],b[0]),self.add(a[1],b[1])
    def times(self,a,b):
        return self.product(a[0],b[0]),self.add(self.product(a[0],b[1]),self.product(a[1],b[0]))
    def star(self,a):
        assert 0<=a[0]<1
        c=self.brc.one_state_recurrent_cwm([a[0]]).total_mass_closure if a[0] else Q(1)
        return c,self.product(self.product(c,a[1]),c)


def accumulate(P,row,key,item):
    row[key]=P.plus(row.get(key,P.zero),item)


def macro_rows(P,delta,exposure=False):
    rows={}
    for x in STATES:
        row={}
        for dest,n,hs in branches(*x):
            mass=Q(n,N)
            for j,h in enumerate(hs,1):
                hit=P.product(mass,P.product(delta,Q(h,49)))
                accumulate(P,row,'F',(hit,P.product(hit,j)))
                # A complete stage chooses either a safe label or a loss label.
                mass=P.product(mass,Q(49-delta*h,49))
            work=Q(sum(hs),49) if exposure else len(hs)
            accumulate(P,row,dest,(mass,P.product(mass,work)))
        assert sum(w for w,m in row.values())==1
        rows[x]=row
    return rows


def solve(P,K,states,goals):
    """Positive elimination and back-substitution of the two marked equations."""
    rows={x:dict(K[x]) for x in states}
    upper={}
    for i,x in enumerate(states):
        loop=P.star(rows[x].pop(x,P.zero))
        upper[x]={z:P.times(loop,w) for z,w in rows[x].items() if w!=P.zero}
        for y in states[i+1:]:
            weight=rows[y].pop(x,P.zero)
            if weight==P.zero:continue
            for z,w in upper[x].items():
                accumulate(P,rows[y],z,P.times(weight,w))
    output={}
    for x in reversed(states):
        outputs={g:upper[x].get(g,P.zero) for g in goals}
        for y,w in upper[x].items():
            if y in output:
                for g in goals:accumulate(P,outputs,g,P.times(w,output[y][g]))
        output[x]=outputs
    for x in states:
        assert sum(output[x][g][0] for g in goals)==1
        for g in goals:
            rhs=K[x].get(g,P.zero)
            for y,w in K[x].items():
                if y in output:rhs=P.plus(rhs,P.times(w,output[y][g]))
            assert rhs==output[x][g]
    return output


def entry_law(P):
    # BC side is suppressed only before its first release; both side labels exist.
    pre={}
    for m in range(16):
        row={m^bit:(Q(1,32),0) for bit in (1,2,4,8)}
        release=Q(1,784) if m&8 else Q(0)
        if release:row[('O',m&7)]=(release,0)
        row[m]=(1-Q(4,32)-release,0)
        pre[m]=row
    goals=[('O',b) for b in range(8)]
    solved=solve(P,pre,list(range(16)),goals)
    return {g:w[0] for g,w in solved[0].items()}


def observation_groups(rows,mark):
    part=[list(STATES)]
    while True:
        blocks=part+[['R'],['F']]
        refined=[]
        for block in part:
            groups=defaultdict(list)
            for x in block:
                sig=tuple(sum(rows[x].get(y,(0,0))[k] for y in dest)
                          for dest in blocks for k in range(2 if mark else 1))
                groups[sig].append(x)
            refined+=list(groups.values())
        if refined==part:return part
        part=refined


def joint(P,law,sol):
    out=P.zero
    for x,p in law.items():
        out=P.plus(out,P.times((p,0),sol[x]))
    return out


def account(repo):
    src=repo/'src/enterprise_math/brc_weighted.py';raw=src.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='3f205696709e847909958a153f8fe10d3f6b70f0'
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted
    P=Pointed(brc_weighted)
    root=repo/'research_inputs/U27F_20261012/fixtures'
    docs={}
    for k,digest in PINS.items():
        raw=(root/(k+'.json')).read_bytes()
        assert sha(raw)==digest;docs[k]=json.loads(raw)
    for tag,word in [('carry_P',[1,1,0,0,0]),('carry_Q',[1]*5)]:
        assert [len(it['eligible']) for it in docs[tag]['data']]==word
    law=entry_law(P)
    assert sum(law.values())==1 and len(set(law.values()))==4
    walsh=[Q(1,98*j*(j+1)+2*j+1) for j in range(4)]
    for mask in range(8):
        inv=sum((-1)**((mask & u).bit_count())*walsh[u.bit_count()] for u in range(8))/8
        assert law['O',mask]==inv
    coeff=solve(P,macro_rows(P,Q(0),True),STATES,TAGS)
    exposure=joint(P,law,{x:o['R'] for x,o in coeff.items()})[1]
    assert exposure==Q(90462203875,1899962848)
    a,b=polynomial_risks()
    summary={'task':TASK,'pre_release_distribution':{str(x[1]):str(w) for x,w in law.items()},
             'risk_degree':[max(len(v)-1 for v in z.values()) for z in (a,b)],
             'pre_release_Walsh_by_weight':list(map(str,walsh)),
             'one_macro':separation(a),'second_macro':separation(b),
             'delta_zero_eventual_exposure':str(exposure),'four_oracles':{}}
    numeric={}
    for tag,case in docs['recorded_oracles']['cases'].items():
        targets=case['values'];delta=Q(targets['work_loss_delta'])
        rows=macro_rows(P,delta)
        for x in STATES:
            assert peval(a[x],delta/49)/N==rows[x]['F'][0]
            two=sum(P.product(w[0],rows[y]['F'][0]) for y,w in rows[x].items() if y in rows)
            assert peval(b[x],delta/49)/(N*N)==two
        sol=solve(P,rows,STATES,TAGS)
        result={g:joint(P,law,{x:o[g] for x,o in sol.items()}) for g in TAGS}
        work=P.add(result['R'][1],result['F'][1])
        assert (result['R'][0],result['F'][0],work,exposure)==tuple(
            Q(targets[k]) for k in ('repair_before_new_loss','new_loss_before_completion',
                                     'expected_executed_work_to_stop','exposure_coefficient'))
        numeric[tag]=rows
        groups=[observation_groups(rows,mark) for mark in (False,True)]
        summary['four_oracles'][str(delta)]={'exact_aggregate_targets_matched':4,
            'per_transient_state_marked_scalar_equations':96,
            'strong_quotient_block_sizes':[[len(z) for z in part] for part in groups],
            'mean_work_rounded_8dp':format(float(work),'.8f')}
    return summary,law,numeric


def original(path,law,numeric):
    assert sha(path.read_bytes())==ARCHIVE
    with tempfile.TemporaryDirectory() as tmp,zipfile.ZipFile(path) as z:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(tmp)
        pkg=Path(tmp)/'em_u27_followup';base=pkg/'baseline/cell_u27'
        for name,digest in SOURCE_PINS.items():assert sha((base/name).read_bytes())==digest
        assert sha((pkg/'provenance/intake_validation.json').read_bytes())=='065359ca6b1704ae87f2b02273b60fa3b56c6e530d1678c89cac351ea23bbe4c'
        for folder in (pkg,base):
            m=json.loads((folder/'PACKAGE_MANIFEST.json').read_bytes())['files']
            for f,v in m.items():assert sha((folder/f).read_bytes())==v['sha256']
        sys.path.insert(0,str(base))
        import check_u27 as source_checks
        h=source_checks.h
        prep=source_checks.setup_damaged()
        assert set(prep.paths.table())=={(0,1),(0,3),(2,3)}
        comp=h.full_comparison()
        compiled,stats=h.build_episodes(comp)
        def label(state):
            moved=[i for i,v in enumerate(state.paths.cells) if v[2]]
            g={(): 'O',(1,):'B',(2,):'C'}[tuple(moved)]
            mask=sum(v for v,m in zip((4,2,1),state.modes) if m=='D')
            return g,mask
        ix={i:label(comp['states'][i]) for i in comp['damaged']}
        assert len(comp['intact'])==32 and set(ix.values())==set(STATES)
        for i,paths in compiled.items():
            actual=Counter()
            for j,w,lab,tag,frames in paths:
                local=tuple(len(f['eligible']) for f in frames)
                actual[(ix.get(j,'R'),local)]+=w.total
            expected=Counter()
            for j,w,hs in branches(*ix[i]):expected[j,hs]+=Q(w,N)
            assert actual==expected
        checked_rows=0
        for case,rows in numeric.items():
            with gzip.open(base/'evidence'/(case+'.json.gz'),'rt') as src:arch=json.load(src)
            for i in comp['damaged']:
                assert Q(arch['first_release_law'][str(i)]['total'])==law.get(ix[i],0)
                empirical={}
                for d,w in arch['marked_rows'][str(i)].items():
                    y={'REPAIRED':'R','INTERRUPTED':'F'}.get(d)
                    if y is None:y=ix[int(d)]
                    empirical[y]=tuple(Q(z['total']) for z in w)
                for y in set(empirical)|set(rows[ix[i]]):
                    assert empirical.get(y,(0,0))==rows[ix[i]].get(y,(0,0))
                checked_rows+=1
        return {'archive_sha256':ARCHIVE,'source_pins':SOURCE_PINS,
                'matched_all_archived_marked_rows':checked_rows,
                'recompiled_damaged_branches':stats['compiled_branch_histories'],
                'recompiled_stage_count':stats['compiled_work_stages'],'intact_states':32,'damaged_states':24}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path)
    ap.add_argument('--archive',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    candidates=[Path.cwd(),*Path(__file__).resolve().parents,Path('/workspace/enterprise-math')]
    repo=args.repo or next((r for r in candidates if (r/'research_inputs/U27F_20261012/fixtures').is_dir()),None)
    if not repo:ap.error('use --repo path to public enterprise-math checkout')
    result,law,rows=account(repo)
    if args.archive:result['frozen_source_comparison']=original(args.archive,law,rows)
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')


if __name__=='__main__':main()
