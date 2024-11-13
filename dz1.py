import time
br_bacanja = 0
a = 75
m = 2**16 + 1
c = 74
seed = round(time.time()*1000)%m
sum_dole = 0
sum_gore = 0
sum_rucna = 0
def prazan_talon():
    ret_mat = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], [], []]
    rucna = [i for i in range(0, 10)]
    talon = []
    na_gore = 9
    na_dole = 0
    return ret_mat, talon, rucna
def kockice(broj_koc):
    global seed
    kockica = []
    for i in range(broj_koc):
        seed = (a * seed +c) % m
        kockica.append(seed % 6 + 1)
    return kockica
def menu(ret_mat, talon, rucna, br_bacanja):
    print("--------MENI-------\n"
          "Izaberi opciju:\n"
          "1.Stvori prazan talon za igru\n"
          "2.Ispiši talon uz ispis trenutnog broja bodova\n"
          "3.Odigraj jedan potez bacanjem kockica\n"
          "4.Izaberi opciju pomoć prijatelja\n"
          "5.Završi partiju\n")
    x = input()
    try:
        x = int(x)
        if x < 0 or x > 5:
            print("Unesite ispravnu opciju\n")

    except:
        print("Unesite broj kao opciju\n")
    finally:
        if x == 2:
            ispis(ret_mat, talon)
        elif x == 1:
            ret_mat, talon, rucna = prazan_talon()
        elif x == 3:
            br_bacanja += 1
            igra(ret_mat, talon, rucna)
        elif x == 4:
            pomoc_prijatelja(rucna, ret_mat, talon)
    return x, ret_mat, talon, rucna, br_bacanja
def verovatnoca(n, p, l):
    s = 0
    for i in range(0, 1000000):
        kockica = kockice(n)
        if kockica.count(p) >= l:
            s += 1
    m = s / 1000000
    return m
