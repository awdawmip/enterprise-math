"use strict";
// PREFIX-844 independent exact BigInt checker; run with node.
function run() {
 const gcd=(a,b)=>{while(b){const r=a%b;a=b;b=r}return a};
 const lcm=(a,b)=>a/gcd(a,b)*b;
 const eff=(m,c)=>m/gcd(m,c);
 const cop=(m,c)=>{for(let k=2n;k*k<=c;k++)if(c%k===0n){while(c%k===0n)c/=k;while(m%k===0n)m/=k}if(c>1n)while(m%c===0n)m/=c;return m};
 const ok=(x,s)=>{if(!x)throw Error(s)};
 const z={familyCount:0,observerCases:0,orderedAssignments:0,unorderedPairs:0,monoChecks:0,longHorizonChecks:0,allExactAssertionsPassed:true,domain:"p=1..3,W=2..3,a,b=1..3,t=1..7,m1,m2=1..9; temporal stabilization at t=28"};
 for(let p=1;p<=3;p++)for(let W=2;W<=3;W++){
  const N=W**p,S=Array.from({length:p},(_,i)=>W**i).reduce((a,b)=>a+b,0);
  for(let a=1;a<=3;a++)for(let b=1;b<=3;b++){
   z.familyCount++;
   for(let m1=1;m1<=9;m1++)for(let m2=1;m2<=9;m2++){
    const x=BigInt(m1),y=BigInt(m2),M=lcm(x,y),Linf=cop(M,BigInt(a*b));
    let prev=null;
    for(let t=1;t<=7;t++){
     const c=BigInt(a)**BigInt(Math.floor(t/2))*BigInt(b)**BigInt(Math.floor((t-1)/2));
     const L=lcm(eff(x,c),eff(y,c));
     ok(L===eff(M,c),"joint lcm");if(prev!==null){ok(prev%L===0n,"time nesting");z.monoChecks++}prev=L;
     const sig=[];
     for(let u=0;u<N;u++){const U=BigInt(u),v=c*(BigInt(S)+U);sig.push(String(v%x)+":"+String(v%y));ok(U===U%L+(U/L)*L,"repair");z.orderedAssignments++}
     const counts=new Map();for(const v of sig)counts.set(v,(counts.get(v)||0)+1);
     ok(counts.size===Math.min(N,Number(L)),"classes");
     ok(Math.max(...counts.values())===Math.ceil(N/Number(L)),"largest fiber");
     for(let u=0;u<N;u++)for(let v=u+1;v<N;v++){ok((sig[u]===sig[v])===(BigInt(v-u)%L===0n),"fiber");z.unorderedPairs++}
     z.observerCases++;
    }
    const c=BigInt(a)**14n*BigInt(b)**13n;
    ok(eff(M,c)===Linf,"terminal coprime part");z.longHorizonChecks++;
   }
  }
 }
 const observations=Array.from({length:4},(_,u)=>({U:u,mod4:Number(4n*(3n+BigInt(u))%4n),mod5:Number(4n*(3n+BigInt(u))%5n)}));
 ok(observations.every(q=>q.mod4===0)&&new Set(observations.map(q=>q.mod5)).size===4,"late channel");
 z.restorationWitness={p:2,W:2,a:2,b:1,t:4,S:3,N:4,observations};
 return z;
}
console.log(JSON.stringify(run(),null,2));
