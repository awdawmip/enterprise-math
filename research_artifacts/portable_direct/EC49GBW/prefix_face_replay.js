function replay(){
 let seed=20261127; const rng=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
 const stats={seed:20261127,models:400,referenceSubsets:0,budgets:0,certifiedWithoutDP:0,dpBudgets:0,forcedCuts:0,multiBlockDP:0,blockSubsetChecks:0,unfactoredSubsetUniverse:0,dpPairs:0,nonSupportedGap:0,disagreements:0};
 for(let model=0;model<stats.models;model++){
  const n=1+rng(4),m=1+rng(7),d=1+rng(5),N=m+d,all=(1<<N)-1;
  const c=Array.from({length:n},()=>1+rng(3)), masks=[],v=[],a=[];
  for(let i=0;i<m;i++){masks.push(1+rng((1<<n)-1));v.push(1+rng(15));a.push(0)}
  for(let i=0;i<d;i++){const j=rng(n);c[j]++;masks.push(1<<j);v.push(0);a.push(1+rng(11))}
  const total=a.reduce((x,y)=>x+y,0), cs=Array.from({length:1<<n},(_,s)=>c.reduce((z,x,i)=>z+((s>>i&1)?x:0),0));
  const ok=new Uint8Array(1<<N), val=new Int32Array(1<<N), kept=new Int32Array(1<<N), ref=Array(total+1).fill(-1);
  for(let s=0;s<=all;s++){stats.referenceSubsets++;let good=true;
   for(let t=1;t<(1<<n);t++){let f=0;for(let i=0;i<N;i++)if((s>>i&1)&&!(masks[i]&~t))f++;if(f>=cs[t]){good=false;break}}
   if(!good)continue;ok[s]=1;
   for(let i=0;i<N;i++)if(s>>i&1){val[s]+=v[i];kept[s]+=a[i]}
   const cost=total-kept[s];ref[cost]=Math.max(ref[cost],val[s])
  }
  for(let b=1;b<=total;b++)ref[b]=Math.max(ref[b],ref[b-1]);
  const greedy=(order)=>{let s=0;const bases=[0];for(const i of order){if(ok[s|(1<<i)])s|=1<<i;bases.push(s)}return bases};
  const ratios=[[0,1]];for(let i=0;i<m;i++)for(let j=m;j<N;j++)ratios.push([v[i],a[j]]);
  const supports=[];
  for(const [p,q] of ratios){const scores=v.map((x,i)=>q*x+p*a[i]);
   for(const tie of [1,-1]){
    const order=Array.from({length:N},(_,i)=>i).sort((i,j)=>scores[j]-scores[i]||tie*(i-j));
    const bases=greedy(order),s=bases[N],h=q*val[s]+p*kept[s]-p*total;
    supports.push({p,q,s,h,order,bases,scores});
   }
  }
  for(let B=0;B<=total;B++){
   stats.budgets++;let L=-1,cert=null;
   for(const z of supports){
    if(total-kept[z.s]<=B)L=Math.max(L,val[z.s]);
    const u=z.h+z.p*B;
    if(!cert||u*cert.q<cert.u*z.q)cert={...z,u}
   }
   if(L<0)throw Error("no incumbent");
   const {q,u,order,bases,scores}=cert;
   if(L>ref[B]||q*ref[B]>u)throw Error("bad bound");
   if(Math.floor(u/q)===L){stats.certifiedWithoutDP++;if(L!==ref[B])throw Error("bad cert");continue}
   stats.dpBudgets++;if(L<ref[B])stats.nonSupportedGap++;
   const ends=[];
   for(let j=1;j<=N;j++){const gap=scores[order[j-1]]-(j===N?0:scores[order[j]]);
    if(gap>u-q*L){ends.push(j);stats.forcedCuts++}}
   if(ends[ends.length-1]!==N)ends.push(N);
   if(ends.length>1)stats.multiBlockDP++;
   stats.unfactoredSubsetUniverse+=1<<N;
   let dp=new Map([[0,{reward:0,mask:0}]]),start=0;
   for(const end of ends){
    const block=order.slice(start,end),prior=bases[start];
    const finalGap=scores[order[end-1]]-(end===N?0:scores[order[end]]);
    const force=finalGap>u-q*L, rank=pop(bases[end])-pop(prior);
    let local=new Map();
    for(let ss=0;ss<(1<<block.length);ss++){
     stats.blockSubsetChecks++;
     if(force&&pop(ss)!==rank)continue;
     let sm=0,cost=0,reward=0;
     for(let j=0;j<block.length;j++){const i=block[j];if(ss>>j&1){sm|=1<<i;reward+=v[i]}else cost+=a[i]}
     if(!ok[prior|sm]||cost>B)continue;
     if(!local.has(cost)||local.get(cost).reward<reward)local.set(cost,{reward,mask:sm});
    }
    const next=new Map();
    for(const [cost,x] of dp)for(const [lc,y] of local){stats.dpPairs++;const nc=cost+lc;if(nc>B)continue;const reward=x.reward+y.reward;if(!next.has(nc)||next.get(nc).reward<reward)next.set(nc,{reward,mask:x.mask|y.mask})}
    dp=next;start=end;
   }
   let best={reward:-1,mask:0};
   for(const x of dp.values())if(x.reward>best.reward)best=x;
   if(best.reward!==ref[B]||!ok[best.mask]||val[best.mask]!==best.reward||total-kept[best.mask]>B)throw Error("DP disagreement");
  }
 }
 return stats;
}
console.log(JSON.stringify(replay()));
