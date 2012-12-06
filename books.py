from sys import argv

# get and open the file
script, book_list_file = argv
book_list_file = open(book_list_file)

# assemble a list of text in the file to parse for titles
raw_list = [line[:-1] for line in book_list_file if line[0] != '\n' and line[0] != ' ']

find_char       = lambda c,x:   ((c == x) and True) or False

find_char_index = lambda l,i,x: ((i < 0) and (False, i)) or \
                                ((find_char(l[i],x) == True) and (True, i)) or \
                                (find_char_index(l,i-1,x))                               

book_list = [] # empty booklist
def find_title(line):
    global book_list
    end_of_line = len(line) - 1
    foo, city_index_2      = find_char_index(line, end_of_line,':')
    bar, city_index_1      = find_char_index(line, city_index_2,'.')
    baz, start_title_index = find_char_index(line, city_index_1-1,'.')
    
    foo == True and bar == True and baz == True and \
    book_list.append(line[start_title_index+2:city_index_1])

map(find_title,raw_list)
print book_list
