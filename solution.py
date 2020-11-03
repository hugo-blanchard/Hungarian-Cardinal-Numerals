import copy

first = {0:'nulla', 1:'egy', 2:'kettő', 3:'három', 4:'négy', 5:'öt', 6:'hat', 7:'hét', 8:'nyolc', 9:'kilenc'}
second = {0:'', 1:'tizen', 2:'huszon', 3:'harminc', 4:'negyven', 5:'ötven', 6:'hatvan', 7:'hetven', 8:'nyolcvan', 9:'kilencven'}
third = {0:'', 1:'száz', 2:'kétszáz', 3:'háromszáz', 4:'négyszáz', 5:'ötszáz', 6:'hatszáz', 7:'hétszáz', 8:'nyolcszáz', 9:'kilencszáz'}

def hungarian_numeral(n):
    first_b = copy.deepcopy(first)
    second_b = copy.deepcopy(second)
    third_b = copy.deepcopy(third)
    places = (first_b, second_b, third_b)
    
    res = ""
    n_list_str = list(str(n))
    #reverse the list, the numbers will be treated from right to left, it seems way easier
    n_list_str.reverse()
    n_list = [int(i) for i in n_list_str]
    
    #if at least two digits, rid "first" of the "0" case and check if "10" or "20"
    if n > 9:
        first_b[0] = ''
        if n_list[0] == 0:
            second_b.update({1:'tíz', 2:'húsz'})
    
    #for the first three from the right, ready the res variable for the return
    for i, c in zip(n_list[0:3], places):
        res = c[i] + res
    
    #end early if it should
    if n < 1000:
        return res
    
    #put a "-" before the thousands if needed
    if n >= 2000 and int("".join(n_list_str[:3])) != 0:
        res = "-" + res

    #adding the 'ezer' and taking care of edgecases
    res = 'ezer' + res
    if n < 2000:
        first_b[1] = ''
    first_b[2] = 'két'
    if n_list[3] == 0:
        second_b.update({1:'tíz', 2:'húsz'})
    else:
        second_b.update({1:'tizen', 2:'huszon'})
        
    #from the fourth to the sixth included, from the right, ready the res variable for the return
    for i, c in zip(n_list[3:], places):
        res = c[i] + res
    
    return res
