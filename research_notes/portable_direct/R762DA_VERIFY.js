"use strict";
// R762DA: exact positive N-BRC sparse named-state sampling verifier.
// Run: node R762DA_VERIFY.js (Node >= 18). Pure BigInt; no dependencies.
function gcd(a,b) { while(b!==0n) { const t=a%b; a=b; b=t; } return a; }
function gcdAll(xs) { return xs.reduce((a,b)=>gcd(a,b),0n); }
function c3(n,p,q) {
  let v=[1n,0n,0n];
  for(let t=0;t<n;t++) {
    const w=[];
    for(let j=0;j<3;j++) w[j]=p*v[(j+2)%3]+q*v[(j+1)%3];
    v=w;
  }
  return v;
}
function checkSchedules(C, maxH, weights) {
  let schedules=0,events=0,zeros=0;
  for(const [p,q] of weights) {
    const a=BigInt(p),b=BigInt(q);
    const cs=Array.from({length:maxH+1},(_,i)=>C(i,a,b));
    const D=a+b;
    for(let h=1;h<=maxH;h++) for(let mask=1;mask<(1<<h);mask++) {
      const ts=[];
      for(let t=1;t<=h;t++) if(mask&(1<<(t-1))) ts.push(t);
      const ds=ts.map((t,i)=>t-(ts[i-1]||0));
      let products=[1n], expected=1n;
      for(const d of ds) {
        const hist=cs[d];
        expected*=gcdAll(hist);
        const next=[];
        for(const x of products) for(const y of hist) next.push(x*y);
        products=next;
      }
      const actual=gcdAll(products);
      if(actual!==expected) throw Error("GCD failed: "+JSON.stringify({p,q,h,ts}));
      if(D**BigInt(ts[ts.length-1])%expected!==0n)
        throw Error("Noninteger budget");
      schedules++;
      events+=products.length;
      zeros+=products.filter(v=>v===0n).length;
    }
  }
  return {schedules,events,positiveEvents:events-zeros,zeroEvents:zeros};
}
const normalizedPairs=[];
for(let p=1;p<=6;p++)for(let q=1;q<=6;q++) {
  const z=gcd(BigInt(p),BigInt(q));
  normalizedPairs.push([Number(BigInt(p)/z),Number(BigInt(q)/z)]);
}
const cycle=checkSchedules(c3,8,normalizedPairs);
const permutations=[];
for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++)
  if(new Set([a,b,c]).size===3) permutations.push([a,b,c]);
const key=x=>x.join("");
const indices=Object.fromEntries(permutations.map((x,i)=>[key(x),i]));
const compose=(a,b)=>[a[b[0]],a[b[1]],a[b[2]]];
const gen=[[1,0,2],[1,2,0]].map(x=>indices[key(x)]);
const edges=permutations.map(x=>gen.map(j=>indices[key(compose(x,permutations[j]))]));
function s3(n,p,q) {
  let v=Array(6).fill(0n);
  v[indices["012"]]=1n;
  for(let t=0;t<n;t++) {
    const w=Array(6).fill(0n);
    for(let j=0;j<6;j++) {
      w[edges[j][0]]+=p*v[j];
      w[edges[j][1]]+=q*v[j];
    }
    v=w;
  }
  return v;
}
const s3pairs=[];
for(let p=1;p<=3;p++)for(let q=1;q<=3;q++) s3pairs.push([p,q]);
const nonabelian=checkSchedules(s3,6,s3pairs);
if(cycle.schedules!==18072 || cycle.positiveEvents!==669348 ||
   cycle.zeroEvents!==2476044 || nonabelian.schedules!==1080 ||
   nonabelian.events!==1235250) throw Error("Expected evidence totals changed");
const rows=[];
for(let t=1;t<=5;t++) {
  const g=gcdAll(c3(t,1n,2n))*gcdAll(c3(6-t,1n,2n));
  rows.push({times:[t,6],minSeeds:String(729n/g)});
}
if(rows.map(x=>x.minSeeds).join(",")!=="81,243,81,243,81") throw Error("Schedule example failed");
console.log(JSON.stringify({
  status:"PASS", arithmetic:"BigInt exact", model:"finite group positive right walk",
  c3:cycle, s3:nonabelian, twoTimeExample:rows,
  claim:"verified gcd factorization and denominator integrality in bounded domains",
  review:"NOT_REVIEWED", nativeEventAdmission:false
},null,2));
