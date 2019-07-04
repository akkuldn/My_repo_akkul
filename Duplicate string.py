def get_list():
    list_one=[]
    for i in range(5):
        name=input("input name into the list")
        list_one.append(name)
    return(list_one)
def rem_duplicate(list_one):
    final_list=[]
    for num in list_one:
        if num not in final_list:
            final_list.append(num)
    #print(final_list)
    return final_list

def title_case(final_list):
    title=[]
    for name in final_list:
        print(name)
        title.append(name.title())
  
    print(title)
    
    return title
def sort_list(title_cased):
    splitted_list=[]
    for name in title_cased:
      splitted_list.append(name.split()[0])
    print(splitted_list)

    splitted_list.sort()
    print (splitted_list)
    return splitted_list
def shortest(sorted_list):
    min=1000
    for name in sorted_list:
        if len(name)<min:
            min=len(name)
    shortest= name
    print(shortest)
    
if __name__=='__main__':
    list_one=get_list()
    rem_duplicate(list_one)
    final_list=rem_duplicate(list_one) 
    print(final_list)
    #title_case(final_list)
    title_cased=title_case(final_list)
    sorted_list=sort_list(title_cased)
    shortest(sorted_list)
    