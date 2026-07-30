#include <iostream>

using namespace std;

int main(){
    int arr[]={12,13,14,15,16};
    int target=14;
    int n=sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<n;i++){
        if(arr[i] ==target){
            cout<<" found ";
        }
    }
    
    return 0;
}