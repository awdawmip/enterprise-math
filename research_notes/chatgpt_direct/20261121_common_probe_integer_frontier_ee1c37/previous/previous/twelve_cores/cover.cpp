#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using U=uint64_t;using M=__uint128_t;
int at(M x){return U(x)?countr_zero(U(x)):64+countr_zero(U(x>>64));}
int pc(M x){return popcount(U(x))+popcount(U(x>>64));}
struct Row{M m;int size,rc,price;};long long nodes=0;vector<Row> chosen,solution;
bool solve(M f,int k,int slack,const vector<Row>& pool){
 ++nodes;if(!f)return !k;if(k<1)return false;
 vector<Row>active;array<int,125>d{},low;low.fill(100000000);int mins[14];fill(mins,mins+14,100000000);
 for(auto r:pool){if(r.rc>slack||(r.m&~f))continue;
 if(k==1){if(r.m==f){solution=chosen;solution.push_back(r);return true;}continue;}
 active.push_back(r);mins[r.size]=min(mins[r.size],r.rc);int rate=r.rc/r.size;
 for(M t=r.m;t;t&=t-1){int b=at(t);d[b]++;low[b]=min(low[b],rate);}}
 if(k==1)return false;
 int sum=0,pivot=at(f),n=pc(f);
 for(M t=f;t;t&=t-1){int b=at(t);if(!d[b])return false;if(d[b]<d[pivot])pivot=b;sum+=low[b];}
 if(sum>slack)return false;
 int dp[13][126];fill(&dp[0][0],&dp[0][0]+13*126,100000000);dp[0][0]=0;
 for(int h=1;h<k;h++)for(int s=0;s<=13;s++)if(mins[s]<100000000)for(int a=s;a<=n;a++)dp[h][a]=min(dp[h][a],dp[h-1][a-s]+mins[s]);
 for(auto r:active)if((r.m>>pivot)&1){if(r.rc+dp[k-1][n-r.size]>slack)continue;
 int val=sum;for(M t=r.m;t;t&=t-1)val-=low[at(t)];if(val+r.rc>slack)continue;
 chosen.push_back(r);if(solve(f^r.m,k-1,slack-r.rc,active))return true;chosen.pop_back();}
 return false;
}
int main(int argc,char**argv){
 ifstream rows(argv[1],ios::binary),weights(argv[2]),input(argv[3]);int budget=stoi(argv[4]),w[126];for(int&v:w)weights>>v;
 U a,b;input>>a>>b;M full=(M(b)<<64)|a;int labels=stoi(argv[5]);int objective=labels*w[125];for(M t=full;t;t&=t-1)objective+=w[at(t)];
 int slack=1000*budget-objective;vector<Row>all;int s,c;long long material=0;
 struct Rec{unsigned char pts[13];unsigned char size;uint16_t price;};Rec rr;while(rows.read((char*)&rr,sizeof(rr))){M f=0;for(int i=0;i<rr.size;i++)f|=M(1)<<rr.pts[i];s=rr.size;c=rr.price;int rc=1000*c-w[125];for(M t=f;t;t&=t-1)rc-=w[at(t)];if(rc<0)return 2;
 if(rc<=slack)all.push_back({f,s,rc,c});material++;}
 if(slack>=0)solve(full,labels,slack,all);
 cout<<objective<<" "<<material<<" "<<all.size()<<" "<<nodes<<" "<<solution.size();
 for(auto r:solution)cout<<" "<<U(r.m)<<" "<<U(r.m>>64);cout<<endl;
}
