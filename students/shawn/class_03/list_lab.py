
## Series 1
def list_series1(list=["Apples","Pears","Oranges","Peaches"]):

    print(list)

    more_fruit=input("Add some fruit > ")

    if more_fruit:
        list.append(more_fruit)

        print(list)

    pos=0
    while not (1<= pos <len(list)+1 ):
        pos = int(input("Enter fruit number > "))

        if not (1<= pos <len(list)+1):
            print("Numbers between 0 and {}".format(len(list)))

    else:
        print("Position {} is  {}".format(pos, list[pos-1]))








list_series1()
