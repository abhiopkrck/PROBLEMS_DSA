#include <iostream>
using namespace std;

int main(){
    int arr[]={11,31,45,67,19,56};
    
    int n=sizeof(arr)/sizeof(arr[0]);

    int even=0;
    
    for(int i=0;i<n;i++){
        if(arr[i] %2==0){
            even+=1;
        }
    }
    cout<<"Even:"<<even;
    return 0;
}