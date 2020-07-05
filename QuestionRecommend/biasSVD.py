import torch


def biasSVD(data, k, steps, learning_rate, l):
    print(data)
    n = data.shape[0]
    m = data.shape[1]
    item = torch.randn(m, k).normal_(0, 1)
    user = torch.randn(n, k).normal_(0, 1)
    bi = torch.randn(m, 1).normal_(0, 1)
    bu = torch.randn(n, 1).normal_(0, 1)
    miu = 3.5
    train = torch.load('/content/drive/My Drive/train', map_location=torch.device('cpu'))
    _ = train.shape[0]
    print(user.shape)
    print(item.shape)
    for t in range(steps):
        print('----------ROUND', t, '----------BEGIN')
        user_gradient = torch.zeros(n, k)
        item_gradient = torch.zeros(m, k)
        bi_gradient = torch.zeros(m, 1)
        bu_gradient = torch.zeros(n, 1)
        for __ in range(_):
            i = train[__][0]
            j = train[__][1]
            error = torch.dot(user[i], item[j].t()) + bi[j] + bu[i] + miu - data[i][j]
            user_gradient[i] = torch.add(user_gradient[i], torch.mul(error, item[j]))
            item_gradient[j] = torch.add(item_gradient[j], torch.mul(error, user[i]))
            bu_gradient[i] = torch.add(bu_gradient[i], error)
            bi_gradient[j] = torch.add(bi_gradient[j], error)
        user_gradient = torch.add(user_gradient, torch.mul(l, user))
        item_gradient = torch.add(item_gradient, torch.mul(l, item))
        bu_gradient = torch.add(bu_gradient, torch.mul(l, bu))
        bi_gradient = torch.add(bi_gradient, torch.mul(l, bi))
        print('----------gradient has trained----------')
        user = torch.sub(user, learning_rate * user_gradient)
        item = torch.sub(item, learning_rate * item_gradient)
        bu = torch.sub(bu, learning_rate * bu_gradient)
        bi = torch.sub(bi, learning_rate * bi_gradient)
        error = 0
        count = train.shape[0]
        for __ in range(_):
            i = train[__][0]
            j = train[__][1]
            error += torch.pow(data[i][j]-torch.dot(user[i], item[j].t())-miu-bi[j]-bu[i], 2)
        print('----------ROUND', t, '----------RMSE is: ', torch.sqrt((1/count)*error))
        print('----------ROUND', t, '----------TRAIN END')
    test = torch.load('/content/drive/My Drive/test', map_location=torch.device('cpu'))
    _ = test.shape[0]
    for __ in range(_):
      i = test[__][0]
      j = test[__][0]
      error += torch.pow(data[i][j]-torch.dot(user[i], item[j].t())-miu-bi[j]-bu[i], 2)
      print(torch.sqrt((1/count)*error))