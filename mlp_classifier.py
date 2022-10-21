# Library imports
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# File imports
from compute_performance import get_true_cv_target_data, write_to_performance_file

# 2.3.3: Base-MLP
def base_mlp(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Base MLP')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    base_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )

    # Test on sentiments
    print()
    print('Sentiments:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=2)
    base_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )

# Base-MLP model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def base_mlp_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    # Using default parameters for MLPClassifier
    # classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter = 200, activation = 'relu', solver = 'adam')
    classifier = MLPClassifier(verbose=True, early_stopping=True)


    # Train the model
    model = classifier.fit(X=cv_train_fit, y=target_true_train)
    # print("Class priors log = ", model.class_log_prior_)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Write to file
    model_description = 'The Base-MLP model ' + target_name + ' with default hyper-parameter values'
    write_to_performance_file(
        model_description=model_description,
        target_true_test=target_true_test,
        target_predict=target_predict
    )

# 2.3.4: Top-MLP
def top_mlp(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Top MLP')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    top_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )

    # Test on sentiments
    print()
    print('Sentiments:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=2)
    top_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )


# Top-MLP model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def top_mlp_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    parameters = {
        'hidden_layer_sizes': [(200, 150, 100), (100, 75)],
        'max_iter': [200],
        'activation': ['logistic', 'tanh', 'relu', 'identity'],
        'solver': ['adam', 'sgd'],
        'verbose': [True],
        'early_stopping': [True]
    }
    
    classifier = MLPClassifier()
    grid_search = GridSearchCV(classifier, parameters)

    # Train the model
    model = grid_search.fit(X=cv_train_fit, y=target_true_train)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Write to file
    # model_description = 'The Top-MLP model ' + target_name + \
    #                     ' with GridSearchCV and hyper-parameter alpha of list: ' + \
    #                     ', '.join(str(alpha) for alpha in alpha_list)
    # write_to_performance_file(
    #     model_description=model_description,
    #     target_true_test=target_true_test,
    #     target_predict=target_predict
    # )
