"use strict";
// Author-side reproducible R762FP exact finite-state verification; Node.js >= 18.
const verify = function verify(){
 const fact=n=>{let v=1;for(let j=2;j<=n;j++)v*=j;return v};
 const perms=n=>{let o=[];function r(a,b){if(!b.length){o.push(a);return}b.forEach((x,i)=>r([...a,x],b.filter((_,j)=>j!==i)))}r([],Array.from({length:n},(_,j)=>j));return o};
 const key=s=>s.map(p=>p.join(":")).join("|");
 const histories=k=>{const p=perms(k),o=[];for(const u of p)for(const v of p)o.push(u.map((x,i)=>[x,v[i]]));return o};
 const edges=(k,m)=>{let o=[],b=0;for(let i=0;i<k;i++)for(let j=i+1;j<k;j++,b++)if(m&(1<<b))o.push([i,j]);return o};
 const radius=(k,es,a,h)=>{let d=Array(k).fill(Infinity),queue=[a];d[a]=0;for(let j=0;j<queue.length;j++)for(const [u,v] of es){let x=u===queue[j]?v:v===queue[j]?u:-1;if(x>=0&&d[x]===Infinity){d[x]=d[queue[j]]+1;queue.push(x)}}return d.filter(x=>x<=h).length};
 function levels(states,es,a,H){const lookup=new Map(states.map(s=>[key(s),s]));let labels=new Map(states.map(s=>[key(s),s[a].join(":")])),out=[];
  for(let h=0;h<=H;h++){let counts=new Map();for(let label of labels.values())counts.set(label,(counts.get(label)||0)+1);
   out.push({classes:counts.size,fibers:[...counts.values()].sort((x,y)=>x-y),labels});
   if(h<H){let next=new Map();for(const s of states){let parts=[s[a].join(":")];for(const [u,v] of es){let t=s.slice();[t[u],t[v]]=[t[v],t[u]];let n=lookup.get(key(t));parts.push(n?labels.get(key(n)):"BLOCK")}next.set(key(s),JSON.stringify(parts))}labels=next}
  }return out}
 let graphCases=0,historyCases=0,partialCases=0,directPairs=0;
 for(let k=1;k<=4;k++)for(let m=0;m<2**(k*(k-1)/2);m++){const es=edges(k,m),s=histories(k);
  for(let a=0;a<k;a++){let ls=levels(s,es,a,k-1);ls.forEach((v,h)=>{let r=radius(k,es,a,h),p=fact(k-r);if(v.classes!==(fact(k)/p)**2||v.fibers.some(x=>x!==p*p))throw Error("unrestricted regression "+[k,m,a,h]);graphCases++;historyCases+=s.length})}
 }
 const allow=new Set(["0:0:0","1:1:1","1:2:2","1:1:2","2:2:2","2:1:1","2:2:1"]);
 const witness=histories(3).filter(s=>s.every((p,i)=>allow.has(`${i}:${p[0]}:${p[1]}`)));
 const wl=levels(witness,[[1,2]],0,3);
 if(witness.length!==3||JSON.stringify(wl.map(v=>[v.classes,v.fibers]))!==JSON.stringify([[1,[3]],[2,[1,2]],[2,[1,2]],[2,[1,2]]]))throw Error("witness mismatch");
 let seed=71437;const rnd=()=>seed=(Math.imul(seed,1664525)+1013904223)>>>0;
 for(let sample=0;sample<12;sample++){const legal=new Set(["0:0:0","1:1:1","2:2:2"]);for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let l=0;l<3;l++)if((rnd()>>>29)&1)legal.add(`${i}:${j}:${l}`);
  const states=histories(3).filter(s=>s.every((p,i)=>legal.has(`${i}:${p[0]}:${p[1]}`))),lookup=new Map(states.map(s=>[key(s),s]));
  for(let m=0;m<8;m++)for(let a=0;a<3;a++){const es=edges(3,m),ls=levels(states,es,a,3),words=[[]];
   for(let h=0;h<=3;h++){if(h)words.push(...words.filter(w=>w.length===h-1).flatMap(w=>es.map((_,i)=>[...w,i])));
    const direct=new Map();for(const s of states){const values=[];for(const w of words){let t=s,blocked=false;for(const i of w){const [u,v]=es[i],z=t.slice();[z[u],z[v]]=[z[v],z[u]];t=lookup.get(key(z));if(!t){blocked=true;break}}values.push(blocked?"BLOCK":t[a].join(":"))}direct.set(key(s),JSON.stringify(values))}
    for(let i=0;i<states.length;i++)for(let j=i+1;j<states.length;j++){const x=key(states[i]),y=key(states[j]);if((ls[h].labels.get(x)===ls[h].labels.get(y))!==(direct.get(x)===direct.get(y)))throw Error("direct word mismatch "+[sample,m,a,h]);directPairs++}
    partialCases++
   }
  }
 }
 return {schema:"R762FP_PARTIAL_TRIAD_OBSERVER_V1",status:"PASS",exact_regression:{unrestricted_all_simple_graphs_k:"1..4",graph_root_horizon_cases:graphCases,history_signature_checks:historyCases,comparison:"R762FO sharp class counts and uniform fibers"},partial_legality:{sampled_hyperedge_tensors:12,k:3,graph_root_horizon_cases:partialCases,independent_known_word_pair_comparisons:directPairs,max_horizon:3},counterexample:{k:3,legal_histories:witness.map(s=>s.map(p=>p.map(x=>x+1))),root:"A1",graph_edge:"A2--A3",horizon_classes:wl.map(x=>x.classes),horizon_fibers:wl.map(x=>x.fibers),result:"remote edge enable/disable distinguishes hidden histories from h=1"},review:"AUTHOR_SIDE_EXACT_ENUMERATION; NOT_REVIEWED"};
};
process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
