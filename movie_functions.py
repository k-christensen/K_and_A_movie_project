import pandas as pd

def unique(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def adventure(l):
    adv_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Adventure' in l[ind]:
            adv_list[ind] = 1
        else:
            adv_list[ind] = 0
    return adv_list

def drama(l):
    dra_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Drama' in l[ind]:
            dra_list[ind] = 1
        else:
            dra_list[ind] = 0
    return dra_list

def romance(l):
    rom_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Romance' in l[ind]:
            rom_list[ind] = 1
        else:
            rom_list[ind] = 0
    return rom_list

def action(l):
    act_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Action' in l[ind]:
            act_list[ind] = 1
        else:
            act_list[ind] = 0
    return act_list

def crime(l):
    cri_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Crime' in l[ind]:
            cri_list[ind] = 1
        else:
            cri_list[ind] = 0
    return cri_list

def scifi(l):
    sci_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Sci-Fi' in l[ind]:
            sci_list[ind] = 1
        else:
            sci_list[ind] = 0
    return sci_list

def comedy(l):
    com_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Comedy' in l[ind]:
            com_list[ind] = 1
        else:
            com_list[ind] = 0
    return com_list
            
def family(l):
    fam_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Family' in l[ind]:
            fam_list[ind] = 1
        else:
            fam_list[ind] = 0
    return fam_list

def animation(l):
    ani_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Animation' in l[ind]:
            ani_list[ind] = 1
        else:
            ani_list[ind] = 0
    return ani_list

def thriller(l):
    thr_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Thriller' in l[ind]:
            thr_list[ind] = 1
        else:
            thr_list[ind] = 0
    return thr_list

def mystery(l):
    mys_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Mystery' in l[ind]:
            mys_list[ind] = 1
        else:
            mys_list[ind] = 0
    return mys_list

def horror(l):
    hor_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Horror' in l[ind]:
            hor_list[ind] = 1
        else:
            hor_list[ind] = 0
    return hor_list
            
def biography(l):
    bio_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Biography' in l[ind]:
            bio_list[ind] = 1
        else:
            bio_list[ind] = 0
    return bio_list

def history(l):
    his_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'History' in l[ind]:
            his_list[ind] = 1
        else:
            his_list[ind] = 0
    return his_list

def fantasy(l):
    fan_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Fantasy' in l[ind]:
            fan_list[ind] = 1
        else:
            fan_list[ind] = 0
    return fan_list
            
def music(l):
    mus_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Music' in l[ind]:
            mus_list[ind] = 1
        else:
            mus_list[ind] = 0
    return mus_list
     
def war(l):
    war_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'War' in l[ind]:
            war_list[ind] = 1
        else:
            war_list[ind] = 0
    return war_list
            
def sport(l):
    spo_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Sport' in l[ind]:
            spo_list[ind] = 1
        else:
            spo_list[ind] = 0
    return spo_list
            
def western(l):
    wes_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Western' in l[ind]:
            wes_list[ind] = 1
        else:
            wes_list[ind] = 0
    return pd.Series(wes_list)

def documentary(l):
    doc_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Documentary' in l[ind]:
            doc_list[ind] = 1
        else:
            doc_list[ind] = 0
    return pd.Series(doc_list)

def musical(l):
    musal_list = [0]*len(l)
    for ind in range(0, len(l)):
        if 'Musical' in l[ind]:
            musal_list[ind] = 1
        else:
            musal_list[ind] = 0
    return pd.Series(musal_list)
            
