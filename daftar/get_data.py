import urllib.request
import json
import sqlite3
import time
from tqdm import tqdm


# def hook(obj):
#     value = obj.get('id')
#     if value:
#         pbar = tqdm(value)
#         for item in pbar:
#             pass
#             pbar.set_description('loading')
#         return obj


conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Provinsi (
        id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
        nama    TEXT
    );

    CREATE TABLE IF NOT EXISTS Kabupaten (
        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
        id_prov INTERGER NOT NULL,
        nama TEXT
    );

    CREATE TABLE IF NOT EXISTS Kecamatan (
        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
        id_kabupaten INTERGER NOT NULL,
        nama TEXT
    );

    CREATE TABLE IF NOT EXISTS Desa (
        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
        id_kecamatan INTERGER NOT NULL,
        nama TEXT
    )
    ''')

provinsi_url = 'http://dev.farizdotid.com/api/daerahindonesia/provinsi'
provinsi_response = urllib.request.urlopen(provinsi_url)
provinsi_data = json.loads(provinsi_response.read())
# print(json.dumps(provinsi_data, indent=4))

for provinsi in tqdm(provinsi_data['semuaprovinsi']):
    # print('Provinsi', provinsi['nama'])
    cur.execute('''INSERT OR IGNORE INTO Provinsi (id, nama)
                VALUES (?, ?)''', (provinsi['id'], provinsi['nama']))

    kabupaten_url = 'http://dev.farizdotid.com/api/daerahindonesia/provinsi/'\
        + provinsi['id'] + '/kabupaten'
    kabupaten_response = urllib.request.urlopen(kabupaten_url)
    kabupaten_data = json.loads(kabupaten_response.read())
    # print(json.dumps(kabupaten_data, indent=4))

    for kabupaten in tqdm(kabupaten_data['kabupatens']):
        # print('Kabupaten', kabupaten['nama']))
        cur.execute('''INSERT OR IGNORE INTO Kabupaten (id, id_prov, nama)
                    VALUES (?, ?, ?)''', (kabupaten['id'],
                                          kabupaten['id_prov'],
                                          kabupaten['nama']))

        kecamatan_url = 'http://dev.farizdotid.com/api/daerahindonesia/'\
            + 'provinsi/kabupaten/'\
            + kabupaten['id'] + '/kecamatan'
        kecamatan_response = urllib.request.urlopen(kecamatan_url)
        kecamatan_data = json.loads(kecamatan_response.read())
        # print(json.dumps(kabupaten_data, indent=4))

        for kecamatan in tqdm(kecamatan_data['kecamatans']):
            cur.execute('''INSERT OR IGNORE INTO Kecamatan
                        (id, id_kabupaten, nama)
                        VALUES (?, ?, ?)''', (kecamatan['id'],
                                              kecamatan['id_kabupaten'],
                                              kecamatan['nama']))

            desa_url = 'http://dev.farizdotid.com/api/daerahindonesia/'\
                + 'provinsi/kabupaten/kecamatan/'\
                + kecamatan['id'] + '/desa'
            desa_response = urllib.request.urlopen(desa_url)
            desa_data = json.loads(desa_response.read())
            # print(json.dumps(kabupaten_data, indent=4))

            for desa in tqdm(desa_data['desas']):
                cur.execute('''INSERT OR IGNORE INTO Desa
                            (id, id_kecamatan, nama)
                            VALUES (?, ?, ?)''', (desa['id'],
                                                  desa['id_kecamatan'],
                                                  desa['nama']))

conn.commit()
cur.close()
