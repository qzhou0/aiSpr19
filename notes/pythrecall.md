
# Python notes from 

`sys.argv[i]` -- command line inputs

`dir()` -- stuff in library

`list.append()` faster than `list+=`
`stuff in set` faster than `stuff in list`

## classes

```python 

class NAME:
    
    variable = asdfagg #cf static in java, shared by all instances
    #refered to as NAME.variable=asdf
    
    def __init__(self, stuff, stuff,stuff):
      self.stuff=stuff
      <etc>
      
    def fxn(self, nonself):
      ...
      
"""-----------------------------------------------------"""

Frederick = NAME(stuff1,stuff2,stuff3)
Frederick.fxn(nonself)
Frederick.stuff=asda
Frederick.newstuff=new
# now new is in Frederick.__dict__
```


