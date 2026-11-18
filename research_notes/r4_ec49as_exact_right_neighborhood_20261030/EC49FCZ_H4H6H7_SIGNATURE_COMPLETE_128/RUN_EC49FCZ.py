"""All exact seven-slot H6/H7 signature variations, frozen model and labelled trie DP.
Execute from directory containing BUILD_EC49FCZ_TRIES.py and exact_dp executable.
"""
import json,subprocess,time
from pathlib import Path
from functools import lru_cache
import frozen_model, BUILD_EC49FCZ_TRIES as B

HERE=Path(__file__).resolve().parent
# Semantic cache only: tuples retain original literal candidate order.
orig=frozen_model.candidates
frozen_model.candidates=lru_cache(None)(orig)
B.candidates=frozen_model.candidates

def main():
 t=time.monotonic();rows=[]
 work=HERE/'generated'
 work.mkdir(exist_ok=True)
 for branch in ['A','B']:
  base=['5:16','8:2','8:4','9:16'] if branch=='A' else ['5:32','8:1','8:8','9:32']
  for h6 in (1,2,4,8):
   for h7 in (1,2,4,8):
    for h4 in (1,2,4,8):
     keys=[f'4:{h4}',base[0],f'6:{h6}',f'7:{h7}',*base[1:]]
     path=work/f'{branch}_4_{h4}_6_{h6}_7_{h7}.trie.txt'
     meta=B.build(keys,path)
     out=subprocess.check_output([str(HERE/'exact_dp'),str(path)],text=True)
     result=json.loads(out)
     if result['fixed_edges']!=meta['fixed_edges'] or result['trie_nodes']!=meta['trie_nodes']:
      raise AssertionError(('input mismatch',keys,result,meta))
     row={'branch':branch,'H4':h4,'H6':h6,'H7':h7,**result,'candidate_counts':meta['pool_sizes']}
     rows.append(row)
     path.unlink()
     if len(rows)%16==0:print('computed',len(rows),'wall',round(time.monotonic()-t,1),flush=True)
 report={'schema':'EC49FCZ_SEVEN_SLOT_H6_H7_COMPLETE_EXACT_V1','frozen_source_git_blob':'7e97065ac9a0ff70435b92ee2f4bd718c9bf1859','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','model':'24 original positions; native signed ordered primitive prefixes; fixed L=(4,2,1),M=(7,3,2)','rows':rows}
 (HERE/'EC49FCZ_128_EXACT_CERTIFICATE.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
 print('counts',len(rows),'optima',sorted(set(x['total_exact_optimum'] for x in rows)),'wall',round(time.monotonic()-t,2))
if __name__=='__main__':main()
