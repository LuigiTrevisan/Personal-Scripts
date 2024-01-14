import itertools
from colorama import Fore, Style, Back

colors = ['▲', '▼', '◄', '►']
num_pegs = 4
unknown = '?'
all_combinations = list(itertools.product(colors, repeat=num_pegs))
current_guess = ('▲', '▲', '▼', '▼')


def score_guess(guess, all_combinations):
    possible_feedbacks = [(black, white) for black in range(
        num_pegs + 1) for white in range(num_pegs + 1 - black)]
    scores = []
    for feedback in possible_feedbacks:
        remaining_combinations = filter_combinations(
            all_combinations, guess, feedback)
        scores.append(len(all_combinations) - len(remaining_combinations))
    return min(scores)


def get_best_guess(all_combinations):
    best_score = -1
    best_guess = None
    for guess in all_combinations:
        score = score_guess(guess, all_combinations)
        if score > best_score or (score == best_score and guess in all_combinations):
            best_score = score
            best_guess = guess
    return best_guess


def next_guess(all_combinations):
    min_max = float('inf')
    for guess in all_combinations:
        max_combinations = 0
        for feedback in itertools.product(range(num_pegs + 1), repeat=2):
            count = len(
                [comb for comb in all_combinations if get_feedback(guess, comb) == feedback])
            max_combinations = max(max_combinations, count)
        if max_combinations < min_max:
            min_max = max_combinations
            best_guess = guess
    return best_guess


def print_guess(guess, no_score=False):
    for peg in guess:
        if peg in ['▲', '▼']:
            print(Fore.YELLOW + peg, end=' ')
        else:
            print(Fore.BLUE + peg, end=' ')
    if not no_score:
        print(Back.RESET + Fore.RESET + "\nThe score of this guess is: " + Fore.RED +
              str(score_guess(current_guess, all_combinations)))
    print(Style.RESET_ALL)


def get_feedback(guess, secret):
    black = sum(g == s for g, s in zip(guess, secret))
    white = sum(min(guess.count(c), secret.count(c)) for c in colors) - black
    return black, white


def filter_combinations(all_combinations, guess, feedback):
    return [comb for comb in all_combinations if feedback_matches(get_feedback(guess, comb), feedback)]


def feedback_matches(actual, expected):
    return all(a == e or e == unknown for a, e in zip(actual, expected))


def reset_game(error=None):
    if error:
        print(Fore.RED + error)
    print(Fore.GREEN + "Starting a new game...\n\n")
    all_combinations = list(itertools.product(colors, repeat=num_pegs))
    current_guess = ('▲', '▲', '▼', '▼')
    return all_combinations, current_guess


def get_user_feedback():
    black = input(Fore.GREEN + "✅: " + Style.RESET_ALL)
    while black not in [str(i) for i in range(num_pegs + 1)] or not (black.isdigit() or black == unknown):
        black = input(Fore.GREEN + "✅: " + Style.RESET_ALL)
    black = int(black) if black != unknown else unknown
    white = input(Fore.GREEN + "⚪: " + Style.RESET_ALL)
    while white not in [str(i) for i in range(num_pegs + 1)] or not (white.isdigit() or white == unknown):
        white = input(Fore.GREEN + "⚪: " + Style.RESET_ALL)
    white = int(white) if white != unknown else unknown
    return black, white


def game_loop(all_combinations, current_guess):
    print_guess(current_guess)
    black, white = get_user_feedback()
    print()

    if black == num_pegs:
        print(Back.RESET + Fore.RESET + "🌟🌟🌟" + Style.RESET_ALL)
        print("The secret code is: " + Style.RESET_ALL, end='')
        print_guess(current_guess, no_score=True)
        print(Back.RESET + Fore.RESET + "🌟🌟🌟\n" + Style.RESET_ALL)
        all_combinations, current_guess = reset_game()
        return all_combinations, current_guess

    all_combinations = filter_combinations(
        all_combinations, current_guess, (black, white))
    if len(all_combinations) < 1:
        all_combinations, current_guess = reset_game(
            "There are no combinations that match that feedback. Please check your input and try again.")
        return all_combinations, current_guess

    if len(all_combinations) == 1:
        print(Back.RESET + Fore.RESET + "🌟🌟🌟" + Style.RESET_ALL)
        print("The secret code is: " + Style.RESET_ALL, end='')
        print_guess(all_combinations[0], no_score=True)
        print(Back.RESET + Fore.RESET + "🌟🌟🌟\n" + Style.RESET_ALL)
        all_combinations, current_guess = reset_game()
        return all_combinations, current_guess

    current_guess = next_guess(all_combinations)
    return all_combinations, current_guess


if __name__ == "__main__":
    print(Back.RED + Fore.BLACK + "Welcome to Codebreaker Solver!" + Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK +
          "Developed by: @LuigiTrevisan\n" + Style.RESET_ALL)

    while True:
        try:
            all_combinations, current_guess = game_loop(
                all_combinations, current_guess)
        except KeyboardInterrupt:
            print(Back.RESET + Fore.RED + "\n\nExiting..." + Style.RESET_ALL)
            break
        except Exception as e:
            print(Back.RESET + Fore.RED + "\n\nAn error occured: \n" +
                  str(e) + Style.RESET_ALL)
            break
