# -*- coding: utf-8 -*-

from goodreads3_stats import *
from my_shelves_global import *

stats = Stats(MY_BOOKS_JSON, MY_SHELF_NAMES_JSON)

"""
Filtering:
"""

# stats.filter_by_range((NUM_PAGES, 200, 300), (NUM_RATINGS, 1000, float('inf')))
# stats.filter_by_date((DATE_STARTED, 2016, 2017), (DATE_READ, 2017, 2017))

# stats.filter_by_shelves(incl_and=(READ, PHILOSOPHY, POETICS_AND_LINGUISTICS))

# to_excl = tuple(set(MY_SHELF_NAMES) - {READ, PHILOSOPHY, POETICS_AND_LINGUISTICS, DEIGMA})
# stats.filter_by_shelves(excl=to_excl)

# stats.filter_by_shelves(incl_or=(DEIGMA, ANTIQUITY))


"""
Printing allotments:
"""

prettyprint_allotment(stats.allotment)  # whole

# prettyprint_allotment(stats.grouped)  # grouped into shelves


"""
Calculations:
"""

# stats.find_total_mean(SPEED)
# stats.find_mean_per_shelf(rubric=SPEED, alpha=False, large_to_small=False)
# stats.find_est_books(rubric=TIME_GAP, large_to_small=True, num_books=10, by_shelf=True)
# stats.find_total_variance(NUM_PAGES)
# stats.find_total_sd(NUM_PAGES)
# stats.find_variance_per_shelf(rubric=SPEED, alpha=True, large_to_small=False)
# stats.find_sd_per_shelf(rubric=SPEED, alpha=False, large_to_small=True)


"""
Updating book:
"""

# title = u"The Wise King: A Christian Prince, Muslim Spain, and the Birth of the Renaissance"
# update_book_shelves(MY_BOOKS_JSON, title, [HISTORY, ISLAMIC_WORLD, MEDIEVAL_AND_RENAISSANCE, READ])
