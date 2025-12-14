# utils.py

ROUNDS_COMPLETED = 3  # 👈 YOU manually update this (0–4)

def user_team_total(user_tracked_golfers):
    selections = [
        user_tracked_golfers.selection1,
        user_tracked_golfers.selection2,
        user_tracked_golfers.selection3,
        user_tracked_golfers.selection4,
        user_tracked_golfers.selection5,
    ]

    total = 0
    count = 0

    for golfer in selections:
        if not golfer:
            continue

        scores = [
            golfer.day_1_score_Masters26,
            golfer.day_2_score_Masters26,
            golfer.day_3_score_Masters26,
            golfer.day_4_score_Masters26,
        ]

        # Only include rounds that are completed
        valid_scores = scores[:ROUNDS_COMPLETED]

        if any(score is not None for score in valid_scores):
            total += sum(score for score in valid_scores if score is not None)
            count += 1

    if count == 0:
        return 0

    return total / count
