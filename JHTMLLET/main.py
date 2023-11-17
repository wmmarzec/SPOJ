import sys
try:

    while True:
        n = input()
        output = ""
        received_opening_html_mark = False
        received_closing_html_mark = False
        for i in range (0, len(n)):
            if n[i] == "<":
                received_opening_html_mark = True
                received_closing_html_mark = False
            elif n[i] == ">":
                received_closing_html_mark = True
                received_opening_html_mark = False
                
            if received_opening_html_mark == True:
                output += n[i].upper()
            else:
                output += n[i]
        print (output)

except:
    sys.exit(0)