def pomoc_prijatelja(rucna, ret_mat, talon):
    global sum_dole
    global sum_gore
    global sum_rucna
    z_koc = []
    na_dole, na_gore = popunjeno_element(ret_mat, talon)
    kockica = kockice(5)
    broj_pon = ponavljanja(kockica)
    k = 0
    if len(broj_pon) == 1 and 9 in rucna:
        k = 1
        v = 50 + kockica[0] * 5
        l = 'ru'
        r = 9
        unos(ret_mat, talon, l, na_dole, na_gore,v,r)
        sum_rucna += v
    elif 8 in rucna and list(broj_pon.values()) == [4, 1] or list(broj_pon.values()) == [5] or list(broj_pon.values()) == [1,4]:
        k = 1
        for pon in broj_pon:
            if broj_pon[pon] == 4 or broj_pon[pon] == 5:
                v = 40 + 4 * pon
        l = 'ru'
        r = 8
        unos(ret_mat, talon, l, na_dole, na_gore, v, r)
        sum_rucna += v
    elif 7 in rucna and list(broj_pon.values()) == [2, 3] or list(broj_pon.values()) == [3, 2]:
        k = 1
        v = 0
        for pon in broj_pon:
            v += 30 + broj_pon[pon] * pon
        l = 'ru'
        r = 7
        unos(ret_mat, talon, l, na_dole, na_gore, v, r)
        sum_rucna += v
    elif 6 in rucna and kockica == [1, 2, 3, 4, 5] or kockica == [2,3,4, 5, 6]:
        k = 1
        v = 66
        l = 'ru'
        r = 8
        unos(ret_mat, talon, l, na_dole, na_gore, v, r)
        sum_rucna += v
    else:
        for pon in broj_pon:
            if broj_pon[pon] * pon > k and  pon-1 in rucna:
                v = broj_pon[pon] * pon
                c = pon - 1
        l = 'ru'
        r = c
        unos(ret_mat, talon, l, na_dole, na_gore, v, r)
        sum_rucna += v
        k = 1
    if na_dole > 5 and na_gore < 6 and k == 0:
        if na_dole == 6 and kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4,5 ,6 ]:
            b = 'nd'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_dole += v
            n = 1
            p = 1
            l = 1
        elif na_dole == 7 and 2 in list(broj_pon.values()) or 3 in list(broj_pon.values()):
            b = 'nd'
            r = 0
            if 3 in list(broj_pon.values()):
               for pon in broj_pon:
                   if broj_pon[pon] == 3:
                       j = pon
               if 2 in list(broj_pon.values()):
                   v = 30
                   for pon in broj_pon:
                       v += pon * broj_pon[pon]
                   unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                   sum_dole += v
               else:
                   for pon in broj_pon:
                       if broj_pon[pon] == 1:
                           p = pon
                           n = 1
                           l = 1
                           v = 30 + 3 * j + 2 * p
            elif list(broj_pon.values()).count(2) == 2:
                v = 30
                for pon in broj_pon:
                    if broj_pon[pon] == 2:
                        z_koc.append(pon)
                p = z_koc[0]
                l = 1
                n = 1
                v += 3* z_koc[0] + 2*z_koc[1]
            else:
                for pon in broj_pon:
                    if broj_pon[pon] == 1:
                        p = pon
                        n = 3
                        l = 3
                    else:
                        for i in range(2):
                            z_koc.append(pon)
                v = 30 + p * 3 + z_koc[0] * 2
        elif na_dole == 8:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 4 - u
            v = 40 + 4 * p
            for i in range(n):
                z_koc.append(p)
        elif na_dole == 9:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 5 - u
            v = 50 + 5 * p
        if verovatnoca(n, p, l) > 0.35:
            t = 0
            while t < 2:
                kockica = kockice(5 - len(z_koc))
                if kockica.count(p) == l:
                    t = 2
                    l = 'nd'
                    r = 0
                    unos(ret_mat, talon, l, na_dole, na_gore, v, r)
                    sum_dole += v
                    up = True
                else:
                    t += 1
                    br_pon = ponavljanja(kockica)
                    if p in br_pon:
                        l -= br_pon[p]
                        n -= br_pon[p]
                        for c in range(br_pon[p]):
                            z_koc.append(p)
            if not up:
                v = kockica.count(na_gore + 1) * (na_gore + 1)
                b = 'ng'
                r = 0
                unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                sum_gore += v
        else:
            v = kockica.count(na_gore + 1) * (na_gore + 1)
            b = 'ng'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_gore += v
    elif na_dole < 6 and na_gore < 6 and k == 0:
        if kockica.count(na_dole + 1) >= kockica.count(na_gore + 1):
            v = kockica.count(na_dole+1) * (na_dole + 1)
            b = 'nd'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_dole += v
        else:
            v = kockica.count(na_gore + 1) * (na_gore + 1)
            b = 'ng'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_gore += v
    elif na_dole < 6 and na_gore > 5 and k == 0:
        if na_gore == 6 and kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
            b = 'ng'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_gore += v
            n = 1
            p = 1
            l = 1
        elif na_gore == 7 and 2 in list(broj_pon.values()) or 3 in list(broj_pon.values()):
            b = 'ng'
            r = 0
            if 3 in list(broj_pon.values()):
                for pon in broj_pon:
                    if broj_pon[pon] == 3:
                        j = pon
                if 2 in list(broj_pon.values()):
                    v = 30
                    for pon in broj_pon:
                        v += pon * broj_pon[pon]
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_dole += v
                else:
                    for pon in broj_pon:
                        if broj_pon[pon] == 1:
                            p = pon
                            n = 1
                            l = 1
                            v = 30 + 3 * j + 2 * p
            elif list(broj_pon.values()).count(2) == 2:
                v = 30
                for pon in broj_pon:
                    if broj_pon[pon] == 2:
                        z_koc.append(pon)
                p = z_koc[0]
                l = 1
                n = 1
                v += 3 * z_koc[0] + 2 * z_koc[1]
            else:
                for pon in broj_pon:
                    if broj_pon[pon] == 1:
                        p = pon
                        n = 3
                        l = 3
                    else:
                        for i in range(2):
                            z_koc.append(pon)
                v = 30 + p * 3 + z_koc[0] * 2
        elif na_gore == 8:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 4 - u
            v = 40 + 4 * p
            for i in range(n):
                z_koc.append(p)
        elif na_gore == 9:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 5 - u
            v = 50 + 5 * p
        if verovatnoca(n, p, l) > 0.35:
            t = 0
            while t < 2:
                kockica = kockice(5 - len(z_koc))
                if kockica.count(p) == l:
                    t = 2
                    b = 'ng'
                    r = 0
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_gore += v
                    up = True
                else:
                    t += 1
                    br_pon = ponavljanja(kockica)
                    if p in br_pon:
                        l -= br_pon[p]
                        n -= br_pon[p]
                        for c in range(br_pon[p]):
                            z_koc.append(p)
            if not up:
                v = kockica.count(na_dole + 1) * (na_dole + 1)
                b = 'nd'
                r = 0
                unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                sum_dole += v
        else:
            v = kockica.count(na_dole + 1) * (na_dole + 1)
            b = 'nd'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_dole += v
    elif k == 0:
        if na_dole == 6 and kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
            b = 'nd'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_dole += v
            n = 1
            p = 1
            l = 1
        elif na_dole == 7 and 2 in list(broj_pon.values()) or 3 in list(broj_pon.values()):
            b = 'nd'
            r = 0
            if 3 in list(broj_pon.values()):
                for pon in broj_pon:
                    if broj_pon[pon] == 3:
                        j = pon
                if 2 in list(broj_pon.values()):
                    v = 30
                    for pon in broj_pon:
                        v += pon * broj_pon[pon]
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_dole += v
                else:
                    for pon in broj_pon:
                        if broj_pon[pon] == 1:
                            p = pon
                            n = 1
                            l = 1
                            v = 30 + 3 * j + 2 * p
            elif list(broj_pon.values()).count(2) == 2:
                v = 30
                for pon in broj_pon:
                    if broj_pon[pon] == 2:
                        z_koc.append(pon)
                p = z_koc[0]
                l = 1
                n = 1
                v += 3 * z_koc[0] + 2 * z_koc[1]
            else:
                for pon in broj_pon:
                    if broj_pon[pon] == 1:
                        p = pon
                        n = 3
                        l = 3
                    else:
                        for i in range(2):
                            z_koc.append(pon)
                v = 30 + p * 3 + z_koc[0] * 2
        elif na_dole == 8:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 4 - u
            v = 40 + 4 * p
            for i in range(n):
                z_koc.append(p)
        elif na_dole == 9:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 5 - u
            v = 50 + 5 * p
        verovatnoca_d = verovatnoca(n, p, l)
        if na_gore == 6 and kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
            b = 'ng'
            r = 0
            unos(ret_mat, talon, b, na_dole, na_gore, v, r)
            sum_gore += v
            n = 1
            p = 1
            l = 1
        elif na_gore == 7 and 2 in list(broj_pon.values()) or 3 in list(broj_pon.values()):
            b = 'ng'
            r = 0
            if 3 in list(broj_pon.values()):
                for pon in broj_pon:
                    if broj_pon[pon] == 3:
                        j = pon
                if 2 in list(broj_pon.values()):
                    v = 30
                    for pon in broj_pon:
                        v += pon * broj_pon[pon]
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_dole += v
                else:
                    for pon in broj_pon:
                        if broj_pon[pon] == 1:
                            p = pon
                            n = 1
                            l = 1
                            v = 30 + 3 * j + 2 * p
            elif list(broj_pon.values()).count(2) == 2:
                v = 30
                for pon in broj_pon:
                    if broj_pon[pon] == 2:
                        z_koc.append(pon)
                p = z_koc[0]
                l = 1
                n = 1
                v += 3 * z_koc[0] + 2 * z_koc[1]
            else:
                for pon in broj_pon:
                    if broj_pon[pon] == 1:
                        p = pon
                        n = 3
                        l = 3
                    else:
                        for i in range(2):
                            z_koc.append(pon)
                v = 30 + p * 3 + z_koc[0] * 2
        elif na_gore == 8:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 4 - u
            v = 40 + 4 * p
            for i in range(n):
                z_koc.append(p)
        elif na_gore == 9:
            u = 0
            for pon in broj_pon:
                if broj_pon[pon] > u:
                    u = broj_pon[pon]
                    v = pon
            n = 5 - u
            p = v
            l = 5 - u
            v = 50 + 5 * p
        verovatnoca_g = verovatnoca(n, p, l)
        if verovatnoca_g >= verovatnoca_d:
            t = 0
            while t < 2:
                kockica = kockice(5 - len(z_koc))
                if kockica.count(p) == l:
                    t = 2
                    b = 'ng'
                    r = 0
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_gore += v
                    up = True
                else:
                    t += 1
                    br_pon = ponavljanja(kockica)
                    if p in br_pon:
                        l -= br_pon[p]
                        n -= br_pon[p]
                        for c in range(br_pon[p]):
                            z_koc.append(p)
            if not up:
                v = 0
                b = 'ng'
                r = 0
                unos(ret_mat, talon, b, na_dole, na_gore, v, r)
        else:
            t = 0
            while t < 2:
                kockica = kockice(5 - len(z_koc))
                if kockica.count(p) == l:
                    t = 2
                    l = 'nd'
                    r = 0
                    unos(ret_mat, talon, l, na_dole, na_gore, v, r)
                    sum_dole += v
                    up = True
                else:
                    t += 1
                    br_pon = ponavljanja(kockica)
                    if p in br_pon:
                        l -= br_pon[p]
                        n -= br_pon[p]
                        for c in range(br_pon[p]):
                            z_koc.append(p)
            if not up:
                v = 0
                b = 'ng'
                r = 0
                unos(ret_mat, talon, b, na_dole, na_gore, v, r)
