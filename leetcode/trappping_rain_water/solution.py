class Solution:
    def trap(self, height: list[int]) -> int:
        l_left    = [0] * len(height)
        max_left  =  height[0]
        l_left[0] = max_left

        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]

            l_left[i] = max_left

        # RIGHT
        l_right     = [0] * len(height)
        max_right   = height[-1]
        l_right[-1] = max_right
        
        step = -1
        for i in range(len(height)-2, -1, step):
            if height[i] > max_right:
                max_right = height[i]
            l_right[i] = max_right
        
        total = 0
        for i in range(len(height)):
            w_level = min(l_left[i], l_right[i])
            diff = w_level - height[i]
            if diff > 0: 
                total += diff
        return total

