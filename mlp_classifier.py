# Library imports
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# File imports
from compute_performance import get_true_cv_target_data, write_to_performance_file
from embeddings import average_embeddings

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
        target_true_test=target_true_test,
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

# 3.5: Base-MLP for embeddings
def base_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, corpus, corpus_name='Word2Vec'):
    print()
    print('-------------------------------------------------')
    print('Base MLP')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name = "emotions"

    cv_train_fit, cv_test_transform = average_embeddings(train_tokens, test_tokens, corpus)
    target_true_train = [data_array[1] for data_array in data_train]
    target_true_test = [data_array[1] for data_array in data_test]

    base_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test,
        corpus_name=corpus_name,
        embedding=True
    )


    # Test on sentiments
    print()
    print('Sentiments:')

    target_name = "sentiments"
    target_true_train = [data_array[2] for data_array in data_train]
    target_true_test = [data_array[2] for data_array in data_test]

    base_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test,
        corpus_name=corpus_name,
        embedding=True
    )

# Base-MLP model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def base_mlp_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test, corpus_name="Word2Vec", embedding=False):
    # Define the model classifier
    # Using default parameters for MLPClassifier
    # classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter = 200, activation = 'relu', solver = 'adam')
    classifier = MLPClassifier(early_stopping=True)


    # Train the model
    model = classifier.fit(X=cv_train_fit, y=target_true_train)
    # print("Class priors log = ", model.class_log_prior_)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Write to file
    if embedding:
        model_description = 'Embeddings: The Base-MLP model using ' + corpus_name + ' for ' + target_name + ' with default hyper-parameter values'
        write_to_performance_file(
            model_description=model_description,
            target_true_test=target_true_test,
            target_predict=target_predict
        )
    else:
        model_description = 'The Base-MLP model for ' + target_name + ' with default hyper-parameter values'
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
        target_true_test=target_true_test,
        hidden_layer_sizes=[(5, 5, 5), (10, 10)],
        activation=['logistic', 'tanh', 'relu', 'identity'],
        solver=['adam', 'sgd']
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
        target_true_test=target_true_test,
        hidden_layer_sizes=[(5, 5, 5), (10, 10)],
        activation=['logistic', 'tanh', 'relu', 'identity'],
        solver=['adam', 'sgd']
    )

# 3.6: Top-MLP for embeddings
def top_mlp_embeddings(data_train, data_test, train_tokens, test_tokens, corpus, corpus_name="Word2Vec"):
    print()
    print('-------------------------------------------------')
    print('Top MLP')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name = "emotions"

    cv_train_fit, cv_test_transform = average_embeddings(train_tokens, test_tokens, corpus)
    target_true_train = [data_array[1] for data_array in data_train]
    target_true_test = [data_array[1] for data_array in data_test]

    top_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test,
        hidden_layer_sizes=[(10, 5)],
        activation=['relu'],
        solver=['adam'],
        corpus_name=corpus_name,
        embedding=True
    )

    # Test on sentiments
    print()
    print('Sentiments:')
    target_name = "sentiments"

    cv_train_fit, cv_test_transform = average_embeddings(train_tokens, test_tokens, corpus)
    target_true_train = [data_array[2] for data_array in data_train]
    target_true_test = [data_array[2] for data_array in data_test]

    top_mlp_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test,
        corpus_name=corpus_name,
        hidden_layer_sizes=[(10, 5)],
        activation=['relu'],
        solver=['adam'],
        embedding=True
    )


# Top-MLP model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def top_mlp_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test, 
hidden_layer_sizes, activation, solver, corpus_name="Word2Vec", embedding=False):
    # Define the model classifier
    parameters = {
        'hidden_layer_sizes': hidden_layer_sizes,
        'activation': activation,
        'solver': solver,
        'max_iter': [15],
        'early_stopping': [True]
    }
    
    classifier = MLPClassifier()
    grid_search = GridSearchCV(classifier, parameters, n_jobs=-1)

    # Train the model
    model = grid_search.fit(X=cv_train_fit, y=target_true_train)

    # Predict
    target_predict = model.predict(cv_test_transform)
    print("Best parameters: ", grid_search.best_params_)

    # Write to file
    if embedding:
        model_description = 'Embeddings: The Top-MLP model using ' + corpus_name + ' for ' + target_name + \
                            ' with GridSearchCV and hyper-parameter hidden_layer_sizes of lists: ' + \
                            str(hidden_layer_sizes) + ', activation of list: ' + str(activation) + 'solver of list: ' +  str(solver)
        write_to_performance_file(
            model_description=model_description,
            target_true_test=target_true_test,
            target_predict=target_predict)
    else:
        model_description = 'The Top-MLP model for ' + target_name + \
                            ' with GridSearchCV and hyper-parameter hidden_layer_sizes of lists: ' + \
                            str(hidden_layer_sizes) + ', activation of list: ' + str(activation) + 'solver of list: ' +  str(solver)
        write_to_performance_file(
            model_description=model_description,
            target_true_test=target_true_test,
            target_predict=target_predict)