def ispis(ret_mat, talon):
    print('{:^7}{:^7}{:^7}{:^7}'.format('JAMB','Na dole ','Na gore', 'Ručna'))
    y = 0
    if len(ret_mat) != 0 :
        talon = konverzija(ret_mat, talon)
        y = 1
    for m in range(len(talon)):
        if m < 6:
            print('{:^7}{:^7}{:^7}{:^7}'.format(m+1,talon[m][0],talon[m][1], talon[m][2]))
        elif m == 6:
            print('{:^7}{:^7}{:^7}{:^7}'.format('Kenta',talon[m][0],talon[m][1], talon[m][2]))
        elif m == 7:
            print('{:^7}{:^7}{:^7}{:^7}'.format('Ful',talon[m][0],talon[m][1], talon[m][2]))
        elif m == 8:
            print('{:^7}{:^7}{:^7}{:^7}'.format('Poker', talon[m][0], talon[m][1], talon[m][2]))
        elif m == 9:
            print('{:^7}{:^7}{:^7}{:^7}'.format('Jamb', talon[m][0], talon[m][1], talon[m][2]))
    s = sum_dole + sum_gore + sum_rucna
    print('Ukupan broj bodova je:{}'.format(s))
    if y:
        talon = []
def unos(ret_mat, talon, l, na_dole, na_gore,v,r):
    talon = konverzija(ret_mat, talon)
    if len(ret_mat) != 0:
        ret_mat[0][-1] += 1
        if l == 'nd':
            if ret_mat[0][na_dole] == -1:
                if na_dole == 0:
                    ret_mat[0][na_dole] = 0
                else:
                    c = 0
                    for t in range(na_dole):
                        if ret_mat[0][t] != -1:
                            d = ret_mat[0][t]
                            c = 1
                        elif c == 0:
                            d = -1
                    ret_mat[0][na_dole] = d + 1
            if na_dole != 9:
                for i in range(na_dole+1, 10):
                    if ret_mat[0][i] != -1:
                        ret_mat[0][i] += 1
            ret_mat[1].insert(ret_mat[0][na_dole], 0)
            ret_mat[2].insert(ret_mat[0][na_dole], v)
        elif l == 'ng':
            if ret_mat[0][na_gore] == -1:
                if na_gore == 0:
                    ret_mat[0][na_gore] = 0
                else:
                    c = 0
                    for t in range(na_gore):
                        if ret_mat[0][t] != -1:
                            d = ret_mat[0][t]
                            c = 1
                        elif c == 0:
                            d = -1
                    ret_mat[0][na_gore] = d + 1
            if na_gore != 9:
                for i in range(na_gore+1, 10):
                    if ret_mat[0][i] != -1:
                        ret_mat[0][i] += 1
            if talon[r][0] != ' ':
                f = 1
            else:
                f = 0
            ret_mat[1].insert(ret_mat[0][na_gore] + f, 1)
            ret_mat[2].insert(ret_mat[0][na_gore] + f, v)
        else:
            if ret_mat[0][r] == -1:
                if r == 0:
                    ret_mat[0][r] = 0
                else:
                    c = 0
                    for t in range(r):
                        if ret_mat[0][t] != -1:
                            d = ret_mat[0][t]
                            c = 1
                        elif c == 0:
                            d = -1
                    ret_mat[0][r] = d + 1
            if r != 9:
                for i in range(r+1, 10):
                    if ret_mat[0][i] != -1:
                        ret_mat[0][i] += 1
                if talon[r][0] != ' ' and talon[r][1] != ' ':
                    f = 2
                elif talon[r][0] != ' ' or talon[r][1] != ' ':
                    f = 1
                else:
                    f = 0
            ret_mat[1].insert(ret_mat[0][r] + f, 2)
            ret_mat[2].insert(ret_mat[0][r] + f, v)
    else:
        if l == 'nd':
            talon[na_dole][0] = v
        elif l == 'ng':
            talon[na_gore][1] = v
        else:
            talon[r][2] = v

