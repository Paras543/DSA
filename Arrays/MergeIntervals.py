class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """


        intervals.sort(key=lambda x: x[0])
        answer_list = [intervals[0]]

        for current_interval in range(1,len(intervals)):
            current  = intervals[current_interval]
            current_start = current[0]
            
            

           
            if current_start <= answer_list[-1][1]:
                answer_list[-1][1] = max(current[1],answer_list[-1][1])

            else:    
                answer_list.append(current)

        return answer_list





        