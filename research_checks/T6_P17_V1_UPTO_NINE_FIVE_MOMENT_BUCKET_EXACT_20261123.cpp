// Exact five-moment p17-v1 profile injection through nine atoms, mass <=2331.
// Binary bucket-sort of 64-bit mixed-radix residues; independent generating-function domain count.
// Requires disk space for 389,844,237 64-bit signatures; run without a short time limit.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;
constexpr int CAP=2331,P=17,NMAX=9, B=256;
constexpr array<int,5> MOD={17,289,4913,83521,1419857};
constexpr array<uint64_t,10> EXPECTED={1,129,4220,62225,531399,3017496,12469599,39974384,104260287,229524497};
array<array<int,5>,138> ATOM{};
array<uint64_t,10> counted{};
array<uint64_t,B> bucket_count{};
array<FILE*,B> fp{};
uint64_t duplicates=0;
vector<uint64_t> witnesses;
int inverse(int a,int m){long long t=0,nt=1,r=m,nr=a; while(nr){long long q=r/nr, x=t-q*nt;t=nt;nt=x;x=r-q*nr;r=nr;nr=x;} assert(r==1); t%=m;if(t<0)t+=m;return (int)t;}
uint64_t encode(const array<int,5>&s){uint64_t key=0,place=1;for(int i=0;i<5;i++){key+=(uint64_t)s[i]*place;place*=MOD[i];}assert(place==2862423051509815793ULL);return key;}
void enumerate(int start,int n,int cost,const array<int,5>&sig){
 counted[n]++;
 uint64_t key=encode(sig);
 int b=(int)(key&255); bucket_count[b]++;
 if(fwrite(&key,sizeof(key),1,fp[b])!=1){fprintf(stderr,"fwrite failure\n");exit(2);}
 if(n==NMAX)return;
 for(int u=start;u<=137;u++){
  if(u%17==0)continue;
  int c=17*u-1; if(cost+c>CAP)break;
  array<int,5> nx;
  for(int i=0;i<5;i++){int val=sig[i]+ATOM[u][i]; nx[i]=val>=MOD[i]?val-MOD[i]:val;}
  enumerate(u,n+1,cost+c,nx);
 }
}
array<uint64_t,10> independent_counts(){
 static uint64_t dp[NMAX+1][CAP+1]{};dp[0][0]=1;
 for(int u=1;u<=137;u++){if(u%17==0)continue;int c=17*u-1;
  for(int n=1;n<=NMAX;n++)for(int m=c;m<=CAP;m++)dp[n][m]+=dp[n-1][m-c];
 }
 array<uint64_t,10> out{};for(int n=0;n<=NMAX;n++)for(int m=0;m<=CAP;m++)out[n]+=dp[n][m];return out;
}
int main(){
 for(int u=1;u<=137;u++){if(u%17==0)continue;for(int i=0;i<5;i++){int inv=inverse(u,MOD[i]);uint64_t pw=1;for(int j=0;j<=i;j++)pw=pw*inv%MOD[i];ATOM[u][i]=(int)pw;}}
 for(int i=0;i<B;i++){string filename="t6p17bucket_"+to_string(i)+".bin";fp[i]=fopen(filename.c_str(),"wb");if(!fp[i]){perror("fopen");return 2;}setvbuf(fp[i],nullptr,_IOFBF,65536);}
 enumerate(1,0,0,{});
 for(int i=0;i<B;i++)if(fclose(fp[i])){perror("fclose");return 2;}
 auto independent=independent_counts();
 fprintf(stderr,"Domain verification:\n");for(int n=0;n<=NMAX;n++){fprintf(stderr," n=%d recursion=%llu DP=%llu target=%llu\n",n,(unsigned long long)counted[n],(unsigned long long)independent[n],(unsigned long long)EXPECTED[n]);if(counted[n]!=EXPECTED[n]||independent[n]!=EXPECTED[n])return 3;}
 uint64_t total=0;for(auto n:counted)total+=n;
 fprintf(stderr,"Total %llu. Sorting 256 buckets...\n",(unsigned long long)total);
 for(int i=0;i<B;i++){
  string filename="t6p17bucket_"+to_string(i)+".bin";FILE*f=fopen(filename.c_str(),"rb");if(!f){perror("read open");return 4;}
  vector<uint64_t> arr(bucket_count[i]);
  if(fread(arr.data(),8,arr.size(),f)!=arr.size()){perror("read");return 5;}
  fclose(f);
  sort(arr.begin(),arr.end());
  for(size_t j=1;j<arr.size();j++)if(arr[j]==arr[j-1]){duplicates++;if(witnesses.size()<20)witnesses.push_back(arr[j]);}
  remove(filename.c_str());
  if(i%32==31)fprintf(stderr,"  buckets=%d / 256, duplicate pairs=%llu\n",i+1,(unsigned long long)duplicates);
 }
 printf("BY_N:");for(int n=0;n<=NMAX;n++)printf(" %d:%llu",n,(unsigned long long)counted[n]);
 printf("\nTOTAL=%llu UNIQUE=%llu COLLISION_PAIRS=%llu\n",(unsigned long long)total,(unsigned long long)(total-duplicates),(unsigned long long)duplicates);
 for(uint64_t w:witnesses)printf("COLLISION_KEY=%llu\n",(unsigned long long)w);
 return 0;
}
