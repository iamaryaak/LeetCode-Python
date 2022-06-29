class Solution:
    def average(self, salary: List[int]) -> float:
        # sort the array in ascending order
        salary = sorted(salary)
        salary = salary[1:len(salary)-1]
        
        avg = 0
        for i in salary:
            avg += i
        avg = avg / len(salary)
        return avg
