def rgba_convert(r, g, b):
    r_new = r/255
    g_new = g/255
    b_new = b/255

    print('RGBA: ({:.2f}, {:.2f}, {:.2f}, 1)'.format(r_new, g_new, b_new))

rgba_convert(255, 99, 71)