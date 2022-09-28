elections={
    "2006":"DMK",
    "2011":"ADMK",
    "2016":"ADMK",
    "2021":"DMK",
    "2019":"DMK",
    "2014":"ADMK"
}

try:
    year=input("tell us year to find victorious party ")
    print(elections[year])
except KeyError as e:
    print(e,"\n entered year not in the record")
    year=input("tell us year to find victorious party ")
    print(elections[year])