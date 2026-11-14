"""Check complete 540-row eight-slot exact certificate and optionally reproduce the full finite DP.
Run: python REPLAY_EC49FDB_COMPACT.py --check [--recompute --limit 4].
"""
import argparse,base64,gzip,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
from functools import lru_cache
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'
if SRC.is_dir(): sys.path.insert(0,str(SRC))
else: SRC=HERE
import frozen_model as fm
try: import BUILD_EC49FCZ_TRIES as builder
except ImportError: import build_trie as builder
builder.candidates=lru_cache(None)(fm.candidates)
SHA='d69c6ce8efda1e41b5401b22e0bc93ccf6b3bdcfe88f30990f42127b7a26d40f'
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def cases():
    for b in (0,1):
      for r in (2,4,8):
       for s in (1,2,4,8):
        for t in (1,2,4,8):
         if s==t==1:continue
         for fam in (0,1):
          for extra in (1,2,4,8):
           if extra!=(s if fam==0 else t):yield b,r,s,t,fam,extra

def keys(c):
    b,r,s,t,fam,e=c
    fixed=['5:16',f'6:{s}',f'7:{t}','8:2','8:4','9:16'] if b==0 else ['5:32',f'6:{s}',f'7:{t}','8:1','8:8','9:32']
    return [f'4:{r}',*fixed,f'{6 if fam==0 else 7}:{e}']

def check():
    raw=gzip.decompress(base64.b64decode((HERE/'EC49FDB_540_ROW_TABLE.json.gz.b64').read_text().strip()))
    assert hashlib.sha256(raw).hexdigest()==SHA
    data=json.loads(raw); rows=data['rows']
    assert data['pin']==PIN and data['optimum_all_rows']==158
    assert len(rows)==540 and [q[:6] for q in rows]==[list(c) for c in cases()]
    assert sum(q[8] for q in rows)==196555855176
    assert max(q[7] for q in rows)==59174
    print('ROW_TABLE_SHA_COVERAGE_AND_COUNTS_PASS',len(rows))
    return rows

def replay(rows,limit):
    source=SRC/'EXACT_PREFIX_TRIE_DP.cpp'
    if not source.exists():source=HERE/'exact_prefix_trie_dp.cpp'
    with tempfile.TemporaryDirectory(prefix='ec49fdb_') as d:
      d=Path(d);exe=d/'solver'
      subprocess.run(['g++','-O3','-std=c++17',str(source),'-o',str(exe)],check=True)
      num=0
      for q in rows[:limit]:
        file=d/'input.trie.txt';meta=builder.build(keys(q[:6]),file)
        got=json.loads(subprocess.check_output([str(exe),str(file)],text=True))
        assert (got['total_exact_optimum'],got['fixed_edges'],got['trie_nodes'],got['dp_transitions'])==(158,*q[6:9])
        num+=1
    print('FULL_LANGUAGE_EXACT_REPLAY_PASS',num)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--check',action='store_true');p.add_argument('--recompute',action='store_true')
    p.add_argument('--limit',type=int,default=540)
    a=p.parse_args();rows=check()
    if a.recompute:replay(rows,a.limit)
