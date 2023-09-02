import random as ran

player_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Environment:
    @staticmethod
    def get_result(battle_scores, top_three):
        """Determine the match result based on current scores and top three scores."""
        # If the highest score in the current battle is greater than the lowest of the top three scores
        if max(battle_scores) > min(top_three) and min(top_three) != 0:
            return ran.randint(-1, ran.randint(0, ran.randint(2, 4)))
        else:
            return ran.randint(0, ran.randint(1, ran.randint(2, 3)))

class SwissBracket:
    def __init__(self, player_list):
        self.player_scores = [[player for player in player_list]]
        self.new_player_scores = [[]]
        self.game_history = set()  # To keep track of previous matches
        self.player_count = len(player_list)

    def play_round(self):
        """Play a round of the tournament."""
        print(f"Round {len(self.new_player_scores)}")
        self.new_player_scores.append([])
        top_three = [0]
        for _ in range(int(self.player_count / 2)):
            self._play_match(top_three)

        # Update player scores for the next round
        self.player_scores = [list(players) for players in self.new_player_scores]
        self.new_player_scores = [[] for _ in self.new_player_scores]

        print("Standings:")
        # Print current standings
        placing = 0
        for players in self.player_scores[::-1]:
            if players:
                print(f"#{placing + 1}: {', '.join(players)}")
            placing += len(players)

    def _play_match(self, top_three):
        """Play a match between two players."""
        battle = ['', '']
        # Remove empty score lists
        while not self.player_scores[-1]:
            self.player_scores.pop()
        battle_scores = [len(self.player_scores) - 1, 0]
        battle[0] = self.player_scores[-1].pop(0)

        # Create a sorted list of players and their scores
        e = list(zip(
            list(range(len(self.player_scores))),
            [''.join(player_i) for player_i in self.player_scores]
        ))
        e = sorted(e, key=lambda a: a[0])
        found_player = False

        # Determine the top three scores
        for score_j, players in e[::-1]:
            if (score_j > min(top_three) or len(top_three) < min(len(self.new_player_scores), 2)) and score_j not in top_three and players:
                if top_three == [0]:
                    top_three = []
                top_three.append(score_j)
                top_three.sort()
                top_three = top_three[:3]

        # Pair players for a match
        for score_j, players in e[::-1]:
            for player_j in players:
                battle[1] = player_j
                battle_scores[1] = int(score_j)
                if ''.join(sorted(battle)) in self.game_history:  # Check for rematches
                    continue
                elif battle[1] in self.player_scores[battle_scores[1]]:
                    found_player = True
                    self.player_scores[battle_scores[1]].remove(battle[1][-1])
                    self.game_history.add(''.join(sorted(battle)))
                    result = Environment.get_result(battle_scores, top_three)
                    if ''.join(sorted(battle)) != ''.join(battle):
                        result = 3 - result
                    battle_scores[0] += 3 - result
                    battle_scores[1] += result
                    for _ in range(max(0, max(battle_scores) + 1 - len(self.new_player_scores))):
                        self.new_player_scores.append([])
                    self.new_player_scores[battle_scores[0]].append(battle[0][-1])
                    self.new_player_scores[battle_scores[1]].append(battle[1][-1])
                    # Print match result
                    if max(battle_scores) > min(top_three) and min(top_three) != 0:
                        print(f"{battle[0][-1]} vs. {battle[1][-1]} {['3-0', '3-1', '3-2', '2-3', '1-3', '0-3'][result + 1]}")
                    else:
                        print(f"{battle[0][-1]} vs. {battle[1][-1]} {['2-0', '2-1', '1-2', '0-2'][result]}")
                if found_player:
                    break
            if found_player:
                break

        # Handle cases where a new opponent couldn't be found (rematch scenario)
        if not found_player:
            while not self.player_scores[-1]:
                self.player_scores.pop()
            battle_scores[1] = len(self.player_scores) - 1
            battle[1] = self.player_scores[-1].pop(0)
            result = Environment.get_result(battle_scores, top_three)
            if ''.join(sorted(battle)) != ''.join(battle):
                result = 3 - result
            battle_scores[0] += 3 - result
            battle_scores[1] += result
            for _ in range(max(0, max(battle_scores) + 1 - len(self.new_player_scores))):
                self.new_player_scores.append([])
            self.new_player_scores[battle_scores[0]].append(battle[0])
            self.new_player_scores[battle_scores[1]].append(battle[1])
            # Print rematch result
            if max(battle_scores) > min(top_three) and min(top_three) != 0:
                print(f"{battle[0][-1]} vs. {battle[1][-1]} {['3-0', '3-1', '3-2', '2-3', '1-3', '0-3'][result + 1]} {['', 'Rematch'][int(''.join(sorted(battle)) in self.game_history)]}")
            else:
                print(f"{battle[0][-1]} vs. {battle[1][-1]} {['2-0', '2-1', '1-2', '0-2'][result]} {['', 'Rematch'][int(''.join(sorted(battle)) in self.game_history)]}")
            self.game_history.add(''.join(sorted(battle)))

    def run_tournament(self, rounds):
        """Run the entire tournament for a specified number of rounds."""
        for _ in range(rounds):
            self.play_round()

# Main execution
swiss = SwissBracket(player_list)
rounds = max(5, len(player_list) - 10)
swiss.run_tournament(rounds)
input("Press Enter to exit...")
