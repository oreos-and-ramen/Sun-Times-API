import json, sys

from usage import usage
from get_data import get_data
from clean import clean_data, fix_times

def main():

    if len(sys.argv) < 2:
        usage()

    if sys.argv[1] != "daily":
        usage("Not a valid forecast specifier") # make sure other default works

    if len(sys.argv) > 2:
        raw_data = get_data(sys.argv[2]) # under assumption that the other defaults will still work
        cleaned_data = clean_data(raw_data, ["latitude","longitude",sys.argv[1]])
        fix_times(cleaned_data, sys.argv[2])
        return json.dumps(cleaned_data, indent=1)

    # System default output
    raw_data = get_data()
    cleaned_data = clean_data(raw_data)
    fix_times(cleaned_data)
  
    return json.dumps(cleaned_data, indent=1)


week_sun_times = main()
print(week_sun_times)
