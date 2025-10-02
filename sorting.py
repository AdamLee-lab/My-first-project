import random


def RandomList(min, max, num):
    output=list(range(1, num+1))
    for i in range(0, len(output)):
        output[i]=random.randint(min, max)
        # print(RandomList[i])
    return output

def sort(list):
    for i in range(len(list)-1, -1, -1):
        for j in range(0, i):
            if (list[j]>list[j+1]):
                cache=list[j]
                list[j]=list[j+1]
                list[j+1]=cache
                # swap(list[j], list[j+1])
                # print(list[j])

t=RandomList(1, 10, 50)

print(t)
sort(t)
print(t)

