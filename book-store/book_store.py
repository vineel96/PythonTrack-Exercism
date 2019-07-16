from collections import Counter

PRICE={1:800,2:1520,3:2160,4:2560,5:3000}


def total(book_list):
    if book_list==[]:
        return 0
    if len(book_list)==1:
        return 800
    cost=[]
    books_count=Counter(book_list)
    cost.append(sum([800*x for x in books_count.values()]))

    for i in range(2,6):
        copy=books_count.copy()
        cost.append(0)
        while copy:
            temp=Counter(dict(copy.most_common(i)).keys())
            cost[-1]+=PRICE[len(temp)]
            copy-=temp

    return min(cost)


