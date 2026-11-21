'use strict';
// Independent integer-only check of the nine-dimensional sign data for
// the conditional R70 star-moment difference observer (no native physics).
const ids=[[1,0,0],[0,1,0],[0,0,1]];
const z= [ [0,0,0], [0,0,0], [2,6,12], [6,24,60], [14,78,252] ];
const B=[];
for(let i=1;i<=4;i++)for(let j=i+1;j<=4;j++)B.push(z[j].map((x,k)=>x-z[i][k]));
const rows=[...ids,...B];
const dot=(u,v)=>u.reduce((acc,x,i)=>acc+x*v[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const gcd=(a,b)=>b===0?Math.abs(a):gcd(b,a%b);
function normalize(v){let g=v.reduce((a,b)=>gcd(a,b),0);if(!g)return null;let w=v.map(x=>x/g);let f=w.find(x=>x!==0);if(f<0)w=w.map(x=>-x);return w;}
const keys=new Set();for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++){let v=normalize(cross(rows[i],rows[j]));if(v)keys.add(v.join(','));}
const axes=[...keys].map(s=>s.split(',').map(Number));
const rays=axes.flatMap(v=>[v,v.map(x=>-x)]);
const q=v=>Math.max(v.reduce((a,x)=>a+Math.max(x,0),0),v.reduce((a,x)=>a+Math.max(-x,0),0));
const s=v=>rows.map(r=>Math.sign(dot(v,r)));
const sig=rays.map(s);
function agree(i,j){return sig[i].every((x,k)=>x*sig[j][k]>=0);}
let ntrip=0,mx=0, witness=null;
for(let i=0;i<rays.length;i++)for(let j=i+1;j<rays.length;j++)if(agree(i,j))for(let k=j+1;k<rays.length;k++)if(agree(i,k)&&agree(j,k)){ntrip++;let val=q(rays[i])+q(rays[j])+q(rays[k]);if(val>mx){mx=val;witness=[rays[i],rays[j],rays[k]];}}
const pass=keys.size===28 && rays.length===56 && Math.max(...rays.map(q))===125 && ntrip===212 && mx===235;
if(!pass)throw new Error(JSON.stringify({lines:keys.size,rays:rays.length,ntrip,mx}));
process.stdout.write(JSON.stringify({status:'PASS',lines:keys.size,oriented_rays:rays.length,compatible_triples:ntrip,max_port_sum:mx,universal_bound:Math.max(...rays.map(q),mx-1),witness})+'\n');
