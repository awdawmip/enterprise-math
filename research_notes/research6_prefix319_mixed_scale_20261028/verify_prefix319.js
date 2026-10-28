#!/usr/bin/env node
"use strict";
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t}return a||1n}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denom");if(d<0n){n=-n;d=-d}const g=gcd(n,d);return {n:n/g,d:d/g}}
const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d), sub=(a,b)=>F(a.n*b.d-b.n*a.d,a.d*b.d);
const mul=(a,b)=>F(a.n*b.n,a.d*b.d),div=(a,b)=>F(a.n*b.d,a.d*b.n);
const eq=(a,b)=>a.n===b.n&&a.d===b.d, fmt=a=>a.d===1n?String(a.n):a.n+"/"+a.d;
const neg=a=>F(-a.n,a.d), bounded=(a,m)=>abs(a.n)*m.d<=m.n*a.d;
const C=(re=0,im=0)=>({re:F(re),im:F(im)}),CC=(re,im)=>({re,im});
const ca=(a,b)=>CC(add(a.re,b.re),add(a.im,b.im));
const cn=a=>CC(neg(a.re),neg(a.im));
const cs=(a,b)=>ca(a,cn(b));
const cj=a=>CC(a.re,neg(a.im));
const cm=(a,b)=>CC(sub(mul(a.re,b.re),mul(a.im,b.im)),add(mul(a.re,b.im),mul(a.im,b.re)));
const cd=(a,k)=>CC(div(a.re,F(k)),div(a.im,F(k)));
const ce=(a,b)=>eq(a.re,b.re)&&eq(a.im,b.im);
const norm=a=>add(mul(a.re,a.re),mul(a.im,a.im));
const str=a=>[fmt(a.re),fmt(a.im)];
function chk(x,m){if(!x)throw Error(m)}
const A=[[C(4),C(4),C(0)],[C(0),C(-4),C(4)],[C(-5,3),C(0),C(-3,1)],[C(-2,-2),C(4,4),C(2,2)],[C(-2),C(0),C(5,2)]];
const b0=[C(-2),C(0,-2),C(1)],b2=[C(0,2),C(2),C(0,-1)];
const t0=CC(F(-7,14),F(3,14)),t2=CC(F(-7,14),F(-3,14));
const a0=b0.map(x=>cm(t0,x)), a2=b2.map(x=>cm(t2,x));
function port(state,j){let v=C();for(let k=0;k<3;k++)v=ca(v,cd(cm(A[j][k],state[k]),8));return v}
function paths(state,j){return state.map((x,k)=>["source:"+String(k+1),cd(cm(A[j][k],x),8)])}
let masses=0,pairs=0;
function BRC(state,j,ref){
 const p=paths(state,j);if(ref==="1")p.push(["reference:1",C(1)]);if(ref==="i")p.push(["reference:i",C(0,1)]);
 let value=C();
 for(const [label,v] of p)for(const [other,w] of p)value=ca(value,cm(v,cj(w)));
 chk(eq(value.im,F(0))&&value.re.n>=0n,"not a positive real BRC mass");
 masses++;pairs+=p.length*p.length;return value.re;
}
function observe(state){return {Q0:A.map((_,j)=>BRC(state,j,"0")),Q1:A.map((_,j)=>BRC(state,j,"1")),Qi:A.map((_,j)=>BRC(state,j,"i"))}}
const O=observe(a0),P=observe(a2);
const u0=A.map((_,j)=>port(b0,j)),u2=A.map((_,j)=>port(b2,j));
const expectedNorm=["2","5/4","37/32","25/8","85/64"];
for(let j=0;j<5;j++){
 chk(eq(norm(u0[j]),norm(u2[j]))&&fmt(norm(u0[j]))===expectedNorm[j],"base shape port mismatch");
 chk(eq(O.Q0[j],P.Q0[j]),"Q0 unequal");
}
let gram=0;
for(let k=0;k<3;k++)for(let l=0;l<3;l++){
 let v=C();for(let j=0;j<5;j++)v=ca(v,cm(cj(A[j][k]),A[j][l]));v=cd(v,64);
 chk(eq(v.im,F(0))&&eq(v.re,k===l?[F(31,32),F(1),F(63,64)][k]:F(0)),"Gram");
 gram++;
}
const D=A.map((_,j)=>cs(port(a0,j),port(a2,j)));
const E=[CC(F(1),F(1)),CC(F(-6,7),F(-6,7)),CC(F(-3,7),F(-1,14)),CC(F(0),F(1)),CC(F(-1,4),F(-11,28))];
for(let j=0;j<5;j++){
 chk(ce(D[j],E[j])&&bounded(D[j].re,F(1))&&bounded(D[j].im,F(1)),"reference bands");
 chk(eq(sub(O.Q1[j],P.Q1[j]),mul(F(2),D[j].re)),"Q1 identity");
 chk(eq(sub(O.Qi[j],P.Qi[j]),mul(F(2),D[j].im)),"Qi identity");
}
const cross=ca(cm(cj(u0[0]),u2[0]),cm(cj(u0[3]),u2[3]));
chk(ce(cross,CC(F(1),F(7,8)))&&eq(add(norm(u0[0]),norm(u0[3])),F(41,8)),"Port1+4 analytic bound");
const dist2=a0.reduce((v,x,k)=>add(v,norm(cs(x,a2[k]))),F(0));
chk(eq(dist2,F(240,49))&&eq(norm(t0),F(29,98))&&eq(norm(t2),F(29,98)),"r and distance");
chk(masses===30&&pairs===410,"BRC operation counts");
const Y={Q0:O.Q0.map(fmt),Q1:O.Q1.map((x,j)=>fmt(div(add(x,P.Q1[j]),F(2)))),
 Qi:O.Qi.map((x,j)=>fmt(div(add(x,P.Qi[j]),F(2))))};
const certificate={verdict:"PASS",arithmetic:"BigInt Gaussian rational tagged BRC",
 source_states:{a0:a0.map(str),a2:a2.map(str)},
 squared_scale:"29/98",r:"sqrt(58)/14",
 universal_exclusion_for_r_above:"4/sqrt(41-sqrt(113))",
 same_five_Q0:true,reference_interval_intersections:10,
 port_amplitude_differences:D.map(str),common_report:Y,
 port1_and_4_cross:str(cross),
 minimum_enclosing_ball_squared:fmt(div(dist2,F(4))),
 gram_entries:gram,source_tagged_masses:masses,ordered_path_pairs:pairs,
 classification:"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED",
 native_X6_Detector_bridge:"UNPROVEN"};
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
certificate;
