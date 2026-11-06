#!/usr/bin/env node
'use strict';
// PREFIX546 exact BRC–gate symbolic certificate; frozen scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
function run(maxDepth=16){
 const stars=[[1,3,6],[1,4,5],[2,3,5],[2,4,6]];
 const near=(a,c)=>stars[a].filter(k=>k!==Math.abs(c)).map(k=>(c>0?-1:1)*k);
 const P=[];for(let a=0;a<4;a++)for(const k of stars[a])for(const s of [-1,1])for(const p of near(a,s*k))P.push([a,p,s*k]);
 const idx=Object.fromEntries(P.map((x,i)=>[x.join(","),i]));
 const N=P.map(([a,p,c])=>{const b=stars.findIndex((v,j)=>j!==a&&v.includes(Math.abs(c)));return [...near(a,c).filter(x=>x!==p).map(x=>[a,c,x]),...near(b,c).map(x=>[b,c,x])].map(x=>idx[x.join(",")])});
 const target=idx[[0,1,-3].join(",")];
 if(P.length!==48||N.some(x=>x.length!==3)||N[target].includes(target))throw Error("frozen model mismatch");
 const sign=i=>Math.abs(P[i][2])===1?Math.sign(P[i][2]):0;
 const tau=(r,i,j)=>{const x=Math.abs(sign(i))+Math.abs(sign(j))-Math.abs(sign(j)-r)+Math.abs(sign(i)-r);if(x%2||x<0||x>2)throw Error("bad BRC cocycle");return x/2};
 const edge=(r,v,a)=>{const i=v>>1,b=v&1,j=N[i][a>>1],c=a&1;return [2*j+c,tau(r,i,j),Number(b===1&&c===1&&j===target)]};
 const fpstr=m=>[...m].sort((a,b)=>a[0].localeCompare(b[0])).map(([k,n])=>k+"="+n).join(";");
 const peq=(a,b)=>a.size===b.size&&[...a].every(([k,n])=>b.get(k)===n);
 const step=(r,F)=>Array.from({length:96},(_,v)=>{const out=new Map();for(let a=0;a<6;a++){const [w,p,h]=edge(r,v,a);for(const [k,n] of F[w]){const [x,y]=k.split(",").map(Number),kk=[p+x,h+y].join(",");out.set(kk,(out.get(kk)||0n)+n)}}return out});
 function quotient(r){
  let F=Array.from({length:96},()=>new Map([["0,0",1n]])),fp=Array.from({length:96},()=>[]),growth=[];
  for(let d=0;d<=5;d++){for(let v=0;v<96;v++)fp[v].push(fpstr(F[v]));growth.push(new Set(fp.map(x=>x.join("|"))).size);if(d<5)F=step(r,F)}
  const ids=new Map(),cls=fp.map(x=>{const k=x.join("|");if(!ids.has(k))ids.set(k,ids.size);return ids.get(k)});
  if(ids.size!==28)throw Error("bad quotient size");
  const Q=new Map();
  for(let v=0;v<96;v++){const row=new Map();for(let a=0;a<6;a++){const [w,p,h]=edge(r,v,a),k=[cls[w],p,h].join(",");row.set(k,(row.get(k)||0)+1)}const old=Q.get(cls[v]);if(old&&(old.size!==row.size||[...row].some(([k,n])=>old.get(k)!==n)))throw Error("row incompatibility");Q.set(cls[v],row)}
  if(Q.size!==28||[...Q.values()].reduce((x,y)=>x+y.size,0)!==73)throw Error("entry count");
  return {cls,Q,growth};
 }
 const all=Object.fromEntries([-1,0,1].map(r=>[r,quotient(r)])),cl=all[0].cls,signs=Array(28).fill(null),sizes=Array(28).fill(0);
 let partitions=0;
 for(let v=0;v<96;v++){const c=cl[v],s=sign(v>>1);if(signs[c]!==null&&signs[c]!==s)throw Error("sign mixed");signs[c]=s;sizes[c]++;for(let r of [-1,1]){if(all[r].cls[v]!==c)throw Error("partition mismatch");partitions++;}}
 const pot=(r,s)=>r===0?0:s===r?-1:0;
 let portChecks=0,quotChecks=0;
 for(let r of [-1,1]){
  for(let v=0;v<96;v++)for(let a=0;a<6;a++){const [w,p,h]=edge(r,v,a),[w0,p0,h0]=edge(0,v,a);if(w!==w0||h!==h0||p-p0!==pot(r,sign(v>>1))-pot(r,sign(w>>1)))throw Error("port gauge failed");portChecks++}
  for(let [c,row] of all[0].Q){const shift=new Map();for(let [k,n] of row){let [d,p,h]=k.split(",").map(Number),kk=[d,p+pot(r,signs[c])-pot(r,signs[d]),h].join(",");shift.set(kk,(shift.get(kk)||0)+n)}const actual=all[r].Q.get(c);if(actual.size!==shift.size||[...shift].some(([k,n])=>actual.get(k)!==n))throw Error("quot gauge failed");quotChecks++}
 }
 let F=Object.fromEntries([-1,0,1].map(r=>[r,Array.from({length:96},()=>new Map([["0,0",1n]]))]));
 let Y=Object.fromEntries([-1,0,1].map(r=>[r,Array.from({length:28},(_,c)=>new Map([[pot(r,signs[c])===-1?"1,0":"0,0",1n]]))]));
 let polynomialChecks=0;
 for(let d=0;d<=maxDepth;d++){
  for(const r of [-1,0,1])for(let v=0;v<96;v++){const got=new Map();for(let [k,n] of Y[r][cl[v]]){const [p,h]=k.split(",").map(Number),ex=p+pot(r,signs[cl[v]]);if(ex<0)throw Error("negative q exponent");got.set(ex+","+h,n)}if(!peq(F[r][v],got))throw Error("polynomial disagreement "+[r,d,v]);polynomialChecks++}
  if(d===maxDepth)break;
  for(const r of [-1,0,1]){F[r]=step(r,F[r]);Y[r]=Array.from({length:28},(_,c)=>{const z=new Map();for(let [k,m] of all[0].Q.get(c)){const [j,p,h]=k.split(",").map(Number);for(let [xy,n] of Y[r][j]){const [x,y]=xy.split(",").map(Number),kk=[p+x,h+y].join(",");z.set(kk,(z.get(kk)||0n)+BigInt(m)*n)}}return z})}
 }
 const histogram={};for(const s of sizes)histogram[s]=(histogram[s]||0)+1;
 const signClassCounts={};for(const s of signs)signClassCounts[s]=(signClassCounts[s]||0)+1;
 return {result:"ALL_CHECKS_PASS",scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",phase_states:48,port_states:96,directed_phase_edges:144,quotient_classes:28,quotient_class_size_multiset:histogram,quotient_class_sign_counts:signClassCounts,scalar_fingerprint_growth_by_root:Object.fromEntries([-1,0,1].map(r=>[r,all[r].growth])),identical_partition_checks:partitions,exact_port_gauge_edge_checks:portChecks,exact_quotient_gauge_row_checks:quotChecks,exact_all_port_polynomial_checks:polynomialChecks,checked_depths:[0,maxDepth],arithmetic:"exact BigInt integer coefficient polynomials"};
}
if (typeof module !== 'undefined' && require.main === module) console.log(JSON.stringify(run(Number(process.argv[2] || 16)),null,2));
