"""Check recorder decisions and recoverable schedules on the pinned three-channel source."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as R
from hashlib import sha1, sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import runpy

TASK = 'research_tasks/RS-EULER-RR-20261012-02.md'
TASK_BLOB = '9ec8f79bffd0583e1f2bb8d875fb0efa38c00b99'
PREVIOUS_SHA = '77299a430908181c7de17050380a5dc3037dd3fd43b6d4292e9bdcb08307f53a'


def sector(x):
    _,_,f,w,_ = x
    return w ^ (2*((f >> 2)^((f >> 1)&1)) + ((f >> 2)^(f&1)))


def shuffles(slots):
    for positions in combinations(range(slots+3), 3):
        old = iter('HUC')
        yield tuple(next(old) if i in positions else 'R' for i in range(slots+3))


def inside(word):
    p = [i for i,v in enumerate(word) if v == 'R']
    return p[0] < word.index('C') < p[1]


def sense(x, order, source_atom):
    snapshots = []
    for event in order:
        if event == 'R':
            snapshots.append(x)
        else:
            x = source_atom(x,event)
    return x,snapshots


def risks(hist):
    # Each history stores loss counts for second-slot choices hold, contact.
    return {mode:str(sum(min(x) for x in cells.values()))
            for mode,cells in hist.items()}


def same_slot(j, a, r, z):
    """One stationary rule; returns a physical contact decision and one new bit."""
    if r==a:
        if z:
            return 0,0
        return int(j!=a),int((j-a)%3 in (0,2))
    sign=(r-a)%3
    return int(sign*(1+z)%3==2),0


def actual(source, brc):
    old = list(product(range(3),range(2),range(8),range(4),range(2)))
    orders = list(shuffles(2))
    risk = {g:{m:defaultdict(lambda:[R(0),R(0)]) for m in
               ('hit_core','hit_no_sheet','first_core','first_no_sheet')}
            for g in (R(0),R(1,5),R(3,10),R(2,3),R(9,10),R(1))}
    sectors = defaultdict(Counter)
    repairs = Counter()
    direct = [brc.CWM_ZERO for _ in range(3)]
    for x,order in product(old,orders):
        end,(A,B) = sense(x,order,source['source_atom'])
        assert end == source['published_cycle'](x) and sector(end) == sector(x)
        gap = inside(order)
        for a,sign in product(range(3),(-1,1)):
            k,l = ((j-a)*sign%3 for j in (A[0],B[0]))
            step1 = int(A[0]!=a)
            r = (a+sign*step1)%3
            live = (r+sign*int(l==2))%3
            planned = (r+sign*int(k==2))%3
            assert planned == A[0]
            assert (live != A[0]) == ((k==2)!=(l==2))
            assert (live != B[0]) == ((k!=0)!=(l!=0))
            # A receiver-sheet-blind snapshot repair: use the signed native
            # change deduced from the receiving register after first contact.
            stored = int((A[0]-a)%3 == 2)
            inferred = (r-a)%3
            if r == a:
                restore = r
                repaired = r
            else:
                pre_diff = 2 if stored else 1
                restore = (r + inferred*int(inferred*pre_diff%3 == 2))%3
                local_l = inferred*(B[0]-a)%3
                first_if_gap = -inferred*(-1)**B[1] %3
                decision = (local_l if local_l else first_if_gap)-1
                assert decision in (0,1)
                repaired = (r+inferred*decision)%3
            assert restore == A[0] and repaired in (A[0],B[0])
            hit,bit = same_slot(A[0],a,a,0)
            r_mid = (a+hit*sign)%3
            hit,bit = same_slot(B[0],a,r_mid,bit)
            assert (r_mid+hit*sign)%3 == A[0] and bit == 0
            repairs['rows'] += 1
            for protocol,answer in [('live',live),('planned',planned)]:
                val = 'start' if answer == x[0] else 'end' if answer == end[0] else 'third'
                sectors[(sector(x),sign,protocol)][val] += 1
            # Native positive CWM masses independently propagate both receiver
            # slots and each old command on one fixed sector and sheet.
            if sector(x)==0 and sign==1:
                branch = brc.cwm_edge(R(1,2880))
                for _ in order:
                    branch = brc.cwm_propagate(branch,brc.CWM_ONE)
                i = 0 if live==x[0] else 1 if live==end[0] else 2
                direct[i] = brc.cwm_recoalesce(direct[i],branch)
            if sector(x)!=0 or sign!=1:
                continue
            # Everything except the source sheet is supplied in the first
            # observer. This is stronger than supplying current j alone.
            z = B[0], B[2:], a, r
            for g,modes in risk.items():
                weight = (g/3 if gap else (1-g)/7)/288
                for add in (0,1):
                    out = (r+sign*add)%3
                    for typ,err in [('first',out!=A[0]),('hit',out not in (A[0],B[0]))]:
                        modes[typ+'_no_sheet'][z][add] += weight*err
                        modes[typ+'_core'][(z,B[1])][add] += weight*err
    for (q,sign,protocol), c in sectors.items():
        assert c == ({'start':2016,'end':576,'third':288} if protocol=='live'
                     else {'start':2592,'end':288})
    assert [mass.total for mass in direct] == [R(7,10),R(1,5),R(1,10)]
    rows = {}
    for g,modes in risk.items():
        actual_risks = risks(modes)
        theory = dict(hit_core=0,hit_no_sheet=g/6,first_core=min(g,1-g)/3,
                      first_no_sheet=g/6+R(2,3)*min(1-g,g/2))
        assert actual_risks == {k:str(v) for k,v in theory.items()}
        rows[str(g)] = actual_risks
    # At B even the complete old core, projected old history, source program
    # counter, receiver, reference, and event number agree.
    x = (2,1,0,1,0)
    twin = []
    for word in ('HURCR','HUCRR'):
        _,(A,B) = sense(x,word,source['source_atom'])
        twin.append((A[0],B,int(A[0]!=0)))
    assert [v[0] for v in twin]==[2,1] and twin[0][1:]==twin[1][1:]
    return dict(ready_input_schedule_rows=repairs['rows'],sector_count=4,receiver_sheets=2,
                same_rule_one_bit_exact_snapshot_rows=repairs['rows'],
                per_sector_and_sheet={k:dict(sectors[(0,1,k)]) for k in ('live','planned')},
                positive_CWM_fixed_sector_sheet=[[v.count,str(v.total),str(v.dominant)] for v in direct],
                ambiguous_exact_snapshot=twin, decision_risk=rows)


def rank(rows):
    rows = [list(map(R,r)) for r in rows]
    n=0
    for j in range(len(rows[0])):
        k=next((k for k in range(n,len(rows)) if rows[k][j]),None)
        if k is None:
            continue
        rows[k],rows[n]=rows[n],rows[k]
        piv=rows[n][j]
        rows[n]=[v/piv for v in rows[n]]
        for k in range(n+1,len(rows)):
            if rows[k][j]:
                factor=rows[k][j]
                rows[k]=[x-factor*y for x,y in zip(rows[k],rows[n])]
        n+=1
    return n


def layout_rows(L, wiring, start):
    # A fixed positive normalized jump, all L+1 possible cuts.
    v,p,q=wiring
    results=[]
    for h in range(L+1):
        end=(start+1)%3
        k_v,k_p,k_q=(start if i<=h else end for i in (v,p,q))
        results.append((int(k_v==1)+int(k_p==2)+int(k_q==2))%3)
    return [[int(x==label) for x in results] for label in range(3)]


def tomography(source):
    data=[]
    for L in range(2,13):
        allpos=list(range(1,L+1))
        rows1=[]
        for i in range(0,L,2):
            p,q=allpos[i:i+2] if i+1<L else (L-1,L)
            rows1+=layout_rows(L,(p,p,q),2)
        rows3=[]
        for i in range(0,L,3):
            cut=allpos[i:i+3]
            p,q=(cut[0],cut[1]) if len(cut)>1 else (L-1,L)
            v=cut[-1]
            for start in (0,2):
                rows3+=layout_rows(L,(v,p,q),start)
        assert rank(rows1)==rank(rows3)==L+1
        # Calibrated sentinel with a changing old writer. Its two native fields
        # mark the first three old stages; j distinguishes the final contact.
        order_count=comb(L+3,3)
        sentinels=set()
        for word in shuffles(L):
            _,views=sense((0,0,0,0,0),word,source['source_atom'])
            codes=tuple((j,0 if w==0 else 1+s) for j,s,f,w,th in views)
            sentinels.add(codes)
        assert len(sentinels)==order_count
        data.append(dict(slots=L,full_shuffles=order_count,observable_cuts=L+1,
                         normalized_hidden_freedom=order_count-(L+1),single_settings=len(rows1)//3,
                         tagged_layouts=len(rows3)//6,rank_including_normalization=rank(rows3),
                         distinct_marked_sentinel_transcripts=len(sentinels)))
    return data


def main(repo, previous):
    source_data=previous.read_bytes()
    assert sha256(source_data).hexdigest()==PREVIOUS_SHA
    old = runpy.run_path(str(previous))
    data=(repo/TASK).read_bytes()
    assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==TASK_BLOB
    brc=old['source'](repo)
    return dict(task='RS-EULER-RR-20261012-02',task_blob=TASK_BLOB,
                reused_public_checker_sha256=PREVIOUS_SHA, public_core_blobs=old['PINS'],
                observed=actual(old,brc), inverse_cut_laws=tomography(old))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--previous',type=Path,default=Path(__file__).resolve().parent.parent/'seventyeighth'/'aperture_check.py')
    args=parser.parse_args()
    print(json.dumps(main(args.repo,args.previous),sort_keys=True,indent=2))
