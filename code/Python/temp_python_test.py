import pcc_100_100_helper_functions


TEST001 = True  # STRING PARTITIONS
TEST002 = True  # pcc_100_100_helper_functions.ExtractModuleNameFromFileName

# module variables that shouldn't be exported
_BANNER_WIDTH = 80
_STR_WIDTH = 15


# module functions that shouldn't be exported
def _PrintBanner(msg=None):
    if msg is not None:
        print(msg)
    print("".ljust(_BANNER_WIDTH, "*"))


# TEST001 - STRING PARTITIONS
if TEST001:
    _PrintBanner()
    v1 = "This.Is.A.Test"
    rhs = v1.rpartition(".")
    print("rhs".ljust(_STR_WIDTH), f" = {rhs}")
    print("type(rhs)".ljust(_STR_WIDTH), f" = {type(rhs)}")
    print("rhs[0]".ljust(_STR_WIDTH), f" = {rhs[0]}")
    print("type(rhs[0])".ljust(_STR_WIDTH), f" = {type(rhs[0])}")
    print("")

# TEST002 - pcc_100_100_helper_functions.ExtractModuleNameFromFileName
if TEST002:
    _PrintBanner(
        "help(pcc_100_100_helper_functions.\
ExtractModuleNameFromFileName)"
    )
    print(help(pcc_100_100_helper_functions.ExtractModuleNameFromFileName))
