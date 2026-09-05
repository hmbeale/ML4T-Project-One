""""""  		  	   		 		  		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 		  		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 		  		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 		  		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 		  		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 		  		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 		  		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 		  		  		  		    	 		 		   		 		  
or edited.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 		  		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 		  		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 		  		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Student Name: Holden Beale (replace with your name)  		  	   		 		  		  		  		    	 		 		   		 		  
GT User ID: hbeale7 (replace with your User ID)  		  	   		 		  		  		  		    	 		 		   		 		  
GT ID: 904202603 (replace with your GT ID)  		  	   		 		  		  		  		    	 		 		   		 		  
"""  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
import matplotlib

import matplotlib.pyplot as plt
import numpy as np  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def author():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    return "hbeale7"    		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def gtid():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    return 904202603    		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 		  		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    result = False  		  	   		 		  		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 		  		  		  		    	 		 		   		 		  
        result = True  		  	   		 		  		  		  		    	 		 		   		 		  
    return result  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def test_code():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
      		  	   		 		  		  		  		    	 		 		   		 		  
    np.random.seed(gtid())  	   
    episode_size = 1000 # number of spins in an episode

    experiment1(episode_size)
    experiment2(episode_size)


def experiment1(episode_size):
    num_episodes = 10
    spin_record = spin_multiple_episodes(num_episodes, episode_size, 0, False)

    for i in range(num_episodes):
        plt.plot(spin_record[i], label=f"Episode {i + 1}")

    plt.title("fig. 1: 10 Roulette Episodes")
    std_plot()  

    plt.savefig("figure_1.png")
    plt.close()

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    plt.title("fig. 2: Mean Values for 10 episodes of Roulette")
    std_plot()

    plt.savefig("figure_2.png")
    plt.close()

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    plt.title("fig. 3: Median Values for 10 episodes of Roulette")
    std_plot()

    plt.savefig("figure_3.png")
    plt.close()

    print_results("experiment 1 results", means, medians, stddevs)

def experiment2(episode_size):
    num_episodes = 1000
    spin_record = spin_multiple_episodes(num_episodes, episode_size, -256, True)

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    plt.title("fig. 4: Mean Values for 1000 episodes of Roulette")
    std_plot()

    plt.savefig("figure_4.png")
    plt.close()

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    plt.title("fig. 5: Median Values for 1000 episodes of Roulette")
    std_plot()

    plt.savefig("figure_5.png")
    plt.close()

    values, counts = np.unique(spin_record[:, -1], return_counts=True)
    print(values, counts)
    EV = EV_calc(values, counts)
    print("EV", EV)
    print_results("experiment 2 results", means, medians, stddevs)

def EV_calc(values, counts):
    total = np.sum(counts)
    EV = np.sum(values * counts) / total
    return EV

def std_plot():
    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

def print_results(title, mean, median, std):
    with open(title + ".txt", "w") as f:
        f.write("Roulette Simulation Results\n")
        f.write("===========================\n\n")

        # f.write(f"Episodes: {winnings_arr.shape[0]}\n")
        # f.write(f"Spins: {winnings_arr.shape[1]}\n")
        # f.write("Starting bankroll: $256\n\n")

        f.write("winnings by spin:\n")
        f.write("Spin\tMean\tMedian\tStd Dev\n")

        for spin in [0, 9, 49, 99, 249, 499, 999]:
            f.write(
                f"{spin + 1}\t"
                f"{mean[spin]:.2f}\t"
                f"{median[spin]:.2f}\t"
                f"{std[spin]:.2f}\n"
            )

def spin_multiple_episodes(num_episodes, episode_size, bankroll_limit, has_bankroll_limit):
    filled_arr = np.empty((num_episodes, episode_size))
    if (has_bankroll_limit):
        for i in range(num_episodes):
            filled_arr[i] = episode_spin_bankroll(episode_size, bankroll_limit, has_bankroll_limit)
    else:        
        for i in range(num_episodes):
            filled_arr[i] = episode_spin(episode_size, bankroll_limit, has_bankroll_limit)
    return filled_arr

def episode_spin(episode_size, bankroll_limit, has_bankroll_limit):
    win_probability = 0.4737  # set appropriately to the probability of a win
    winnings_arr = []
    episode_winnings = 0
    attempts = 0

    while episode_winnings < 80 and attempts < episode_size:
        won = False
        bet_amount = 1
        if episode_winnings <= bankroll_limit and has_bankroll_limit:
            # print("bust")
            break
        while not won:
            won = get_spin_result(win_probability)
            winnings_arr.append(episode_winnings)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            attempts = attempts + 1
            if episode_winnings <= bankroll_limit and has_bankroll_limit:
                # print("attempt", attempts, "bust")
                break
            if (bet_amount > 100):
                # print("attempt", attempts, "episode_winnings", episode_winnings, "bet amount", bet_amount)
                pass
    #fill remaining with highest value
    while attempts < episode_size:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr


def episode_spin_bankroll(episode_size, bankroll_limit, has_bankroll_limit):
    win_probability = 0.4737  # set appropriately to the probability of a win
    winnings_arr = []
    episode_winnings = 0
    attempts = 0

    while episode_winnings < 80 and attempts < episode_size:
        won = False
        bet_amount = 1
        if episode_winnings <= bankroll_limit and has_bankroll_limit:
            # print("attempt", attempts, "top bust")
            break
        while not won and attempts < episode_size:
            won = get_spin_result(win_probability)
            winnings_arr.append(episode_winnings)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                # std martingale, bet double 
                if (episode_winnings + (bankroll_limit * -1)) > bet_amount * 2:
                    bet_amount = bet_amount * 2
                # broken martingale, bet what you got
                else:
                    bet_amount = episode_winnings + (bankroll_limit * -1)
            attempts = attempts + 1
            if episode_winnings <= bankroll_limit and has_bankroll_limit:
                # print("attempt", attempts, "episode_winnings", episode_winnings, "bust")
                break
    #fill remaining with highest value
    while attempts < episode_size:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr

if __name__ == "__main__":  		  	   		 		  		  		  		    	 		 		   		 		  
    test_code()  		  	   		 		  		  		  		    	 		 		   		 		  
