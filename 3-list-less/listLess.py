#list-less-than-ten
#take in a list, and print out all of the elements that are less than 5

compare = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
for i in range(0, len(compare)):
    if(compare[i] < 5):
        print("%d" %compare[i])

#note to self:
#use square brackets when referencing list items