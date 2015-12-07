"""
There is a classroom of 'n' students and you are given their names and marks in physics. Store them in a nested list and print the name of each student who got the second lowest marks in physics.

If there are more than one student getting same marks, make sure you print the names of all students in alphabetical order, in different lines.

def secondLowest(arr, N):
    if 2<=N<=5:
        # ~NlgN
        arr.sort(key=lambda x: x[1])
        #get minimum score record
        minScoreLaddie = arr[0]
        count = 0
        res = arr[count]
        ans = []

        #get second lowest score from records- trivial <<< N
        while (res[1] == minScoreLaddie[1]):
            count += 1
            res = arr[count]

        ans.append(res)
        count += 1
        res = arr[count]

        #get more like this record- trivial <<<N
        while (ans[0][1] == res[1]):
            ans.append(res)
            count += 1
            res = arr[count]

        for eachRecord in sorted(ans, key= lambda x: x[0]):
            print eachRecord[0]
"""



# a better way
def secondLowest(arr, N):
    # ~NlgN
    arr.sort(key=lambda x: x[1])
    #get minimum score record
    minScore = min(arr, key=lambda x: x[1])
    #get second lowest score from records- trivial <<< N
    minList = [record for record in arr if record[1] != minScore[1]]
    assert minList[0][1] != minScore[1]

    ans = [minList[0]]
    for eachRecord in minList[1:]:
        if eachRecord[1] == ans[0][1]:
            ans.append(eachRecord)
        else:
            break
    for eachRecord in sorted(ans, key= lambda x: x[0]):
        print eachRecord[0]