def ImgDownload():
    import ftplib, os, time

    WAIT_DIR = os.path.abspath("./waiting")

    ses = ftplib.FTP("winners.dothome.co.kr", "winners", "tkdals96!")
    ses.cwd("./html/waiting")

    while True:
        data = []
        ses.dir(data.append)
        if len(data) == 0:
            time.sleep(3)
            continue

        for file in data:
            ses.mkd("./../" + file[55:-4])
            ses.rename(file[55:], "./../" + file[55:-4] + "/" + file[55:])

            CUR_DIR = os.path.join(WAIT_DIR, file[55:-4])
            os.mkdir(CUR_DIR)

            ses.cwd("./../" + file[55:-4])
            with open(os.path.join(CUR_DIR, file[55:]), 'wb') as localfile:
                ses.retrbinary("RETR " + file[55:], localfile.write)
            localfile.close()
            ses.delete(file[55:])
            ses.cwd("./../waiting")