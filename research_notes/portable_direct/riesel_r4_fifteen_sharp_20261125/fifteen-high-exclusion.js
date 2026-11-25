
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const weight=n=>{let w=0;for(let p=2;p<=n;p++)for(;n%p===0;n/=p)w+=p-1;return w;};
const h0=Array.from({length:35840},(_,i)=>i+1).filter(h=>weight(h/gcd(h,35))<=10);
const scale=h0.map(h=>h/gcd(35,h)).reduce(lcm,1);
const eligible=h0.filter(h=>h>=9&&h!==10);
const fixed=[[2,1],[3,1],[4,2]];
const rows=[0,1,2,3,5];
const bits=(mask,arr)=>arr.filter((_,i)=>(mask>>i)&1);
const assert=(test,message)=>{if(!test)throw Error(message);};
const surviving=new Map;
const branches=[];
for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=bits(f,fixed), R=bits(r,rows);
  const k=11-F.length-R.length;
  if(k<1)continue;
  const L=F.reduce((n,[m])=>lcm(n,m),35);
  const D=Array.from({length:L},(_,i)=>i).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
  if(D.length===0)continue;
  const candidate=new Map;
  for(const h of eligible){
    const g=gcd(h,L),m=h/g;
    if(weight(m)>k-1)continue;
    const incidence=Array(g).fill(0);
    for(const x of D)incidence[x%g]++;
    assert(scale%m===0,'mass scale');
    const mass=Math.max(...incidence)*(scale/m);
    if(mass)candidate.set(h,mass);
  }
  const best=Math.max(0,...candidate.values()), survivors=[];
  for(const [h,mass] of candidate){
    
    let m=h/gcd(h,L), cap=mass+(k-1-weight(m))*best;
    for(let p=2;p<=m;p++){
      for(let power=p;m%p===0;power*=p,m/=p){
        const constrained=Math.max(0,...Array.from(candidate).filter(([v])=>v/gcd(v,L)%power===0).map(([,value])=>value));
        cap+=(p-1)*constrained;
      }
    }
    if(cap<D.length*scale)continue;
    survivors.push(h);
    if(!surviving.has(h))surviving.set(h,[]);
    surviving.get(h).push({F,R,k,L});
  }
  branches.push({F,R,k,L,remain:D.length,survivors});
}




const factors=n=>{const a=[];for(let p=2;p<=n;p++)if(n%p===0){let j=1;do{n/=p;j*=p;}while(n%p===0);a.push([p,j]);}return a;};
const mod=(x,n)=>(x%n+n)%n;
const eg=(a,b)=>b?((([g,x,y])=>[g,y,x-Math.floor(a/b)*y])(eg(b,a%b))):[a,1,0];


function neighbors(h,L,P,x){  const ds=factors(h).flatMap(([p,H])=>{
   const Pp=factors(P).find(([q])=>p===q)[1], v=L%p?1:factors(L).find(([q])=>p===q)[1];
   const q0=P/Pp, t0=q0*mod(eg(q0,Pp)[1],Pp);
   const out=[];
   for(let u=v;u<H;u*=p)for(let j=1;j<p;j++)out.push(mod(t0*u*j,P));
   return out;
  });

return ds.map(d=>(x+d)%P);}

