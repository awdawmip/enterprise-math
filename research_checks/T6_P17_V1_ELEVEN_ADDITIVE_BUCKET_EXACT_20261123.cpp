// T6 exact p17-valuation-one profiles: stage-n11 additive full-signature enumeration.
// Complements prior T6_P17_V1_UPTO_TEN_FIVE_MOMENT_BUCKET_EXACT_20261123.cpp.
// Exact signature buckets written separately as "t6p17eleven_<b>.bin", b=0..255.
// Reproduce: run previous checker "emit" to get t6p17ten_<b>.bin; run this "emit11";
// concatenate per bucket with: cat t6p17eleven_<b>.bin >> t6p17ten_<b>.bin
// Then run previous checker "check 0 64", "check 64 128", "check 128 192",
// "check 192 256" on disjoint ranges. Only conclude after all phases pass.
// 17-adic five-coordinate signature and full per-side mass budget 2331.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;
constexpr int CAP=2331,NMAX=11,P=17,BUCKETS=256;
constexpr array<int,5> MOD={17,289,4913,83521,1419857};
constexpr array<uint64_t,NMAX+1> EXPECTED={
  1,129,4220,62225,531399,3017496,12469599,39974384,
  104260287,229524497,439058783,747018123
};
array<array<int,5>,138> atom{};
array<uint64_t,NMAX+1> counted{};
array<FILE*,BUCKETS> out{};
uint64_t needle=0,hits=0;
array<int,NMAX> chain{};
int invert(int a,int m){
 long long t=0,nt=1,r=m,nr=a;
 while(nr){long long q=r/nr,x=t-q*nt;t=nt;nt=x;x=r-q*nr;r=nr;nr=x;}
 assert(r==1);t%=m;return (int)(t<0?t+m:t);
}
uint64_t encode(const array<int,5>&s){
 uint64_t place=1,key=0;
 for(int k=0;k<5;k++){key+=place*s[k];place*=MOD[k];}
 assert(place==2862423051509815793ULL);return key;
}
void rec(int umin,int n,int mass,const array<int,5>&s,int mode){
 counted[n]++;
 auto key=encode(s);
 if(mode==1 && n==NMAX){
  int b=key&255;
  if(fwrite(&key,sizeof(key),1,out[b])!=1){perror("fwrite");exit(10);}
 }
 if(mode==2 && key==needle){
  printf("WITNESS n=%d mass=%d:",n,mass);
  for(int j=0;j<n;j++)printf(" %d",chain[j]);
  printf("\n");hits++;
 }
 if(n==NMAX)return;
 for(int u=umin;u<=137;u++){
  if(u%17==0)continue;
  int c=17*u-1;if(mass+c>CAP)break;
  array<int,5> nxt;
  for(int k=0;k<5;k++){int x=s[k]+atom[u][k];nxt[k]=x>=MOD[k]?x-MOD[k]:x;}
  chain[n]=u;
  rec(u,n+1,mass+c,nxt,mode);
 }
}
array<uint64_t,NMAX+1> dpcounts(){
 static uint64_t dp[NMAX+1][CAP+1]{};
 dp[0][0]=1;
 for(int u=1;u<=137;u++){
  if(u%17==0)continue;int c=17*u-1;
  for(int n=1;n<=NMAX;n++)
   for(int mass=c;mass<=CAP;mass++)dp[n][mass]+=dp[n-1][mass-c];
 }
 array<uint64_t,NMAX+1> ret{};
 for(int n=0;n<=NMAX;n++)for(int m=0;m<=CAP;m++)ret[n]+=dp[n][m];
 return ret;
}
string fname(int i){return "t6p17eleven_"+to_string(i)+".bin";}
int main(int argc,char**argv){
 if(argc<2)return 1;
 string mode=argv[1];
 if(mode=="check"){
  if(argc<4)return 2;
  int first=atoi(argv[2]),last=atoi(argv[3]);
  uint64_t total=0,dup=0;
  for(int b=first;b<last;b++){
   FILE*f=fopen(fname(b).c_str(),"rb");if(!f){perror("open");return 3;}
   if(fseek(f,0,SEEK_END)!=0)return 4;
   long len=ftell(f);rewind(f);if(len<0||len%8)return 5;
   vector<uint64_t> a((size_t)len/8);
   if(fread(a.data(),8,a.size(),f)!=a.size())return 6;
   fclose(f);sort(a.begin(),a.end());total+=a.size();
   for(size_t j=1;j<a.size();j++)if(a[j]==a[j-1]){
    dup++;printf("COLLISION bucket=%d key=%llu\n",b,(unsigned long long)a[j]);
   }
   printf("CHECKED bucket=%d size=%zu cumulative_duplicate_pairs=%llu\n",b,a.size(),(unsigned long long)dup);
  }
  printf("RANGE %d-%d total_keys=%llu duplicate_pairs=%llu\n",
    first,last-1,(unsigned long long)total,(unsigned long long)dup);
  return 0;
 }
 for(int u=1;u<=137;u++)if(u%17)for(int k=0;k<5;k++){
  int inv=invert(u,MOD[k]);uint64_t p=1;
  for(int j=0;j<=k;j++)p=p*inv%MOD[k];
  atom[u][k]=p;
 }
 if(mode=="emit11"){
  for(int b=0;b<BUCKETS;b++){
   out[b]=fopen(fname(b).c_str(),"wb");
   if(!out[b]){perror("open");return 7;}
   setvbuf(out[b],nullptr,_IOFBF,65536);
  }
  rec(1,0,0,{},1);
  for(int b=0;b<BUCKETS;b++)if(fclose(out[b]))return 8;
  auto d=dpcounts();uint64_t tot=0;
  for(int n=0;n<=NMAX;n++){
   printf("n=%d enumerated=%llu independent_DP=%llu expected=%llu\n",
     n,(unsigned long long)counted[n],(unsigned long long)d[n],
     (unsigned long long)EXPECTED[n]);
   if(counted[n]!=d[n]||d[n]!=EXPECTED[n])return 9;
   tot+=counted[n];
  }
  printf("EMIT_ELEVEN_COMPLETE traversed_profiles=%llu buckets=%d\n",
    (unsigned long long)tot,BUCKETS);
  return 0;
 }
 if(mode=="witness"){
  if(argc<3)return 11;needle=strtoull(argv[2],nullptr,10);
  rec(1,0,0,{},2);
  printf("WITNESS_TOTAL=%llu\n",(unsigned long long)hits);
  return 0;
 }
 return 12;
}
