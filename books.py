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

def find_title(line):
    end_of_line = len(line) - 1
    foo, city_index_2      = find_char_index(line, end_of_line,':')
    bar, city_index_1      = find_char_index(line, city_index_2,'.')
    baz, start_title_index = find_char_index(line, city_index_1-1,'.')
    
    title_found = lambda x, y, z: (x == True and y == True and z == True and True) or False
    
    return (title_found(foo,bar,baz),start_title_index+2,city_index_1)

# pull out the titles    
x         = map(find_title,raw_list)
book_list = [raw_list[i][x[i][1]:x[i][2]] for i in range(len(x)) if x[i][0] == True]

print book_list

