'use strict';
// Independent finite certificate checker, no packages or floating point.
const axes=[0,1,2,3,4,5];
function choose(a,k){if(k===0)return [[]];if(a.length<k)return [];return [...choose(a.slice(1),k-1).map(t=>[a[0],...t]),...choose(a.slice(1),k)];}
const ports=choose(axes,2).map(a=>a.join(''));
const supports=choose(axes,3).map(a=>a.join(''));
const prototypes={
  0:[2,1,0,2,2,0,2,0,2,0,0,0,1,0,1,2,2,1,1,0],
  1:[2,2,2,2,2,2,0,1,0,2,2,2,0,2,2,0,0,0,0,2],
  2:[2,2,2,2,0,1,1,0,1,2,0,0,1,1,1,2,2,2,2,2],
  3:[2,2,2,2,0,2,2,0,0,0,0,2,2,0,0,0,2,2,0,0]
};
const standards={0:[],1:['01'],2:['01','23'],3:['01','23','45']};
const choices=[[0,1],[0,2],[1,2]];
function entries(choice){
  return supports.map((s,i)=>{
    const [a,b,c]=s.split(''); const tri=[a+b,a+c,b+c];
    return [s,tri[choices[choice[i]][0]],tri[choices[choice[i]][1]]];
  });
}
function verify(es,omitted){
  if(es.length!==20)throw Error('not one edge per support');
  const counts=new Map(), degrees=new Map(ports.map(p=>[p,0]));
  const adj=new Map(ports.map(p=>[p,new Set()]));
  for(const [s,a,b] of es){
    if(!supports.includes(s)||!ports.includes(a)||!ports.includes(b)||a===b)throw Error('invalid indices');
    const tri=choose(s.split(''),2).map(x=>x.join(''));
    if(!tri.includes(a)||!tri.includes(b))throw Error('edge outside support');
    counts.set(s,(counts.get(s)||0)+1);
    degrees.set(a,degrees.get(a)+1);degrees.set(b,degrees.get(b)+1);
    adj.get(a).add(b);adj.get(b).add(a);
  }
  if(supports.some(s=>counts.get(s)!==1))throw Error('not all supports exactly once');
  const missing=[...degrees].filter(([p,d])=>d===0).map(([p])=>p);
  if(missing.join(',')!==omitted.slice().sort().join(','))throw Error('incorrect active ports');
  if([...degrees.values()].some(d=>d%2))throw Error('non-even port degree');
  const active=ports.filter(p=>degrees.get(p)>0), seen=new Set([active[0]]), stack=[active[0]];
  while(stack.length){const v=stack.pop();for(const w of adj.get(v))if(!seen.has(w)){seen.add(w);stack.push(w);}}
  if(seen.size!==active.length)throw Error('disconnected Port graph');
  return {active_ports:active.length,degree_sequence:active.map(p=>degrees.get(p)).sort((a,b)=>a-b)};
}
function permutations(a){if(!a.length)return [[]];return a.flatMap((x,i)=>permutations([...a.slice(0,i),...a.slice(i+1)]).map(p=>[x,...p]));}
function renumber(s,p){return s.split('').map(c=>p[Number(c)]).sort((a,b)=>a-b).join('');}
const seen=new Map(),checks={prototypes:0,permutation_witnesses:0,distinct_matchings:0,matching_count_by_size:[0,0,0,0]};
let example14=null, example60=null;
for(let k=0;k<=3;k++){
  const original=entries(prototypes[k]);
  verify(original,standards[k]);checks.prototypes++;
  if(k===1){
    example14=original;
    // Every support occurs three times, all on the witness edge.
    const triple=original.flatMap(e=>[e,e,e]);
    const deg=new Map(ports.map(p=>[p,0])),adj=new Map(ports.map(p=>[p,new Set()]));
    for(const [s,a,b] of triple){deg.set(a,deg.get(a)+1);deg.set(b,deg.get(b)+1);adj.get(a).add(b);adj.get(b).add(a);}
    if(triple.length!==60||deg.get('01')!==0||ports.some(p=>deg.get(p)%2))throw Error('60-edge omission counterexample failed');
    const seen14=new Set(['02']),q=['02'];while(q.length){let v=q.pop();for(let w of adj.get(v))if(!seen14.has(w)){seen14.add(w);q.push(w);}}
    if(seen14.size!==14)throw Error('omission example disconnected');
    example60={total_events:60,inactive_port:'01',all_support_multiplicities:3,active_ports:14};
  }
  for(const perm of permutations(axes)){
    const transported=original.map(([s,a,b])=>[renumber(s,perm),renumber(a,perm),renumber(b,perm)]).sort((x,y)=>x[0].localeCompare(y[0]));
    const missing=standards[k].map(s=>renumber(s,perm)).sort();
    verify(transported,missing);
    const key=missing.join(',');
    seen.set(key,{k,missing});
    checks.permutation_witnesses++;
  }
}
checks.distinct_matchings=seen.size;
for(const o of seen.values())checks.matching_count_by_size[o.k]++;
if(checks.prototypes!==4||checks.permutation_witnesses!==2880||checks.distinct_matchings!==76||checks.matching_count_by_size.join(',')!=='1,15,45,15')throw Error('incomplete S6 coverage');
const result={schema:'R762IN_FULL_ODD_SUPPORT_SHARP_20_V1',status:'PASS',frozen_science:'a72226e2430ffa4786321ac86e7f0c599d5f0389',model:'15 pair-Ports, 20 triple supports, one of three Port edges per support',claim:'Every positive odd support histogram admits a 20-event legal Euler witness with the same active Port set as any legal original; 20 is minimum for support presence.',completeness:'All inactive Port sets must be matchings in K6; all 76 matchings are verified via S6 translations of 4 exact integer certificates.',checks,example60,example14};
console.log(JSON.stringify(result,null,2));
