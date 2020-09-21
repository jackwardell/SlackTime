# Things to do:
*  Add a list and str type hints for comma separated list e.g.
```
def func(comma_seperated_thing: Union[List, Str], ...):
    comma_seperated_thing = ','.join(comma_seperated_thing) if isinstance(comma_seperated_thing, list) else comma_seperated_thing
```
