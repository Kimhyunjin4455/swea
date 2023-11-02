T = int(input())
for test_case in range(1,T+1):
    n,k = map(int, input().split())
    student_list = []
    result = ""
    for i in range(1, n+1):
        student_list.append(i)
    work_list = list(map(int, input().split()))
    for work_student in work_list:
        if (work_student in student_list):
            student_list.remove(work_student)
    for not_work in student_list:
        result += (str(not_work)+" ")
    print("#{} {}".format(test_case, result))

