# Will later add sys for user control
import json, sys

from usage import usage
from get_data import get_data
from clean import clean_data, fix_times

def main():

    if len(sys.argv) < 2:
        usage()

    raw_data = get_data() # will later add sys as arguments
    cleaned_data = clean_data(raw_data) # second arg can be sys later
    fix_times(cleaned_data)
  
    return json.dumps(cleaned_data, indent=1)
    # finished product, ready for use :)

week_sun_times = main()
print(week_sun_times)
