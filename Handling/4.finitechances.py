elections={
    "2006":"DMK",
    "2011":"ADMK",
    "2016":"ADMK",
    "2021":"DMK",
    "2019":"DMK",
    "2014":"ADMK"
}

def find(attempts=2):
    try:
        year=input("tell us year to find victorious party ")
        print(elections[year])
    except KeyError as e:
        if attempts<=3:
            print(e,"\n entered year not in the record")
            attempts+=1
            find(attempts) # recusrive call: function call by itself from itself
        else:
            print("Maximum no of attempts reached")
            return

find()