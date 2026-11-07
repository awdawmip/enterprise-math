/* Exact S23 finite-policy scan; frozen input 43ec6098b1330ae86d0a7863be336c5d97f6ef34. */
'use strict';
const N=50400, M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1], B=[2,2,3,2,2,4], C=[5,6,7,8,9,10], G=[0,0,1,2,2,3];
const PAIRS=['34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12','12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14'];
const FREE=['5/7 0 2/7 0;3/7 0 2/7 2/7;3/7 0 1/35 19/35;3/7 10/21 0 2/21','11/21 10/21 0 0;10/21 11/21 0 0;1/21 10/21 0 10/21;0 0 11/21 10/21','1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 1/2 0;1/2 0 1/2 0'];
function assert(x,m){if(!x)throw Error(m)}
function value(s){const [a,b='1']=String(s).split('/').map(Number), x=a*N/b;assert(Number.isSafeInteger(x),'fraction '+s);return x}
function mix(rows){return M.map((w,i)=>Array.from({length:4},(_,j)=>{let x=w.reduce((v,t,s)=>v+t*rows[s][j],0)/20;assert(Number.isSafeInteger(x),'mix '+i);return x}))}
function decoder(rows){return mix(G.map(g=>rows[g]))}
const PAIR=s=>s.split(' ').map(x=>[1,2,3,4].map(k=>N*[...x].filter(t=>Number(t)===k).length/2));
const KERNEL=s=>s.split(';').map(r=>r.trim().split(/\s+/).map(value));
const bank=PAIRS.filter((_,i)=>i!==4).map(s=>decoder(PAIR(s))).concat(FREE.map(s=>decoder(KERNEL(s))));
function prepare(z){const source=A.map((a,s)=>{const x=z[a],b=z[B[s]],c=z[C[s]],r=N-x,q=r*(N-b)/N,t=q*c/N;assert(Number.isSafeInteger(q)&&Number.isSafeInteger(t),'causal rational');return [x,r*b/N,t,q-t]});return mix(source)}
function risks(p){return bank.map(q=>Math.max(...p.map((row,i)=>row.reduce((sum,v,j)=>sum+Math.abs(v-q[i][j]),0))))}
function minrisk(p){return Math.min(...risks(p))}
function ratio(x){let a=x,b=2*N;const gcd=(x,y)=>y?gcd(y,x%y):x;let d=gcd(a,b);return `${a/d}/${b/d}`}
function scan(base){const total=base**11;let max=0,countMax=0,countAbove=0,at4sevenths=0;
 for(let id=0;id<total;id++){let k=id,z=[];for(let j=0;j<11;j++){const v=k%base;k=Math.floor(k/base);z.push(v*N/(base-1))}const r=minrisk(prepare(z));
  if(r>max){max=r;countMax=0}if(r===max)countMax++;if(r*7>8*N)countAbove++;if(r*7===8*N)at4sevenths++}
 return {total,max:ratio(max),maximizer_count:countMax,above_4_7:countAbove,at_4_7:at4sevenths}}
function edges(){let max=0,above=0,first=null,total=0;
 for(let free=0;free<11;free++)for(let bits=0;bits<1024;bits++){let z=[],shift=0;for(let j=0;j<11;j++)z.push(j===free?0:((bits>>shift++)&1)*N);
 for(let t=1;t<8;t++){z[free]=t*N/8;const r=minrisk(prepare(z));total++;if(r>max)max=r;if(r*7>8*N){above++;if(!first)first={free_index_0based:free,binary_other_coordinates:bits,free_value:`${t}/8`,risk:ratio(r)}}}}
 return {total,max:ratio(max),above_4_7:above,first}}
const J=t=>prepare([N,value(t),0,0,0,0,0,0,0,N,0]);
const binary=scan(2),ternary=scan(3),edge=edges(),sharp=risks(J('17/63')).map(ratio);
assert(binary.total===2048&&binary.max==='4/7'&&binary.maximizer_count===64&&binary.above_4_7===0,'binary result');
assert(ternary.total===177147&&ternary.max==='4/7'&&ternary.maximizer_count===972&&ternary.above_4_7===0,'ternary result');
assert(edge.total===78848&&edge.max==='5/8'&&edge.above_4_7===256,'edge result');
assert(sharp[4]==='40/63'&&sharp[7]==='40/63','critical J risk');
console.log(JSON.stringify({pass:'PASS_BRC_S23_GRID_AND_ONE_FREE_COORDINATE_20261102',pin:'43ec6098b1330ae86d0a7863be336c5d97f6ef34',scale:N,bank_order:['D1','D2','D3','D4','D6','D7','D8','K1','K2','K3'],binary,ternary,one_fractional_coordinate_eighth_grid:edge,J_at_17_63_risks:sharp,arithmetic:'safe exact integers; rational denominator 50400 and TV denominator 100800; 6 original source mixtures, shared b_U'},null,2));
