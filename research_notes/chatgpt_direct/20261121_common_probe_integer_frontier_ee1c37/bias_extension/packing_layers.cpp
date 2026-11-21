#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
struct O {int c,d,h;};
constexpr int K=11,T=18,INF=1000000,M=10,H=12;
int limit(int m){return m>=4?3:m==3?4:m==2?6:m==1?7:11;}
int main(int argc,char**argv){if(argc!=3)return 2;ifstream in(argv[1]);int n,cap=stoi(argv[2]);in>>n;array<vector<O>,13> opts;int mn[13];fill(mn,mn+13,INF);
 for(int i=0;i<n;i++){int s,c,d;in>>s>>c>>d;int deficit=13-s;mn[deficit]=min(mn[deficit],c);if(s==11&&c==1059){opts[deficit].push_back({c,179,1});opts[deficit].push_back({c,33,0});}else opts[deficit].push_back({c,d,0});}
 for(auto& v:opts)sort(v.begin(),v.end(),[](auto a,auto b){return a.c<b.c;});
 int least[K+1][T+1];for(auto&r:least)fill(r,r+T+1,INF);least[0][0]=0;for(int k=1;k<=K;k++)for(int d=0;d<=T;d++)for(int s=0;s<=min(12,d);s++)least[k][d]=min(least[k][d],least[k-1][d-s]+mn[s]);
 size_t stride=cap+1,plane=(T+1)*stride,total=M*H*plane;vector<int16_t>a(total,-1),b(total,-1);a[0]=0;uint64_t states=0,updates=0;
 for(int k=0;k<K;k++){fill(b.begin(),b.end(),-1);for(int m=0;m<=min(k,M-1);m++)for(int h=0;h<=min(k-m,limit(m));h++)for(int d=0;d<=T;d++){int hi=cap-least[K-k][T-d];if(least[k][d]>hi)continue;size_t base=((m*H+h)*(T+1)+d)*stride;for(int c=least[k][d];c<=hi;c++){int old=a[base+c];if(old<0)continue;states++;for(int s=0;s<=min(12,T-d);s++){int nm=m+(s==0);if(nm>=M)continue;int nd=d+s,maxc=cap-least[K-k-1][T-nd];if(maxc<c+mn[s])continue;for(auto o:opts[s]){int nc=c+o.c;if(nc>maxc)break;int nh=h+o.h;if(nh>limit(nm))continue;auto& v=b[((nm*H+nh)*(T+1)+nd)*stride+nc];if(old+o.d>v){v=old+o.d;updates++;}}}}}a.swap(b);}
 int global=-1;for(int c=0;c<=cap;c++){int v=-1;for(int m=0;m<M;m++)for(int h=0;h<=min(limit(m),c<11925?6:11);h++)v=max(v,int(a[((m*H+h)*(T+1)+T)*stride+c]));if(v>=0)cout<<c<<" "<<v<<"\n";global=max(global,v);}cerr<<"states "<<states<<" updates "<<updates<<" memory "<<total*4<<" cap_max "<<global<<"\n";
}
