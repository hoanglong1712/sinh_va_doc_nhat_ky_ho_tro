import docx
import sys
import pickle
import thuvien
import os

def running(dictionary, doc):
    for table in doc.tables:
        ban_ghi = thuvien.BanGhi(table)
        dictionary[ban_ghi.ma_phieu] = ban_ghi
        pass
    pass

def nhap_du_lieu(ten_file, dau_ra):
    if len(ten_file) < 1:
        return False
    try:
        print(ten_file)
        doc = docx.Document(ten_file)
        dictionary = {}
        try:
            with open(dau_ra, "rb") as out:
                dictionary = pickle.load(out)
            pass
        except Exception as ex:
            print(ex)
        running(dictionary, doc)
        with open(dau_ra, "wb") as out:
            pickle.dump(dictionary, out)
            pass
        pass
    except ValueError as e:
        print(e)

    return True


if __name__ == '__main__':

    dir_list = os.listdir(sys.argv[1])

    for item in dir_list:
        if item.endswith('.docx'):
            nhap_du_lieu(os.path.join(sys.argv[1], item), sys.argv[2])
            pass
        pass
    pass