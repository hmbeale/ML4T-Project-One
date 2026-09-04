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
  		  	   		 		  		  		  		    	 		 		   		 		  
Student Name: Holden Beale
GT User ID: hbeale7	  	   		 		  		  		  		    	 		 		   		 		  
GT ID: 904202603		  	   		 		  		  		  		    	 		 		   		 		  
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

# DO NOT SUBMIT PLT.SHOW

def author():
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 		  		  		  		    	 		 		   		 		  
    """
    return "hbeale7"  # replace tb34 with your Georgia Tech username.

def study_group():
    """
    Returns
            A comma separated string of GT_Name of each member of your study group
            # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone

        Return type
            str
    """
    return "hbeale7"

def gtid():
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 		  		  		  		    	 		 		   		 		  
    """
    return 904202603  # replace with your GT ID number

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
    # add your code here to implement the experiments
    np.random.seed(gtid())  # do this only once
    win_probability = 0.4737  # set appropriately to the probability of a win  		
    episode_size = 1000 # number of spins in an episode
        	 		 		   		 		  
    experiment1(win_probability, episode_size)
    experiment2(win_probability, episode_size)

def experiment1(win_probability, episode_size):
    num_episodes = 10

    empty_arr = np.empty((num_episodes, episode_size))
    # def spin_multiple_episodes(num_spins, big_arr, win_probability):

    spin_record = spin_multiple_episodes(num_episodes, empty_arr, episode_size, win_probability)

    for i in range(num_episodes):
        plt.plot(spin_record[i], label=f"Episode {i + 1}")

    plt.title("10 Roulette Episodes")
    std_plot()  

    plt.savefig("figure_1.png")
    plt.close()

    arr_height = 1000
    empty_arr = np.empty((arr_height, num_episodes))
    spin_record = spin_multiple_episodes(arr_height, empty_arr, episode_size, win_probability)

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    plt.title("Mean Values for ")
    std_plot()

    plt.savefig("figure_2.png")
    plt.close()

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    std_plot()

    plt.savefig("figure_3.png")
    plt.close()


def experiment2(win_probability, episode_size):
    num_episodes = 1000
    empty_arr = np.empty((num_episodes, episode_size))
    parameters = {
        "empty_arr": empty_arr,
        "num_episodes": num_episodes,
        "episode_size": episode_size,
        "win_probability": win_probability,
        "bankroll_limit": -256,
        "has_bankroll_limit": True
    }
    spin_record = spin_multiple_episodes_with_bankroll(**parameters)

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    std_plot()

    plt.savefig("figure_4.png")
    plt.close()

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    std_plot()

    plt.savefig("figure_5.png")
    plt.close()

def std_plot():
    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

def spin_multiple_episodes(num_episodes, big_arr, episode_size, win_probability):
    filled_arr = big_arr.copy()
    for i in range(num_episodes):
        filled_arr[i] = episode_spin(episode_size, win_probability)
    return filled_arr

def spin_multiple_episodes_with_bankroll(num_episodes, big_arr, episode_size, win_probability, bankroll_limit, has_bankroll_limit):
    filled_arr = big_arr.copy()
    for i in range(num_episodes):
        filled_arr[i] = episode_spin_with_bankroll(episode_size, win_probability, bankroll_limit)
    return filled_arr

def episode_spin(episode_size, win_probability):
    winnings_arr = []
    episode_winnings = 0
    attempts = 0
    while episode_winnings < 80 and attempts < episode_size:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_probability)
            winnings_arr.append(episode_winnings)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            attempts = attempts + 1
    #fill remaining with highest value
    while attempts < episode_size:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr


def episode_spin_with_bankroll(episode_size, win_probability, bankroll_limit):
    winnings_arr = []
    episode_winnings = 0
    attempts = 0
    # bankroll_limit = -256

    # smaller bankroll doesn't make it
    # bankroll_limit = -25

    # high limit looks like unlimited
    # bankroll_limit = -999999999999999999999
    while episode_winnings < 80 and attempts < episode_size:
        won = False
        bet_amount = 1
        if episode_winnings <= bankroll_limit:
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
            if episode_winnings <= bankroll_limit:
                # print("bust")
                break
    #fill remaining with highest value
    while attempts < episode_size:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr


if __name__ == "__main__":
    test_code()
