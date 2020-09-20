from matplotlib import font_manager
import matplotlib as mpl
import matplotlib.pyplot as plt
import imageio

mpl.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]
mpl.rcParams["font.family"] = "sans-serif"


def config_parser(filename):
    temp = ""
    temp2 = []
    config = []
    with open(filename) as f:
        temp = f.readlines()

    del f

    # remove comment and remove blank lines
    for x in temp:
        if not (x.startswith("#") or x.startswith("\n")):
            temp2.append(x.strip())

    # print(temp2)
    
    for x in temp2:
        config.append(x.split("|"))
    
    return config


# print(config_parser("content.txt"))


def make_poster():
    image = imageio.imread('blah.jpg')

    # init
    dpi=100
    xsize = image.shape[1]/dpi
    ysize = image.shape[0]/dpi
    aspect = ysize/xsize

    # init subplot
    plt.figure(num="poster", figsize=(xsize,ysize), dpi=dpi)
    splt = plt.subplot()
    splt.cla()
    plt.setp(splt.get_xticklabels(), visible=False)
    plt.setp(splt.get_xticklines(), visible=False)
    plt.setp(splt.get_yticklabels(), visible=False)
    plt.setp(splt.get_yticklines(), visible=False)

    ## copied from posterify but not using it. It can be helpful in future, maybe
    # imageaspect = float(image.shape[0])/float(image.shape[1])
    # if imageaspect > aspect:
    #     trim = int((image.shape[0] - aspect*image.shape[1])/2)
    #     image = image[trim:-trim, :]
    # elif imageaspect < aspect:
    #     trim = int((image.shape[1] - image.shape[0]/aspect)/2)
    #     image = image[:,trim:-trim]

    # Show image on canvas (no need to trim the image as canvas is exact size)
    splt.imshow(image,interpolation='nearest', extent=[0, xsize, 0, ysize], vmax=500)


    settings = { "fontsize" : 30,
    "ha" : "center",
    "va" : "center",
    "color" : "#1586c9",
    "weight" : "bold" }

    splt.text(xsize/2,ysize- (ysize/4),"Title of Talk", **settings)
    # splt.text(xsize/2,ysize/2+3,"ashjkdjkasdasd", **settings)
    plt.show()

make_poster()
