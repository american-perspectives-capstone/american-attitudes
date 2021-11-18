###Import Libraries necessary for the functions
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, recall_score, plot_confusion_matrix
from sklearn.linear_model import LogisticRegression


#####First we will create a DataFrame with a list of scores for each model, so we can easily compare models#######
def test_a_model(X_train, y_train, X_validate, y_validate, model, model_name, score_df):
    '''
    Function takes in X and y train
    X and y validate (or test) 
    A model with it's hyper parameters
    And a df to store the scores 
    - Set up an empty dataframe with score_df first
    - score_df = pd.DataFrame(columns = ['model_name', 'train_score', 'validate_score'])
    '''
    #Set model
    this_model = model
    
    #Fit the model with the train dataset
    this_model.fit(X_train, y_train)

    #Get accuracy score on train dataset
    train_score = this_model.score(X_train, y_train)
    
    #Get accuracy score on validate dataset
    validate_score = this_model.score(X_validate, y_validate)
    
    #Create dictionary with model_name and scores
    model_dict = {'model_name': model_name, 
                  'train_score': train_score, 
                  'validate_score':validate_score}
    score_df = score_df.append(model_dict, ignore_index = True)
    
    #Return DataFrame
    return score_df


#####The functions below create Classification Models and Labels for these Models#################################
#####We will use test_a_model function above to evaluate the models defined by the functions below################

def decision_tree_models(depth):
    '''
    This function takes the use input for max depth, then creates a defines a series of Decision Tree models and 
    labels for those decision tree models from 3 to the user-specified depth. 
    '''
    #Make empty list of Decision Tree Models
    tree_list = []
    
    #Loop through user-defined depths to make Decision Tree Models
    for i in range(3, depth):
        tree_list.append(DecisionTreeClassifier(max_depth = i, random_state = 123))

    #Make empty list of Decision Tree Model names
    tree_model_name_list = []

    # create list of model names that correspond to models
    for i in range(3, 10):
        tree_model_name_list.append(f"decision_tree_depth_{i}")

    
    #Return list of models and model names
    return tree_list, tree_model_name_list

def random_forest_models(samples, depth, number_of_features):
    '''
    This function take the user input for:
    (1) the maximum number of min samples leaf
    (2) the maximum depth
    (3) the number of features the user plans on using in the model. 
    The function then defines a series of Random Forest models and labels for those models 
    based on the user-specied data. 
    The user inputs the number inputs the number of features they want to use because we will 
    use this function to model various amounts of features. Including the amount of features in the 
    label will let us avoid duplicate labels. 
    '''
    #Make empty list of Random Forest Models
    forest_list = []

    #Loop through user-defined depths and number of samples to make Random Forest Models 
    for i in range(3, samples):
        for j in range(1, depth):
            forest_list.append(RandomForestClassifier(min_samples_leaf = i, max_depth = j))

    #Make empty list of Random Forest model names
    forest_name_list = []
    
    #Loop through user-defines depths and number of samples to make Random Forest Model labels
    for i in range(3, samples):
        for j in range(0, depth):
            forest_name_list.append(f"{number_of_features}_features_random_forest_min_samples_leaf_{i}_depth_{j}")
        
    #Return list of models and list of model names
    return forest_list, forest_name_list

def k_neighbors_models(num_neighbors):
    '''
    This function takes the user input for the maximum number of neighbors. 
    The function then defines a series of K Nearest Neighbors models and labels for those models up
    to the maximum number of neighbors that the user specified. 
    '''
    #Make empty list of K Nearest Neighbors Models
    k_neighbors_list = []

    #Loop through user-defined number of neighbors to make K-Nearest Neighbors Models
    for i in range(5, num_neighbors):
        k_neighbors_list.append(KNeighborsClassifier(n_neighbors = i, weights = 'uniform'))

    #Make empty list of K Nearest Neighbors model labels
    k_names_list = []
    
    #Loop through the user-defined number of neighbors to make labels for the K Nearest Neighbros Models
    for i in range(5, num_neighbors):
        k_names_list.append(f"k_nearest_neighbors_{i}")
    
    return k_neighbors_list, k_names_list