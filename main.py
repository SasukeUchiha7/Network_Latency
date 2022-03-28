import utils
import post

PATH = 'models/trained_model.h5'

#load model
model = utils.load_model(PATH)

#load data
x_train, x_test, y_test = utils.load_dataset()

score=model.evaluate(x_test,y_test)

print('Test loss',score[0])
print('Test accuracy',score[1])

layers = ['input_layer', 'conv_1', 'pool_1', 'dropout_1', 'flate_1', 'dense_1', 'dropout_2', 'output_layer']

## posting output of each layer
for layer in layers:
    packet, shape = utils.intermediate(model, layer, x_train)
    post.post(packet, layer, shape)