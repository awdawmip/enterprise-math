#!/usr/bin/env node
'use strict';
const L='acdefg',N={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]},D=[[0,0,0,0],[0,1,0,0],[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]];
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const B=[0,0,4,1,16,32,8,2,0];
function native(v,c){return v.map(q=>{let s=Math.floor(q/3),p=q%3;for(let b of N[c]){if(p===1&&b===2){if(s===0)s=1;else if(s===2)s=4;}else if(p===2&&b===1){if(s===0)s=2;else if(s===1)s=3;}p=b===1?1:b===2?2:0;}return 3*s+p;});}
function check(){
 const init=[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[3,0],[4,0]].map(([s,p])=>3*s+p);
 const q=[init],ids=new Map([[init.join(','),0]]);
 for(let i=0;i<q.length;i++)for(let c of L){const w=native(q[i],c),k=w.join(',');if(!ids.has(k)){ids.set(k,q.length);q.push(w);}}
 if(q.length!==12)throw Error('raw state count');
 for(let i=0;i<12;i++)for(let j=0;j<6;j++)if(Math.min(ids.get(native(q[i],L[j]).join(',')),8)!==T[Math.min(i,8)][j])throw Error('native quotient');
 const words=['de','ed','ce','ec','feg','gef'];
 for(let j=0;j<6;j++){let v=init;for(let c of words[j])v=native(v,c);if(B[Math.min(ids.get(v.join(',')),8)]!==1<<j)throw Error('signature');}
 if(B[T[0][4]]===B[T[1][4]]||B[T[0][4]]===B[T[8][4]]||B[T[1][1]]===B[T[8][1]])throw Error('minimality witnesses');
 return {raw_states:12,minimal_states:9,checked_transitions:72};
}
function rank(m){return !!((m&18)&&(m&20)&&(m&33)&&(m&40));}
function main(maxh=13){
 const certificate=check(),rows=[];let dp=new Map([['0,0,0,0,0',1n]]);
 for(let h=1;h<=maxh;h++){
 const nd=new Map();
 for(let [k,n] of dp){let [e,r,f,g,s]=k.split(',').map(Number);for(let j=0;j<6;j++){let a=D[j],v=[e+a[0],r+a[1],f+a[2],g+a[3],T[s][j]].join(',');nd.set(v,(nd.get(v)||0n)+n);}}
 dp=nd;if(h<2)continue;
 let legal=0n,allowed=0n,masks=new Map();
 for(let [k,n] of dp){let [e,r,f,g,s]=k.split(',').map(Number);if(2*e+r+f+g!==h+1)continue;
 legal+=n;if(!B[s])continue;allowed+=n;let x=[2*e+r+f,r+g,e].join(',');masks.set(x,(masks.get(x)||0)|B[s]);}
 let raw=[];
 for(let x=0;x<=h+1;x++)for(let y=0;y<=h+1;y++)for(let z=1;2*z<=h+1;z++)if(Math.max(x-1,y+2*z-1)<=h&&h<=x+y-1)raw.push([x,y,z].join(','));
 rows.push({h,endpoint_words:legal.toString(),allowed_words:allowed.toString(),raw_keys:raw.length,allowed_keys:masks.size,rank9_keys:[...masks.values()].filter(rank).length,without_allowed:raw.filter(k=>!masks.has(k)),dp_states:dp.size});
 }
 let old=[[8,6,3,3,1],[51,38,7,6,4],[304,206,13,13,9],[1770,1062,22,21,17],[10224,5352,34,34,28],[58947,26644,50,49,43],[340064,131686,70,70,62],[1964862,647930,95,94,86]];
 for(let i=0;i<8;i++){let p=rows[i],a=[+p.endpoint_words,+p.allowed_words,p.raw_keys,p.allowed_keys,p.rank9_keys];if(a.some((x,j)=>x!==old[i][j]))throw Error('Historical census mismatch '+p.h);}
 return {schema:'EC49FAX_MINIMAL_X6_OBSERVER_V1',date:'2026-11-05',scientific_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',prior_commit:'bf0262d78004110a10372faa531b9fdfbb5c80d7',certificate,alphabet:L,table:T,signature_bits:B,original_census_H2_H9_pass:true,census:rows};
}
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(main(Number(process.argv[2]||13)),null,2));
if(typeof module!=='undefined')module.exports=main;
