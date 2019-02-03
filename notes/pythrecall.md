
# Python notes from 

## Command Line

`sys.argv[i]` -- command line inputs

## Libraries

`dir()` -- stuff in library

## Speed
`list.append()` faster than `list+=`

`stuff in set` faster than `stuff in list`

## List Comprehensions

`range(n)`-->0-n

`[(expression w/ x) for x in it if (condition for x)]`

`dict.items()`==`dict_items([(key,item),(key,item),...])`

## Classes

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

Frederick = NAME(stuff1,stuff2,stuff3)#reference/pointer
Frederick.fxn(nonself)
Frederick.stuff=asda
Frederick.newstuff=new
# now new is in Frederick.__dict__
```


