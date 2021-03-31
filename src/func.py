class PNG:
    def __init__(self,filename):
        self.filename = filename
        self.data = self.__read_file__(filename)

    def __read_file__(self,filename):
        from PIL import Image
        return Image.open(filename)

    def to_jpg(self,filename=None):
        self.data = self.data.convert("RGB")
        if filename is not None:
            self.data.save(filename,"jpeg")
        else:
            self.data.save(self.filename.replace(".png",".jpg"),"jpeg")

    def grayscale(self):
        self.data = self.data.convert("L")

    def black_and_white(self):
        # lambda function to convert each point to black or white
        self.__data = self.__data.point(lambda x: 0 if x < 128 else 255, '1')

class JPEG:
    def __init__(self, filename):
        self.filename = filename
        self.__data = self.__read_file__(filename)

    def __read_file__(self, filename):
        from PIL import Image
        return Image.open(filename)
    def to_png(self, filename=None):
        if filename is not None:
            self.__data.save(filename, "png")
        else:
            self.__data.save(self.filename.replace(".jpg", ".png"), "png")

