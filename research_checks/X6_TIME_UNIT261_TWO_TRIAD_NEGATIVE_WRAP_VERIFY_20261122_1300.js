'use strict';
// Exact replay + independent breadth-first shortest-distance/count verification of Unit261.
const fs=require('fs');
const cert=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const B=80,W=2*B+1,N=13*13*W*W,P=12;
const basis=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
const x=[];for(let r=0;r<6;r++){x[2*r]=basis[r];x[2*r+1]=basis[r].map((v,k)=>v+basis[(r+1)%6][k]);}x[P]=[0,0,0];
const key=(a,b,u,v)=>((a*13+b)*W+u+B)*W+v+B;
function unkey(k){const v=k%W-B;k=(k-v-B)/W;const u=k%W-B;k=(k-u-B)/W;return [Math.floor(k/13),k%13,u,v];}
function moves(s,i,j){return s===P?[[j,0]]:[[(s+1)%12,1],[(s+11)%12,-1],...(s===i?[[P,0]]:[])];}
function assert(ok,msg){if(!ok)throw Error(msg);}
function signed(from,to){const d=x[to].map((v,k)=>v-x[from][k]);assert(d.filter(v=>v!==0).length===1&&d.every(v=>Math.abs(v)<=1),'nonprimitive X6 step');return d;}
function replay(c){let a=0,b=2,u=0,v=0;for(const ch of c.route){
  const who=ch===ch.toUpperCase()?0:1,to=ch.charCodeAt(0)-(who===0?65:97),from=who===0?a:b;
  assert(to>=0&&to<=12,'route token');assert(to!==(who===0?b:a),'target collision');
  assert(!(who===0&&from===0&&to===11),'forbidden A negative wrap');
  const step=moves(from,c.ingress,c.egress).find(([t])=>t===to);assert(step,'invalid Port/OUTER event');signed(from,to);
  if(who===0){a=to;u+=step[1];}else{b=to;v+=step[1];}
}assert(a===0&&b===2&&u===-12&&v===12,'wrong original two-triad target');assert(c.route.length===c.restricted_min_events,'route length');}
function bfs(i,j){const ds=new Int16Array(N);ds.fill(-1);const q=new Int32Array(N);const counts=new Map();
  const start=key(0,2,0,0),goal=key(0,2,-12,12);ds[start]=0;q[0]=start;counts.set(start,1n);let head=0,tail=1;
  while(head<tail){const p=q[head++],d=ds[p];if(p===goal)break;
    const [a,b,u,v]=unkey(p);
    for(let w=0;w<2;w++)for(const [t,delta] of moves(w===0?a:b,i,j)){
      if(t===(w===0?b:a)||(w===0&&a===0&&t===11))continue;
      const uu=u+(w===0?delta:0),vv=v+(w===1?delta:0);
      if(Math.abs(uu)>B||Math.abs(vv)>B)continue;
      const h=key(w===0?t:a,w===1?t:b,uu,vv);
      if(ds[h]<0){ds[h]=d+1;counts.set(h,counts.get(p));q[tail++]=h;}
      else if(ds[h]===d+1)counts.set(h,counts.get(h)+counts.get(p));
    }
  }
  assert(ds[goal]>=0&&ds[goal]<B,'exact BFS bound');return [ds[goal],counts.get(goal).toString()];}
const rows=cert.cases;assert(rows.length===15,'fifteen i<j Ports');
let unchanged=0;
for(const c of rows){assert(c.ingress<c.egress,'wrong orientation');replay(c);const [cost,n]=bfs(c.ingress,c.egress);assert(cost===c.restricted_min_events&&n===c.shortest_histories,'shortest cost/count mismatch');assert(c.extra_events===cost-c.original_min_events,'baseline difference');if(c.extra_events===0)unchanged++;}
assert(unchanged===5,'same-cost count');assert(JSON.stringify(signed(0,11))===JSON.stringify([0,0,-1]),'P000 one-based -E3 axis');
console.log(JSON.stringify({status:'PASS',cases:rows.length,cost_unchanged:unchanged,native_vector:signed(0,11)}));
