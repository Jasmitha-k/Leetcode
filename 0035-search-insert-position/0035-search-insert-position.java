class Solution {
    public int searchInsert(int[] nums, int target) {

        int n=nums.length,c=0;
        for(int i=0;i<n;i++){
            if(target==nums[i]){
                c=i;
                break;
            }
        }
        if (c==0){
            if(target<nums[0]){
                c=0;
            }
            else if(target > nums[n-1]){
                c=n;
            }
            else if(n==2){
               if(nums[0]<target && target<nums[1]){
                c=1;
               }
            }
            else{
                for(int i=1;i<n-1;i++){
                    if(target>nums[i] && target<nums[i+1]){
                        c=i+1;
                    }
                    else if(target<nums[i] && target>nums[i-1]){
                        c=i;
                    }
                }
            }
        }
        return c;
       
    
        
    }
}