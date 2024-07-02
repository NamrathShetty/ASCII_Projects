from PIL import Image
def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    img = Image.open(image)
    width, height = img.size

    img.resize((width//scale, height//scale)).save("resized.%s" % type)

    img = Image.open("resized.%s" % type)
    width, height = img.size

    grid = []
    for i in range(height):
        grid.append(["X"] * width)

    pix = img.load()

    for y in range(height):
        for x in range(width):
            if(sum(pix[x, y]) == 0):
                grid[y][x] = "#"
            elif(sum(pix[x, y]) in range(1, 100)):
                grid[y][x] = "X"
            elif(sum(pix[x, y]) in range(100, 200)):
                grid[y][x] = "%"
            elif(sum(pix[x, y]) in range(200, 300)):
                grid[y][x] = "&"
            elif(sum(pix[x, y]) in range(300, 400)):
                grid[y][x] = "*"
            elif(sum(pix[x, y]) in range(400, 500)):
                grid[y][x] = "+"
            elif(sum(pix[x, y]) in range(500, 600)):
                grid[y][x] = "/"
            elif(sum(pix[x, y]) in range(600, 700)):
                grid[y][x] = "("
            elif(sum(pix[x, y]) in range(700, 750)):
                grid[y][x] = "'"
            else:    
                grid[y][x] = ""
    
    art = open(saveas, 'w')

    for row in grid:
        art.write("".join(row) + "\n")

    art.close()

if __name__ == "__main__":
    asciiConvert("Au_ani_00032.jpg", "jpg", "ASCII.txt", "3")

