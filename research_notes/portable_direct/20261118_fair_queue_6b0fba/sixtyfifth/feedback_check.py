"""Replay one saved material row; enumerate feedback and labelled release observations."""
import argparse
from collections import Counter
from hashlib import sha256
from importlib import util
from itertools import permutations, product
import gzip
from zipfile import ZipFile
import json
from pathlib import Path
import sys

CORE='7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'
R10='02c7f1bb20e567a6f652adaf600f9ac434894c79680375f78f727c56e5651af3'
GATE=(1,)
DELAYS=(1,2,3)


def checked_module(name,path,digest):
    if sha256(path.read_bytes()).hexdigest()!=digest:
        raise ValueError('source mismatch '+str(path))
    spec=util.spec_from_file_location(name,path)
    obj=util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


class Positive:
    def __init__(self,core):
        self.core=core
        self.calls=Counter()

    def add(self,a,b):
        self.calls['parallel']+=1
        mat=[[0,a,b,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
        value=self.core.recurrent_mass_power(mat,2)[0][-1]
        assert value.denominator==1
        return value.numerator

    def gap(self,old,n):
        if n>old:
            raise ValueError('negative resource balance')
        rem=old-n
        assert self.add(rem,n)==old
        return rem


def burst(ar,k,b,gate,f):
    hist=[0,0,0]
    m=0
    while m<k and b in gate:
        m=ar.add(m,1)
        hist[b]=ar.add(hist[b],1)
        b=f[b]
    return m,b,tuple(hist)


def trace(ar,f,source_burst=None):
    q=(2,3,4)
    b=0
    pend=Counter()
    wall=Counter()
    rows=[]
    emitted=[]
    for t in range(3,10):
        if t>3:
            b=(b+1)%3
            new=Counter()
            for (j,r,d),n in pend.items():
                if d==1:
                    wall[j,r]=ar.add(wall[j,r],n)
                else:
                    new[j,r,ar.gap(d,1)]=n
            pend=new
            args=(min(q),b,GATE,f)
            m,end,hist=burst(ar,*args)
            if source_burst:
                assert source_burst(*args)==(m,end,hist)
            q=tuple(ar.gap(n,m) for n in q)
            for old,k in enumerate(hist):
                if k:
                    emitted.extend([t]*k)
                    for j,d in enumerate(DELAYS):
                        r=(j+old)%3
                        pend[j,r,d]=ar.add(pend[j,r,d],k)
            b=end
        assert sum(q)+sum(pend.values())+sum(wall.values())==9
        rows.append(dict(time=t,q=q,phase=b,
                         pending=[[*key,n] for key,n in sorted(pend.items())],
                         wall=[[*key,n] for key,n in sorted(wall.items())]))
    return rows,tuple(emitted)


def waits(gate,f,s,order):
    phase=s
    elapsed=0
    events=[]
    while len(events)<2:
        if phase in gate:
            events.append((elapsed,phase))
            phase=f[phase]
        else:
            phase=(phase+1)%order
            elapsed+=1
    return tuple(events)


def partial_tables():
    groups=[]
    maps=list(product(range(3),repeat=3))
    for mask in range(8):
        gate=tuple(i for i in range(3) if mask>>i&1)
        classes=Counter()
        for f in maps:
            signature=[]
            for s in gate:
                (_,first),(dt,second)=waits(gate,f,s,3)
                assert first==s and (second-dt)%3==f[s]
                signature.append((dt,second))
            classes[tuple(signature)]+=1
        assert len(classes)==3**len(gate) and set(classes.values())=={3**(3-len(gate))}
        groups.append(dict(gate=gate,observable_classes=len(classes),tables_per_class=next(iter(classes.values()))))
    return groups


def named_releases():
    slots=(('A0','B0'),('A1','B1','B2'),('A2','A3','B3','B4'))
    h=Counter()
    ordered=Counter()
    for y in permutations(slots[1],2):
        for z in permutations(slots[2],2):
            pairs=list(zip(slots[0],y,z))
            typ=['P' if len({u[0] for u in tri})==1 else 'M' for tri in pairs]
            h[typ.count('M')]+=1
            for sequence in permutations(range(2)):
                events=[pairs[i] for i in sequence]
                used=[v for tri in events for v in tri]
                assert len(set(used))==6
                for s,q0 in [('A',4),('B',5)]:
                    remainder=[v for group in slots for v in group if v[0]==s and v not in used]
                    assert sum(v[0]==s for v in used)+len(remainder)==q0
                word=''.join(typ[i] for i in sequence)
                ordered[word]+=1
    assert (h[0],h[1],h[2])==(8,20,44)
    # Each gap is read from two consecutive release instants; the last
    # postphase (or an extra marked pulse) reads the outstanding gap.
    for dp,dm in product(range(3), repeat=2):
        hist=Counter()
        count_types={}
        for word,num in ordered.items():
            gaps=tuple({'P':dp,'M':dm}[c] for c in word)
            hist[gaps]+=num
            count_types.setdefault(sum(gaps),set()).add(word.count('M'))
        assert len(hist)==(4 if dp!=dm else 1)
        assert all(len(v)==1 for v in count_types.values())==(dp!=dm)
    return dict(inventory={'A':[1,1,2],'B':[1,2,2]},unordered_by_mixed=dict(sorted(h.items())),
                ordered_by_type=dict(sorted(ordered.items())),chronologies=sum(ordered.values()))


def delay_check():
    finite=0
    for release in product(range(3),repeat=6):
        total=[sum(release[t-d] for d in DELAYS if 0<=t-d<len(release)) for t in range(9)]
        recovered=[]
        for i in range(6):
            recovered.append(total[i+1]-sum(recovered[j] for j in (i-1,i-2) if j>=0))
        assert tuple(recovered)==release
        finite+=1
    cyclic=[]
    for period in range(1,12):
        seen={}
        for a in product(range(2), repeat=period):
            y=tuple(sum(a[(t-d)%period] for d in DELAYS) for t in range(period))
            if y in seen:
                diff=tuple(i-j for i,j in zip(a,seen[y]))
                assert period%3==0 and sum(diff[:3])==0 and all(v==diff[t%3] for t,v in enumerate(diff))
            seen[y]=a
        assert (len(seen)<2**period)==(period%3==0)
        cyclic.append([period,len(seen)])
    return dict(finite_words=finite,cyclic_period_vs_binary_images=cyclic)


def check_release(q,b,gate,fb,events,post):
    available=list(q)
    phase=b
    for ports in events:
        if phase not in gate or not all(available): raise ValueError('closed gate or missing role')
        if ports!=tuple(('+',j,(j+phase)%3,d) for j,d in enumerate(DELAYS)):
            raise ValueError('port, old role, sign or delay')
        available=[a-1 for a in available]
        phase=fb[phase]
    if (tuple(available),phase)!=post: raise ValueError('poststate')
    if all(available) and phase in gate: raise ValueError('incomplete burst')


def mutations():
    f=(1,2,0)
    initial=(2,3,4)
    ports=lambda ph: tuple(('+',j,(j+ph)%3,d) for j,d in enumerate(DELAYS))
    good=ports(1)
    check_release(initial,1,GATE,f,[good],((1,2,3),2))
    check_release(initial,1,GATE,(0,1,2),[good,good],((0,1,2),1))
    cases={'negative_alias':([tuple(('-',*p[1:]) if j==0 else p for j,p in enumerate(good))],((1,2,3),2)),
           'postphase_routing':([ports(2)],((1,2,3),2)),
           'double_spend':([good,good],((0,1,2),2)),
           'unpaid_release':([good],(initial,2)),
           'unsettled':([], (initial,1))}
    for key,(es,end) in cases.items():
        try:check_release(initial,1,GATE,f,es,end)
        except ValueError: continue
        raise AssertionError(key)
    return sorted(cases)


ARCHIVE='c1b1d2d3c9ce952e922263b04537d849419832e6d6acde0060eb45e6de684335'
SNAPSHOTS='c2d2725eb9a80727f664da56c9fb4896e57b1f7f6f3dec1acfe5724573ba7683'
EVENTS='fd8b1f61dcf11e1ab70f11ccafcee7865dc64d8f037f6a8177ee9de7f5de3ffe'


def compare_archive(path,rows):
    if sha256(path.read_bytes()).hexdigest()!=ARCHIVE:
        raise ValueError('wrong original R10 archive')
    with ZipFile(path) as z:
        prefix='residual_feedback_R10/run2/'
        def data(name,digest):
            raw=z.read(prefix+name)
            assert sha256(raw).hexdigest()==digest
            return json.loads(gzip.decompress(raw))
        saved=data('FULL_MAIN_STATES.json.gz',SNAPSHOTS)
        original_events=data('MAIN_EVENTS.json.gz',EVENTS)
        assert [i for i,row in enumerate(saved[3]['cells']) if row[1:4]==[2,3,4]]==[735]
        assert [row[:6] for row in original_events if row[0]=='feedback-release' and row[2]==7]==[
            ['feedback-release',4,7,1,1,2],['feedback-release',6,7,1,1,2]]
        code=saved[3]['cells'][735][0]
        for row in rows:
            t=row['time']
            assert saved[t]['t']==t and len(saved[t]['cells'])==5832
            walls=[0]*9
            for j,i,n in row['wall']: walls[3*j+i]=n
            expected=[code,*row['q'],walls,row['pending'],*[int(row['phase']==i) for i in range(3)]]
            assert expected==saved[t]['cells'][735]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--core',type=Path)
    p.add_argument('--r10',type=Path,help='optional private original test_feedback.py, with its parents')
    p.add_argument('--archive',type=Path,help='optional original R10 ZIP for full stored row comparison')
    args=p.parse_args()
    if args.core is None:
        roots=(Path.cwd(), *Path(__file__).resolve().parents)
        args.core=next((f for r in roots for f in [r/'src/enterprise_math/brc_weighted_recurrent.py'] if f.is_file()),None)
    if not args.core:p.error('run from a checkout with src/enterprise_math or pass --core')
    ar=Positive(checked_module('public_p08_core',args.core,CORE))
    reference=None
    if args.r10:
        model=checked_module('p08_original_r10',args.r10,R10)
        assert sha256(next(args.r10.parent.rglob('brc_weighted_recurrent.py')).read_bytes()).hexdigest()==CORE
        native=model.P.Arithmetic()
        native.stage='one_material_only'
        def reference(*values):
            lit=model.burst_unit(native,*values)
            assert lit==model.burst_orbit(native,*values)
            return lit
    family=Counter()
    originals=[]
    for f in product(range(3),repeat=3):
        rows,times=trace(ar,f,reference)
        family[times]+=1
        if f==(1,2,0):
            originals=rows
            assert [(u['time'],u['q'],u['phase']) for u in rows if u['time'] in (3,4,6,9)]==[
                (3,(2,3,4),0),(4,(1,2,3),2),(6,(0,1,2),2),(9,(0,1,2),2)]
    if args.archive: compare_archive(args.archive,originals)
    assert family=={(4,4):9,(4,5):9,(4,6):9}
    print(json.dumps(dict(core_sha256=CORE,original_r10_sha256=R10,
                          local_reference_target_count=27*6,archive_sha256=ARCHIVE,archived_snapshot_member_sha256=SNAPSHOTS,
                          archived_event_member_sha256=EVENTS,verified_snapshot_row_count=7,
                          shared_public_BRC_calls=ar.calls,original_local_rows=originals,
                          release_times_vs_table_count=[[list(k),v] for k,v in sorted(family.items())],
                          all_masks=partial_tables(),two_source=named_releases(),negative_controls=mutations(),
                          delayed_observer=delay_check()),indent=2,sort_keys=True))


if __name__=='__main__': main()
