function replay(){
 let seed=20261127;function rnd(n){seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return (seed>>>0)%n}
 let stats={models:0,feasibilityChecks:0,subsets:0,swapChecks:0,changedSwaps:0,budgets:0,strictGap:0,exact:0,disagreements:0};
 function check(ok,msg){if(!ok){stats.disagreements++;throw Error(msg)}}
 for(let z=0;z<400;z++){
  let n=1+rnd(4),m=1+rnd(7),d=1+rnd(5),cap=Array.from({length:n},()=>1+rnd(3)),h=cap.slice(),E=[],v=[],a=[];
  for(let j=0;j<m;j++){E.push(1+rnd((1<<n)-1));v.push(1+rnd(12));a.push(0)}
  for(let j=0;j<d;j++){let i=rnd(n);h[i]++;E.push(1<<i);v.push(0);a.push(1+rnd(9))}
  const L=m+d,S=(1<<L),C=a.reduce((x,y)=>x+y,0);
  let bounds=Array.from({length:1<<n},(_,W)=>h.reduce((t,c,i)=>t+((W>>i&1)?c:0),0)-1);
  const feasible=new Uint8Array(S),cost=new Int32Array(S),reward=new Int32Array(S);
  for(let U=0;U<S;U++){
   stats.subsets++;let ok=true;
   for(let W=1;W<(1<<n);W++){stats.feasibilityChecks++;let count=0;for(let j=0;j<L;j++)if((U>>j&1)&&((E[j]&W)===E[j]))count++;if(count>bounds[W]){ok=false;break}}
   feasible[U]=+ok;let cc=C,rr=0;for(let j=0;j<L;j++)if(U>>j&1){cc-=a[j];rr+=v[j]}cost[U]=cc;reward[U]=rr;
  }
  let opt=Array(C+1).fill(0);
  for(let U=0;U<S;U++)if(feasible[U])opt[cost[U]]=Math.max(opt[cost[U]],reward[U]);
  for(let b=1;b<=C;b++)opt[b]=Math.max(opt[b],opt[b-1]);
  function greedy(order){let U=0;for(let j of order){let T=U|(1<<j);if(feasible[T])U=T}return U}
  const act=Array.from({length:m},(_,i)=>i).sort((i,j)=>v[j]-v[i]||i-j),dum=Array.from({length:d},(_,i)=>m+i).sort((i,j)=>a[j]-a[i]||i-j);
  let order=act.concat(dum),U=greedy(order),start=U,trans=[];
  let ratios=[];for(let x of act)for(let y of dum)ratios.push([v[x],a[y]]);
  ratios.sort((p,q)=>p[0]*q[1]-q[0]*p[1]);
  ratios=ratios.filter((p,i)=>!i||p[0]*ratios[i-1][1]!==ratios[i-1][0]*p[1]);
  for(let [p,q] of ratios){
   const score=i=>q*v[i]+p*a[i];
   let target=order.slice().sort((i,j)=>score(j)-score(i)||(+(j>=m))-(+(i>=m))||i-j);
   for(let i=0;i<L;i++){let j=order.indexOf(target[i]);while(j>i){
    let x=order[j-1],y=order[j];check(score(x)===score(y),"non-tie swap");
    order[j-1]=y;order[j]=x;j--;let T=greedy(order);stats.swapChecks++;
    check(q*reward[U]-p*cost[U]===q*reward[T]-p*cost[T],"score change");
    if(T!==U){stats.changedSwaps++;let removed=U&~T,added=T&~U;
     check(removed===(1<<x)&&added===(1<<y),"nonlocal greedy change");
     check(cost[T]<=cost[U]&&reward[T]<=reward[U],"nonmonotone");
     if(cost[T]<cost[U]){check(x<m&&y>=m,"bad cross swap");trans.push({old:U,now:T,p,q,x,y});}
    }U=T;
   }}
  }
  check(cost[U]===0,"final not feasible at zero");
  for(let b=0;b<=C;b++){stats.budgets++;
   let F=start,ub=q0(),bound=0;
   function q0(){return reward[start]}
   if(cost[start]>b){let t=trans.find(t=>cost[t.old]>b&&cost[t.now]<=b);check(!!t,"missing crossing");F=t.now;
    let numerator=t.q*reward[F]+t.p*(b-cost[F]);ub=numerator/t.q;bound=v[t.x];
    check(numerator>=t.q*opt[b],"dual bound below opt");
    check(numerator-t.q*reward[F]<t.q*bound,"strict loss failed");
   }
   check(feasible[F]&&cost[F]<=b&&reward[F]<=opt[b]&&opt[b]<=ub,"budget check");
   if(opt[b]===reward[F])stats.exact++;else{stats.strictGap++;check(opt[b]-reward[F]<bound,"gap exceeds lost label")}
  }stats.models++;
 }
 return {seed:20261127,...stats}
}
console.log(JSON.stringify(replay()));
