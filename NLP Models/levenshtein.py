from thefuzz import fuzz
from thefuzz import process
# https://towardsdatascience.com/natural-language-processing-for-fuzzy-string-matching-with-python-6632b7824c49
a = fuzz.partial_ratio('phone_number', 'phone')
print(a)
