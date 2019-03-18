import random


class ArrayMaker:

    @staticmethod
    def save_to_file(list_to_save):
        list_to_save = [str(x) for x in list_to_save]
        with open("saved_array.sv", "w") as fp:
            fp.write(" ".join(list_to_save))

    @staticmethod
    def read_form_file():
        with open("saved_array.sv", "r") as fp:
            file_data = fp.read()
            file_data = file_data.split(" ")
            file_data = [int(x) for x in file_data]
            return file_data

    @staticmethod
    def make_array(length):
        new_arr = []
        for i in range(length):
            el = random.randrange(0, 1000)
            new_arr.append(el)
        return new_arr


if __name__ == "__main__":
    am = ArrayMaker()
    arr = am.make_array(1000)
    am.save_to_file(arr)
    arr = am.read_form_file()
    print(1)
