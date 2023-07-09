import pandas as pd
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def load_train(path):
    labels = pd.read_csv(path + "labels.csv")
    train_datagen = ImageDataGenerator(
        validation_split=0.25,
        rescale=1./255,
        horizontal_flip=True,
        rotation_range=20,
    )
    train_datagen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + "final_files/",
        x_col="file_name",
        y_col="real_age",
        target_size=(224, 224),
        batch_size=32,
        subset="training",
        class_mode="raw",
        seed=12345,
    )

    return train_datagen_flow


def load_test(path):
    labels = pd.read_csv(path + "labels.csv")
    valid_datagen = ImageDataGenerator(validation_split=0.25, rescale=1./255)
    valid_datagen_flow = valid_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + "final_files/",
        x_col="file_name",
        y_col="real_age",
        target_size=(224, 224),
        batch_size=32,
        subset="validation",
        class_mode="raw",
        seed=12345,
    )

    return valid_datagen_flow


def create_model(input_shape):

    optimizer = Adam(learning_rate=0.0001)

    backbone = ResNet50(
        input_shape=input_shape,
        include_top=False,
        weights="/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5",
    )

    model = Sequential()

    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation="relu"))

    model.compile(loss="mean_squared_error", optimizer=optimizer, metrics=["mae"])

    return model


def train_model(
    model,
    train_data,
    test_data,
    batch_size=None,
    epochs=15,
    steps_per_epoch=178,
    validation_steps=60,
):
    model.fit(
        train_data,
        validation_data=test_data,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        epochs=epochs,
        batch_size=batch_size,
        verbose=2,
    )

    return model
