# to create a own error


class SureshError(RuntimeError):
    def __str__(self):
        return "Item not found in source"
    


hey=[56,90,34,78,11,55,30,7,4,10]

def search():
    try:
        val=int(input("Tell us value to search "))
        for x in range(len(hey)):
            if hey[x]==val:
                print(val,"exists @",x)
                return
        raise SureshError
    except SureshError as s:
        print(s)
        search()
        sleep(2)
    

search()