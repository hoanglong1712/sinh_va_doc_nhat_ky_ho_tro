
import thuvien
import pickle
import rapidfuzz
import prioritylist

def tim_kiem(dictionary):
    an_input = input('Nhap yeu cau: ')
    plist = prioritylist.PriorityList()
    for key, value in dictionary.items():
        plist.add(rapidfuzz.fuzz.ratio(an_input, value.noi_dung), key, value.thoi_gian_tiep_nhan)
        pass
    return plist
    pass

def running(dau_vao):
    dictionary = {}
    with open(dau_vao, "rb") as out:
        dictionary = pickle.load(out)

    index = 0

    while index != 3:
        print('Danh muc')
        print('1, Tim kiem')
        print('2, Nhap ma phieu')
        print('3, Dung')

        index = int(input('==> '))
        if index == 1:
            ket_qua = tim_kiem(dictionary)
            print('cac ket qua hang dau')
            i = 0
            for item in ket_qua:
                print(item.value, end=' ')
                i = i + 1
                if i > 5:
                    break
                pass
            print('')
            pass
        elif index == 2:
            ma = input('Nhap ma: ')
            value = dictionary[ma]
            if value is not None:

                with open(f'{ma}.txt', 'w', encoding='utf8') as w:
                    w.write(value.chi_tiet)
                    print(f'ghi ra {ma}.txt')
                    pass
                pass
            pass

    pass

if __name__ == '__main__':

    running('tudien.bin')
    pass
