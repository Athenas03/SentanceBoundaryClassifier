from sklearn.tree import DecisionTreeClassifier, export_text
import sys
def read_file(filename):
    data = []

    with open(filename,"r") as file:
        for line in file:
            parts = line.strip().split()
            position=parts[0]
            token=parts[1]
            label=parts[2]
            #stored and has 3 values+ adds 3 values to list 
            data.append((position,token,label))
    return data

train_data = read_file(sys.argv[1])
test_data = read_file(sys.argv[2])

vocabulary = set()
for i in range(len(train_data)):
    token = train_data[i][1]
    #remove period from token
    token=token.rstrip('.')
    if token.isalpha():
        vocabulary.add(token)


        
X=[]
y=[]

for i in range(len(train_data) - 1):
    token = train_data[i][1]
    
    if token.endswith('.'):
        L=token.rstrip('.')
        R=train_data[i + 1][1]
        #training data x. y
        
        #feature 1
        feature1=int(L in vocabulary)
        #feature2
        feature2= int(R in vocabulary)

        #Length of L < 4 (values: binary)
        feature3= int(len(L)<4)
        #Is L a number (values: binary)
        feature4= int(L.isdigit())
        ##Is R capitalized (values: binary)
        feature5= int(R[0].isupper())
        #feature 6-does R contain a number
        feature6=0
        for char in R:
            if char.isdigit():
                feature6 = 1
                break
        #feature 7- does L have more than 1 character 
        feature7= int(len(L) >1)
        #feature 8- does R have more than 1 character 
        feature8= int(len(R) >1)
        features= [feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8]
        X.append(features)
        label= train_data[i][2]
        y.append(label)


classifier =DecisionTreeClassifier()
classifier.fit(X, y)


feature_names= ["L_vocab","R_vocab","L_len_less_4","L_is_num","R_capitalized","R_contains_num","L_len_greater_1","R_len_greater_1"]

tree_rules = export_text(classifier, feature_names=feature_names)
print(tree_rules)

X_test=[]
y_test=[]

for i in range(len(test_data)-1):
    token = test_data[i][1]
    if token.endswith("."):
        L=token.rstrip('.')
        R=test_data[i+1][1]
        # 1
        feature1=int(L in vocabulary)
        #2
        feature2= int(R in vocabulary)
        #Length of L < 4 (values: binary)
        feature3= int(len(L)<4)
        #Is L a number (values: binary)
        feature4= int(L.isdigit())
        ##Is R capitalized (values: binary)
        feature5= int(R[0].isupper())
        #feature 6-does R contain a number
        feature6=0
        for char in R:
            if char.isdigit():
                feature6 = 1
                break
        #feature 7- does L have more than 1 character 
        feature7= int(len(L) >1)
        #feature 8- does R have more than 1 character 
        feature8= int(len(R) >1)
        features= [feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8]
        X_test.append(features)

        label= test_data[i][2]
        y_test.append(label)

predictions = classifier.predict(X_test)

correct = 0
for i in range(len(predictions)):
    if predictions[i] == y_test[i]:
        correct+=1
accuracy = correct /len(predictions)*100
print(f"Accuracy:{accuracy:.2f}%")

prediction_index=0
with open("SBD.test.out","w")as file:
    for i in range(len(test_data)-1):
        token = test_data[i][1]
        
        if token.endswith("."):
            position= test_data[i][0]
            token=test_data[i][1]
            
            prediction= predictions[prediction_index]
            
            file.write(position+" "+ token + " "+ prediction+ "\n")
            prediction_index +=1 
