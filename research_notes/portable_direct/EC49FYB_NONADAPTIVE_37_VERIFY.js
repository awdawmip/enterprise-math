'use strict';
// EC49FYB. Auxiliary Farey/P10/C11 only; frozen input BRC16943.
const assert=(x,m)=>{if(!x)throw Error(m)};
const mod=(a,n)=>(a%n+n)%n;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inv5=a=>{for(let x=1;x<5;x++)if(a*x%5===1)return x;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
 const value=h%5===0?5:mod(n*inv5(h%5),5);
 return slopes[`${h%2},${n%2}`].includes(value);
}
let dirs=0;const ms=new Set();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 dirs++;let x=-1,y=-1;
 scan:for(let xx=0;xx<10;xx++)for(let yy=0;yy<10;yy++)if(mod(c*xx-a*yy+1,10)===0){x=xx;y=yy;break scan}
 assert(x>=0,'no representative');let m=0;
 for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))m|=1<<t;
 ms.add(m);
}
const U=[...ms].sort((x,y)=>x-y);assert(dirs===72&&U.length===50&&!ms.has(0),'census');
const bitCount=x=>{let n=0;for(;x;x&=x-1)n++;return n};
const hits=x=>U.every(m=>(m&x)!==0);
const triples=[];let hitPairs=0,minWith5=11,minWith9=11,minWithBoth=11;
for(let T=0;T<(1<<10);T++)if(hits(T)){
 const n=bitCount(T),has5=!!(T&32),has9=!!(T&512);
 if(n<=2)hitPairs++;
 if(n===3)triples.push(T);
 if(has5)minWith5=Math.min(minWith5,n);
 if(has9)minWith9=Math.min(minWith9,n);
 if(has5&&has9)minWithBoth=Math.min(minWithBoth,n);
}
assert(hitPairs===0&&triples.join(',')==='7,13,145,259','hitting triple census');
assert(minWith5===4&&minWith9===4&&minWithBoth===5,'column inequality');
assert(ms.has(91)&&ms.has(123)&&((91^123)===32),'row 5 singleton pair');
assert(ms.has(101)&&ms.has(613)&&((101^613)===512),'row 9 singleton pair');
const colRows=[
 [0,4,7], [0,2,3], [0,4,7], [0,1,2], [0,1,8], [0,1,2],
 [0,4,7], [0,4,7], [2,5,6,8], [0,3,5,6,9], [0,3,6,9]
];
const sites=colRows.flatMap((rows,j)=>rows.map(t=>[t,j]));
assert(sites.length===37&&new Set(sites.map(([t,j])=>11*t+j)).size===37,'37 distinct positions');
assert(colRows.every(rows=>hits(rows.reduce((s,t)=>s|(1<<t),0))),'column hits');
const row5=sites.filter(([t])=>t===5).map(x=>x[1]);
const row9=sites.filter(([t])=>t===9).map(x=>x[1]);
assert(new Set(row5).size===2&&new Set(row9).size===2,'two columns for each special row');
const states=[];for(const u of U)for(let z=-1;z<11;z++)states.push({u,z});
assert(states.length===600,'states');
const read=(s,t,j)=>Number(!!(s.u&(1<<t))&&s.z!==j);
const signatures=new Map();let singles=0,signatureOneCnt=Infinity,signatureMaxCnt=0;
for(let id=0;id<states.length;id++){
 const s=states[id];let value=0n,ones=0;
 for(let k=0;k<sites.length;k++){
  let x=read(s,...sites[k]);ones+=x;
  if(x)value|=1n<<BigInt(k);
 }
 assert(!signatures.has(value),'collision '+id+' '+signatures.get(value));
 signatures.set(value,id);signatureOneCnt=Math.min(signatureOneCnt,ones);signatureMaxCnt=Math.max(signatureMaxCnt,ones);
 if(s.z===-1)singles++;
}
// Distinct 37-bit signatures check each one of the 600 choose 2 pairs.
const all=[...signatures.keys()];let pairChecks=0;
for(let i=0;i<all.length;i++)for(let j=i+1;j<all.length;j++){
 assert((all[i]^all[j])!==0n,'pair collision');pairChecks++;
}
assert(pairChecks===179700&&signatures.size===600,'full pair verification');
const output={schema:'EC49FYB_NONADAPTIVE_FAREY_37_V1',date:'2026-11-23',frozen_scientific_pin:'BRC16943',
 status:'ALL_PASS',domain:{direction_representatives:dirs,support_masks:U.length,states:states.length,physical_sites:110},
 lower_bound:{min_column_hitting_number:3,all_hitting_triples:triples,
  min_hitting_including_row5:minWith5,min_hitting_including_row9:minWith9,
  min_hitting_including_both:minWithBoth,
  forcing_pairs:[{masks:[91,123],different_row:5},{masks:[101,613],different_row:9}],
  min_columns_querying_row5:2,min_columns_querying_row9:2,
  formula:'11*3 + 2 + 2 = 37'},
 upper_bound:{nonadaptive_sites:sites.length,column_row_sets:colRows,
  unique_signatures:signatures.size,checked_state_pairs:pairChecks,
  min_observed_ones:signatureOneCnt,max_observed_ones:signatureMaxCnt},
 result:'N_nonadaptive=37; Q_adaptive in [14,15] by EC49FYA; adaptation saves at least 22 reads in worst-case'};
console.log(JSON.stringify(output,null,2));
