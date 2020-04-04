# Use python script in ruby on rails

* call a python script from ruby file with: `` `python lib/assets/python/test.py` `` (see app/controllers/pages_conroller.rb)
* the script can take arguments: `` `python3 lib/assets/python/test.py "#{argument}"` ``
* create a python script in lib/python
* retrun has to be a string, therefore use print as "return" from python (see lib/assets/python/test.py)

## What's needed for the python files:
* python3 confirmedCases.py country --- country is the parameter $country as a plain string
