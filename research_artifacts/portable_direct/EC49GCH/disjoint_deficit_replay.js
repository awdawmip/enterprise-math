function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,bruteSubsets:0,budgets:0,witnessChecks:0,initialRankChecks:0,generatedRankChecks:0,stages:0,generated:0,states:0,peak:0,comparisons:0,rankEntries:0,initialEntries:0,transitionMinima:0,canonicalizations:0,weightChecks:0,containmentMaxima:0,disjointMaxima:0,preprocessPairs:0,rawNoncanonicalEntries:0,rawNoncanonicalProfiles:0,disagreements:0};
 const ck=(p,m)=>{if(!p)throw Error(m)},sub=(a,b)=>(a&b)===a;
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  const cc=Array.from({length:N},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  const gs=new Map();for(let j=0;j<m;j++)gs.set(A[j].e,(gs.get(A[j].e)||0)|(1<<j));
  const groups=[...gs.values()],supports=[...gs.keys()],k=groups.length,rank=new Uint8Array(M),ok=new Uint8Array(M),P=new Uint16Array(M),S=new Uint16Array(M);
  stats.models++;
  for(let z=0;z<M;z++){stats.bruteSubsets++;ok[z]=+independent(z);if(z){let y=z&-z,j=31-Math.clz32(y);P[z]=P[z^y]+A[j].p;S[z]=S[z^y]+A[j].s}if(ok[z])rank[z]=pop[z];else for(let q=z;q;q&=q-1)rank[z]=Math.max(rank[z],rank[z^(q&-q)])}
  let stages=[];
  for(let i=0;i<=k;i++){
   let F=0,closure=new Set([0]);for(let j=i;j<k;j++){F|=groups[j];for(let w of [...closure])closure.add(w|supports[j])}
   let W=[...closure].sort((a,b)=>a-b),ix=new Map(W.map((w,j)=>[w,j])),sets=W.map(w=>F&contained[w]),counts=sets.map(z=>pop[z]),lower=W.map(()=>[]),split=W.map(()=>[]);
   for(let a=1;a<W.length;a++)for(let b=a+1;b<W.length;b++){stats.preprocessPairs++;if(sub(W[a],W[b]))lower[b].push(a);if(!(W[a]&W[b]))split[ix.get(W[a]|W[b])].push([a,b])}
   stages.push({W,ix,sets,counts,lower,split});
  }
  function normalize(st,q){let D=new Int16Array(q.length),g=new Uint8Array(q.length);stats.canonicalizations++;let changed=false;
   for(let j=1;j<q.length;j++){stats.weightChecks++;let d=Math.max(0,st.counts[j]-q[j]);for(let a of st.lower[j]){stats.containmentMaxima++;d=Math.max(d,D[a])}for(let [a,b] of st.split[j]){stats.disjointMaxima++;d=Math.max(d,D[a]+D[b])}D[j]=d;g[j]=st.counts[j]-d;ck(d<=st.counts[j],"nonnegative rank");if(g[j]!==q[j]){stats.rawNoncanonicalEntries++;changed=true}}
   if(changed)stats.rawNoncanonicalProfiles++;return g
  }
  let st=stages[0],initial=normalize(st,st.W.map(w=>w?cc[w]-1:0));stats.initialEntries+=initial.length-1;
  for(let j=0;j<initial.length;j++){stats.initialRankChecks++;ck(initial[j]===rank[st.sets[j]],"initial canonical")}
  function options(H){let real=[],aux=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?aux:real).push(j);real.sort((i,j)=>A[j].p-A[i].p||i-j);aux.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=ls=>{let v=[0];for(let j of ls)v.push(v[v.length-1]|(1<<j));return v};let out=[];for(let r of pre(real))for(let a of pre(aux)){let z=r|a;out.push({z,t:pop[z],p:P[z],s:S[z]})}return out}
  let states=[{v:initial,p:0,s:0,z:0}];
  for(let i=0;i<k;i++){
   let old=stages[i],next=stages[i+1],E=supports[i],opts=options(groups[i]),map=new Map();
   for(let a of states){let byT=new Map();for(let o of opts){
    // Only H may be chosen: rank(H) = min(|H|, min old quota containing E).
    if(o.t>Math.min(pop[groups[i]],a.v[old.ix.get(E)]))continue;
    let v=byT.get(o.t);if(!v){let q=next.W.map(w=>{if(!w)return 0;stats.transitionMinima++;return Math.min(a.v[old.ix.get(w)],a.v[old.ix.get(w|E)]-o.t)});v=normalize(next,q);byT.set(o.t,v)}
    let z=a.z|o.z;ck(ok[z],"legal");
    for(let j=0;j<v.length;j++){stats.generatedRankChecks++;ck(v[j]===rank[z|next.sets[j]]-pop[z],"child canonical rank")}
    stats.generated++;let key=v.join(",")+"|"+(a.s+o.s),p=a.p+o.p,s=a.s+o.s,prior=map.get(key);if(!prior||p>prior.p)map.set(key,{v,p,s,z});
   }}
   let keep=[];for(let a of [...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s)){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;stats.comparisons++;if(q.v.every((x,j)=>x>=a.v[j])){dominated=true;break}}if(!dominated)keep.push(a)}
   states=keep;stats.stages++;stats.states+=states.length;stats.peak=Math.max(stats.peak,states.length);stats.rankEntries+=states.length*(next.W.length-1)
  }
  const D=S[M-1],best=Array(D+1).fill(-1);for(let z=0;z<M;z++)if(ok[z])best[D-S[z]]=Math.max(best[D-S[z]],P[z]);for(let j=1;j<=D;j++)best[j]=Math.max(best[j],best[j-1]);
  for(let j=0;j<=D;j++){stats.budgets++;let win=states.find(x=>D-x.s<=j);ck(win&&win.p===best[j],"optimum");ck(ok[win.z]&&P[win.z]===win.p&&S[win.z]===win.s&&D-win.s<=j,"witness");stats.witnessChecks++}
 }
 return stats
}
console.log(JSON.stringify(replay(),null,2));
