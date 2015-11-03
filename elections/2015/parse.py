import re
import json

def split_upper(s):
    return filter(None, re.split("([A-Z][^A-Z]*)", s))

def split_number(s):
    return filter(None, re.split("([0-9]*)", s))

def parse(filename):
    positions = []
    index = -1
    with open(filename, 'r') as f:
        lines = f.read().replace('\r\n','\n').split('\n')
    for i in range(0, len(lines)):
        last_line = None
        if i != 0:
            last_line = lines[i-1]
        line = lines[i]
        # test for position
        if line.strip() == '':
            pass
        elif line.isupper():
            name = line.strip().title()
            positions.append({
                'name': name,
                'candidates': [],
            })
            index += 1
        else:
            party = split_upper(line)[0].strip().title()
            rest = line[len(party):]
            name = split_number(rest)[0].strip().title()
            address = rest[len(name):].strip().title()
            candidate = {
                'name': name,
                'parties': [
                    party
                ],
                'address': address,
            }
            found = False
            for j in range(0, len(positions[index]['candidates'])):
                if positions[index]['candidates'][j]['name'] == name and positions[index]['candidates'][j]['address'] == address:
                    positions[index]['candidates'][j]['parties'].append(party)
                    found = True
                    break
            if not found:
                positions[index]['candidates'].append(candidate)

    return positions


if __name__ == '__main__':
    print json.dumps( parse('election2015.txt'), indent=4 )
    with open('site/election2015.json', 'w') as f:
        f.write(json.dumps({'positions': parse('election2015.txt')}, indent=4))
