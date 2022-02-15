import datetime

class BanGhi:
    def __init__(self, bang_du_lieu):
        self.ma_phieu = bang_du_lieu.cell(2, 1).text
        self.mang_cong_nghe = bang_du_lieu.cell(3,1).text
        self.ma_yeu_cau = bang_du_lieu.cell(4,1).text
        self.noi_dung = bang_du_lieu.cell(5, 1).text
        self.nguoi_yeu_cau = bang_du_lieu.cell(6, 1).text
        self.nguoi_tiep_nhan = bang_du_lieu.cell(7, 1).text
        self.nguoi_thuc_hien = bang_du_lieu.cell(8,1).text

        thoi_gian = bang_du_lieu.cell(9, 1).text
        self.thoi_gian_tiep_nhan = datetime.datetime.strptime(thoi_gian, "%d/%m/%Y %H:%M:%S")

        thoi_gian = bang_du_lieu.cell(10, 1).text
        self.thoi_gian_xu_ly = datetime.datetime.strptime(thoi_gian, "%d/%m/%Y %H:%M:%S")

        thoi_gian = bang_du_lieu.cell(11, 1).text
        self.thoi_gian_hoan_thanh = datetime.datetime.strptime(thoi_gian, "%d/%m/%Y %H:%M:%S")

        try:
            self.ngay_qua_han = int(bang_du_lieu.cell(12, 1).text)
        except:
            self.ngay_qua_han = 0
            pass


        self.chi_tiet = bang_du_lieu.cell(14, 0).text

        pass
    pass