def konverzija(ret_mat, talon):
    talon = []
    for i in range(len(ret_mat[0])-1):
        l = []
        if ret_mat[0][i] != -1:
            c = 0
            if i != 9:
                a = 0
                for j in range(i+1, len(ret_mat[0])-1):
                    if ret_mat[0][j] != -1 and a == 0:
                        w = ret_mat[0][j]
                        a = 1
                    elif a == 0:
                        w = ret_mat[0][i] + 1
                for p in range(ret_mat[0][i],w):
                    if ret_mat[1][p] != c:
                        l.append(' ')
                        if ret_mat[1][p] > c:
                            c += 1
                            if ret_mat[1][p] == c:
                                l.append(ret_mat[2][p])
                                c += 1
                            elif ret_mat[1][p] > c:
                                l.append(' ')
                                c += 1
                                if ret_mat[1][p] == c:
                                    l.append(ret_mat[2][p])
                                else:
                                    l.append(' ')
                    else:
                        l.append(ret_mat[2][p])
                        c += 1
            else:
                for p in range(ret_mat[0][i], len(ret_mat[1])):
                    if ret_mat[1][p] != c:
                        l.append(' ')
                        if ret_mat[1][p] > c:
                            c += 1
                            if ret_mat[1][p] == c:
                                l.append(ret_mat[2][p])
                                c += 1
                            elif ret_mat[1][p] > c:
                                c += 1
                                if ret_mat[1][p] == c:
                                    l.append(ret_mat[2][p])
                    else:
                        l.append(ret_mat[2][p])
                        c += 1
        else:
            l = [' ', ' ', ' ']
        if len(l) < 3:
            while len(l) < 3:
                l.append(' ')
        talon.append(l)
    return talon
