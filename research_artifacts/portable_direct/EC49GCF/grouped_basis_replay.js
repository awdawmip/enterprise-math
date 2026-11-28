function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,budgets:0,bruteSubsets:0,witnessChecks:0,rankChecks:0,chainChecks:0,repairAdditions:0,removedH:0,contractionExchanges:0,thetaChecks:0,disagreements:0};
 const modes=["groupedGreedy","groupedCached"],counts=()=>({stages:0,generated:0,states:0,peak:0,rankCalls:0,quotaVisits:0,comparisons:0,rankEntries:0,basisBits:0});
 for(const mode of modes)stats[mode]=counts();
 const check=(p,m)=>{if(!p)throw Error(m)},sub=(a,b)=>(a&b)===a;
 let models=[];
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  models.push({n,m,c,N,M,A})
 }
 function solve(model,mode,st,verify){
  const {n,m,c,N,M,A}=model,cc=Array.from({length:N},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  const direct=(z,Q)=>{let I=0;for(let q=Q;q;q&=q-1){let y=q&-q;if(independent(z|I|y))I|=y}return I};
  const groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  function stage(F){let unions=new Set([0]);for(let q=F;q;q&=q-1){let y=q&-q,j=31-Math.clz32(y);for(let w of [...unions])unions.add(w|A[j].e)}let w=[...unions].filter(Boolean).sort((a,b)=>a-b);return{w,f:w.map(x=>contained[x]&F)}}
  function value(z){let p=0,s=0;for(let j=0;j<m;j++)if(z>>j&1){p+=A[j].p;s+=A[j].s}return{p,s}}
  function options(H){let real=[],aux=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?aux:real).push(j);real.sort((i,j)=>A[j].p-A[i].p||i-j);aux.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=ls=>{let v=[0];for(let j of ls)v.push(v[v.length-1]|(1<<j));return v};let out=[];for(let r of pre(real))for(let a of pre(aux)){let mask=r|a;out.push({mask,t:pop[mask],...value(mask)})}return out}
  let F=M-1,old=stage(F),bs=old.f.map(Q=>direct(0,Q)),states=[{v:bs.map(b=>pop[b]),b:mode==="groupedCached"?bs:null,p:0,s:0,mask:0}];
  for(let H of groups.values()){
   F^=H;let next=stage(F),prior=next.w.map(w=>old.w.indexOf(w)),map=new Map(),opts=options(H),hi=old.f.map((L,i)=>L&H?i:-1).filter(i=>i>=0);
   function add(z){st.generated++;let key=z.v.join(",")+"|"+z.s,prev=map.get(key);if(!prev||z.p>prev.p)map.set(key,z)}
   for(let a of states){
    const feasible=Q=>{for(let i=0;i<old.f.length;i++){st.quotaVisits++;if(pop[Q&old.f[i]]>a.v[i])return false}return true};
    const memo=new Map(),rank=Q=>{if(memo.has(Q))return memo.get(Q);st.rankCalls++;let I=0;for(let q=Q;q;q&=q-1){let y=q&-q;if(feasible(I|y))I|=y}let r=pop[I];memo.set(Q,r);return r};
    let maxTake,pairs,chains;
    if(mode==="groupedGreedy"){
     maxTake=rank(H);pairs=next.f.map((Q,i)=>old.f[prior[i]]&H?[rank(Q),a.v[prior[i]]]:[a.v[prior[i]],rank(Q|H)]);
    }else{
     maxTake=pop[H];for(let j of hi){st.quotaVisits++;maxTake=Math.min(maxTake,a.v[j])}
     chains=next.f.map((Q,i)=>{
      let B=a.b[prior[i]],I=B&Q,k=pop[B&H],rep=0;
      if(verify)stats.removedH+=k;
      while(rep<k){
       let D=0;for(let j=0;j<old.f.length;j++){st.quotaVisits++;let L=old.f[j];if(pop[I&L]===a.v[j])D|=L}
       let Y=Q&~(I|D);if(!Y)break;I|=Y&-Y;rep++;
      }
      if(verify){stats.repairAdditions+=rep;check(pop[I]===pop[direct(a.mask,Q)]&&independent(a.mask|I),"deletion repair")}
      let theta=pop[H];for(let j of hi){st.quotaVisits++;theta=Math.min(theta,a.v[j]-pop[I&old.f[j]])}
      if(verify){stats.thetaChecks++;check(theta===pop[direct(a.mask,Q|H)]-pop[I],"theta");if(old.f[prior[i]]&H)check(pop[I]+theta===a.v[prior[i]],"old union rank")}
      let out=Array(maxTake+1).fill(I);
      for(let t=theta+1;t<=maxTake;t++){
       let C=I,tight=false;for(let j of hi){st.quotaVisits++;let L=old.f[j];if(pop[I&L]+t-1===a.v[j]){C&=L;tight=true}}
       check(tight&&C!==0,"empty contraction exchange");I^=C&-C;out[t]=I;if(verify)stats.contractionExchanges++;
      }
      return out
     });
    }
    for(let o of opts)if(o.t<=maxTake){
     let b=chains?chains.map(ch=>ch[o.t]):null,v=b?b.map(x=>pop[x]):pairs.map(([r,u])=>Math.min(r,u-o.t));
     if(verify&&b)for(let i=0;i<b.length;i++){stats.chainChecks++;check(sub(b[i],next.f[i])&&independent(a.mask|o.mask|b[i])&&v[i]===pop[direct(a.mask|o.mask,next.f[i])],"generated chain")}
     add({v,b,p:a.p+o.p,s:a.s+o.s,mask:a.mask|o.mask})
    }
   }
   let vals=[...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s),keep=[];
   for(let a of vals){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;st.comparisons++;if(q.v.every((x,i)=>x>=a.v[i])){dominated=true;break}}if(!dominated)keep.push(a)}
   states=keep;st.stages++;st.states+=states.length;st.peak=Math.max(st.peak,states.length);st.rankEntries+=states.length*next.f.length;if(mode==="groupedCached")st.basisBits+=states.length*next.f.length*pop[F];
   if(verify)for(let a of states)for(let i=0;i<next.f.length;i++){stats.rankChecks++;check(a.v[i]===pop[direct(a.mask,next.f[i])],"retained rank")}
   old=next;
  }
  if(verify){
   let D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);
   for(let z=0;z<M;z++){if(mode==="groupedGreedy")stats.bruteSubsets++;if(!independent(z))continue;let {p,s}=value(z);best[D-s]=Math.max(best[D-s],p)}
   for(let k=1;k<=D;k++)best[k]=Math.max(best[k],best[k-1]);
   for(let k=0;k<=D;k++){if(mode==="groupedGreedy")stats.budgets++;let winner=states.find(x=>D-x.s<=k);check(winner&&winner.p===best[k],"budget optimum");let v=value(winner.mask);check(independent(winner.mask)&&v.p===winner.p&&v.s===winner.s&&D-v.s<=k,"label witness");stats.witnessChecks++}
  }
  return states
 }
 for(let model of models){for(let mode of modes)solve(model,mode,stats[mode],true);stats.models++}
 stats.timingsMs={groupedGreedy:[],groupedCached:[]};
 for(let i=0;i<5;i++)for(let mode of (i%2?[...modes].reverse():modes)){let st=counts(),start=Date.now();for(let model of models)solve(model,mode,st,false);stats.timingsMs[mode].push(Date.now()-start);check(JSON.stringify(st)===JSON.stringify(stats[mode]),"timed counters")}
 return stats
}
console.log(JSON.stringify(replay(),null,2));
