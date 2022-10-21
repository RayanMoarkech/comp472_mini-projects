# Library imports
from sklearn import tree
from sklearn.model_selection import GridSearchCV

# File imports
from compute_performance import get_true_cv_target_data, write_to_performance_file


# 2.3.2: Base-DT
def base_dt(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Base DT')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    base_dt_model(
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
    base_dt_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )


# Base-DT model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def base_dt_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    classifier = tree.DecisionTreeClassifier()

    # Train the model
    model = classifier.fit(X=cv_train_fit, y=target_true_train)
    # print("Class priors log = ", model.class_log_prior_)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Write to file
    model_description = 'The Base-DT model ' + target_name + ' with default hyper-parameter values'
    write_to_performance_file(
        model_description=model_description,
        target_true_test=target_true_test,
        target_predict=target_predict
    )





# 2.3.4: Top-DT
def top_dt(data_train, data_test):
    print()
    print('-------------------------------------------------')
    print('Top MNB')
    print('-------------------------------------------------')

    # Test on emotions
    print()
    print('Emotions:')
    target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test = \
        get_true_cv_target_data(data_train=data_train, data_test=data_test, index=1)
    top_dt_model(
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
    top_dt_model(
        target_name=target_name,
        cv_train_fit=cv_train_fit,
        target_true_train=target_true_train,
        cv_test_transform=cv_test_transform,
        target_true_test=target_true_test
    )


# Top-DT model that takes in the index to train and test
# the emotions with index 1
# or the sentiments with index 2
def top_dt_model(target_name, cv_train_fit, target_true_train, cv_test_transform, target_true_test):
    # Define the model classifier
    max_depth = [5,10]
    min_samples = [2,5,10]
    parameters = {'criterion': ['entropy'],
                 'max_depth': max_depth,
                  'min_samples_split': min_samples}

    classifier = tree.DecisionTreeClassifier()
    grid_search = GridSearchCV(classifier, parameters)

    # Train the model
    model = grid_search.fit(X=cv_train_fit, y=target_true_train)

    # Predict
    target_predict = model.predict(cv_test_transform)

    # Write to file
    model_description = 'The Top-DT model ' + target_name + \
                        ' with GridSearchCV and hyper-parameters max depth of ' + \
                        ' & '.join(str(max) for max in max_depth) + \
                        ' and min_samples_split of ' +\
                        ' & '.join(str(min) for min in min_samples) +\
                        ' and criterion of entropy:'
    write_to_performance_file(
        model_description=model_description,
        target_true_test=target_true_test,
        target_predict=target_predict
    )



