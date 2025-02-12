import numpy as np

# Function 1
def modifier(data):
    print("Task 1")
    print()
    # Part 1
    print("Part 1:")
    print(f'{data[0,0]}, {data[0,-1]}, {data[-1,0]}, {data[-1,-1]}')
    print()

    # Part 2
    print("Part 2:")
    new_array = np.random.randint(1,100, size=(len(data),1))
    data = np.hstack((data,new_array))
    print(data)
    print()

    # Part 3
    print("Part 3:")
    new_array = data[-2]
    new_array = np.flip(new_array)
    print(new_array)
    print()

    # Part 4
    print("Part 4:")
    means = np.mean(data,axis=0)
    means = np.round(means,2)
    print(means)
    print()
    return 


#Function 2
def grade_stats(data):
    print("Task 2")
    print()
    print("Part 1:")
    means = np.mean(data[:, 1:], axis=0)
    means = np.round(means,2)
    above_70 = np.where(means > 7.0)[0] + 1
    if len(above_70)>0:
        print(f'Quizzes with mean above 70%: {', '.join(f'Quiz {q}' for q in above_70)}')
    else:
        print("No quizzes with mean above 70%")
    print()

    print("Part 2:")
    means = np.mean(data[:,1:], axis=1)
    above_79 = data[means > 7.9, 0]
    if len(above_79)>0:
        print(f'Students with mean above 79%: {', '.join(f'{q}' for q in above_79)}')
    else:
        print(f'No student with mean above 79%')
    
    print()

    print("Part 3:")
    marks = data[:,-1]
    perfect_score = data[marks==10,0]
    if len(perfect_score) >0:
        print(f'Students with 100% in last quiz: {', '.join(f'{q}' for q in perfect_score)}')
    else:
        print("No students scored 100% in the last quiz")
    print()
    return



#Funtion 3

def matrix_manipulator(A,B):
    print("Task 3")
    print()
    print("Part 1:")
    A_transpose = np.transpose(A)
    print(A_transpose)
    print()
    print("Part 2:")
    AB_dot = np.dot(A,B)
    print(AB_dot)
    print()
    print("Part 3:")
    result = AB_dot + np.transpose(B)
    print(result)
    return
