import copy
def permute(nums):
        res = []
        track = []
        def backtrack(track, res):
            #nonlocal res
            if len(track) == len(nums): 
                print(copy.deepcopy(track), nums)
                res.append(copy.deepcopy(track)); return
            for i in range(len(nums)):
                if nums[i] in track: continue
                track.append(nums[i])
                backtrack(track, res)
                track.pop(-1)
        backtrack(track, res)   
        return res
print(permute([1,2,3]))
