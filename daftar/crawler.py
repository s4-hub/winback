# import json, sqlite3, collections


# def toJson(self):
#     conn = sqlite3.connect("./db.sqlite3")
#     curr = conn.cursor()

#     curr.execute('''
#                     SELECT * FROM  daftar_datatk
#                     ''')
#     rows = curr.fetchall()
#     lists = []
#     for row in rows:
#         d = collections.OrderedDict()
#         d['id'] = row.id
#         d['nik'] = row.nik
#         d['nama'] = row.nama
#         d['tgl_lhr'] = row.tgl_lhr
#         d['tempat_lhr'] = row.tempat_lhr
#         d['alamat'] = row.alamat
#         lists.append(d)
    
#     j = json.dumps(lists)
#     with open('tk.js', 'w')
    

#     return j