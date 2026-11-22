// EC49FXA finite certificate checker: pure exact integer / BigInt arithmetic.
// BRC16943, inherited frozen P10 / CRT observer; no floating point.
"use strict";
const HEX = [
  "0040002004100100000000000000",
  "1010048200310000000000000000",
  "00b0004024700200000000000000",
  "0306520208028500000000000000",
  "0fe480f006000000000000000000",
  "034c07c209920c00000000000000",
  "0c3e061147c0a200000000000000",
  "040ce7870e326300000000000000",
  "07fff011f8000700000000000000",
  "0c7cff39c0706300000000000000",
  "3410a5d0273063802109a00c6040",
  "0016bfca00311b00216f84000216",
  "0874ff5e0e23031029ce80000006",
  "3c31fe594819438823e420803080",
  "0014ffe848bb6b00006ec00066d6",
  "3ff01e09c1b83f81e03c03836000",
  "0e1f7f5e4877db0408ec80800686",
  "3c00bffffc3fff80014000007ec0",
  "3c7cfffe4e7b639821ce800060c0",
  "3fffffffffffff80000000000000",
  "3df4f6ffce93ff98c1ede0002046",
  "383efff17bbf639039dee08466c6",
  "3d77ff5b6fbfdba0e3fe220030b2",
  "2d77ff7d7fbf5bd8ebceb09c2081",
  "3fb6dfffffb7ff3021b80fc063e2",
  "35ffffffff3e7b88b90ef09e64c6",
  "3dffffffeff7bf80ffe00fd0007e",
  "3fefffffffff7b1cc9ce7394e886",
  "3fffffffffffffbfffff22000002",
  "3fffffffffffff98380e0f9fe7c6",
  "3dd6ff73bf9ffffba9fee77f37ff",
  "3db6fffbebbf7bfb6dfff7d77ef7",
  "3dbbfffdfbf7fefb77ffdbf76ff5",
  "3e3fffdfffffdff47f7fbffdff97",
  "3fffbfdfdf7ffbff7f7fbf9efff7",
  "3f3fffdffffedffe7fffbffffdbf",
  "37ffffffefffffedfeffffdffff7",
  "3fffffffffffffffeffff7fefaff",
  "3fffffffffffffffffeeffffffff",
  "3fffffffffffffffffffffffffff"
];
function assert(ok, why) { if (!ok) throw new Error(why); }
function verify(hex, r) {
 const mask = BigInt("0x"+hex), sites = [];
 assert((mask >> 110n) === 0n, "site range");
 for (let t=0;t<110;t++) if (((mask >> BigInt(t)) & 1n) !== 0n) sites.push(t);
 const h=r+Math.ceil(r/10), lower=Math.ceil(5*h/2);
 assert(sites.length===lower, "optimal size at r="+r);
 let min=Infinity, minAt=null;
 for (const d of [0,1]) for (let i=0;i<5;i++) for (let j=0;j<11;j++){
  let distance=0;
  for (const t of sites) {
   if (t%5===i && t%11!==j) distance++;
   if (((d-t+110)%5)===i && ((d-t+110)%11)!==j) distance++;
  }
  if (distance<min) {min=distance; minAt=[d,i,j];}
 }
 assert(min>=r, "distance at r="+r+": "+min);
 return {r, h, optimum:sites.length, observed_min_distance:min, minimizer:minAt, mask_hex:hex};
}
const rows=HEX.map((hex,i)=>verify(hex,i+1));
for(let r=1;r<=40;r++) {
 const h = r+Math.ceil(r/10);
 assert(h-Math.ceil(h/11)>=r, "h upper");
 assert((h-1)-Math.ceil((h-1)/11)<r,"h minimal");
}
const output = {
 research_unit:"EC49FXA",
 frozen_pin:"BRC16943",
 relative_phase_set:[0,1],
 physical_sites:110,
 check_count:40*2*5*11,
 model:"two independent Boolean channel bits per activation; one mod11 deletion",
 theorem:"N_fixed({0,1};r)=ceil(5*(r+ceil(r/10))/2), 1<=r<=40; impossible for r>=41",
 rows,
 status:"ALL_PASS",
 review:"AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED"
};
if (typeof console!=="undefined") console.log(JSON.stringify(output,null,2));
