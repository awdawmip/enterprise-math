"""Optional source-identical performance and positive-control replay."""
from pathlib import Path
import argparse,hashlib,itertools,json,struct,subprocess,time
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--controls-only',action='store_true');a=p.parse_args()
here=Path(__file__).resolve().parent;baseline=a.baseline.resolve();w=a.work.resolve();out=a.output.resolve();out.mkdir(parents=True,exist_ok=True)
ident=json.loads((here/'inputs_sha256.json').read_text());sources={'original':baseline/'bias/weighted_native.cpp','new':here/'weighted_ordered_orbit.cpp'}
for name,digest in ident.items():
 f=sources[name.removesuffix('_source')] if name.endswith('_source')else w/name
 assert hashlib.sha256(f.read_bytes()).hexdigest()==digest,str(f)
binaries={}
for key,src in sources.items():
 binary=out/key;subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(src),'-o',str(binary)],check=True);binaries[key]=binary
raw=(w/'obs').read_bytes();offset=125*125*4*8;obs=list(struct.iter_unpack('<QQQQ',raw[:offset]));triples=[tuple(raw[i:i+3])for i in range(offset,len(raw),3)];maps=(w/'maps').read_bytes();parents=[]
for line in (w/'parent').read_text().splitlines()[:250]:
 lo,hi=map(int,line.split());parents.append(lo+(hi<<64))
def bits(m):
 while m:
  b=m&-m;m-=b;yield b.bit_length()-1
def run(engine,args):
 cmd=[str(binaries[engine]),*map(str,args)]
 if engine=='new':cmd.append(str(w/'maps'))
 start=time.time();r=subprocess.run(cmd,capture_output=True,text=True,check=True)
 return list(map(int,r.stderr.split())),r.stdout,time.time()-start
label=lambda s:','.join(map(str,s));P=[2]*45+[11,11];frame=out/'positive_frame.txt';frame.write_text('0\n')
args=[w/'obs',w/'parent',w/'B',frame,label(P),'13',1296,100000,0,1,0,0,','.join(['0']*14)]
expected=json.loads((here/'positive_control_result.json').read_text());controls=[]
for i,engine in enumerate(['original','new']):
 counts,stdout,elapsed=run(engine,args);assert counts==expected[i]['counts'];tokens=stdout.split();assert tokens[:2]==['hit','1']
 groups=[int(x)+(int(y)<<64)for x,y in (v.split(':')for v in tokens[2:])];assert len(groups)==48 and sorted(m.bit_count()for m in groups)==P+[13]
 union=0;cost=0;delta=0;eleven=[]
 for m in groups:
  assert not union&m;union|=m;pts=list(bits(m));assert all(not(all(m>>x&1 for x in t))for t in triples)
  if len(pts)!=13:assert all(m&~parent for parent in parents)
  for x in pts:
   h=[0]*4
   for y in pts:
    for j,v in enumerate(obs[125*x+y]):h[j]|=v
   cost+=sum(v.bit_count()for v in h);delta+=h[0].bit_count()+(h[1]&((1<<61)-1)).bit_count()-(h[1]>>61).bit_count()-h[2].bit_count()-h[3].bit_count()
  if len(pts)==11:eleven.append(m)
 assert union==(1<<125)-1 and len(eleven)==2
 same=any(sum(1<<g[x]for x in bits(eleven[0]))==eleven[1]for g in (maps[j:j+125]for j in range(0,len(maps),125)))
 assert same and cost==expected[i]['cost'] and delta==expected[i]['signed_difference']
 controls.append({'engine':engine,'counts':counts,'cost':cost,'signed_difference':delta,'eleven_same_affine_orbit':same,'class_count':len(groups),'elapsed_seconds':elapsed})
 print(json.dumps(controls[-1]),flush=True)
result={'positive_controls':controls}
if not a.controls_only:
 b=json.loads((here/'benchmark.json').read_text());args=[w/'obs',w/'parent',w/'B',w/'f4_52',label(b['P']),label(b['E']),b['floor'],b['ceiling'],b['first'],b['end'],b['q'],b['weightedE'],b['proper_weights']]
 bench=[]
 for engine in ['original','new']:
  counts,stdout,elapsed=run(engine,args);assert not stdout and counts==b[engine+'_counts'];bench.append({'engine':engine,'counts':counts,'elapsed_seconds':elapsed});print(json.dumps(bench[-1]),flush=True)
 result['benchmark']=bench
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