const pop32=x=>{x-=(x>>>1)&0x55555555;x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24;};
const pc=x=>{let n=0;while(x){n+=pop32(Number(x&0xffffffffn));x>>=32n;}return n;};
function prove(B,t,limit=100000,reverse=false){
 const {i,L,P,k,D,hs}=B,{h,x,neighbors}=t;
 const points=[],seen=new Set;
 function add(n){if(n%h===x%h||seen.has(n))return;seen.add(n);points.push(n);}
 for(const n of neighbors)add(n);
 for(let j=0;j<3;j++)for(const d of D)add(d+j*L);
 let rounds=0,total=0;
 for(;rounds<1000;rounds++){
  const raw=new Map;
  for(let i=0;i<points.length;i++){
    const n=points[i], bit=1n<<BigInt(i);
    for(const g of hs){
      const b=n%g;if(x%g===b)continue;
      const id=g*100000+b;
      raw.set(id,(raw.get(id)??0n)|bit);
    }
  }
  const q=new Map;
  for(const [id,mask] of raw)if(!q.has(mask))q.set(mask,id);
  let O=Array.from(q,([m,id])=>({m,id,n:pc(m)}));
  O.sort((a,b)=>b.n-a.n||(reverse?b.id-a.id:a.id-b.id));
  // On the finite witness set, dominated masks can be replaced by their superset.
  O=O.filter((o,j)=>!O.slice(0,j).some(z=>(o.m&z.m)===o.m));
  const X=(1n<<BigInt(points.length))-1n;
  const at=points.map((_,i)=>{const bit=1n<<BigInt(i);return {i,bit,O:O.filter(o=>o.m&bit)}}).sort((a,b)=>a.O.length-b.O.length||(reverse?b.i-a.i:a.i-b.i));
  const cap=[0];for(let n=0;n<k-1;n++)cap.push(cap[n]+(O[n]?.n??0));
  const cache=Array.from({length:k},()=>new Set);
  const choices=[];
  function dfs(todo,r,n){
   if(++total>limit)return -1;
   if(todo===0n)return 1;
   if(!r||n>cap[r]||cache[r].has(todo))return 0;
   const p=at.find(o=>o.bit&todo);
   for(const o of p.O){
    if(o.n+cap[r-1]<n)break;
    const added=pc(todo&o.m);
    if(added+cap[r-1]<n)continue;
    const a=dfs(todo&~o.m,r-1,n-added);
    if(a===1){choices.push(o.id);return a;}
    if(a===-1)return a;
   }
   cache[r].add(todo);return 0;
  }
  const yes=dfs(X,k-1,points.length);
  if(yes!==1)return {i,h,x,yes,rounds,total,w:points};
  const classes=choices.map(id=>[Math.floor(id/100000),id%100000]);
  classes.push([h,x%h]);
  let j=0;
  search:for(let y=0;y<P;y+=L)for(const d of D){
    const n=y+d;
    if(!classes.some(([p,b])=>n%p===b)){add(n);if(++j===8)break search;}
  }
  if(!j)return {i,h,x,yes:1,rounds,total,classes};
 }
 return {i,h,x,yes:-1,rounds,total};
}

const threshold=Number(typeof process==='undefined'?2240:process.argv[2]??2240);
const reverse=typeof process!=='undefined'&&process.argv[3]==='reverse';
const byPeriod={};
let total=0,maxRounds=0,maxPoints=0,pass=0,fail=0,liveBranches=0;
const examples=[];
for(const [i,v] of branches.entries()){
 if(!v.survivors.some(h=>h>threshold))continue;
 ++liveBranches;
 const {F,R,k,L,survivors:hs}=v;
 const D=Array.from({length:L},(_,x)=>x).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
 const P=hs.reduce(lcm,L), b={i,L,P,k,D,hs};
 for(const h of hs)if(h>threshold){
  for(const x of D){
   const q={h,x,neighbors:neighbors(h,L,P,x)};
   const z=prove(b,q,1000000,reverse);
   if(z.yes===-1)throw Error('incomplete '+JSON.stringify(z));
   total+=z.total;maxRounds=Math.max(maxRounds,z.rounds);maxPoints=Math.max(maxPoints,z.w?.length??0);
   (byPeriod[h]??=[0,0])[z.yes]++;
   if(z.yes===0)fail++;
   else{pass++;if(examples.length<16)examples.push(z);}
  }
 }
}
console.log(JSON.stringify({threshold,reverse,liveBranches,fail,pass,total,maxRounds,maxPoints,byPeriod,examples},null,2));
