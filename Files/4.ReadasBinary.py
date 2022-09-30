from pickle import *

say={
    "front end":"jinja",
    "back end":['django','flask'],
    "data base":"mongodb"
}

# binary format
quick=dumps(say)
print(quick)

awake=loads(quick)
print(awake)