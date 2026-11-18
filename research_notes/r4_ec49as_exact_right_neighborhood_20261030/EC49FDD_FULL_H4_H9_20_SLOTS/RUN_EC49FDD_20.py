"""Build all twenty frozen H4--H9 languages and solve their exact shared-prefix optimum.

Dependencies: sibling EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128 files
`frozen_model.py` (blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859)
and `BUILD_EC49FCZ_TRIES.py` (blob 4c74b4ee243c939494d9f7eedb3f61255e16f91f).
Compile this directory's SPARSE_PREFIX_TRIE_DP.cpp using g++ -O3 -std=c++17.
"""
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'))
from frozen_model import REQ
import BUILD_EC49FCZ_TRIES as B
KEYS=[f'{h}:{s}' for h in (4,5,6,7,8,9) for s in REQ[h]]
assert len(KEYS)==20
path=HERE/'EC49FDD_ALL20.trie.txt'
meta=B.build(KEYS,path)
raw=path.read_bytes()
result=json.loads(subprocess.check_output([str(HERE/'exact_sparse_dp'),str(path),'1000'],text=True))
assert result['total_exact_optimum']==158
assert (result['trie_nodes'],result['fixed_edges'],result['variable_slots'])==(109973,16,20)
report={'schema':'EC49FDD_CPP_FULL20_EXACT_V1','input_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','trie_sha256':hashlib.sha256(raw).hexdigest(),'pool_sizes':meta['pool_sizes'],**result}
(HERE/'EC49FDD_CPP_REPORT.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
path.unlink()
