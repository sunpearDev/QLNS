# coding=utf8
from openerp.osv import fields,osv

class phongban (osv.osv):
    _name='quanlyns.phongban'
    _columns = {
        # cac thuoc tinh cua lop danh muc hoc phan
        'name': fields.char('Tên phòng ban', size=25, required=True, translate=True),
        'ids': fields.char('Mã phòng ban', size=25, required=True, translate=True),
    }
    


class nhanvien(osv.osv):
    _name = 'quanlyns.nhanvien'
    _columns = {
        'manhanvien': fields.char('Mã nhân viên', size=25, required=True, translate=True),
        'tennhanvien': fields.char('Tên nhân viên', size=25, required=True, translate=True),
        'sdt': fields.char('SĐT', size=25, required=True, translate=True),
        'phongban': fields.many2one('quanlyns.phongban', "Tên phòng ban", help="Phòng ban"),
        
    }
phongban()
nhanvien() #tao 1 the hien cho lop quanlyns_quanlyns
