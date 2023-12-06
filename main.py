input_path = "./input.txt"
output_path = "./output.txt"

with open(input_path) as f:
    av = []
    anv = []
    bv = []
    bnv = []
    na = []

    for line in f.readlines():
        command = line.split(' ')[0]
        if command == 'fin':
            av_line = f'AV : [{",".join(av)}]\n'
            anv_line = f'ANV : [{",".join(anv)}]\n'
            bv_line = f'BV : [{",".join(bv)}]\n'
            bnv_line = f'BNV : [{",".join(bnv)}]\n'
            na_line = f'NA : [{",".join(na)}]\n'
            with open(output_path, 'w') as g:
                g.write(av_line)
                g.write(anv_line)
                g.write(bv_line)
                g.write(bnv_line)
                g.write(na_line)
            break
        if command == 'init':
            max_capacity = int(line.split(' ')[1].split('/')[0])
        if command == 'reg':
            line = line.strip()
            words = line.split(' ')
            serial_num = words[1]
            dept = words[2]
            food_pref = words[3]
            if food_pref == 'V':
                if dept == 'A':
                    if len(av) + 1 <= (max_capacity // 4):
                        av.append(serial_num)
                    else:
                        na.append(serial_num)
                else:
                    if len(bv) + 1 <= (max_capacity // 4):
                        bv.append(serial_num)
                    else:
                        na.append(serial_num)
            else:
                if dept == 'A':
                    if len(anv) + 1 <= (max_capacity // 4):
                        anv.append(serial_num)
                    else:
                        na.append(serial_num)
                else:
                    if len(bnv) + 1 <= (max_capacity // 4):
                        bnv.append(serial_num)
                    else:
                        na.append(serial_num)