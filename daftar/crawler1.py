import requests, sqlite3
from bs4 import BeautifulSoup
import json, os


def crawler(nik):

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    conn = sqlite3.connect('C:/venv/winback/db.sqlite3')
    curr = conn.cursor()

    src = 'http://smile.bpjsketenagakerjaan.go.id/smile/mod_kn/ajax/kn5000_detail.php?NIK='+nik
    url = requests.get(src).text
    # page = req.request('GET', url, preload_content=False)
    soup = BeautifulSoup(url, 'html.parser')

    rows = soup.find_all('td')
    # rows = table.find('td')
    # t_data = table.find_all('tr')
    # rows = table.find_all('td', recursive=False)
    datas = {}
    # print(rows)
    data = [row.string for row in rows]
        # data = row.find_all('td')
        # data = row.find_all('td', attrs={'style': 'padding-top:10px;'})
        # nik = data[2:].text
    datas = {
        "nik" : data[3],
        "nama" : data[9],
        "tempat_lahir" : data[15],
        "tgl_lhr" : data[18],
        "alamat" : data[27],
        "kota" :  data[30],
        "provinsi" : data[33]
    }
    datas['nik'] = data[3]
    datas['nama'] = data[9]
    datas['tgl_lahir'] = data[18]
    datas['tempat_lahir'] = data[15]
    datas['alamat'] = data[27]

    curr.execute('''INSERT INTO daftar_datatk (nik, nama, tempat_lhr, tgl_lhr, alamat) VALUES (?, ?, ?, ?, ?)''',
                    (datas['nik'], datas['nama'], datas['tempat_lahir'], datas['tgl_lahir'], datas['alamat']))
    # x = json.dump(datas, open('datas.json', 'w'))
    # y = eval(x)
    # print(y)
    # y = json.dumps(js_file)
    # with open('datas.json', 'w') as outfile:
    #     eval(x)

    conn.commit()
    conn.close()