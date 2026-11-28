function replay(){
 let seed=20261128;
 const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const check=(p,m)=>{if(!p)throw Error(m)}, sub=(a,b)=>(a&b)===a;
 const sum=a=>a.reduce((s,x)=>s+x,0), dot=(a,J)=>sum(a.map((x,i)=>(J>>>i&1)?x:0));
 const stats={seed:20261128,models:350,originalSubsets:0,initialRows:0,initialCountAtoms:0,initialComponents:0,modelsSplit:0,minorStates:0,minorRejected:0,minorRows:0,minorComponents:0,minorSplit:0,minorSubsetChecks:0,componentPartitionChecks:0,dominanceChecks:0,dominanceFailures:0,greedyRankChecks:0,globalPrefixCandidates:0,componentPrefixCandidates:0,convolutionPairs:0,budgetChecks:0,witnessChecks:0,uniformDistinct:[]};
 function norm(rows,m){
   let active=m.reduce((s,x,i)=>s|(x?1<<i:0),0),map=new Map();
   for(let [J,b] of rows){J&=active;check(b>=0,"negative credit");if(dot(m,J)<=b)continue;if(!map.has(J)||map.get(J)>b)map.set(J,b)}
   let a=[...map].sort((x,y)=>x[0]-y[0]||x[1]-y[1]);
   // Sequential removal, so an equivalence cycle cannot delete every witness.
   for(let i=a.length-1;i>=0;i--){let [J,b]=a[i];if(a.some(([K,h],j)=>j!==i&&h+dot(m,J&~K)<=b))a.splice(i,1)}
   return a;
 }
 const feasible=(rows,v)=>rows.every(([J,b])=>dot(v,J)<=b);
 function greedy(rows,m,J){let v=m.map(()=>0),credits=rows.map(x=>x[1]);for(let i=0;i<m.length;i++)if(J>>>i&1){let d=m[i];for(let j=0;j<rows.length;j++)if(rows[j][0]>>>i&1)d=Math.min(d,credits[j]);v[i]=d;for(let j=0;j<rows.length;j++)if(rows[j][0]>>>i&1)credits[j]-=d}return v}
 function components(rows,m){
   let B=greedy(rows,m,(1<<m.length)-1),parent=m.map((_,i)=>i),find=i=>{while(parent[i]!==i)i=parent[i];return i},join=(i,j)=>{i=find(i);j=find(j);if(i!==j)parent[j]=i};
   for(let i=0;i<m.length;i++)if(B[i]<m[i]){
     let tight=rows.filter(([J,b])=>(J>>>i&1)&&dot(B,J)===b);
     check(tight.length>0,"nonbasis not blocked");
     for(let j=0;j<m.length;j++)if(B[j]>0&&tight.every(([J])=>J>>>j&1))join(i,j);
   }
   let out=new Map();for(let i=0;i<m.length;i++)if(m[i]){let r=find(i);out.set(r,(out.get(r)||0)|(1<<i))}
   return [...out.values()].sort((a,b)=>a-b);
 }
 function transfer(rows,m,r,q){check(feasible(rows,r),"illegal selection");let mm=m.map((x,i)=>x-r[i]-q[i]);return norm(rows.map(([J,b])=>[J,b-dot(r,J)]),mm)}
 function fromPorts(c,E,m){let rows=[];for(let u=1;u<(1<<c.length);u++){let J=0;for(let i=0;i<E.length;i++)if(sub(E[i],u))J|=1<<i;rows.push([J,dot(c,u)-1])}return norm(rows,m)}
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
   for(let u=1;u<N;u++){cap[u]=dot(c,u);for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}
   const ok=new Uint8Array(M);
   for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
   let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
   const E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]),mult=vec(M-1),rows=fromPorts(c,E,mult);
   const maskOf=J=>H.reduce((s,h,i)=>s|((J>>>i&1)?h:0),0);
   const lift=(v,F)=>{let z=0;for(let i=0;i<H.length;i++){let h=H[i]&F;for(let j=0;j<v[i];j++){check(h!==0,"lift");let b=h&-h;z|=b;h^=b}}return z};
   function verifyState(R,F,rs,cs){
     let mm=vec(F),direct=mm.map((_,i)=>1<<i);
     for(let x=F;;x=(x-1)&F){
       let v=vec(x),actual=!!ok[R|x];check(feasible(rs,v)===actual,"cut language");
       check(cs.every(J=>!!ok[R|(x&maskOf(J))])===actual,"component product");
       if(x&&!actual){let circ=true;for(let b=x;b;b&=b-1)if(!ok[R|(x^(b&-b))]){circ=false;break}
         if(circ){let J=v.reduce((s,y,i)=>s|(y?1<<i:0),0),u=J;
           for(let i=0;i<mm.length;i++)if(J>>>i&1)u|=direct[i];
           for(let i=0;i<mm.length;i++)if(u>>>i&1)direct[i]=u;
         }
       }
       stats.minorSubsetChecks++;if(!x)break;
     }
     let expected=[...new Set(direct.filter((_,i)=>mm[i]))].sort((a,b)=>a-b);
     check(JSON.stringify(expected)===JSON.stringify(cs),"minimal class partition");stats.componentPartitionChecks++;
   }
   const cs=components(rows,mult);stats.initialRows+=rows.length;stats.initialComponents+=cs.length;if(cs.length>1)stats.modelsSplit++;
   let counts=new Set();
   for(let z=1;z<M;z++)if(!ok[z]){let yes=true;for(let b=z;b;b&=b-1)if(!ok[z^(b&-b)]){yes=false;break}if(yes)counts.add(vec(z).join(","))}
   stats.initialCountAtoms+=counts.size;verifyState(0,M-1,rows,cs);
   for(let tr=0;tr<8;tr++){
     let P=rnd(M),F=(M-1)^P,R1=rnd(M)&P,R2=rnd(M)&P;
     if(!ok[R1]||!ok[R2]){stats.minorRejected++;continue}
     let mm=vec(F),r1=transfer(rows,mult,vec(R1),vec(P^R1)),r2=transfer(rows,mult,vec(R2),vec(P^R2)),cc=components(r1,mm);
     stats.minorStates++;stats.minorRows+=r1.length;stats.minorComponents+=cc.length;if(cc.length>1)stats.minorSplit++;
     verifyState(R1,F,r1,cc);
     // S=r1 dominates T=r2 iff T's greedy rank on every S row fits S's credit.
     let pred=true,ref=true;
     for(let [J,b] of r1){
       let v=greedy(r2,mm,J),rank=sum(v),rr=0,mask=F&maskOf(J);
       for(let x=mask;;x=(x-1)&mask){if(ok[R2|x])rr=Math.max(rr,pop[x]);if(!x)break}
       check(rank===rr,"greedy rank");stats.greedyRankChecks++;
       if(rank>b){let w=lift(v,F);check(ok[R2|w]&&!ok[R1|w],"dominance witness");pred=false;break}
     }
     for(let x=F;;x=(x-1)&F){if(ok[R2|x]&&!ok[R1|x]){ref=false;break}if(!x)break}
     check(pred===ref,"dominance");stats.dominanceChecks++;if(!pred)stats.dominanceFailures++;
   }
   const value=z=>{let p=0,s=0;for(let j=0;j<m;j++)if(z>>>j&1){p+=A[j].p;s+=A[j].s}return{p,s,mask:z}};
   const options=h=>{let a=[],b=[];for(let j=0;j<m;j++)if(h>>>j&1)(A[j].s?b:a).push(j);a.sort((i,j)=>A[j].p-A[i].p||i-j);b.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=l=>{let o=[0];for(let j of l)o.push(o.at(-1)|(1<<j));return o};return pre(a).flatMap(x=>pre(b).map(y=>x|y))};
   const opts=H.map(options);stats.globalPrefixCandidates+=opts.reduce((p,a)=>p*a.length,1);
   function pareto(a){let best=new Map();for(let x of a){let old=best.get(x.s);if(!old||x.p>old.p)best.set(x.s,x)}let out=[],p=-1;for(let x of [...best.values()].sort((a,b)=>b.s-a.s)){if(x.p>p){out.push(x);p=x.p}}return out}
   let frontier=[value(0)];
   for(let J of cs){
     let ids=H.map((_,i)=>i).filter(i=>J>>>i&1),local=[];
     function rec(i,z){if(i===ids.length){stats.componentPrefixCandidates++;if(feasible(rows,vec(z)))local.push(value(z));return}for(let x of opts[ids[i]])rec(i+1,z|x)}
     rec(0,0);local=pareto(local);let next=[];for(let x of frontier)for(let y of local){next.push({p:x.p+y.p,s:x.s+y.s,mask:x.mask|y.mask});stats.convolutionPairs++}frontier=pareto(next);
   }
   let D=sum(A.map(x=>x.s)),best=Array(D+1).fill(-1);for(let z=0;z<M;z++)if(ok[z]){let x=value(z);best[D-x.s]=Math.max(best[D-x.s],x.p)}
   for(let b=1;b<=D;b++)best[b]=Math.max(best[b],best[b-1]);
   for(let b=0;b<=D;b++){let w=frontier.filter(x=>D-x.s<=b).sort((a,b)=>b.p-a.p)[0];check(w&&w.p===best[b],"component budget");stats.budgetChecks++;let x=value(w.mask);check(ok[w.mask]&&x.p===w.p&&x.s===w.s&&D-x.s<=b,"component witness");stats.witnessChecks++}
 }
 const choose=(n,k)=>{let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n-i+1)/BigInt(i);return v.toString()};
 for(let d=5;d<=10;d++){
   let all=(1<<d)-1,E=[];for(let i=0;i<d;i++)E.push(all^(1<<i));for(let i=0;i<d;i++)E.push(all^(1<<i)^(1<<((i+1)%d)));
   check(new Set(E).size===2*d,"distinct supports");
   let rows=fromPorts(Array(d).fill(1),E,Array(2*d).fill(1));check(rows.length===1&&rows[0][0]===(1<<(2*d))-1&&rows[0][1]===d-1,"uniform row");
   stats.uniformDistinct.push({ports:d,classes:2*d,rows:rows.length,countAntichain:choose(2*d,d)});
 }
 stats.uniformTheoreticalD30={ports:30,classes:60,rows:1,countAntichain:choose(60,30)};
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
