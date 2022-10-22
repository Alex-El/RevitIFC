f_input_name = './test.txt'
f_output_name = '../RevitIFC.wiki/AllParameters.md'
output = []

with open(f_input_name) as f:
    lines = [line.rstrip() for line in f]
  

colapse_header = ''
colapse_open_1 = '<details>\n   <summary>'
colapse_open_2 = '</summary>'
colapse_close = '</details>'
tbl_header = '''|PARAM|GUID|NAME|DATATYPE|DATACATEGORY|GROUP|VISIBLE|\n
|---|---|---|---|---|---|---|'''

is_first_param_of_colapse = False

for line in lines:
    if not line.startswith('#') and not line.startswith('PARAM'):
        output.append(line)
    if line == '#':
        continue
    if line.startswith('# '):
        colapse_header += line
        output.append(colapse_open_1 + colapse_header + colapse_open_2)
        output.append(tbl_header)
        is_first_param_of_colapse = True
    if line.startswith('PARAM') and is_first_param_of_colapse:
        colapse_header = ''
        output.append(colapse_close)
        output.append(tbl_header)
        is_first_param_of_colapse = False
    if line.startswith('PARAM') and not is_first_param_of_colapse:
        output.append( '\n|' + '|'.join(line.split()) + '|')

with open(f_output_name , 'w') as fp:
    for item in output:
        fp.write("%s\n" % item)
    print('Done')