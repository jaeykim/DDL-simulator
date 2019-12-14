from tensorflow import keras

def load_data(data_id):
    x_train, y_train, x_test, y_test = [], [], [], []

    if data_id is 'fashion_mnist':
        (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0
    
    elif data_id is 'mnist':
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255

    elif data_id is 'cifar10':
        (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

    else:
        raise ValueError

    return x_train, y_train, x_test, y_test
