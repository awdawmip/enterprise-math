"""Replay the exact 16-history fixed-table upgrade proof.

Default: standalone Python standard library + C++17. Optional --rebuild-bank
and --native use the previous round8 package, supplied with --previous.
"""
import argparse
import contextlib
import io
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from prove_skeleton import hungarian,prove

def rebuild_bank(previous,work):
 archive=previous/'previous'
 second=archive.joinpath(*(['previous']*5));third=second.parent
 os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
 sys.path[:0]=[str(third/'group'),str(second/'curve'),str(second/'bounds')]
 from generate import maps
 from prior_bounds import observation_file
 observation_file(work/'observations')
 exe=work/'bank'
 subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(archive/'nesting/bank.cpp'),'-o',str(exe)],check=True)
 subprocess.run([str(exe),str(work/'observations'),str(work/'seeds')],check=True,stdout=subprocess.DEVNULL)
 seeds=defaultdict(set)
 for line in (work/'seeds').read_text().splitlines():
  size,price,*row=map(int,line.split())
  if size in (5,6):
   assert price=={5:120,6:201}[size]
   seeds[size].add(tuple(row))
 linear,translations,_=maps();bank={}
 for size,rows in seeds.items():
  rotated={tuple(sorted(f[x] for x in row)) for row in rows for f in linear}
  bank[str(size)]=sorted({tuple(sorted(f[x] for x in row)) for row in rotated for f in translations})
 return bank

def run(previous=None,rebuild=False,native=False):
 bank_raw=json.loads((HERE/'class_bank.json').read_text())
 bank={int(k):set(map(frozenset,v))for k,v in bank_raw.items()}
 assert {k:len(v)for k,v in bank.items()}=={5:3300,6:12000}
 for size,rows in bank.items():
  assert {frozenset(5*(x//5)+(x+1)%5 for x in row)for row in rows}==rows
 witness=json.loads((HERE/'witness23.json').read_text());old=list(map(frozenset,witness['source_old22']));new=list(map(frozenset,witness['groups']))
 assert len(old)==22 and len(new)==23
 assert all(r in bank[len(r)]for r in old+new)
 assert sorted(x for r in old for x in r)==list(range(125))
 assert sorted(x for r in new for x in r)==list(range(125))
 minima=(0,0,12,36,72,120,201,292,419,557,744,936,1104,1296)
 assert all(minima[s]>=81*s-285 for s in range(1,14))
 assert {s for s in range(1,14)if minima[s]==81*s-285}=={5,6}
 assert sum(minima[len(r)]for r in old)==3855
 assert sum(minima[len(r)]for r in new)==3570
 minimum,assignment=hungarian([[-len(a&b)for b in new]for a in old])
 assert 125+minimum==16
 previous_transition=json.loads((HERE/'twenty_transition.json').read_text())
 q=frozenset(json.loads((HERE/'two_step_extension.json').read_text())['branches'][0]['first_new_label'])
 assert [frozenset(r)-q for r in previous_transition['new']]+[q]==old
 def minimum_moves(rows):
  removable={x:i for i,r in enumerate(rows)if len(r)==6 for x in r if r-{x} in bank[5]}
  return [q for q in bank[5]if all(x in removable for x in q)and len({removable[x]for x in q})==5]
 assert not minimum_moves(new)
 old_images=set();new_images=set()
 for t in range(5):
  shift=lambda r:frozenset(5*(x//5)+(x+t)%5 for x in r)
  old_images.add(frozenset(map(shift,old)));new_images.add(frozenset(map(shift,new)))
  assert all(shift(r)in bank[len(r)]for r in old+new)
  assert set(map(shift,map(frozenset,previous_transition['old'])))==set(map(frozenset,previous_transition['old']))
 assert len(old_images)==len(new_images)==5
 with TemporaryDirectory()as temp:
  work=Path(temp)
  if rebuild:
   assert previous is not None
   got=rebuild_bank(previous,work)
   assert all(set(got[k])==set(map(tuple,bank_raw[k]))for k in ('5','6'))
  with contextlib.redirect_stdout(io.StringIO()):
   skeleton=prove(HERE/'class_bank.json',HERE/'witness23.json',work/'skeleton.json')
  expected=json.loads((HERE/'skeleton_proof.json').read_text())
  assert skeleton==expected
  input_path=work/'input'
  with input_path.open('w')as stream:
   print(len(old),file=stream)
   for r in old:print(len(r),*sorted(r),file=stream)
   rows=bank_raw['5']+bank_raw['6'];print(len(rows),file=stream)
   for r in rows:print(len(r),*r,file=stream)
  exe=work/'five_changes'
  subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'exact_five_changes.cpp'),'-o',str(exe)],check=True)
  receipt=subprocess.run([str(exe),str(input_path),'15'],capture_output=True,text=True,check=True)
  last=json.loads(receipt.stdout)
  assert last['status']=='EXHAUSTED'and last['budget']==15
  assert last['eligible_new_classes']==last['completed']==3029
  result={'status':'PASS','fixed_table_optimal_upgrade_distance':16,'target_read_cost':3570,'at_most_four_part_changes':skeleton['total_packings'],'five_part_change_exclusion':last,'translation_images':5,'witness23_minimum_five_history_24_successors':0,'class_bank_rebuilt':rebuild}
  if native:
   assert previous is not None
   original=previous.joinpath(*(['previous']*5))/'original'
   sys.path.insert(0,str(original))
   from frontier9.native.replay_joint import run as native_run
   code=[0]*125
   for label,row in enumerate(new):
    for x in row:code[x]=label
   observed=json.loads(json.dumps(native_run(code,1)))
   assert observed==json.loads((HERE/'native23.json').read_text())
   result['native']=observed
 return result

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--previous',type=Path,help='Root of the preceding round8 delivery directory');parser.add_argument('--rebuild-bank',action='store_true');parser.add_argument('--native',action='store_true');parser.add_argument('--output',type=Path);args=parser.parse_args()
 result=run(args.previous.resolve()if args.previous else None,args.rebuild_bank,args.native)
 text=json.dumps(result,indent=2,sort_keys=True)+'\n'
 if args.output:args.output.write_text(text)
 print(text,end='')
