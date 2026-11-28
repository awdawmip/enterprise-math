function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n},sub=(a,b)=>(a&b)===a,check=(p,m)=>{if(!p)throw Error(m)};
 const stats={seed:20261128,models:350,originalSubsets:0,budgets:0,witnessChecks:0,childSubsetChecks:0,dominanceChecks:0,failedDominanceWitnesses:0,initialCircuits:0,initialVectors:0,initialCandidates:0,uniqueCutConstraints:0,stages:0,generated:0,states:0,peakStates:0,terms:0,expandedTerms:0,peakTerms:0,comparisons:0,vectorTests:0,transitionTerms:0,partialBatches:0,partialSubsetChecks:0,partialRejected:0};
 const le=(a,b)=>a.every((x,i)=>x<=b[i]),sum=a=>a.reduce((x,y)=>x+y,0),cmp=(a,b)=>{for(let i=0;i<a.length;i++)if(a[i]!==b[i])return a[i]-b[i];return 0};
 function minimal(vs){let out=[];for(let v of vs.slice().sort((a,b)=>sum(a)-sum(b)||cmp(a,b)))if(!out.some(w=>le(w,v)))out.push(v);return out.sort(cmp)}
 function construct(c,E,m){
  let cuts=new Map(),k=E.length,N=1<<c.length;
  for(let u=1;u<N;u++){let ids=[];for(let i=0;i<k;i++)if(sub(E[i],u))ids.push(i);let b=c.reduce((s,x,i)=>s+((u>>i&1)?x:0),0);if(ids.reduce((s,i)=>s+m[i],0)<b)continue;let key=ids.join(","),old=cuts.get(key);if(!old||b<old.b)cuts.set(key,{ids,b})}
  let cand=[];for(let {ids,b} of cuts.values()){let v=Array(k).fill(0),suf=Array(ids.length+1).fill(0);for(let j=ids.length-1;j>=0;j--)suf[j]=suf[j+1]+m[ids[j]];
   function rec(j,left){if(j===ids.length){if(left===0)cand.push(v.slice());return}let i=ids[j];for(let x=Math.max(0,left-suf[j+1]);x<=Math.min(left,m[i]);x++){v[i]=x;rec(j+1,left-x)}v[i]=0}rec(0,b)}
  return {v:minimal(cand),candidates:cand.length,cuts:cuts.size}
 }
 const trans=(v,r,q,m)=>minimal(v.filter(a=>a.every((x,i)=>x<=m[i]-q[i])).map(a=>a.map((x,i)=>Math.max(0,x-r[i]))));
 const choose=(n,k)=>{let v=1;for(let i=1;i<=k;i++)v=v*(n-i+1)/i;return v};
 const expansion=(v,m)=>v.reduce((s,a)=>s+a.reduce((p,x,i)=>p*choose(m[i],x),1),0);
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
  const ok=new Uint8Array(M);for(let z=0;z<M;z++){ok[z]=+independent(z);stats.originalSubsets++}
  let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  const E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]),mult=vec(M-1);
  const initial=construct(c,E,mult),iv=initial.v;stats.initialVectors+=iv.length;stats.initialCandidates+=initial.candidates;stats.uniqueCutConstraints+=initial.cuts;
  let ref=[];for(let z=1;z<M;z++)if(!ok[z]){let yes=true;for(let b=z;b;b&=b-1)if(!ok[z^(b&-b)]){yes=false;break}if(yes)ref.push(z)}
  stats.initialCircuits+=ref.length;check(expansion(iv,mult)===ref.length,"initial expansion count");check(JSON.stringify(minimal(ref.map(vec)))===JSON.stringify(iv),"direct constructor");
  const feasible=(v,x)=>!v.some(a=>le(a,x));
  for(let trial=0;trial<8;trial++){let R=rnd(M),Q=rnd(M)&~R;if(!ok[R]){stats.partialRejected++;continue}let F=(M-1)&~(R|Q),v=trans(iv,vec(R),vec(Q),mult);stats.partialBatches++;for(let x=F;;x=(x-1)&F){check(feasible(v,vec(x))===!!ok[R|x],"partial batch");stats.partialSubsetChecks++;if(!x)break}}
  const value=z=>{let p=0,s=0;for(let j=0;j<m;j++)if(z>>j&1){p+=A[j].p;s+=A[j].s}return{p,s}};
  const options=h=>{let a=[],b=[];for(let j=0;j<m;j++)if(h>>j&1)(A[j].s?b:a).push(j);a.sort((i,j)=>A[j].p-A[i].p||i-j);b.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=l=>{let o=[0];for(let j of l)o.push(o.at(-1)|(1<<j));return o};return pre(a).flatMap(x=>pre(b).map(y=>({mask:x|y,...value(x|y)})))};
  const D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);for(let z=0;z<M;z++)if(ok[z]){let {p,s}=value(z);best[D-s]=Math.max(best[D-s],p)}for(let k=1;k<=D;k++)best[k]=Math.max(best[k],best[k-1]);stats.budgets+=D+1;
  const query=(v,x)=>{for(let a of v){stats.vectorTests++;if(le(a,x))return false}return true};
  let F=M-1,states=[{v:iv,p:0,s:0,mask:0}];
  for(let h of H){let oldm=vec(F);F^=h;let map=new Map(),opts=options(h);
   for(let a of states)for(let o of opts){let R=o.mask,Q=h^R,r=vec(R);if(!query(a.v,r))continue;stats.transitionTerms+=a.v.length;
    let v=trans(a.v,r,vec(Q),oldm),child={v,p:a.p+o.p,s:a.s+o.s,mask:a.mask|R};
    for(let x=F;;x=(x-1)&F){check(feasible(v,vec(x))===!!ok[child.mask|x],"child");stats.childSubsetChecks++;if(!x)break}
    stats.generated++;let key=JSON.stringify(v)+"|"+child.s,old=map.get(key);if(!old||child.p>old.p)map.set(key,child)
   }
   let keep=[];for(let a of [...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s)){let dom=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;stats.comparisons++;let witness=q.v.find(x=>query(a.v,x)),pred=witness===undefined;
    let ref=true;for(let x=F;;x=(x-1)&F){if(ok[a.mask|x]&&!ok[q.mask|x]){ref=false;break}if(!x)break}
    check(pred===ref,"dominance");stats.dominanceChecks++;if(witness){let w=0;for(let i=0;i<H.length;i++){let z=H[i]&F;for(let j=0;j<witness[i];j++){check(z!==0,"lift");let b=z&-z;w|=b;z^=b}}check(ok[a.mask|w]&&!ok[q.mask|w],"witness");stats.failedDominanceWitnesses++}
    if(pred){dom=true;break}
   }if(!dom)keep.push(a)}
   states=keep;stats.stages++;stats.states+=states.length;stats.peakStates=Math.max(stats.peakStates,states.length);for(let a of states){stats.terms+=a.v.length;stats.expandedTerms+=expansion(a.v,vec(F));stats.peakTerms=Math.max(stats.peakTerms,a.v.length)}
  }
  for(let k=0;k<=D;k++){let w=states.find(x=>D-x.s<=k);check(w&&w.p===best[k],"budget");let v=value(w.mask);check(ok[w.mask]&&v.p===w.p&&v.s===w.s&&D-v.s<=k,"label witness");stats.witnessChecks++}
 }
 const b=construct([33],[1],[100]);check(JSON.stringify(b.v)==="[[33]]","large multiplicity");let y=trans(b.v,[20],[30],[100]);check(JSON.stringify(y)==="[[13]]","large transition");stats.largeMultiplicity={m:100,capacity:33,vector:b.v,afterSelect20Skip30:y,initialCandidates:b.candidates};
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
