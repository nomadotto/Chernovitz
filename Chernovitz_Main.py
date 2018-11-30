

import Blueprint

b = Blueprint.Blueprint(6)
b.make_random_tasks()
odds = []
for task in b.tasks:
    success_rate = task.make_fixed_difficulty_requirements()
    odds.append(success_rate)