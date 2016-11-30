def residuals(xs, ys, yf_inv, xf_inv=None):
    if xf_inv != None:
        tx = [xf_inv(x) for x in xs]
    else:
        tx = xs
    ty = [yf_inv(y) for y in ys]

    