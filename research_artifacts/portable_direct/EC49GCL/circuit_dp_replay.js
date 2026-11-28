function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n},sub=(a,b)=>(a&b)===a,check=(p,m)=>{if(!p)throw Error(m)};
 const stats={seed:20261128,models:350,originalSubsets:0,budgets:0,witnessChecks:0,childSubsetChecks:0,dominanceChecks:0,failedDominanceWitnesses:0,initialCircuits:0,initialSignedTerms:0,maxInitialCircuits:0,maxInitialSignedTerms:0};
 const count=()=>({stages:0,generated:0,states:0,peakStates:0,terms:0,peakTerms:0,comparisons:0,subsetTests:0,transitionTerms:0});
 const modes=["signed","circuit"];for(let mode of modes)stats[mode]=count();
 let models=[];
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  models.push({n,m,c,N,M,A});
 }
 for(let {n,m,c,N,M,A} of models){
  const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=1;v<N;v++){for(let j=0;j<n;j++)if(v>>j&1)cap[v]+=c[j];for(let j=0;j<m;j++)if(sub(A[j].e,v))L[v]|=1<<j}
  const independent=z=>{for(let v=1;v<N;v++)if(pop[z&L[v]]>=cap[v])return false;return true};
  const r=new Uint8Array(M),ok=new Uint8Array(M),nu=new Int16Array(M);
  for(let z=0;z<M;z++){ok[z]=+independent(z);if(ok[z])r[z]=pop[z];else for(let b=z;b;b&=b-1)r[z]=Math.max(r[z],r[z^(b&-b)]);nu[z]=pop[z]-r[z];stats.originalSubsets++}
  const coeff=Int16Array.from(nu);
  for(let j=0;j<m;j++)for(let z=0;z<M;z++)if(z>>j&1)coeff[z]-=coeff[z^(1<<j)];
  const signed=[];for(let z=1;z<M;z++)if(coeff[z])signed.push([z,coeff[z]]);
  const minimal=ms=>{let out=[];for(let z of [...new Set(ms)].sort((a,b)=>pop[a]-pop[b]||a-b))if(!out.some(y=>sub(y,z)))out.push(z);return out.sort((a,b)=>a-b)};
  const circuits=minimal(signed.map(x=>x[0]));for(let z of circuits)check(coeff[z]===1,"circuit coeff");
  stats.initialCircuits+=circuits.length;stats.initialSignedTerms+=signed.length;stats.maxInitialCircuits=Math.max(stats.maxInitialCircuits,circuits.length);stats.maxInitialSignedTerms=Math.max(stats.maxInitialSignedTerms,signed.length);
  let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  const value=z=>{let p=0,s=0;for(let j=0;j<m;j++)if(z>>j&1){p+=A[j].p;s+=A[j].s}return{p,s}};
  const options=H=>{let a=[],b=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?b:a).push(j);a.sort((i,j)=>A[j].p-A[i].p||i-j);b.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=l=>{let o=[0];for(let j of l)o.push(o.at(-1)|(1<<j));return o};return pre(a).flatMap(x=>pre(b).map(y=>({mask:x|y,...value(x|y)})))};
  const D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);
  for(let z=0;z<M;z++)if(ok[z]){let {p,s}=value(z);best[D-s]=Math.max(best[D-s],p)}for(let k=1;k<=D;k++)best[k]=Math.max(best[k],best[k-1]);stats.budgets+=D+1;
  for(let mode of modes){
   const st=stats[mode],cs=mode==="circuit",query=(v,x)=>{if(cs){for(let a of v){st.subsetTests++;if(sub(a,x))return false}return true}let sum=0;for(let [a,w] of v){st.subsetTests++;if(sub(a,x))sum+=w}return sum===0};
   let F=M-1,states=[{v:cs?circuits:signed,p:0,s:0,mask:0}];
   for(let H of groups.values()){
    F^=H;let map=new Map(),opts=options(H);
    for(let a of states)for(let o of opts){if(!query(a.v,o.mask))continue;let R=o.mask,Q=H^R,v;st.transitionTerms+=a.v.length;
     if(cs)v=minimal(a.v.filter(x=>!(x&Q)).map(x=>x&~R));
     else{let z=new Map();for(let [x,w] of a.v)if(!(x&Q)){let y=x&~R;z.set(y,(z.get(y)||0)+w)}v=[...z].filter(x=>x[1]).sort((a,b)=>a[0]-b[0]);check(!v.some(x=>!x[0]),"empty coefficient")}
     const child={v,p:a.p+o.p,s:a.s+o.s,mask:a.mask|R};
     for(let x=F;;x=(x-1)&F){let observed=cs?!v.some(y=>sub(y,x)):v.reduce((s,[y,w])=>s+(sub(y,x)?w:0),0)===0;check(observed===!!ok[child.mask|x],"child independence");stats.childSubsetChecks++;if(!x)break}
     st.generated++;let key=JSON.stringify(v)+"|"+child.s,old=map.get(key);if(!old||child.p>old.p)map.set(key,child)
    }
    let keep=[];for(let a of [...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s)){
     let dom=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;st.comparisons++;
      let cq=cs?q.v:minimal(q.v.map(x=>x[0]));let witness=cq.find(x=>query(a.v,x));let pred=witness===undefined;
      let ref=true;for(let x=F;;x=(x-1)&F){if(ok[a.mask|x]&&!ok[q.mask|x]){ref=false;break}if(!x)break}
      check(pred===ref,"dominance");stats.dominanceChecks++;if(witness!==undefined){check(ok[a.mask|witness]&&!ok[q.mask|witness],"witness");stats.failedDominanceWitnesses++}
      if(pred){dom=true;break}
     }if(!dom)keep.push(a)
    }
    states=keep;st.stages++;st.states+=states.length;st.peakStates=Math.max(st.peakStates,states.length);for(let a of states){st.terms+=a.v.length;st.peakTerms=Math.max(st.peakTerms,a.v.length)}
   }
   for(let k=0;k<=D;k++){let w=states.find(x=>D-x.s<=k);check(w&&w.p===best[k],"budget");let v=value(w.mask);check(ok[w.mask]&&v.p===w.p&&v.s===w.s&&D-v.s<=k,"label witness");stats.witnessChecks++}
  }
 }
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
