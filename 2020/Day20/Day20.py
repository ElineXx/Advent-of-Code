with open('input20.txt') as f:
    input_list = [x.split("\n") for x in f.read().split("\n\n")[:-1]]

def create_tile_borders(tile):
    return [
        tile[0],
        tile[1],
        tile[-1][::-1],
        "".join(row[-1] for row in tile),
        "".join(row[0] for row in tile)[::-1],
    ]

    tile_borders = []
    right_border = ""
    left_border = ""
    for row_no, row in enumerate(tile):
        if row_no in (0, 1, len(tile) - 1):
            tile_borders.append(row)
        right_border += row[-1]
        left_border += row[0]
    tile_borders.append(right_border[1:])
    tile_borders.append(left_border[1:])
    tile_borders[2] = tile_borders[2][::-1]
    tile_borders[4] = tile_borders[4][::-1]

    return tile_borders

borders_list = sorted([create_tile_borders(tile) for tile in input_list])

# [print(x) for x in borders_list]

for tile1 in borders_list:
    matches = []
    for i1, border1 in enumerate(tile1):
        for tile2 in borders_list:
            if tile1 is tile2:
                continue
            for i2, border2 in enumerate(tile2):
                if border1 == border2[::-1] or border1 == border2:
                    matches.append([[tile1, i1], [tile2, i2]])
    [print(x) for x in matches]