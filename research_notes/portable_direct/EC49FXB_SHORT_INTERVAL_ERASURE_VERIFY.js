"use strict";
// EC49FXB exact finite CRT two-channel checker (no dependencies).
const S8=[64,68,69,81,87,90,100,108], S9=[60,70,81,88,91,92,93,94,109], S10=[0,1,2,3,4,5,6,7,8,9];
function count(S,d,i,j){
 let v=0;
 for (const t of S) {
  if (t%5===i && t%11!==j)v++;
  if (((d-t+110)%5)===i && ((d-t+110)%11)!==j)v++;
 }
 return v;
}
const output=[];
let checks=0;
for(let k=1;k<=55;k++){
 const sites=k<=2?S8:k<=4?S9:S10;
 let min=Infinity;
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
  const n=count(sites,d,i,j);if(n<min)min=n;checks++;
  if(n<2)throw Error("failed k="+k+", d="+d+",i="+i+",j="+j);
 }
 const optimum=k<=2?8:k<=4?9:10;
 if(sites.length!==optimum)throw Error("bad size k="+k);
 output.push({k,optimal_sites:optimum,minimum_sampled_distance:min});
}
if(checks!==84700)throw Error("wrong constraint count "+checks);
if(typeof console!=="undefined")console.log(JSON.stringify({checks,all_pass:true,rows:output},null,2));
