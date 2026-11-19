"""Isolated C2 adapter for the supplied, restored S15 reference. No production edits."""
import argparse
from collections import Counter
from contextlib import contextmanager
from copy import copy
import hashlib
import json
from pathlib import Path
import resource
import sys
from time import perf_counter

PINS = {
    'stable_calibration.py':'c3b3ee20d122935d5c19594191af669a9162f7731807a7fd3cdf88c1a24f86ef',
    'shor_exact.py':'1e89417ec27bbb209130aadd818dd98ac62a2ff1d8e17a4dfae2447f5cf21ad4',
    'test_hierarchy.py':'6046f656e74fb67852bf441d4961e8c23de21f258e30691a4d0d812f38bab623',
    'tree_cost.py':'cbe9d05b57f5693271e1aec325b82c597f270dd8d8f1ed99b480feeba049707f',
}


def digest(value):
    raw = json.dumps(value,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()


def payload(d):
    return tuple(d.items())


class Slot:
    def __init__(self, obj):
        self.obj = obj
        self.identity = id(obj)

    def borrow(self):
        if self.obj is None:
            raise RuntimeError('MOVED')
        return self.obj

    def take(self):
        obj = self.borrow()
        self.obj = None
        return obj


@contextmanager
def trace(arith):
    events = {'signed':[], 'keys':[], 'parents':[]}
    original_call,original_add,original_record=arith.call,arith.sadd,arith.core.record
    def call(op,*args):
        value=original_call(op,*args)
        events['keys'].append((op,args,value))
        return value
    def sadd(x,y):
        value=original_add(x,y)
        events['signed'].append((x,y,value))
        return value
    def record(op,args,result):
        events['parents'].append((op,tuple(args),tuple(result)))
        return original_record(op,args,result)
    assert 'call' not in vars(arith) and 'sadd' not in vars(arith) and 'record' not in vars(arith.core)
    arith.call,arith.sadd,arith.core.record=call,sadd,record
    try:
        yield events
    finally:
        del arith.call,arith.sadd,arith.core.record


class Integration:
    def __init__(self, stable):
        self.stable=stable
        self.step=None
        self.ring=None
        self.rows=[]
        self.selections=[]
        self.totals=Counter()
        self.timings=Counter()
        self.rolling=hashlib.sha256()

    def evaluate_pair(self, ring, data, index, right, inputs, owners, origin):
        """Only the declared four-leaf cone may transfer its private left rows."""
        tick=perf_counter()
        left=data[index]
        evidence=self.rows[-1]
        ref=copy(ring)
        ref.a=self.stable.h.BRC()
        ref.a.cache=dict(ring.a.cache)
        ref.a.stage=ring.a.stage
        ref.metrics=Counter()
        assert list(ref.a.cache.items())==list(ring.a.cache.items())
        external_identities=tuple(map(id,inputs))
        protected=(id(right),payload(right))
        external_snapshot=tuple(payload(d) for d in inputs)
        initial_keys=len(ref.a.cache)
        with trace(ref.a) as ref_events:
            original_plus=ref.add(left,right)
            original_minus=ref.add(left,right,-1)
        self.timings['local_reference_and_snapshots']+=perf_counter()-tick
        tick=perf_counter()
        L,R=len(left),len(right)
        if origin:
            plus,minus=left.copy(),left.copy()
            self.totals['actual_copy_calls']+=2
            self.totals['actual_copied_entries']+=2*L
        else:
            assert index in owners and owners[index].borrow() is left
            assert type(left) is dict and all(id(left)!=v for v in external_identities)
            assert sum(x is left for x in data)==1 and left is not right
            self.totals['scope_object_checks']+=len(data)+len(inputs)+2
            minus=left.copy()
            data[index]=None
            left=None
            plus=owners[index].take()
            try:
                owners[index].borrow()
            except RuntimeError as exc:
                assert str(exc)=='MOVED'
            else:
                raise AssertionError('old handle still readable')
            assert id(plus)==owners[index].identity
            self.totals['actual_copy_calls']+=1
            self.totals['actual_copied_entries']+=L
            self.totals['saved_copied_entries']+=L
            self.totals['transfers']+=1
        self.timings['node_preflight_transfer_and_copy']+=perf_counter()-tick
        tick=perf_counter()
        self.totals['baseline_copy_calls']+=2
        self.totals['baseline_copied_entries']+=2*L
        # MeterRing's original FIVE is also the frozen learner input.
        ring.metrics['copied_terms']+=2*L
        ring.metrics['coefficient_visits']+=2*R
        ring.metrics['polynomial_additions']+=2
        local=Counter()
        with trace(ring.a) as events:
            for e,v in right.items():
                x=plus.get(e,0)
                positive=ring.a.sadd(x,v)
                negative=ring.a.sadd(x,-v)
                local['right_item_yields']+=1
                local['left_get']+=1
                local['signed_calls']+=2
                for target,result in ((plus,positive),(minus,negative)):
                    local['zero_tests']+=1
                    if result:
                        target[e]=result
                        local['assignments']+=1
                    else:
                        local['pop_attempts']+=1
                        if e in target:
                            ring.metrics['exact_zero_cancellations']+=1
                            local['successful_pops']+=1
                        target.pop(e,None)
        self.totals.update(local)
        self.timings['candidate_node_including_probes']+=perf_counter()-tick
        tick=perf_counter()
        assert plus is not minus and id(plus) not in external_identities and id(minus) not in external_identities
        assert payload(plus)==payload(original_plus) and payload(minus)==payload(original_minus)
        assert tuple(map(id,inputs))==external_identities and tuple(payload(d) for d in inputs)==external_snapshot
        assert (id(right),payload(right))==protected
        assert ring.a.cache==ref.a.cache
        for name in events:
            assert Counter(map(repr,events[name]))==Counter(map(repr,ref_events[name]))
            if events[name]!=ref_events[name]:self.totals[name+'_order_differences']+=1
        self.totals['actual_outer_BRC_keys']+=len(events['keys'])
        self.totals['actual_parent_entries']+=len(events['parents'])
        self.totals['actual_memo_misses']+=len(ref.a.cache)-initial_keys
        self.rolling.update(bytes.fromhex(digest([self.step,index,origin,events])))
        evidence['nodes'].append([index,origin,L,R,len(events['keys']),len(events['parents'])])
        self.timings['local_identity_value_and_ledger_validation']+=perf_counter()-tick
        return plus,minus

    def install(self):
        s=self.stable
        execute=s.t.execute_selected
        def new_execute(selected,prepared,current,old,target,inner,values,eng):
            self.step=s.t.AUD.step
            self.ring=eng.r
            self.selections.append([self.step,selected['method']])
            try:
                return execute(selected,prepared,current,old,target,inner,values,eng)
            finally:
                self.ring=None
        s.t.execute_selected=new_execute
        native_fft=s.h.MeterRing.fft
        def isolated_fft(ring,inputs,label):
            if ring is not self.ring or label!='work:11':
                return native_fft(ring,inputs,label)
            assert ring.Q==512
            self.rows.append({'step':self.step,'nodes':[]})
            raw_objects=[]
            external_signatures=[]
            spans={}
            data=[None]*ring.Q
            for x,p in enumerate(inputs):
                data[int(f'{x:09b}'[::-1],2)]=p
            owners={}
            live=[]
            for level in range(1,10):
                length=1<<level
                half=length//2
                powers=[ring.a.mul(j,ring.Q//length) for j in range(half)]
                for base in range(0,ring.Q,length):
                    for j,e in enumerate(powers):
                        i=base+j
                        right=ring.shift(data[i+half],e)
                        self.totals['eligible_fft_coordinates_tested']+=1
                        if (level,i) in ((6,257),(7,257),(7,289)):
                            new_raw=[data[i],data[i+half]] if level==6 else [data[i+half]]
                            raw_objects.extend(new_raw)
                            external_signatures.extend((id(d),payload(d)) for d in new_raw)
                            if level==6:
                                spans['past']=[dict(d) for d in new_raw]
                            else:
                                spans.setdefault('level6',[]).extend([dict(data[i]),dict(data[i+half])])
                            plus,minus=self.evaluate_pair(ring,data,i,right,inputs,owners,level==6)
                            if level==7:
                                spans.setdefault('level7',[]).extend([dict(plus),dict(minus)])
                            data[i],data[i+half]=plus,minus
                            self.totals['source_shift_item_yields']+=len(right)
                            if level==6:
                                owners[i],owners[i+half]=Slot(plus),Slot(minus)
                                assert len({id(plus),id(minus)})==2
                            else:
                                live.extend((i,i+half))
                            del plus,minus
                        else:
                            v=data[i]
                            data[i]=ring.add(v,right)
                            data[i+half]=ring.add(v,right,-1)
                            del v
                        ring.metrics['butterflies']+=1
                ring.layers.append(dict(label=label,layer=level,terms=sum(map(len,data)),
                                        nonzero_rows=sum(map(bool,data)),largest_row=max(map(len,data))))
                if level==7:
                    assert len(live)==len({id(data[i]) for i in live})==4
                    assert all(slot.obj is None for slot in owners.values())
                    assert [(id(d),payload(d)) for d in raw_objects]==external_signatures
                    assert set(map(id,raw_objects)).isdisjoint(id(data[i]) for i in live)
                    self.rows[-1]['local_window_sha256']=digest([spans['past'],spans['level6'],spans['level7']])
                    self.rows[-1]['four_leaf_sizes']=[len(data[i]) for i in live]
                    if self.step==6:
                        # Frozen request 7, historical c=-1 of the C2 packet.
                        assert self.rows[-1]['four_leaf_sizes']==[41,41,39,39]
                        assert [(x[2],x[3]) for x in self.rows[-1]['nodes']][0][0]==11
                    del spans,raw_objects,external_signatures,new_raw
            assert len(self.rows[-1]['nodes'])==3
            return data
        s.h.MeterRing.fft=isolated_fft


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--intake',type=Path,required=True)
    parser.add_argument('--policy',choices=('s15_65','s15_195'),required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    sys.path.insert(0,str(args.intake/'s15'))
    import stable_calibration as stable
    paths=[stable.__file__,sys.modules[stable.h.BRC.__module__].__file__,stable.h.__file__,stable.t.__file__]
    for p in map(Path,paths):
        assert hashlib.sha256(p.read_bytes()).hexdigest()==PINS[p.name]
    adapter=Integration(stable)
    adapter.install()
    start=perf_counter()
    sys.argv=[stable.__file__,'--policy',args.policy,'--out',str(args.out)]
    stable.main()
    results=dict(policy=args.policy,selected=adapter.selections,cones=adapter.rows,
                 counts=dict(adapter.totals),ordered_ledger_sha256=adapter.rolling.hexdigest(),
                 measured=dict(elapsed_seconds=perf_counter()-start,scoped_seconds=dict(adapter.timings),
                               process_user_seconds=resource.getrusage(resource.RUSAGE_SELF).ru_utime,
                               process_system_seconds=resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                               linux_peak_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    (args.out/'C2_INTEGRATION.json').write_text(json.dumps(results,sort_keys=True,indent=2)+'\n')


if __name__=='__main__':
    main()
