def organize_shoes():
    N_shoes = int(raw_input())

    if not (1<=N_shoes<=1000): return

    collection = {}
    pairs = 0

    company_set = set()
    comp_count = 0
    color_set = set()
    col_count= 0

    #~O(N)
    for _ in xrange(N_shoes):
        Company, Size, Color, Type = raw_input().split()
        if Company not in company_set:
            company_set.add(Company)
            comp_count += 1
        if Color not in color_set:
            color_set.add(Color)
            col_count += 1

        if 1<=comp_count<=20 and 1<=col_count<=20 and 0<=int(Size)<=15:
            collection.setdefault(Company, []).append([Size,Color,Type])
            #print collection

    del company_set, color_set, comp_count, col_count

    # print collection
    # print

    # ~O(N * k^2) < O(N^2)
    for each_company in collection:
        shoe_list = collection[each_company]
        ln = len(shoe_list)

        # ~O(k^2<N^2)
        for i in xrange(ln):
            covered = []
            cur_shoe = shoe_list[i]
            for j in xrange(i+1, ln):
                next_shoe = shoe_list[j]
                # print i,j
                if (cur_shoe[0] == next_shoe[0]) and (cur_shoe[1] == next_shoe[1]) and (cur_shoe[2] != next_shoe[2]) and (i not in covered):
                    covered.append(i)
                    covered.append(j)
                    # print each_company, cur_shoe, next_shoe
                    pairs += 1

    print pairs
    return

organize_shoes()