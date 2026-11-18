"""EC49FDC exact 18-case nine-slot experiment. Reuse sibling frozen model and exact trie solver."""
import json,subprocess,hashlib,sys
from pathlib import Path
from functools import lru_cache
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'
if SRC.is_dir():sys.path.insert(0,str(SRC))
else:SRC=HERE
import frozen_model as fm
try:import BUILD_EC49FCZ_TRIES as B
except ImportError:import build_trie as B
B.candidates=lru_cache(None)(fm.candidates)

def cases():
    for b in ('A','B'):
        for q in (2,4,8):
            for u in (2,4,8):yield b,q,u

def keys(case):
    b,q,u=case
    return ['4:2','5:16','6:1',f'6:{q}','7:1',f'7:{u}','8:2','8:4','9:16'] if b=='A' else ['4:2','5:32','6:1',f'6:{q}','7:1',f'7:{u}','8:1','8:8','9:32']

def run():
    import tempfile
    rows=[]
    source=SRC/'EXACT_PREFIX_TRIE_DP.cpp'
    with tempfile.TemporaryDirectory(prefix='ec49fdc_') as d:
        d=Path(d);exe=d/'solver'
        subprocess.run(['g++','-O3','-std=c++17',str(source),'-o',str(exe)],check=True)
        for c in cases():
            k=keys(c);assert len(set(k))==9
            file=d/'input.trie.txt';meta=B.build(k,file)
            v=json.loads(subprocess.check_output([str(exe),str(file)],text=True))
            assert v['variable_slots']==9 and v['fixed_edges']==meta['fixed_edges'] and v['trie_nodes']==meta['trie_nodes']
            rows.append({'case':list(c),'keys':k,'fixed':v['fixed_edges'],'nodes':v['trie_nodes'],'opt':v['total_exact_optimum'],'transitions':v['dp_transitions'],'pool':list(meta['pool_sizes'].values())})
    report={'schema':'EC49FDC_NINE_SLOT_18_FULL_EXACT_V1','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','method':'Exact labelled signed primitive-prefix trie DP, complete frozen signature languages','rows':rows,'all_158':all(r['opt']==158 for r in rows),'transitions_total':sum(r['transitions'] for r in rows)}
    raw=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
    (HERE/'EC49FDC_18_NINE_SLOT_REPLAY.json').write_bytes(raw)
    print('FULL_LANGUAGE_EXACT_9_SLOT',len(rows),sorted(set(r['opt'] for r in rows)),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':run()
