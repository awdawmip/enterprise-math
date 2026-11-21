import json
from pathlib import Path
here=Path(__file__).resolve().parent;work=here/'work';work=work if (work/'linear').exists() else here/'inputs';FULL=(1<<125)-1
frames=set()
for l in (work/'cores2.txt').read_text().splitlines():
 lo,hi,*centres=map(int,l.split());m=lo+(hi<<64)
 for c in centres:
  if m>>c&1:frames.add(m^(1<<c))
frames=sorted(frames);holes=[FULL^m for m in frames];lookup={m:i for i,m in enumerate(holes)}
linear=[list(map(int,l.split())) for l in (work/'linear').read_text().splitlines()]
covered=set();orbits=[]
for fi,h in enumerate(holes):
 if fi in covered:continue
 p=[i for i in range(125) if h>>i&1];images={}
 for li,a in enumerate(linear):
  for d in range(125):
   tr=[25*((a[i]//25+d//25)%5)+5*((a[i]//5%5+d//5%5)%5)+(a[i]%5+d%5)%5 for i in p]
   z=sum(1<<i for i in tr)
   if z in lookup:images[lookup[z]]={'linear_row':li,'translation':d}
 covered.update(images);orbits.append({'representative':fi,'members':images})
result={'free_masks':list(map(str,frames)),'orbits':orbits}
(here/'mixed_frame_orbits.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
