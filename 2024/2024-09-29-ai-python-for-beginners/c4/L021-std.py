from helper_functions import *
from random import sample

spices = ["cumin", "turmeric", "oregano", "paprika"]
vegetables = ["lettuce", "tomato", "carrot", "broccoli"]
proteins = ["chicken", "tofu", "beef", "fish", "tempeh"]

random_spices = sample(spices, 2)
random_vegetables = sample(vegetables, 2)
random_protein = sample(proteins, 1)


prompt = f"""请推荐一个包含以下食材的食谱。

香料: {random_spices}
蔬菜: {random_vegetables}
蛋白质: {random_protein}
"""

print_llm_response(prompt)