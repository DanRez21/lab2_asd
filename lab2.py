from PIL import Image, ImageDraw

with open('DS0.txt') as f:

    img = Image.new('RGB', (540, 960), '#ffffff')
    draw = ImageDraw.Draw(img)

    for i in f.readlines():

        coord = i.split(' ')
        x, y = float(coord[0]), float(coord[1])
        draw.point((x, y), '#0000ff')

    img.save('image2.png')
    