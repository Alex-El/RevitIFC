f_input_name = './IFC Shared Parameters-RevitIFCBuiltIn_ALL.txt'
f_output_name = '../RevitIFC.wiki/AllParameters.md'
output = []

with open(f_input_name) as f:
    lines = [line.rstrip() for line in f]
  

colapse_header = ''
colapse_open_1 = '<details>\n   <summary>'
colapse_open_2 = '</summary>\n'
colapse_close = '</details>'
tbl_header = '''|PARAM|GUID|NAME|DATATYPE|DATACATEGORY|GROUP|VISIBLE|
|---|---|---|---|---|---|---|'''

is_header = True
is_first_param_of_colapse = True

for line in lines:
    if line == '#':
        is_header = False
        continue
    if is_header:
        output.append(line + '\n')
    else:
        if line.startswith('#'):
            output.append(colapse_close)
            colapse_header += line[1:]
            is_first_param_of_colapse = True
        if line.startswith('PARAM') and is_first_param_of_colapse:
            is_first_param_of_colapse = False
            output.append(colapse_open_1 + colapse_header + colapse_open_2)
            output.append(tbl_header)
            continue
        if line.startswith('PARAM') and not is_first_param_of_colapse:
            colapse_header = ''
            output.append( '|' + '|'.join(line.split()) + '|')

with open(f_output_name , 'w') as fp:
    for item in output:
        fp.write("%s\n" % item)
    print('Done')