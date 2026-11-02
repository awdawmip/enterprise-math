"""Multi-alias invalidation and typed namespace examples, original kernel only."""
from pathlib import Path
import json
import check_multitarget as c
C=c.Compiler(slots=6)
# Five references point to A; the sixth points to disjoint C. They all use
# local color zero, but the last is in the other target namespace.
table=((0,None,0),((0,0),)*5+((2,0),))
J=C.encode(table)
K,_,log=C.run(J,('release',1),True)
actual,bit=C.decode(K)
c.ck(actual==((None,None,0),table[1]) and bit,'One source release removes exactly one current row and preserves all reference records')
responses=[]
for i in range(6):
 K,_,_=C.run(K,('valid',i));tab,bit=C.decode(K)
 c.ck(bit==(i==5),'All aliases of removed A stale, C reference still valid')
 responses.append(bit)
K,_,_=C.run(K,('same',0,1));_,same=c.Compiler.decode(C,K)
c.ck(same,'Stale A aliases retain common origin')
K,_,_=C.run(K,('same',0,5));_,distinct=C.decode(K)
c.ck(not distinct,'Equal color does not merge distinct targets')
out=dict(mode='examples',checks=c.CHECKS,release_commands=len(C.programs[('release',1)]),validity=responses,
         stale_aliases_same=same,cross_target_same=distinct,initial_table=table,after_release=actual,
         release_trace=log,**C.stats())
Path(__file__).with_name('examples.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print({k:v for k,v in out.items() if k in ('checks','release_commands','validity','members','kernel_calls','command_uses')})
