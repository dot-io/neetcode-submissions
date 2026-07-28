class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # min(i, j) * |i - j|
        best_area = 0
        i = 0
        j = len(heights) - 1
        while i <= j:
            print(i, j)
            current_area = min(heights[i], heights[j]) * (j - i)
            if current_area > best_area:
                best_area = current_area
        
        # which bar to scoot over, or test both options?
            if i == len(heights) - 1 or j == 0:
                break
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best_area    
    