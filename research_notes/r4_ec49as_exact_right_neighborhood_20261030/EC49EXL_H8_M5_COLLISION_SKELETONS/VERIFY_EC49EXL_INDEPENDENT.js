// EC49EXL: independent algebraic-key and Hall-subset verifier; Node.js, no deps
'use strict';
const H=Array.from({length:7},(_,i)=>i+2),sets={};
for(const h of H){
  sets[h]={ANY:new Set(),T2:new Set(),T4:new Set()};
  for(let u=0;u<=2*h+2;u++)for(let v=0;v<=h+1;v++)for(let w=1;w<=Math.floor((h+1)/2);w++){
    const r=u+v-h-1,a=w-1,f=h+1-v-2*w,g=h+1-u;
    if([r,a,f,g].some(t=>t<0))continue;
    const key=[u,v,w].join(',');
    if(r>=1){sets[h].T4.add(key);sets[h].ANY.add(key);}
    else if(f>=1&&g>=1){sets[h].T2.add(key);sets[h].ANY.add(key);}
  }
}
const ps=[];
function partitions(seq,n){
  if(seq.length===7){if(n===5)ps.push(seq);return;}
  for(let x=0;x<=n&&x<5;x++)partitions(seq.concat([x]),Math.max(n,x+1));
}
partitions([0],1);
function feasible(p,types){
  const groups=Array.from({length:5},()=>null);
  for(let i=0;i<7;i++){
    const options=sets[H[i]][types[i]];
    if(groups[p[i]]===null)groups[p[i]]=new Set(options);
    else groups[p[i]]=new Set([...groups[p[i]]].filter(k=>options.has(k)));
  }
  // Hall's theorem: distinct reps iff every nonempty subset has >= its size in union
  for(let mask=1;mask<32;mask++){
    const union=new Set();let size=0;
    for(let i=0;i<5;i++)if(mask&(1<<i)){size++;for(const k of groups[i])union.add(k);}
    if(union.size<size)return false;
  }
  return true;
}
const xs=ps.filter(p=>feasible(p,Array(7).fill('ANY')));
const triples=xs.filter(p=>Object.values(p.reduce((acc,t)=>(acc[t]=(acc[t]||0)+1,acc),{})).includes(3)).length;
const excluded_profiles=[];
for(let mask=0;mask<64;mask++){
  const ts=['T4',...Array.from({length:6},(_,i)=>mask&(1<<i)?'T4':'T2')];
  if(!ps.some(p=>feasible(p,ts)))excluded_profiles.push(ts);
}
const result={status:'PASS',partitions:ps.length,realizable:xs.length,excluded:ps.length-xs.length,
  two_pairs:xs.length-triples,one_triple:triples,feasible_profiles:64-excluded_profiles.length,
  excluded_profiles,rank9_keys:Object.fromEntries(H.map(h=>[h,sets[h].ANY.size]))};
if(JSON.stringify([result.partitions,result.realizable,result.one_triple,result.feasible_profiles])!=='[140,40,8,60]')throw Error(JSON.stringify(result));
process.stdout.write(JSON.stringify(result,null,2)+'\n');
