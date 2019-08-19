from misc_fn import dump, load
list = load('emotion.json')
print(list)

training_dict = {
    #  Keltner, Dacher; Cowen, Alan S. (2017-09-19).
    #  "Self-report captures 27 distinct categories of emotion bridged by continuous gradients".
    #  Proceedings of the National Academy of Sciences 114 (38): E7900–E7909.
    #  doi:10.1073/pnas.1702247114. ISSN 0027-8424. PMID 28874542.
    'emotions_list': [
        'Admiration',
        'Adoration',
        'Aesthetic Appreciation',
        'Amusement',
        'Anxiety',
        'Awe',
        'Awkwardness',
        'Boredom',
        'Calmness',
        'Confusion',
        'Craving',
        'Disgust',
        'Empathetic pain',
        'Entrancement',
        'Envy',
        'Excitement',
        'Fear',
        'Horror',
        'Interest',
        'Joy',
        'Nostalgia',
        'Romance',
        'Sadness',
        'Satisfaction',
        'Sexual desire',
        'Sympathy',
        'Triumph'
    ]
    'emoticon_list': [

    ]
}


