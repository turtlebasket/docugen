def remove_dirt(image):
    image = morphology.area_closing(image, area_threshold=250, connectivity=1)
    # image = morphology.opening(image, morphology.square(5))

    return image

def calculate_area(countour):
    c = np.expand_dims(countour.astype(np.float32), 1)
    c = cv.UMat(c)
    
    return cv.contourArea(c)

def center_of_mass(X):
    x = X[:,0]
    y = X[:,1]
    g = (x[:-1]*y[1:] - x[1:]*y[:-1])
    A = 0.5*g.sum()
    cx = ((x[:-1] + x[1:])*g).sum()
    cy = ((y[:-1] + y[1:])*g).sum()

    return 1./(6*A)*np.array([cx,cy])

img = remove_dirt(thresh_gray)

def rg_ratio_normalize(imgarr):
    # set max & min to most extreme values, 
    # work up & down respectively from there
    tmin = MAX_TEMP
    tmax = 0

    imgnew = imgarr
    for i in range(len(imgarr)):
        for j in range(len(imgarr[i])):
            px = imgarr[i][j]
            r_norm = normalization_func(px[0])
            g_norm = normalization_func(px[1])

            # apply camera calibration func
            temp_C = pyrometry_calibration_formula(g_norm, r_norm)

            # remove pixels outside calibration range
            if MAX_TEMP != None and temp_C > MAX_TEMP or MIN_TEMP != None and temp_C < MIN_TEMP:
                temp_C = 0

            # update min & max
            if temp_C < tmin and temp_C >= 0:
                tmin = temp_C
            if temp_C > tmax:
                tmax = temp_C

            imgnew[i][j] = [temp_C, temp_C, temp_C]
    return imgnew, tmin, tmax


def pyrometry_calibration_formula(i_ng, i_nr):
    return 362.73 * math.log10(
        (i_ng/i_nr) ** 3
    ) + 2186.7 * math.log10(
        (i_ng/i_nr) ** 2
    ) + 4466.5 * math.log10(
        (i_ng / i_nr)
    ) + 3753.5
