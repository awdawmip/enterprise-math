'use strict';
// EC49FYD: exact full-factor state certificate theorem under frozen BRC16943.
// No third-party packages. Rebuild the 72-to-50 P10 atlas and check all 50 certificates.
const compute = function compute(){
'use strict';
const assert=(v,m)=>{if(!v)throw new Error(m)};
const mod=(a,b)=>(a%b+b)%b;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inv5=x=>{for(let i=1;i<5;i++)if(i*x%5===1)return i;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
const P=(h,n)=>{h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;return slopes[`${h%2},${n%2}`].includes(h%5===0?5:mod(n*inv5(h%5),5))};
const M=new Set();let directions=0;
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 directions++;let point=null;
 for(let x=0;x<10&&!point;x++)for(let y=0;y<10;y++)if(mod(c*x-a*y+1,10)===0){point=[x,y];break}
 assert(point!==null,'missing line representative');
 let u=0;for(let t=0;t<10;t++)if(P(point[0]+a*t,point[1]+c*t))u|=1<<t;
 M.add(u);
}
const masks=[...M].sort((a,b)=>a-b);assert(directions===72&&masks.length===50&&!M.has(0),'P10 frozen atlas mismatch');
const states=[];for(const u of masks)for(let z=-1;z<11;z++)states.push({u,z});
const W=(s,t,j)=>Number((s.u&(1<<t))!==0&&s.z!==j);
let checked=0;const groups={'0':[],'1':[],'2':[],'3':[]};let maxCert=0;const certificates=[];
function popcount(n){let c=0;for(;n;n&=n-1)c++;return c}
for(const u of masks){
 const supersets=masks.filter(v=>v!==u&&(v&u)===u);
 const extras=supersets.map(v=>v&~u);
 let tau=11,hits=[];
 for(let r=0;r<1024;r++)if(extras.every(e=>(e&r)!==0)){
    const k=popcount(r);if(k<tau){tau=k;hits=[r]}else if(k===tau)hits.push(r);
 }
 assert(tau>=0&&tau<=3&&hits.length>0,'transversal enumeration');
 const supp=[];for(let t=0;t<10;t++)if(u&(1<<t))supp.push(t);
 assert(supp.length>0&&supp.length<=11,'support bound');
 const sites=[];for(let j=0;j<11;j++)sites.push(11*supp[j%supp.length]+j);
 for(let t=0;t<10;t++)if(hits[0]&(1<<t))sites.push(11*t);
 assert(sites.length===11+tau&&new Set(sites).size===sites.length,'certificate length');
 const s={u,z:-1};
 for(const a of states){
    if(a.u===u&&a.z===-1)continue;
    assert(sites.some(k=>W(s,Math.floor(k/11),k%11)!==W(a,Math.floor(k/11),k%11)),'certificate fails '+u);
    checked++;
 }
 groups[tau].push(u);maxCert=Math.max(maxCert,sites.length);
 certificates.push({mask:u,tau,minimum_hitting_sets:hits.length,one_hitting_rows:Array.from({length:10},(_,t)=>t).filter(t=>hits[0]&(1<<t)),certificate_sites:sites});
}
assert(groups[0].length===22&&groups[1].length===17&&groups[2].length===8&&groups[3].length===3,'tau group census');
assert(JSON.stringify(groups[3])===JSON.stringify([101,788,833]),'hard masks mismatch');
const hard={};for(const u of [101,788,833]){
 const extras=masks.filter(v=>v!==u&&(v&u)===u).map(v=>v&~u);
 const hits=[];for(let r=0;r<1024;r++)if(popcount(r)===3&&extras.every(e=>r&e))hits.push(r);
 hard[u]={minimal_hit_sets:hits.map(h=>Array.from({length:10},(_,t)=>t).filter(t=>h&(1<<t))),support_rows:Array.from({length:10},(_,t)=>t).filter(t=>u&(1<<t))};
}
assert(hard[101].minimal_hit_sets.length===6&&hard[788].minimal_hit_sets.length===4&&hard[833].minimal_hit_sets.length===8,'hard census');
assert(!hard[788].support_rows.includes(1)&&hard[788].minimal_hit_sets.every(s=>!s.includes(1)),'row1 forbidden');
return {schema:'EC49FYD_FULL_FACTOR_CERTIFICATE_HITTING_V1',frozen_science:'BRC16943',date:'2026-11-23',
 status:'ALL_PASS',domain:{primitive_directions:directions,support_masks:50,states:600,columns:11,sites:110},
 theorem:'For every nonzero support U, C((U,-1)) = 11 + tau(U); tau is minimum hitting-set size of differences V\\U over strict mask supersets V.',
 distribution:groups,max_full_factor_certificate:maxCert,
 checked_full_factor_to_other_state_pairs:checked,
 hard_masks:hard,certificates};
};
console.log(JSON.stringify(compute(), null, 2));
