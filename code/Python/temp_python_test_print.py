"""For testing only. Do not push to Github."""
import sys


def print_msg(mod_name):
    """
    This text is a Python DocString.
    """

    msg_txt = f"""
  This text is a Python multi-line string that has been stored
  to a variable.

  JUST A TEST:
         The purpose of this function is to test the following
         Python concepts.

         1) Conditionally executing code based on whether

              a) the module was imported,

              b) called from the command line, or

              c) called from the interactive Python command line.

          2)  Testing Python multi-line strings.

          3)  Testing Python DocStrings for documentation.

          4)  Testing Python format strings using the .format() function
              with Python multi-line strings.

  OVERVIEW:
        1)  '{{mod_name}}' =  '{mod_name}'

        2) 'help({{mod_name}})' = help({mod_name})

        3) 'sys.argv[mod_name]' == '{{sys.argv[0]}}' == {sys.argv[0]}
"""
    print(msg_txt)


if __name__ == "__main__":
    print_msg(sys.argv[0])
else:
    print_msg(__name__)
