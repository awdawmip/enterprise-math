function run(data){
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},canon=p=>{p=norm(p);return (p.find(x=>x)??0n)<0n?p.map(x=>-x):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()],neg=p=>p.map(x=>-x),axes=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]];
 const P=uniq(data.flatMap(e=>e.endpoints.map(p=>p.map(BigInt)))),idx=new Map(P.map((p,i)=>[p.join(),i]));
 function patterns(P,vertices=false){
  const S=new Map();
  function rec(r,t=null,p=null,s=1,u=1){
   let a=0n,b=0n;
   for(let i=0;i<P.length;i++){let x=sg(dot(r,P[i]));if(!x&&t)x=s*sg(dot(t,P[i]));if(!x&&p)x=u*sg(dot(p,P[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}
   if(a>b){[a,b]=[b,a];r=neg(r)}
   const key=`${a},${b}`;
   if(!S.has(key))S.set(key,{a,b,verts:new Map()});
   if(vertices){r=norm(r);S.get(key).verts.set(r.join(),r)}
  }
  for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,P[k],s,u)}}}
  return [...S.values()];
 }
 const pc32=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
 const count=x=>pc32(Number(x&0xffffffffn))+pc32(Number(x>>32n));
 function solver(pairs,vertices=false){
  const P=uniq(pairs.flat()),idx=new Map(P.map((p,i)=>[p.join(),i])),S=patterns(P,vertices);
  const Q=S.map(({a,b})=>{let au=0n,av=0n,bu=0n,bv=0n;pairs.forEach(([u,v],i)=>{let x=1n<<BigInt(idx.get(u.join())),y=1n<<BigInt(idx.get(v.join())),z=1n<<BigInt(i);if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});return [au,av,bu,bv]});
  const all=(1n<<BigInt(pairs.length))-1n,cache=new Map();
  function split(u,v,q){let [au,av,bu,bv]=q,pa=(u&au)|(v&av),pb=(u&bu)|(v&bv);return [u&~bu&pa,v&~bv&pa,u&~au&pb,v&~av&pb]}
  function feasible(u,v,d,k){let n=count(u|v);if(n>2**d-1)return false;if(k===0||n<=d)return true;let key=`${u},${v},${d},${k}`;if(cache.has(key))return cache.get(key);let ans=false;for(let q of Q){let [a,b,c,e]=split(u,v,q);if(count(a|b)>2**(d-1)-1||count(c|e)>2**(d-1)-1)continue;if(feasible(a,b,d-1,k-1)&&feasible(c,e,d-1,k-1)){ans=true;break}}cache.set(key,ans);return ans}
  return {P,S,Q,all,split,feasible}
 }
 const pairs=data.map(e=>e.endpoints.map(p=>p.map(BigInt))),old=solver(pairs,true);
 if(old.P.length!==51||old.S.length!==4249||old.P.some((p,i)=>p.join()!==P[i].join()))throw Error("old census mismatch");
 let roots=old.Q.map((q,i)=>({i,s:old.split(old.all,old.all,q)})).filter(({s:[a,b,c,d]})=>count(a|b)<=31&&count(c|d)<=31);
 let stages=[roots.length];
 for(let k=1;k<=5;k++){roots=roots.filter(({s:[a,b,c,d]})=>old.feasible(a,b,5,k)&&old.feasible(c,d,5,k));stages.push(roots.length)}
 if(stages.join()!=="611,537,486,401,393,393")throw Error("survivor mismatch");
 const comps=data.map(e=>({l:e.normal.map(BigInt),parts:e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]})).map(e=>({...e,parts:e.parts.map(pair=>pair.map(p=>p.map(BigInt)))}));
 for(let e of comps)for(let p of e.parts.flat())if(!idx.has(p.join())||dot(e.l,p))throw Error("component source");
 function clip(r,side,labels=false){
  let ret=[];
  for(let e of comps){let parts=[];
   for(let [u,v] of e.parts){let a=BigInt(side)*dot(r,u),b=BigInt(side)*dot(r,v);if(a<=0n&&b<=0n)continue;
    let d=(a<0n||b<0n)?norm(a<0n?u.map((x,j)=>b*x-a*v[j]):v.map((x,j)=>a*x-b*u[j])):null;
    let U=a<0n?{p:d,l:e.l}:{p:u,l:null},V=b<0n?{p:d,l:e.l}:{p:v,l:null};
    parts.push([U,V])
   }
   if(parts.length)ret.push([parts[0][0],parts.at(-1)[1]])
  }
  return ret
 }
 // Candidate event rays: only triples actually coexisting in a clipped child, including axes to span.
 const histogram={},byDim={},details=[];let totalLocal=0,totalGlobal=0;
 const staticRays=uniq(P.concat(axes)),globalEvents=new Map(staticRays.map(p=>[p.join(),p]));
 const den=p=>p.reduce((a,b)=>a+b,0n),cmp=(p,q,j)=>sg(p[j]*den(q)-q[j]*den(p));
 const inPart=(p,part)=>{if(!p.some(x=>x>0n)||p.some(x=>x<0n))return false;let [u,v]=part,j=[0,1,2].find(j=>cmp(u,v,j));return cmp(u,p,j)*cmp(p,v,j)>=0};
 for(let e of comps)for(let i=0;i<staticRays.length;i++)for(let j=i+1;j<staticRays.length;j++){let x=canon(cross(e.l,cross(staticRays[i],staticRays[j])));if(e.parts.some(part=>inPart(x,part)))globalEvents.set(x.join(),x)}
 let interiorBoth=0;
 for(let i=0;i<comps.length;i++)for(let j=i+1;j<comps.length;j++){let a=comps[i],b=comps[j],x=canon(cross(a.l,b.l));if(a.parts.some(p=>inPart(x,p))&&b.parts.some(p=>inPart(x,p))){globalEvents.set(x.join(),x);if(a.parts.some(p=>inPart(x,p)&&p.every(y=>y.join()!==x.join()))&&b.parts.some(p=>inPart(x,p)&&p.every(y=>y.join()!==x.join())))interiorBoth++}}
 if(globalEvents.size!==7702||interiorBoth!==0)throw Error("R180 event mismatch "+globalEvents.size+" "+interiorBoth);
 function rank(v){if(v.length===1)return 1;let h=v.find(p=>cross(v[0],p).some(Boolean));if(!h)return 1;let l=cross(v[0],h);return v.some(p=>dot(l,p))?3:2}
 function variable(x,vs){let pos=false,neg=false;for(let v of vs){let d=dot(x,v);pos ||= d>0n;neg ||= d<0n;if(pos&&neg)return true}return false}
 for(let {i} of roots){
  let c=old.S[i],vs=[...c.verts.values()],r=norm(vs.reduce((a,b)=>a.map((x,j)=>x+b[j]),[0n,0n,0n]));
  let a=0n,b=0n;P.forEach((p,j)=>{let d=dot(r,p);if(d>0n)a|=1n<<BigInt(j);if(d<0n)b|=1n<<BigInt(j)});
  if(a!==c.a||b!==c.b)throw Error("representative mismatch");
  let dim=rank(vs),events=new Map(),globalCount=0;
  for(let x of globalEvents.values())if(variable(x,vs))globalCount++;
  for(let side of [1,-1]){
   let flat=clip(r,side).flat(),stat=uniq(flat.filter(x=>!x.l).map(x=>x.p).concat(axes)),dyn=uniq(flat.filter(x=>x.l).map(x=>x.l));
   for(let l of dyn)for(let j=0;j<stat.length;j++)for(let k=j+1;k<stat.length;k++){let x=canon(cross(l,cross(stat[j],stat[k])));if(x.some(Boolean)&&variable(x,vs)){if(!globalEvents.has(x.join()))throw Error("missing global event");events.set(x.join(),x)}}
  }
  let n=events.size;totalLocal+=n;totalGlobal+=globalCount;histogram[n]=(histogram[n]??0)+1;byDim[dim]??={classes:0,zero:0,global:0,local:0};byDim[dim].classes++;byDim[dim].zero+=+(n===0);byDim[dim].global+=globalCount;byDim[dim].local+=n;
  details.push({i,dim,vertices:vs.length,r:r.map(String),a:String(c.a),b:String(c.b),global:globalCount,local:n,events:[...events.keys()]});
 }
 // The zero-event classes are uniform. Evaluate their exact first-clipped endpoint relaxation.
 let zero=details.filter(x=>!x.local),excluded=[],survived=[];
 for(let c of zero){
  let r=c.r.map(BigInt),ok=true;
  for(let side of [1,-1]){let pp=clip(r,side).map(p=>p.map(x=>x.p));if(pp.length>31){ok=false;break}let sl=solver(pp);if(!sl.feasible(sl.all,sl.all,5,5)){ok=false;break}}
  (ok?survived:excluded).push(c.i)
 }
 return {stages,globalEvents:globalEvents.size,interiorBoth,byDim,histogram,totalGlobal,totalLocal,maxLocal:Math.max(...details.map(c=>c.local)),maxGlobal:Math.max(...details.map(c=>c.global)),zero:zero.length,excluded,survived,details};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(run(data),null,2));
