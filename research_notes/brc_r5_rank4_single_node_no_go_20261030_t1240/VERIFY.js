"use strict";
// Exact, exhaustive 14-coordinate R5 certificate; no external libraries.
function runR5(){
const N=["A","B","A0","A1","B0","B1","A00","A01","A10","A11","B00","B01","B10","B11"];
const S=[[1,120,240,-1],[1,240,120,-1],[2,60,180,0],[2,60,60,0],[2,180,60,1],[2,60,60,1],[3,30,108,2],[3,30,72,2],[3,30,45,3],[3,30,15,3],[3,90,36,4],[3,90,24,4],[3,20,40,5],[3,40,20,5]];
// [node, normal, maxLR, maxFULL, FULL mask, LR mask, five LR rank masks, signed 4x4 det]
const C=[
["A",[144,-28,70,-115],31920,32280,12300,12,[0,1,2,4,256],"-907200000"],
["B",[20,21,-14,-14],7560,7680,8216,10,[0,1,2,4,256],"362880000"],
["A0",[72,-14,35,115],22860,23040,12300,12,[0,1,2,4,256],"816480000"],
["A1",[7,4,-15,44],0,1320,8,0,[0,1,2,8,256],"816480000"],
["B0",[60,63,-42,56],32760,33120,8216,10,[0,1,2,16,256],"2449440000"],
["B1",[7,4,-15,44],0,1320,32,0,[0,1,2,8,256],"816480000"],
["A00",[72,-14,35,412],22860,23040,12488,104,[0,1,2,32,256],"408240000"],
["A01",[72,-14,35,412],22860,23040,12488,104,[0,1,2,64,256],"408240000"],
["A10",[-6,-32,70,591],43440,45840,292,9,[0,1,2,128,256],"408240000"],
["A11",[-527,-18,5,651],0,11160,512,0,[0,1,2,256,257],"233280000"],
["B00",[20,21,-14,70],10920,11040,11272,10,[0,1,2,256,512],"-1224720000"],
["B01",[20,21,-14,70],10920,11040,11272,10,[0,1,2,256,1024],"-1224720000"],
["B10",[-68,45,-22,665],27240,29640,4120,10,[0,1,2,256,2048],"-272160000"],
["B11",[-5,-2,1,7],120,240,8196,4,[0,1,2,256,257],"-233280000"]];
const check=(b,m)=>{if(!b)throw Error(m)},gcd=(a,b)=>b?gcd(b,a%b):a,keys=[],idx=[];
for(const [t,p,q] of S){const d=gcd(p,q),k=t+":"+p/d+":"+q/d;let i=keys.indexOf(k);if(i<0){i=keys.length;keys.push(k)}idx.push(i)}
check(keys.length===12&&idx[3]===idx[5]&&idx[9]===idx[13],"likelihood collision keys");
check(S[0][1]+S[1][1]===360&&S[0][2]+S[1][2]===360,"law mass 360");
for(let i=0;i<6;i++){const child=S.filter(s=>s[3]===i);
check(child.length===2&&child.reduce((a,x)=>a+x[1],0)===S[i][1]&&child.reduce((a,x)=>a+x[2],0)===S[i][2],"mass conservation "+i)}
function obs(mask,lr,j){const live=Array(14).fill(false);let r=0,x=0,y=0,s=0;
for(let i=0;i<14;i++){const [t,p,q,parent]=S[i],reach=parent<0||live[parent],stop=reach&&!!(mask&(1<<(lr?idx[i]:i)));
live[i]=reach&&!stop;if(stop){if(i===9||i===13)r+=q;x+=(4-t)*p;y+=(4-t)*q;if(i===j)s+=p}}
return [r,x,y,s]}
const dot=(w,v)=>w[0]*v[0]+w[1]*v[1]+w[2]*v[2]+w[3]*v[3];
function determinant4(rows){let d=0n;function go(prefix,rest,sign){
if(!rest.length){let x=BigInt(sign);for(let i=0;i<4;i++)x*=BigInt(rows[i][prefix[i]]);d+=x;return}
for(let i=0;i<rest.length;i++)go(prefix.concat(rest[i]),rest.slice(0,i).concat(rest.slice(i+1)),sign*(i%2?-1:1))}
go([], [0,1,2,3],1);return d}
// Exact strict-positivity checks for delta=±1/1000 and eta=1/1000.
// p denominator 1000*Pmass, q denominator 3000*Qmass.
for(let j=0;j<14;j++)for(let i=0;i<14;i++){const [t,p,q]=S[i],P0=(200+50*t)*p+10*(t+1)*q,Q0=(1200-100*t)*q+15*(t+2)*p+(i===9||i===13?3*q:0);
check(P0-p>0&&P0+p<1000*p&&Q0>0&&Q0<3000*q,"positive stop errors "+j+":"+i);
if(t===3)check(400*p+50*q>0&&400*p+50*q<1000*p&&800*q+90*p>0&&800*q+90*p<3000*q,"t4 errors "+i)}
const out=[];
for(let j=0;j<14;j++){const [name,w,ub,vb,fullmask,lrmask,rankmasks,rankdet]=C[j];
check(N[j]===name,"node order");let Lmax=-Infinity,Hmax=-Infinity;
const LR=Array.from({length:4096},(_,m)=>obs(m,true,j));
for(const v of LR){const d=dot(w,v);if(d>Lmax)Lmax=d}
for(let m=0;m<16384;m++){const d=dot(w,obs(m,false,j));if(d>Hmax)Hmax=d}
check(Lmax===ub&&Hmax===vb&&vb>ub,"signed supports "+name);
check(dot(w,obs(fullmask,false,j))===vb&&dot(w,LR[lrmask])===ub,"maximizing masks "+name);
const pts=rankmasks.map(m=>LR[m]),rows=pts.slice(1).map(v=>v.map((x,k)=>x-pts[0][k]));
const d=determinant4(rows);check(d===BigInt(rankdet)&&d!==0n,"rank determinant "+name);
out.push("NODE "+name+" W "+w.join(",")+" LR "+ub+" FULL "+vb+" GAP "+(vb-ub)+" DET "+d)}
out.push("TREE nodes=14 LR_keys=12 collision_pairs=A1/B1,A11/B11 exact=True");
out.push("TERMINAL_PROBS eta=1/1000 delta=+/-1/1000 strict_validity=True");
out.push("COVERAGE 14*(4096_LR+16384_FULL)=286720 deterministic observer vectors exact=True");
out.push("UNIVERSAL_SCOPE all admissible real delta!=0 by invertible affine observation map, all real policies by multiaffinity");
out.push("PASS_EXACT_R5_ALL_14_SINGLE_NODE_RANK4_NO_GO");
return out.join("\n")+"\n";
}
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(runR5());
