import json

new_stations = []

lines = ['District', 'Piccadilly', 'Northern',
         'Hammersmith & City', 'Circle', 'Metropolitan', 'Central', 'Jubilee', 'Bakerloo', 'Waterloo & City', 'Victoria', 'DLR', 'London Overground', 'Crossrail', 'Crossrail 2']

with open('data/tfl_stations.json', 'r') as json_file:
    stations = json.load(json_file)
    all_stations = stations['features']
    print(all_stations[1])
    for station in all_stations:
        new_station = {
            'type': 'Feature',
            'Name': station['properties']['name'],
            'geometry': station['geometry'],
            'Station ID': station['properties']['id'],
            'Zone': station['properties']['zone']
        }
        new_lines = []
        for line in station['properties']['lines']:
            if line['name'] in lines:
                line_name = line['name']
                if line_name in lines[:11]:
                    line_name += " Line"
                if line_name == "DLR":
                    line_name = "Docklands Light Railway"
                if line_name == "London Overground":
                    line_name = "Overground"
                new_lines.append(line_name)
        new_station['Lines'] = ', '.join(new_lines)
        new_station['Number of Lines'] = len(new_lines)
        if len(new_lines) > 0:
            new_stations.append(new_station)

with open('data/tfl_stations_new2.json', 'w') as out:
    out_json = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": new_stations
    }

    json.dump(out_json, out, ensure_ascii=False)

new_connections = []

with open('data/tfl_lines.json', 'r') as json_file:
    ll = json.load(json_file)
    all_lines = ll['features']
    print(all_lines[0])
    for line in all_lines:
        new_lines = []
        for l in line['properties']['lines']:
            if l['name'] in lines:
                print(l)
                line_name = l['name']
                if line_name in lines[:11]:
                    line_name += " Line"
                if line_name == "DLR":
                    line_name = "Docklands Light Railway"
                if line_name == "London Overground":
                    line_name = "Overground"
                new_lines.append({
                    'Line': line_name,
                    'start_sid': l['start_sid'] if ('start_sid' in l) else None,
                    'end_sid': l['end_sid'] if ('end_sid' in l) else None
                })
        for element in new_lines:
            new_element = {
                'type': 'Feature',
                'geometry': line['geometry'],
                'Line': element['Line'],
                'start_sid': element['start_sid'],
                'end_sid': element['end_sid']
            }
            new_connections.append(new_element)

with open('data/tfl_lines_new2.json', 'w') as out:
    out_json = {
        "type": "FeatureCollection",
        "features": new_connections
    }

    json.dump(out_json, out, ensure_ascii=False)
