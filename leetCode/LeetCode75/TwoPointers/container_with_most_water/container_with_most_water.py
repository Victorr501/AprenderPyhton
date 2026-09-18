class Solution(object):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    """
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        izquierda = 0
        derecha = len(height) - 1
        altura = 0
        logitud = 0
        area_maxima = 0
        area = 0
        
        
        while izquierda < derecha:
            altura = min(height[izquierda], height[derecha])
            logitud = (derecha - izquierda)
            area = logitud * altura
            if area > area_maxima:
                area_maxima = area
            if height[izquierda] < height[derecha]:
                izquierda += 1
            else:
                derecha -= 1
        
        return area_maxima    
                
    