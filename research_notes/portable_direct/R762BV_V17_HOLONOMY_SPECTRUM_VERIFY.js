"use strict";
// R762BV author-side exact integer certificate, Node.js >= 18; no dependencies.
// Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389.
// Checks finite polynomial annihilators by every standard basis vector, no floating eigenvalue reliance.
const runCertificate = function runCertificate(){
 const assert=(ok,msg)=>{if(!ok)throw new Error(msg)};
 const perm3=[];for(let a=1;a<=6;a++)for(let b=1;b<=6;b++)if(b!==a)for(let c=1;c<=6;c++)if(c!==a&&c!==b)perm3.push([a,b,c]);
 const frameKey=a=>a.join(",");
 const idx=new Map(perm3.map((p,i)=>[frameKey(p),i]));
 const N=perm3.length;assert(N===120,"120 frame states");
 const adj=perm3.map(p=>{const out=[];for(let j=0;j<3;j++)for(let y=1;y<=6;y++)if(!p.includes(y)){const q=p.slice();q[j]=y;out.push(idx.get(frameKey(q)))}return out});
 assert(adj.every(x=>x.length===9),"nine moves");
 for(let a=0;a<N;a++)for(const b of adj[a])assert(adj[b].includes(a),"symmetric");
 const multiply=(v,nb,weight)=>{const r=Array(v.length).fill(0n);for(let i=0;i<v.length;i++)if(v[i]!==0n)for(let k=0;k<nb[i].length;k++)r[nb[i][k]]+=v[i]*BigInt(weight?weight[i][k]:1);return r};
 const pcoef=roots=>{let c=[1n];for(const root of roots){const n=Array(c.length+1).fill(0n);for(let i=0;i<c.length;i++){n[i]-=BigInt(root)*c[i];n[i+1]+=c[i]}c=n}return c};
 const checkAnnihilation=(nb,weight,roots)=>{const coeff=pcoef(roots),n=nb.length;const traces=Array(coeff.length-1).fill(0n);for(let b=0;b<n;b++){let v=Array(n).fill(0n);v[b]=1n;const acc=Array(n).fill(0n);for(let d=0;d<coeff.length;d++){for(let i=0;i<n;i++)acc[i]+=coeff[d]*v[i];if(d<traces.length)traces[d]+=v[b];if(d+1<coeff.length)v=multiply(v,nb,weight)}assert(acc.every(x=>x===0n),"annihilator failed at "+b)}return {coeff,traces}};
 const arr=checkAnnihilation(adj,null,[9,6,3,2,-1,0,-3]);
 const rootA=[9,6,3,2,-1,0,-3],multA=[1,10,15,18,9,20,47];
 for(let k=0;k<7;k++)assert(arr.traces[k]===rootA.reduce((s,x,i)=>s+BigInt(multA[i])*BigInt(x)**BigInt(k),0n),"A trace "+k);
 const triads=[];for(let a=1;a<=6;a++)for(let b=a+1;b<=6;b++)for(let c=b+1;c<=6;c++)triads.push([a,b,c]);
 const tIdx=new Map(triads.map((s,i)=>[frameKey(s),i]));
 const jnb=triads.map(s=>[]),jsign=triads.map(s=>[]);
 for(let i=0;i<20;i++){let s=triads[i];for(let slot=0;slot<3;slot++)for(let y=1;y<=6;y++)if(!s.includes(y)){
  const transported=s.slice();transported[slot]=y;let t=transported.slice().sort((a,b)=>a-b);
  const inv=Number(transported[0]>transported[1])+Number(transported[0]>transported[2])+Number(transported[1]>transported[2]);
  jnb[i].push(tIdx.get(frameKey(t)));jsign[i].push(inv%2?-1:1);
 }}
 assert(jnb.every(x=>x.length===9),"J degree");
 const jpol=checkAnnihilation(jnb,null,[9,3,-1,-3]);
 const rootJ=[9,3,-1,-3],multJ=[1,5,9,5];
 for(let k=0;k<4;k++)assert(jpol.traces[k]===rootJ.reduce((s,x,i)=>s+BigInt(multJ[i])*BigInt(x)**BigInt(k),0n),"J trace "+k);
 const kpol=checkAnnihilation(jnb,jsign,[3,-3]);
 assert(kpol.traces[0]===20n && kpol.traces[1]===0n,"K trace");
 const base=idx.get("1,2,3");
 const atBase=perm3.map((f,i)=>f.slice().sort((a,b)=>a-b).join(",")==="1,2,3"?i:-1).filter(i=>i>=0);
 assert(atBase.length===6,"base S3");
 const parity=p=>{let z=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(p[i]>p[j])z++;return z%2};
 let v=Array(N).fill(0n);v[base]=1n;const counts=[];
 for(let m=0;m<=12;m++){
  const byFrame=atBase.map(i=>v[i]),C=byFrame.reduce((a,b)=>a+b,0n);
  const E=atBase.reduce((sum,i)=>sum+(parity(perm3[i])===0?v[i]:0n),0n);
  const Odd=C-E;const F=v[base];
  const Ci=(9n**BigInt(m)+5n*3n**BigInt(m)+9n*((-1n)**BigInt(m))+5n*((-3n)**BigInt(m)))/20n;
  const Fi=(9n**BigInt(m)+10n*6n**BigInt(m)+15n*3n**BigInt(m)+18n*2n**BigInt(m)+9n*((-1n)**BigInt(m))+47n*((-3n)**BigInt(m))+(m===0?20n:0n))/120n;
  const Si=(3n**BigInt(m)+(-3n)**BigInt(m))/2n;
  assert(C===Ci&&F===Fi&&E-Odd===Si,"closed form m="+m);
  const t=(C-Si)/6n,cycle=(C+Si-2n*F)/4n;
  assert(atBase.filter(i=>parity(perm3[i])===1).every(i=>v[i]===t),"transpositions match");
  assert(atBase.filter(i=>parity(perm3[i])===0 && i!==base).every(i=>v[i]===cycle),"cycles match");
  counts.push({m,base_triads:C.toString(),identity:F.toString(),each_transposition:t.toString(),each_3cycle:cycle.toString(),sign_sum:Si.toString()});
  v=multiply(v,adj,null)
 }
 assert(counts[3].identity==="18" && counts[3].each_transposition==="6" && counts[3].each_3cycle==="0","m3");
 assert(counts[4].identity==="207" && counts[4].each_transposition==="48" && counts[4].each_3cycle==="9","m4");
 let flat=0,odd=0,cycle3=0;
 for(const i1 of adj[base])for(const i2 of adj[i1])for(const i3 of adj[i2])if(atBase.includes(i3)){
  if(i3===base)flat++;else if(parity(perm3[i3]))odd++;else cycle3++;
 }
 assert(flat===18&&odd===18&&cycle3===0,"independent direct triangle census");
 const w=[[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3]];
 let f=[1,2,3];for(let k=1;k<w.length;k++){const choices=adj[idx.get(frameKey(f))];const target=frameKey(w[k]);const opt=choices.filter(j=>frameKey(perm3[j].slice().sort((a,b)=>a-b))===target);assert(opt.length===1,"unique frame transport");f=perm3[opt[0]]}
 assert(frameKey(f)==="2,3,1","4 loop 3cycle witness");
 return {schema:"R762BV_V17_HOLONOMY_SPECTRUM_V1",validation:"EXACT_INTEGER",vertices:{ordered_frames:120,triads:20,branching_per_state:9},arrangement:{eigenvalues:rootA,multiplicities:multA,annihilating_polynomial_coeff_ascending:arr.coeff.map(String),trace_m0_to_m6:arr.traces.map(String)},johnson:{eigenvalues:rootJ,multiplicities:multJ,trace_m0_to_m3:jpol.traces.map(String)},signed_johnson:{eigenvalues:[3,-3],multiplicities:[10,10],annihilating_polynomial_coeff_ascending:kpol.coeff.map(String),trace_0_1:kpol.traces.map(String)},length3_independent:{identity:flat,transpositions_total:odd,threecycles_total:cycle3},length4_witness:w,counts,checks:"ALL_PASS"};
};
const result = runCertificate();
console.log(JSON.stringify(result,null,2));
