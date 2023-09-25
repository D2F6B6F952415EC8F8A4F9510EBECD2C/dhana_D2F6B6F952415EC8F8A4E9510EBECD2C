"""
Write a function called search_product that takes the list of product aand a target product
name as input.The function should perfrom a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found,or an empty list if the product is not
found.
"""


def linearsearchproduct(productlist, targetProduct):
    indices = []

    for index,product in enumerate (productlist):
      if product == targetProduct:
        indices.append(index)

    return indices


# example usage:
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target ="shoes"
result = linearsearchProduct(product, target)
print(result)