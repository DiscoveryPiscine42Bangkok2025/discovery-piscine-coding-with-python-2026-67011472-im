import sys
import re

if len(sys.argv) < 3:
    print("none")
else:
    word = sys.argv[1]      
    text = sys.argv[2]      
    matches = re.findall(rf"\b{re.escape(word)}\b", text)
    print(len(matches))