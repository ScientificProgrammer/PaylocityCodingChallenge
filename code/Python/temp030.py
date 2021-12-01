# https://stackoverflow.com/questions/25778021/how-can-i-save-a-list-of-dictionaries-to-a-file
#
# How can I save a list of dictionaries to a file?

import json

logic_steps = [
    {
        'pattern': "asdfghjkl",
        'message': "This is not possible"
    },
    {
        'pattern': "anotherpatterntomatch",
        'message': "The parameter provided application is invalid"
    },
    {
        'pattern': "athirdpatterntomatch",
        'message': "Expected value for debugging"
    },
]


output_file = open("./data/temp030-sample_output.txt", 'wt', encoding='utf-8')

for dic in logic_steps:
  json.dump(dic, output_file) 
  output_file.write("\n")

output_file.close()
