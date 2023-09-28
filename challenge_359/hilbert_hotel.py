flor_room_list = []
counter=1
result=0

while counter<=71328803586048:
    if 71328803586048%counter==0:
        result=71328803586048/counter
        flor_room_list.append((counter,result))
        flor_room_list.append((result,counter))
        print(counter,result)
    counter=counter+1

