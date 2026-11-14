#!/usr/bin/env python3
"""Exact original frozen native BRC root-domain/singleton/DFS-sort differential.
Usage: python VERIFY_NEIGHBOR_DIFF.py master_and_radius3_cases.txt NEIGHBOR_FEATURES.json
Reuses VERIFY_EC49FNY_INDEPENDENT.py in the same directory.
"""
from pathlib import Path
import sys,hashlib,json
sys.path.insert(0,str(Path(__file__).resolve().parent))
import VERIFY_EC49FNY_INDEPENDENT as native
src=Path(sys.argv[1])
assert hashlib.sha256(src.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
profile={}
for k in (32279,32315,32318):
    words,keys=native.frozen(src,k)
    tabs={r:native.table(words,keys,r) for r in (3,5,6,7)}
    roots={l:[r for r in (3,5,6,7) if l in tabs[r][1]] for l in range(24)}
    one={l:min(tabs[r][2][1<<tabs[r][1][l]] for r in roots[l]) for l in range(24)}
    order=sorted(range(24),key=lambda l:(len(roots[l]),-one[l],l))
    profile[k]={'keys':keys,'order':order,'roots':roots,'singleton':one}
    print('NATIVE_PROFILE',k,'key set',keys,'order',order)
diff={}
for a,b in ((32279,32315),(32279,32318),(32315,32318)):
    A,B=profile[a],profile[b]
    root_diff={str(l):[A['roots'][l],B['roots'][l]] for l in range(24) if A['roots'][l]!=B['roots'][l]}
    singleton_diff={str(l):[A['singleton'][l],B['singleton'][l]] for l in range(24) if A['singleton'][l]!=B['singleton'][l]}
    position_diff=sum(x!=y for x,y in zip(A['order'],B['order']))
    diff[f'{a}-{b}']={'removed_keys':sorted(set(A['keys'])-set(B['keys'])),'added_keys':sorted(set(B['keys'])-set(A['keys'])),'root_domain_changed':root_diff,'minimum_singleton_changed':singleton_diff,'dfs_order_positions_changed':position_diff}
assert diff['32279-32315']['root_domain_changed']=={'11':[[3,7],[7]],'13':[[3,6,7],[6,7]]}
assert diff['32279-32315']['minimum_singleton_changed']=={str(l):[20,22] for l in (10,11,12,13)}
assert diff['32279-32315']['dfs_order_positions_changed']==24
assert diff['32279-32315']['removed_keys']==[45] and diff['32279-32315']['added_keys']==[81]
assert diff['32279-32318']['removed_keys']==[45] and diff['32279-32318']['added_keys']==[84]
assert diff['32315-32318']['dfs_order_positions_changed']==0
assert not diff['32315-32318']['root_domain_changed'] and not diff['32315-32318']['minimum_singleton_changed']
result={'input_master_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'scope':'3 named 24-demand configurations on original frozen 94-key BRC signed-prefix dataset','profiles':{str(k):v for k,v in profile.items()},'pair_differences':diff}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('NEIGHBOR_FEATURES_EXACT_PASS',list(diff),flush=True)
