class Solution:
    def threeSum(self, nums) :
        nums.sort()
        # -1,-1,0,1,2,4
        ans = []

        for i in range(len(nums)-2):
            if nums[i]>0: break 
            # 기준점이 양수되는 시점이면 l,r도 무조건 양수라 0불가, 무의미하다. 

            l,r= i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]: continue 
            # 이웃한데 동일한 수는 중복값 발생가능

            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s<0: l +=1
                elif s>0: r -=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])

                    # 중복값 발생 회피
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans





a = Solution()

print(a.threeSum([-3,-1,-1,-1,-1,1,4,4,4,4,4,4]))
        