class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        f, r = 0, len(matrix) - 1

        while f <= r:
            mid = ((r - f) // 2) + f
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                f = mid + 1
            else:
                row = matrix[mid]
                f, r = 0, len(row) - 1

                while f <= r:
                    mid = ((r - f) // 2) + f
                    if row[mid] > target:
                        r = mid - 1
                    elif row[mid] < target:
                        f = mid + 1
                    else:
                        return True
        
        return False