def ponavljanja(kockica):
    broj_pon = dict()
    for koc in kockica:
        if koc in broj_pon:
            broj_pon[koc] += 1
        else:
            broj_pon[koc] = 1
    return broj_pon
def popunjeno_element(ret_mat, talon ):
    na_dole = 0
    na_gore = 9
    z = 0
    m = 0
    if len(ret_mat) != 0:
        talon = konverzija(ret_mat, talon)
        z = 1
    for pol in range(len(talon)):
        if talon[pol][0] == ' ' and m == 0:
            na_dole = pol
            m = 1
        if talon[pol][1] != ' ':
            na_gore = pol - 1
    if z:
        talon = []
    return na_dole, na_gore
def igra(ret_mat, talon, rucna):
    global sum_dole
    global sum_gore
    global sum_rucna
    br_poteza = 0
    br_koc = 5
    na_dole, na_gore = popunjeno_element(ret_mat, talon)
    while br_poteza < 3:
        if br_poteza == 0:
            kockica = kockice(br_koc)
            print(*kockica)
            print("Da li želite da ponovo bacate kockice?")
            answer = input()
            if answer == 'Da':
                br_poteza += 1
                print("Koje kockice želite da zadržite?")
                z_kockice = [int(m) for m in input().split()]
            elif answer == 'Ne':
                br_poteza = 3
                print("Izaberite opciju:\n"
                      "1.Popuniti kolonu na dole\n"
                      "2.Popuniti kolonu na gore\n"
                      "3.Popuniti kolonu ručna\n")
                option = int(input())
                o = 0
                while not o:
                    pon_koc = ponavljanja(kockica)
                    if option == 1:
                        b = 'nd'
                        r = 0
                        if (na_dole + 1) in kockica:
                            v = (na_dole + 1) * kockica.count(na_dole + 1)
                        elif na_dole > 5:
                            if na_dole == 6:
                                kockica.sort()
                                if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                    v = 66
                                else:
                                    v = 0
                            elif na_dole == 7:
                                c = list(pon_koc.values())
                                if c == [2, 3] or c == [3, 2]:
                                    v = 30
                                    for pon in pon_koc:
                                        v += pon * pon_koc[pon]
                                else:
                                    v = 0
                            elif na_dole == 8:
                                u = 1
                                for pon in pon_koc:
                                    if pon_koc[pon] == 4:
                                        v = 40 + 4 * pon
                                        u = 0
                                if u:
                                    v = 0
                            else:
                                if len(pon_koc) == 1:
                                    v = 50 + 5*kockica[0]
                        else:
                            v = 0
                        unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                        sum_dole += v
                        o = 1
                    elif option == 2:
                        r = 0
                        b = 'ng'
                        if (na_gore + 1) in kockica:
                            v = (na_gore + 1) * kockica.count(na_gore + 1)
                        elif na_gore > 5:
                            if na_gore == 6:
                                kockica.sort()
                                if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                    v = 66
                                else:
                                    v = 0
                            elif na_gore == 7:
                                c = list(pon_koc.values())
                                if c == [2, 3] or c == [3, 2]:
                                    v = 30
                                    for pon in pon_koc:
                                        v += pon * pon_koc[pon]
                                else:
                                    v = 0
                            elif na_gore == 8:
                                u = 1
                                for pon in pon_koc:
                                    if pon_koc[pon] == 4:
                                        v = 40 + 4 * pon
                                        u = 0
                                if u:
                                    v = 0
                            else:
                                if len(pon_koc) == 1:
                                    v = 50 + 5*kockica[0]
                                else:
                                    v = 0
                        else:
                            v = 0
                        unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                        sum_gore += v
                        o = 1
                    elif option == 3:
                        b = 'ru'
                        br_poteza = 3
                        m = 0
                        while not m:
                            l = ['1', '2', '3', '4', '5', '6']
                            print('Koje polje želite da popunite?\n')
                            polj = input()
                            if polj in l:
                                polj = int(polj)
                                if polj-1 in rucna and polj-1 < 6:
                                    s = polj-1
                                    v = polj*kockica.count(polj)
                                    m = 1
                            else:
                                if polj == 'Kenta':
                                    s = 6
                                    if s in rucna:
                                        m = 1
                                        kockica.sort()
                                        if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                            v = 66
                                        else:
                                            v = 0
                                elif polj == 'Ful':
                                    s = 7
                                    c = list(pon_koc.values())
                                    if s in rucna:
                                        m = 1
                                        if c == [2, 3] or c == [3, 2]:
                                            v = 30
                                            for pon in pon_koc:
                                                v += pon * pon_koc[pon]
                                        else:
                                            v = 0
                                elif polj == 'Poker':
                                    s = 8
                                    u = 1
                                    if s in rucna:
                                        m = 1
                                        for pon in pon_koc:
                                            if pon_koc[pon] == 4 or pon_koc[pon] == 5:
                                                v = 40 + 4 * pon
                                                u = 0
                                        if not u:
                                            v = 0
                                elif polj == 'Jamb':
                                    s = 9
                                    if s in rucna:
                                        if len(pon_koc) == 1:
                                            v = 50 + 5 * kockica[0]
                                        else:
                                            v = 0
                            if not m:
                                print('To polje je popunjeno.Izaberite opet.\n')
                        rucna.remove(s)
                        r = s
                        unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                        sum_rucna += v
                        o = 1
        elif br_poteza == 1:
            kockica = kockice(int(br_koc-len(z_kockice)))
            kockica.extend(z_kockice)
            print(*kockica)
            print("Da li želite opet da bacate kockice?")
            answer = input()
            if answer == 'Da':
                br_poteza += 1
                print("Koje kockice želite da zadržite?")
                z_kockice = [int(z) for z in input().split()]
            elif answer == 'Ne':
                br_poteza = 3
                print("Izaberite opciju:\n"
                      "1.Popuniti kolonu na dole\n"
                      "2.Popuniti kolonu na gore\n")
                option = int(input())
                o = 0
                while not o:
                    pon_koc = ponavljanja(kockica)
                    if option == 1:
                        b = 'nd'
                        r = 0
                        if (na_dole + 1) in kockica:
                            v = (na_dole + 1) * kockica.count(na_dole + 1)
                        elif na_dole > 5:
                            if na_dole == 6:
                                kockica.sort()
                                if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                    v = 56
                                else:
                                    v = 0
                            elif na_dole == 7:
                                c = list(pon_koc.values())
                                if c == [2, 3] or c == [3, 2]:
                                    v = 30
                                    for pon in pon_koc:
                                        v += pon * pon_koc[pon]
                                else:
                                    v = 0
                            elif na_dole == 8:
                                u = 1
                                for pon in pon_koc:
                                    if pon_koc[pon] == 4:
                                        v = 40 + 4 * pon
                                        u = 0
                                if not u:
                                    v = 0
                            else:
                                if len(pon_koc) == 1:
                                    v = 50 + 5 * kockica[0]
                        else:
                            v = 0
                        unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                        sum_dole += v
                        o = 1
                    elif option == 2:
                        b = 'ng'
                        r = 0
                        if (na_gore + 1) in kockica:
                            v = (na_gore + 1) * kockica.count(na_gore + 1)
                        elif na_gore > 5:
                            if na_gore == 6:
                                kockica.sort()
                                if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                    v = 56
                                else:
                                    v = 0
                            elif na_gore == 7:
                                c = list(pon_koc.values())
                                if c == [2, 3] or c == [3, 2]:
                                    v = 30
                                    for pon in pon_koc:
                                        v += pon * pon_koc[pon]
                                else:
                                    v = 0
                            elif na_gore == 8:
                                u = 1
                                for pon in pon_koc:
                                    if pon_koc[pon] == 4:
                                        v = 40 + 4 * pon
                                        u = 0
                                if not u:
                                    v = 0
                            else:
                                if len(pon_koc) == 1:
                                    v = 50 + 5 * kockica[0]
                                else:
                                    v = 0
                        else:
                            v = 0
                        unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                        sum_gore += v
                        o = 1
        else:
            br_poteza += 1
            kockica = kockice(int(br_koc - len(z_kockice)))
            kockica.extend(z_kockice)
            print(*kockica)
            print("Izaberite opciju:\n"
                  "1.Popuniti kolonu na dole\n"
                  "2.Popuniti kolonu na gore\n")
            option = int(input())
            o = 0
            while not o:
                pon_koc = ponavljanja(kockica)
                if option == 1:
                    b = 'nd'
                    r = 0
                    if (na_dole + 1) in kockica:
                        v = (na_dole + 1) * kockica.count(na_dole + 1)
                    elif na_dole > 5:
                        if na_dole == 6:
                            kockica.sort()
                            if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                v = 46
                            else:
                                v = 0
                        elif na_dole == 7:
                            c = list(pon_koc.values())
                            if c == [2, 3] or c == [3, 2]:
                                v = 30
                                for pon in pon_koc:
                                    v += pon * pon_koc[pon]
                            else:
                                v = 0
                        elif na_dole == 8:
                            u = 1
                            for pon in pon_koc:
                                if pon_koc[pon] == 4:
                                    v = 40 + 4 * pon
                                    u = 0
                            if not u:
                                v = 0
                        else:
                            if len(pon_koc) == 1:
                                v = 50 + 5 * kockica[0]
                    else:
                        v = 0
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_dole += v
                    o = 1
                elif option == 2:
                    b = 'ng'
                    r = 0
                    if (na_gore + 1) in kockica:
                        v = (na_gore + 1) * kockica.count(na_gore + 1)
                    elif na_gore > 5:
                        if na_gore == 6:
                            kockica.sort()
                            if kockica == [1, 2, 3, 4, 5] or kockica == [2, 3, 4, 5, 6]:
                                v = 46
                            else:
                                v = 0
                        elif na_gore == 7:
                            c = list(pon_koc.values())
                            if c == [2, 3] or c == [3, 2]:
                                v = 30
                                for pon in pon_koc:
                                    v += pon * pon_koc[pon]
                            else:
                                v = 0
                        elif na_gore == 8:
                            u = 1
                            for pon in pon_koc:
                                if pon_koc[pon] == 4:
                                    v = 40 + 4 * pon
                                    u = 0
                            if not u:
                                v = 0
                        else:
                            if len(pon_koc) == 1:
                                v = 50 + 5 * kockica[0]
                            else:
                                v = 0
                    else:
                        v = 0
                    unos(ret_mat, talon, b, na_dole, na_gore, v, r)
                    sum_gore += v
                    o = 1
    a = 0
    for i in ret_mat:
        a += len(i)
    if a == 30:
        talon = konverzija(ret_mat, talon)
        for i in range(len(ret_mat)):
            del ret_mat[i]

ret_mat, talon, rucna = prazan_talon()
x, ret_mat, talon, rucna, br_bacanja = menu(ret_mat, talon, rucna, br_bacanja)
while x != 5:
    x, ret_mat, talon, rucna, br_bacanja = menu(ret_mat, talon, rucna, br_bacanja)
    if br_bacanja == 30:
        print('Popunili ste ceo talon.Igra je gotova.')
        x = 5