#Purpose of the function is to create a list within list with the range of the nested list being 3 or less if there aren't in groups of 3
#Input is the list which could be [2,3,4,5,6,7]
#Output is the new list that is a nested list  [[2,3,4],[5,6,7]]
def groups_of_3(lst:list[int])->list[list[int]]:
    final_list=[] #Start with empty list
    for i in range(0,len(lst),3): #For loop that goes from 0 to length of list but skip 3 as each iteration will be used within the while loop
        index = 3 #variable needed for the while loop
        new_list = [] #Empty list for each time the loop goes
        itr = 0 #iteration used for the while loop
        while index==3 and i < len(lst): #while loop used to created the nest list with index 3 being used as the cutoff line
            # and i<len(lst) used to prevent a sublist less than three values
            new_list.append(lst[i]) #Append each i to the new_list which is the sublist
            itr+=1 #Keep adding the iter until it reaches 3 where the index won't be 3 anymore ending the loop
            if itr==3:
                index=1
            i += 1 #To continue the while loop with each i in the range
        final_list.append(new_list) #Once while loop is completed append it to the final list.
    return final_list



