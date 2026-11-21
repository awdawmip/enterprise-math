"""Replay bank and exact eleven-label equality controls against native observations."""
from pathlib import Path
from collections import defaultdict
import argparse,hashlib,json,struct,subprocess,time
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();h=Path(__file__).resolve().parent;w=a.work.resolve();out=a.output.resolve();out.mkdir(parents=True,exist_ok=True);cat=defaultdict(dict)
for line in(h/'typed_catalog.txt').read_text().splitlines()[1:]:
 s,e,c,d=map(int,line.split());cat[s,e][c]=d
engines={}
for name,source in [('original',h/'original_weighted_native.cpp'),('active',h/'search.cpp')]:
 exe=out/name;subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(source),'-o',str(exe)],check=True);engines[name]=(exe,source)
raw=(w/'obs').read_bytes();assert hashlib.sha256(raw).hexdigest()=='6ca43dd4301613d9d49d376680cd1d6bf7d53c1751cf42b835b0f69624fdbce9';obs=list(struct.iter_unpack('<QQQQ',raw[:500000]));triples=[tuple(raw[i:i+3])for i in range(500000,len(raw),3)];parents=[]
for line in(w/'parent').read_text().splitlines()[:250]:
 lo,hi=map(int,line.split());parents.append(lo+(hi<<64))
def bits(m):
 while m:
  b=m&-m;m-=b;yield b.bit_length()-1
records=[]
for case,P,E,mothers,q,floor,budget,lower in [('bank',[2]*45+[11,11],[13],[0],2,1296,6046,0),('equality',[10]*6,[13]*5,[11,141,206,86,197],2,6480,11292,11292)]:
 frame=out/(case+'_frame.txt');frame.write_text(' '.join(map(str,mothers))+'\n');weights=','.join(str(min((q*c-d for c,d in cat[s,0].items()),default=999999))for s in range(14));weighted=q*floor
 args=[str(w/'obs'),str(w/'parent'),str(w/'B'),str(frame),','.join(map(str,P)),','.join(map(str,E)),str(floor),str(budget),'0','1',str(q),str(weighted),weights,str(w/'maps')]
 for name,(exe,source)in engines.items():
  command=[str(exe),*args]
  if name=='active':command += [str(h/'typed_catalog.txt'),str(lower)]
  st=time.time();run=subprocess.run(command,capture_output=True,text=True,check=True);counts=list(map(int,run.stderr.split()));assert counts[-1]==1;tokens=run.stdout.split();assert tokens[:2]==['hit','1'];groups=[int(x)+(int(y)<<64)for x,y in(token.split(':')for token in tokens[2:])];assert sorted(m.bit_count()for m in groups)==P+E
  union=0;total=delta=0
  for mask in groups:
   assert not union&mask;union|=mask;points=list(bits(mask));assert all(not all(mask>>v&1 for v in t)for t in triples)
   if mask.bit_count()!=13:assert all(mask&~mother for mother in parents)
   for x in points:
    row=[0]*4
    for y in points:
     for z,value in enumerate(obs[125*x+y]):row[z]|=value
    total+=sum(value.bit_count()for value in row);delta+=row[0].bit_count()+(row[1]&((1<<61)-1)).bit_count()-(row[1]>>61).bit_count()-row[2].bit_count()-row[3].bit_count()
  assert union==(1<<125)-1 and lower<=total<=budget and abs(delta)>=108+q*(total-11292)
  if case=='equality':assert total==11292 and abs(delta)==108 and len(groups)==11
  records.append({'case':case,'engine':name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'q':q,'counts':counts,'C':total,'delta':delta,'I':(total+delta)//2,'D':(total-delta)//2,'groups':[list(bits(m))for m in groups],'native_audit_passed':True,'elapsed_seconds':time.time()-st});print(json.dumps({k:v for k,v in records[-1].items()if k!='groups'}),flush=True)
(out/'positive_controls.json').write_text(json.dumps(records,indent=2)+'\n')
