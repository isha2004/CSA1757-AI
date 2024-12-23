import math
from collections import Counter

# Function to calculate entropy
def entropy(labels):
    total_count = len(labels)
    label_counts = Counter(labels)
    entropy_value = 0.0
    for count in label_counts.values():
        probability = count / total_count
        entropy_value -= probability * math.log2(probability)
    return entropy_value

# Function to calculate information gain
def information_gain(data, labels, feature_index):
    original_entropy = entropy(labels)
    total_count = len(labels)

    # Split the dataset based on the feature index
    feature_values = [row[feature_index] for row in data]
    value_counts = Counter(feature_values)
    weighted_entropy = 0.0

    for value, count in value_counts.items():
        subset_labels = [labels[i] for i in range(total_count) if data[i][feature_index] == value]
        weighted_entropy += (count / total_count) * entropy(subset_labels)

    return original_entropy - weighted_entropy


# Function to build the decision tree
def build_tree(data, labels, features, depth=0):
    # Base case: if all labels are the same, return the label
    if len(set(labels)) == 1:
        return labels[0]

    # Base case: if there are no more features to split, return the most common label
    if len(features) == 0:
        return Counter(labels).most_common(1)[0][0]

    # Find the feature with the highest information gain
    gains = [information_gain(data, labels, i) for i in range(len(features))]
    best_feature_index = gains.index(max(gains))

    # Create a dictionary to store the tree
    tree = {features[best_feature_index]: {}}

    # Split the dataset by the best feature and build the subtree for each unique value
    unique_values = set(row[best_feature_index] for row in data)
    for value in unique_values:
        subset_data = [row[:best_feature_index] + row[best_feature_index + 1:] for row in data if
                       row[best_feature_index] == value]
        subset_labels = [labels[i] for i in range(len(data)) if data[i][best_feature_index] == value]

        # Remove the used feature
        new_features = features[:best_feature_index] + features[best_feature_index + 1:]

        # Build the subtree
        subtree = build_tree(subset_data, subset_labels, new_features, depth + 1)

        # Add the subtree to the tree
        tree[features[best_feature_index]][value] = subtree

    return tree


# Function to predict a label for a single sample
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    feature = next(iter(tree))
    feature_value = sample.get(feature)

    if feature_value in tree[feature]:
        return predict(tree[feature][feature_value], sample)
    else:
        return None


# Example dataset
data = [
    [1, 0], [1, 1], [0, 0], [0, 1], [0, 0]
]
labels = [0, 1, 0, 1, 0]
features = ['Feature 1', 'Feature 2']

# Build the tree
decision_tree = build_tree(data, labels, features)

# Print the tree
print("Decision Tree:")
print(decision_tree)

# Predict using the tree
sample = {'Feature 1': 0, 'Feature 2': 1}
print("\nPrediction for sample {}: {}".format(sample, predict(decision_tree, sample)))