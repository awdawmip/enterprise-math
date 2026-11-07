#!/usr/bin/env python3
"""EC49FDI: exact BRC key-budget switches and 96-edge witness.
Uses already published independent exact-language/Trie checker EC49FDE.
Run in this directory: python VERIFY_EC49FDI.py
"""
import hashlib,importlib.util,json
from pathlib import Path
P=Path(__file__).resolve().parent
SRC=P.parent/'EC49FDE_ALTERNATE_BRC_LATE_KEY_EXACT_112'/'VERIFY_EC49FDE.py'
sp=importlib.util.spec_from_file_location('ec49fde_independent',SRC)
r=importlib.util.module_from_spec(sp); sp.loader.exec_module(r)
A=(4,2,1);B=(6,4,1);C=(5,3,1);D=(6,5,1)
FIXED=set().union(*(r.prefixes(w) for w in r.FIXED.values()))
LABELS=[f'{h}:{s}' for h in range(4,10) for s in r.REQ[h]]
assert len(FIXED)==16 and len(LABELS)==20

def solve(switch6,switch8):
    keys={4:A,5:A,6:C if switch6 else B,7:B,8:D if switch8 else B,9:B}
    pool={f'{h}:{s}':w for h in range(4,10) for s,w in r.language(h,keys[h]).items()}
    assert list(pool)==LABELS and all(pool.values())
    child=[{}];terminal=[0];edges=[0];prefix=['']
    for i,label in enumerate(LABELS):
        for word in pool[label]:
            v=0
            for c in r.native(word):
                if c not in child[v]:
                    u=len(child);child[v][c]=u;child.append({});terminal.append(0)
                    prefix.append(prefix[v]+c);edges.append(int(prefix[u] not in FIXED))
                v=child[v][c]
            terminal[v]|=1<<i
    extra,states,inspected,compatible,peak=r.independent_dp(child,terminal,edges,20)
    return dict(h6_new=switch6,h8_new=switch8,full_positive_keys=3+len(set(keys.values())),
        keys_by_h={str(h):list(v) for h,v in keys.items()},
        optimum=16+extra,fixed_edges=16,
        candidate_words=sum(map(len,pool.values())),trie_nodes=len(child),
        root_states=states,inspected_pairs=inspected,compatible_pairs=compatible,peak_states=peak)

def witness():
    w={
    '2:16':'fe','2:32':'ge','3:16':'feg','3:32':'gef',
    '4:1':'gefd','4:2':'fegd','4:4':'fegc','4:8':'gefc',
    '5:16':'feggf','5:32':'gefgf',
    '6:1':'gefdfg','6:2':'fegdfg','6:4':'feggfc','6:8':'gefgfc',
    '7:1':'gefdfgd','7:2':'fegdfgd','7:4':'feggfcc','7:8':'gefgfcc',
    '8:1':'gefdfggf','8:2':'fegdfggf','8:4':'feggfcfg','8:8':'gefgfcfg',
    '9:16':'feggffggf','9:32':'gefgffggf'}
    keys={4:A,5:A,6:C,7:B,8:B,9:B}
    native={}
    assert len(w)==24
    for label,word in w.items():
        h,s=map(int,label.split(':'))
        assert len(word)==h and r.observe(word)==s
        if h>=4: assert word in r.language(h,keys[h])[s]
        native[label]=r.native(word)
        if h>=4: assert tuple(native[label].count(c) for c in 'ABCDEF')==(*keys[h],0,0,0)
    prefixes={word[:k] for word in native.values() for k in range(1,len(word)+1)}
    assert len(prefixes)==96
    digest=hashlib.sha256(('\n'.join(sorted(prefixes))+'\n').encode()).hexdigest()
    assert digest=='dd8c0a68979ee66fc83970d351bea1d65608d00fa46ebbaaa3fb7ec0b9310f69'
    return {'edge_count':96,'prefix_sha256':digest,'distinct_full_positive_keys':6,
            'label_words':w,'native_words':native}

def main():
    rows=[solve(*x) for x in ((False,False),(True,False),(False,True),(True,True))]
    assert [x['optimum'] for x in rows]==[112,96,106,92]
    assert [x['full_positive_keys'] for x in rows]==[5,6,6,7]
    assert [x['candidate_words'] for x in rows]==[4372,4492,5492,5612]
    assert [x['trie_nodes'] for x in rows]==[26705,25605,31159,30059]
    assert [x['inspected_pairs'] for x in rows]==[21972032,25909100,21984948,25815852]
    report={'schema':'EC49FDI_TWO_SWITCH_NATIVE_KEY_BUDGET_V1',
        'frozen_scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'results':rows,'budgeted_minima_at_most':{'5':112,'6':96,'7':92},'witness96':witness()}
    file=P/'EXACT_REPORT_EC49FDI.json'
    file.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'costs':[x['optimum'] for x in rows],
        'word_counts':[x['candidate_words'] for x in rows],
        'witness96_prefix_sha256':report['witness96']['prefix_sha256'],
        'saved_report_sha256':hashlib.sha256(file.read_bytes()).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
