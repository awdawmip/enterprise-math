function verifyBRC(){
  const P={AU:[9n,11n],AV:[5n,5n],BU:[3n,27n],BV:[30n,30n]},Q={AU:10n,AV:20n,BU:15n,BV:15n};
  const bits={AU:[1,1],AV:[1,-1],BU:[-1,1],BV:[-1,-1]},leaf=[];
  for(const s of Object.keys(P))for(let j=0;j<2;j++)for(let k=0;k<2;k++)leaf.push({s,j,k,p:P[s][j],q:Q[s],h:[...bits[s],j===0?1:-1,k===0?1:-1]});
  function check(b,m){if(!b)throw Error("ASSERT "+m)}
  const sum=a=>a.reduce((x,y)=>x+y,0n),abs=a=>a<0n?-a:a;
  check(leaf.length===16,"16 branches");
  check(sum(leaf.map(x=>x.p))===240n&&sum(leaf.map(x=>x.q))===240n,"normalization");
  check(leaf.every(x=>x.p>0n&&x.q>0n),"positive carrier");
  check(new Set(leaf.map(x=>x.h.join(","))).size===16,"X6 unique path words");
  const cls={},keys=[];
  for(const s of Object.keys(P))for(let j=0;j<2;j++){const r=P[s][j]+"/"+Q[s];cls[s+j]=r;if(!keys.includes(r))keys.push(r)}
  check(keys.length===6,"six LR classes");
  const W=Object.fromEntries(keys.map(k=>[k,Number(BigInt(k.split("/")[0])>BigInt(k.split("/")[1]))]));
  const event=(law,d)=>sum(leaf.filter(x=>d[cls[x.s+x.j]]===1).map(x=>x[law]));
  check(event("p",W)===196n&&event("q",W)===110n,"Hahn event 196/110");
  check(sum(leaf.map(x=>abs(x.p-x.q)))===172n,"full TV=43/120");
  check(sum(leaf.map(x=>x.p>x.q?x.p-x.q:0n))===86n,"positive signed mass");
  const cyl=h=>sum(leaf.filter(x=>h.every((v,i)=>x.h[i]===v)).map(x=>x.p+x.q));
  for(const x of leaf){let h=[],a=1n,b=1n;for(const v of x.h){const c=cyl(h),d=cyl([...h,v]);check(c>0n&&d>0n&&d<c,"Markov probs");a*=d;b*=c;h.push(v)}check(480n*a===b*(x.p+x.q),"midpoint telescopes")}
  check(sum(leaf.map(x=>abs(2n*x.p-(x.p+x.q))))===172n,"P midpoint radius");
  check(sum(leaf.map(x=>abs(2n*x.q-(x.p+x.q))))===172n,"Q midpoint radius");
  let maximum=0n,attain=0;
  for(let mask=0;mask<64;mask++){const d=Object.fromEntries(keys.map((k,i)=>[k,(mask>>i)&1]));const p=event("p",d),q=event("q",d),tv=abs(p-q);if(tv>maximum)maximum=tv;if(tv===86n)attain++;check(tv<=86n,"TV contraction");check(abs(2n*p-p-q)<=86n&&abs(2n*q-p-q)<=86n,"midpoint terminal");}
  check(maximum===86n&&attain===2,"64 legal classifiers");
  check(P.AU[1]===11n&&P.AU[0]+P.AU[1]===20n&&P.BU[1]===27n&&P.BU[0]+P.BU[1]===30n,"conditional prepared AU BU");
  check(P.AV[0]===P.AV[1]&&P.BV[0]===P.BV[1],"AV BV uniform J");
  return "PASS_BRC_N4_LAWFUL_S23_SIGN_WITNESS_20261031\n16 positive source-labelled BRC branches, two normalized laws, 4-step X6 words: PASS\nLegal T3 Decision=P event: P=196/240 Q=110/240; TV=43/120\nSource-blind midpoint prefix kernel sharp uniform lawful-policy minimax: 43/240\n64 S23 deterministic T3 ratio-class classifiers: max TV=43/120; attaining="+attain+"\nStage-2 retained-S statewise lawful future classes=2+1+2+1=6\nAuthor exact integer check only; native physical transition NOT TESTED";
}
process.stdout.write(verifyBRC()+'\n');
