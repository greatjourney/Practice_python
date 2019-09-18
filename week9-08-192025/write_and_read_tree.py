import json

def make_node(num, left, right): 
    return [num, left, right]

def value(tree): 
    return tree[0]

def left(tree): 
    return tree[1]

def right(tree):
    return tree[2]

EmptyTree = None
def is_empty(tree):
    return tree == EmptyTree

def make_leaf(num):
    return make_node(num, EmptyTree, EmptyTree)

def is_leaf(tree):
    return is_empty(left(tree))  and is_empty(right(tree)) 

def make_hush(tree):
    if is_empty(tree):
        return {}
    elif is_leaf(tree):
        return {"center": value(tree), "left": {}, "right": {}}
    elif is_leaf(left(tree)) and is_empty(right(tree)):
        return {"center":value(tree), "left":make_hush(left(tree)), "right":{}}
    elif is_leaf(right(tree)) and is_empty(left(tree)):
        return {"center":value(tree), "left":{}, "right":make_hush(right(tree))}
    elif is_leaf(left(tree)) and is_leaf(right(tree)):
        return {"center":value(tree), "left":make_hush(left(tree)), "right":make_hush(right(tree))}
    else:
        return {"center":value(tree),"left":make_hush(left(tree)), "right":make_hush(right(tree))}

def is_leaf_left(hash):
    return hash["left"]["left"] == hash["left"]["right"] == {}

def is_leaf_right(hash):
    return hash["right"]["left"] == hash["right"]["right"] == {}

def make_tree(hash):
    if hash == {}:
        return EmptyTree

    elif hash["left"] == hash["right"] == {}:
        return make_leaf(hash["center"])

    elif hash["left"] == {}:
        return make_node(hash["center"],EmptyTree,make_leaf(hash["right"]["center"]))

    elif hash["right"] == {}:
        return make_node(hash["center"],make_leaf(hash["left"]["center"]),EmptyTree)
    
    elif is_leaf_left(hash) and is_leaf_right(hash):
        return make_node(hash["center"], make_leaf(hash["left"]["center"]), make_leaf(hash["right"]["center"]))

    elif is_leaf_left(hash) and not is_leaf_right(hash):
        return make_node(hash["center"], make_leaf(hash["left"]["center"]), make_tree(hash["right"]))

    elif not is_leaf_left(hash) and is_leaf_right(hash):
        return make_node(hash["center"], make_tree(hash["left"]), make_leaf(hash["right"]["center"]))

    else: 
        return make_node(hash["center"], make_tree(hash["left"]), make_tree(hash["right"]))

def write_tree(filename, tree):
    with open(str(filename) + ".txt", "w") as file:
        file.write(json.dumps(make_hush(tree)))

def read_tree(filename):
    with open(str(filename) + ".txt", "r") as file:
        for line in file:
            hash = json.loads(line)
    return make_tree(hash)

t0 = make_leaf(2)
t1 = make_node(1, make_leaf(3), make_leaf(5) )
t2 = make_node(3, t1, t0)
t3 = make_node(1, make_leaf(3),EmptyTree)
write_tree("t0", t0)
write_tree("t1", t1)
write_tree("t2", t2)
write_tree("t3", t3)
print(read_tree("t0")==t0)
print(read_tree("t1")==t1)
print(read_tree("t2")==t2)
print(read_tree("t3")==t3)

