"use strict";
// No dependencies; exact BigInt and independent named-partition enumeration.
const evidence=(function verifyBD(){
 const check=(c,s)=>{if(!c)throw Error(s)};
 const fact=n=>{let x=1n;for(let j=2;j<=n;j++)x*=BigInt(j);return x};
 const falling=(a,t)=>{let x=1n;for(let j=0;j<t;j++)x*=BigInt(a-j);return x};
 const profiles=n=>{const out=[];function walk(prefix,left){if(prefix.length===5){out.push([...prefix,left]);return}for(let i=0;i<=left;i++)walk([...prefix,i],left-i)}walk([],3*n);return out};
 function partitions(a){
  const types=a.flatMap((c,i)=>Array(c).fill(i)),N=types.length,used=new Array(N).fill(false),out=[];
  function rec(blocks){
   let i=used.indexOf(false);if(i===-1){out.push(blocks.slice());return}
   used[i]=true;
   for(let j=i+1;j<N;j++){if(used[j]||types[j]===types[i])continue;used[j]=true;
    for(let k=j+1;k<N;k++){if(used[k]||types[k]===types[i]||types[k]===types[j])continue;used[k]=true;
      blocks.push([i,j,k]);rec(blocks);blocks.pop();used[k]=false;
    }used[j]=false;
   }used[i]=false;
  }
  rec([]);return {types,partitions:out};
 }
 const summary={profiles:0,pairChecks:0,saturatedPairTests:0,conditionalAxisTests:0};
 const sample=[];
 for(let n=1;n<=3;n++)for(const a of profiles(n)){
  summary.profiles++;
  const feasible=a.every(v=>v<=n);
  const {types,partitions:ps}=partitions(a);
  check((ps.length>0)===feasible,`existence ${n} ${a}`);
  if(!feasible)continue;
  const first=a.map((v,i)=>v?types.indexOf(i):-1);
  const T=a.map((v,i)=>v===n?i:-1).filter(i=>i>=0);
  for(let r=0;r<6;r++)for(let s=r+1;s<6;s++){
   if(!a[r]||!a[s])continue;
   const predicted=[];
   for(let k=0;k<6;k++)if(k!==r&&k!==s&&a[k]>0&&T.every(i=>i===r||i===s||i===k))predicted.push(k);
   const actual=new Set();
   for(const p of ps)for(const tr of p){
    if(tr.includes(first[r])&&tr.includes(first[s]))actual.add(types[tr.find(i=>i!==first[r]&&i!==first[s])]);
   }
   check(predicted.join(",")===Array.from(actual).sort((x,y)=>x-y).join(","),`fiber ${n}/${a}/${r}/${s}`);
   summary.pairChecks++;
  }
  for(let r=0;r<6;r++)for(let s=r+1;s<6;s++){
   if(a[r]!==n||a[s]!==n)continue;
   const rs=types.map((v,i)=>v===r?i:-1).filter(i=>i>=0);
   const ss=types.map((v,i)=>v===s?i:-1).filter(i=>i>=0);
   check(BigInt(ps.length)===fact(n)**2n,`sat total ${n}/${a}`);
   summary.saturatedPairTests++;
   for(let t=0;t<=n;t++){
    const observed=new Map();
    for(const p of ps){
     const pairBlocks=[];let ok=true;
     for(let j=0;j<t;j++){
      const block=p.find(tr=>tr.includes(rs[j]));
      if(!block.includes(ss[j])){ok=false;break}
      pairBlocks.push(block);
     }
     if(!ok)continue;
     const ks=pairBlocks.map(tr=>types[tr.find(id=>types[id]!==r&&types[id]!==s)]);
     const key=ks.join(",");observed.set(key,(observed.get(key)||0n)+1n);
    }
    let total=0n;
    function walk(ks){
     if(ks.length===t){
      const kcounts=Array(6).fill(0);for(const k of ks)kcounts[k]++;
      const expected=fact(n-t)**2n*kcounts.reduce((q,c,k)=>q*falling(a[k],c),1n);
      const key=ks.join(",");
      check((observed.get(key)||0n)===expected,`conditional ${n}/${a}/${r}/${s}/${key}`);
      total+=expected;summary.conditionalAxisTests++;return;
     }
     for(let k=0;k<6;k++)if(k!==r&&k!==s&&a[k]>0)walk([...ks,k]);
    }
    walk([]);
    const observedTotal=Array.from(observed.values()).reduce((x,y)=>x+y,0n);
    check(observedTotal===total&&total===fact(n)*fact(n-t),`matched ${n}/${a}/${r}/${s}/${t}`);
   }
  }
  if(n===2&&a.join(",")==="2,1,1,1,1,0")sample.push({a,observed_axes:[2,3],third_axes:[0],overall_partitions:ps.length});
 }
 return {schema:"R762BD_SATURATION_FILTER_HYPERGEOMETRIC_CERT_V1",date:"2026-11-15",status:"ALL_ASSERTIONS_PASS",scope:"Six unsigned axes; distinct named equal-weight Cell-local quanta, candidate disjoint triads; exhaustive counts sum=3n, n=1..3",stats:summary,examples:sample};
})();
console.log(JSON.stringify(evidence,null,2));
