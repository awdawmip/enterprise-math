function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const s={seed:20261128,models:0,bruteSubsets:0,budgets:0,witnessChecks:0,rankChecks:0,decodeChecks:0,dominanceChecks:0,fullDominanceCoordinates:0,atomDominanceCoordinates:0,stages:0,generated:0,states:0,peak:0,denseEntries:0,atomEntries:0,initialDense:0,initialAtoms:0,allContainments:0,coverEdges:0,coverConstructionChecks:0,normalizations:0,allContainmentVisits:0,coverVisits:0,splitVisits:0,essentialAtomChecks:0,disagreements:0};
 const ck=(p,m)=>{if(!p)throw Error(m)},sub=(a,b)=>(a&b)===a;
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  const cc=Array.from({length:N},(_,v)=>c.reduce((sum,a,i)=>sum+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  const gs=new Map();for(let j=0;j<m;j++)gs.set(A[j].e,(gs.get(A[j].e)||0)|(1<<j));
  const groups=[...gs.values()],supports=[...gs.keys()],k=groups.length,rank=new Uint8Array(M),ok=new Uint8Array(M),P=new Uint16Array(M),S=new Uint16Array(M);
  s.models++;
  for(let z=0;z<M;z++){s.bruteSubsets++;ok[z]=+independent(z);if(z){let y=z&-z,j=31-Math.clz32(y);P[z]=P[z^y]+A[j].p;S[z]=S[z^y]+A[j].s}if(ok[z])rank[z]=pop[z];else for(let q=z;q;q&=q-1)rank[z]=Math.max(rank[z],rank[z^(q&-q)])}
  let stages=[];
  for(let i=0;i<=k;i++){
   let F=0,closure=new Set([0]);for(let j=i;j<k;j++){F|=groups[j];for(let w of [...closure])closure.add(w|supports[j])}
   let W=[...closure].sort((a,b)=>a-b),ix=new Map(W.map((w,j)=>[w,j])),sets=W.map(w=>F&contained[w]),counts=sets.map(z=>pop[z]),lower=W.map(()=>[]),cover=W.map(()=>[]),split=W.map(()=>[]);
   for(let a=1;a<W.length;a++)for(let b=a+1;b<W.length;b++){if(sub(W[a],W[b]))lower[b].push(a);if(!(W[a]&W[b]))split[ix.get(W[a]|W[b])].push([a,b])}
   for(let j=1;j<W.length;j++){s.allContainments+=lower[j].length;for(let a of [...lower[j]].reverse()){let dominated=false;for(let b of cover[j]){s.coverConstructionChecks++;if(sub(W[a],W[b])){dominated=true;break}}if(!dominated)cover[j].push(a)}s.coverEdges+=cover[j].length}
   stages.push({W,ix,sets,counts,lower,cover,split});
  }
  function decode(st,atoms,omit=-1){let d=new Int16Array(st.W.length),a=new Map(atoms);for(let j=1;j<d.length;j++){let v=j===omit?0:a.get(j)||0;for(let l of st.cover[j])v=Math.max(v,d[l]);for(let [l,r] of st.split[j])v=Math.max(v,d[l]+d[r]);d[j]=v}return d}
  function normalize(st,q){let d=new Int16Array(q.length),atoms=[];s.normalizations++;
   for(let j=1;j<q.length;j++){let v=0;s.allContainmentVisits+=st.lower[j].length;for(let l of st.cover[j]){s.coverVisits++;v=Math.max(v,d[l])}for(let [l,r] of st.split[j]){s.splitVisits++;v=Math.max(v,d[l]+d[r])}let raw=st.counts[j]-q[j];if(raw>v)atoms.push([j,raw]);d[j]=Math.max(v,raw);ck(d[j]<=st.counts[j],"nonnegative rank")}
   const rebuilt=decode(st,atoms);for(let j=0;j<d.length;j++){s.decodeChecks++;ck(d[j]===rebuilt[j],"atom decode")}
   // Removing any atom must change its own coordinate.
   for(let [j,v] of atoms){s.essentialAtomChecks++;ck(decode(st,atoms,j)[j]<v,"essential atom")}
   return {d,atoms}
  }
  let st=stages[0],initial=normalize(st,st.W.map(w=>w?cc[w]-1:0));s.initialDense+=st.W.length-1;s.initialAtoms+=initial.atoms.length;
  for(let j=0;j<st.W.length;j++){s.rankChecks++;ck(st.counts[j]-initial.d[j]===rank[st.sets[j]],"initial rank")}
  function options(H){let real=[],aux=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?aux:real).push(j);real.sort((i,j)=>A[j].p-A[i].p||i-j);aux.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=ls=>{let v=[0];for(let j of ls)v.push(v[v.length-1]|(1<<j));return v};let out=[];for(let r of pre(real))for(let a of pre(aux)){let z=r|a;out.push({z,t:pop[z],p:P[z],s:S[z]})}return out}
  let states=[{...initial,p:0,s:0,z:0}];
  for(let i=0;i<k;i++){
   let old=stages[i],next=stages[i+1],E=supports[i],opts=options(groups[i]),map=new Map();
   for(let a of states){const g=w=>old.counts[old.ix.get(w)]-a.d[old.ix.get(w)];let byT=new Map();for(let o of opts){
    if(o.t>Math.min(pop[groups[i]],g(E)))continue;
    let v=byT.get(o.t);if(!v){v=normalize(next,next.W.map(w=>w?Math.min(g(w),g(w|E)-o.t):0));byT.set(o.t,v)}
    let z=a.z|o.z;ck(ok[z],"legal");
    for(let j=0;j<v.d.length;j++){s.rankChecks++;ck(next.counts[j]-v.d[j]===rank[z|next.sets[j]]-pop[z],"child rank")}
    s.generated++;let key=JSON.stringify(v.atoms)+"|"+(a.s+o.s),p=a.p+o.p,sv=a.s+o.s,prior=map.get(key);if(!prior||p>prior.p)map.set(key,{...v,p,s:sv,z});
   }}
   let keep=[];for(let a of [...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s)){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;s.dominanceChecks++;s.fullDominanceCoordinates+=next.W.length-1;s.atomDominanceCoordinates+=q.atoms.length;const atom=q.atoms.every(([j,v])=>v<=a.d[j]);const dense=q.d.every((v,j)=>v<=a.d[j]);ck(atom===dense,"dominance");if(atom){dominated=true;break}}if(!dominated)keep.push(a)}
   states=keep;s.stages++;s.states+=states.length;s.peak=Math.max(s.peak,states.length);s.denseEntries+=states.length*(next.W.length-1);s.atomEntries+=states.reduce((a,b)=>a+b.atoms.length,0)
  }
  const D=S[M-1],best=Array(D+1).fill(-1);for(let z=0;z<M;z++)if(ok[z])best[D-S[z]]=Math.max(best[D-S[z]],P[z]);for(let j=1;j<=D;j++)best[j]=Math.max(best[j],best[j-1]);
  for(let j=0;j<=D;j++){s.budgets++;let win=states.find(x=>D-x.s<=j);ck(win&&win.p===best[j],"optimum");ck(ok[win.z]&&P[win.z]===win.p&&S[win.z]===win.s&&D-win.s<=j,"witness");s.witnessChecks++}
 }
 return s
}
console.log(JSON.stringify(replay(),null,2));
