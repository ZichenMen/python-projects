# Covering Segment s by Points Problem
# Find the minimum number of points needed to cover all given segments on a line
# Input: a sequence of n segments [l 1, r 1]....[l n, r n] on a line
# Output: a set of points of minimum size

'''
Input: 
    1st line: n, number of segments
    nth lines: each contains two integers l and r, defining the coordinaties of end points of the i-th segment
    
Output: 
    1st line: the minimum number k of points on the first line
    2nd line: integer coordinates of k points (separated by spaces, in any order)

Lemma: always take the most left segment's right end as point

1. sort the segment by their right
2. find the segment that have lowest right
2. create a point at the right end of current segment (append r of current segment to point set)
3. pop out every segments that covered by this point
4. return to step 1
'''

def covering_segments(n,segments):
        point_num = 0
        point_arr = []
        left_segment = [0,0]
        # sort the segments by it's right point
        # take segments as input, then returns it right point
        segments.sort(key = lambda x:x[1])

        # while there is still segments not pop out
        while len(segments) != 0:
            # create a new point at the right end of the left most segment
            point = segments[0][1]
            segments.pop(0)
            point_num += 1
            point_arr.append(point)
            
            # find if there is any segment has been cover by the point just made
            while len(segments) > 0 and segments[0][0] <= point and segments[0][1] >= point:
                 segments.pop(0)
        return point_num, point_arr
                 


if __name__ == '__main__':
    n = int(input())
    

    segments = [list(map(int, input().split())) for i in range(n)]
    points_num, points_coor = covering_segments(n,segments)
    print(points_num)
    print(" ".join(map(str,points_coor)))