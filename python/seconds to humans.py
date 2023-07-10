def make_readable(seconds):
    #hours = seconds / 3600
    hh=seconds//3600
    #minutes = the seconds that couldnt be converted to hours / 60
    mm=(seconds%3600)//60
    # the rest of the seconds
    ss=seconds - ((hh*3600) + (mm*60))
    return "{:02}:{:02}:{:02}".format(hh, mm, ss)