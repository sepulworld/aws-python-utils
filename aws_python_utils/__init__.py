RED 	= '\033[91m'
GREEN 	= '\033[92m'
YELLOW 	= '\033[93m'
CYAN 	= '\033[96m'
ENDC 	= '\033[0m'
BOLD 	= '\033[1m'

def color_string(color, string):
    return "%s%s%s" % (color, string, ENDC)