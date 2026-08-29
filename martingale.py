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

import numpy as np
import matplotlib.pyplot as plt


def author():
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 		  		  		  		    	 		 		   		 		  
    """
    return "hbeale7"  # replace tb34 with your Georgia Tech username.


# study group as well

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
    win_prob = 0.4737  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		 		  		  		  		    	 		 		   		 		  
    # print(get_spin_result(win_prob))  # test the roulette spin
    # add your code here to implement the experiments
    # print("es", episode_spin())

    experiment1_1()
    experiment1_2and1_3()
    experiment2_4and2_5()

    first_bankroll_spin = episode_spin_with_bankroll()
    second_bankroll_spin = episode_spin_with_bankroll()

    # print(first_bankroll_spin)
    # 2nd spin goes bust
    # print(second_bankroll_spin)

def experiment1_1():
    arr_height = 10
    empty_arr = np.empty((10, 1000))
    spin_record = spin_multiple_episodes(arr_height, empty_arr)
    # spin_record = spin_multiple_episodes_with_bankroll(arr_height, empty_arr)

    for i in range(arr_height):
        plt.plot(spin_record[i], label=f"Episode {i + 1}")
    # print(spin_record)

    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.title("10 Roulette Episodes")

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.legend()
    plt.show()


def experiment1_2and1_3():
    arr_height = 1000
    num_spins = 1000
    empty_arr = np.empty((arr_height, 1000))
    spin_record = spin_multiple_episodes(num_spins, empty_arr)

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    # print("sr", spin_record)
    # print("med", medians)
    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.show()

    # for i in range(arr_height):
    #     plt.plot(spin_record[i], label=f"Episode {i + 1}")
    # print(spin_record)

    # plt.xlabel("Spin")
    # plt.ylabel("Value")
    # plt.title("10 Roulette Episodes")
    #
    # plt.xlim(0, 300)
    # plt.ylim(-256, 100)
    #
    # plt.legend()
    # plt.show()


def experiment2_4and2_5():
    arr_height = 1000
    num_spins = 1000
    empty_arr = np.empty((arr_height, num_spins))
    spin_record = spin_multiple_episodes_with_bankroll(num_spins, empty_arr)

    means = np.mean(spin_record, axis=0)
    medians = np.median(spin_record, axis=0)
    stddevs = np.std(spin_record, axis=0)

    # print("sr", spin_record)
    # print("med", medians)
    plt.figure()
    plt.plot(means, label="Mean")
    plt.plot(means + stddevs, label="Mean + Std Dev")
    plt.plot(means - stddevs, label="Mean - Std Dev")

    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.figure()
    plt.plot(medians, label="Median")
    plt.plot(medians + stddevs, label="Median + Std Dev")
    plt.plot(medians - stddevs, label="Median - Std Dev")

    plt.xlabel("Spin")
    plt.ylabel("Value")
    plt.legend()

    plt.xlim(0, 300)
    plt.ylim(-256, 100)

    plt.show()


def spin_multiple_episodes(num_spins, big_arr):
    filled_arr = big_arr.copy()
    for i in range(num_spins):
        filled_arr[i] = episode_spin()
    return filled_arr

def spin_multiple_episodes_with_bankroll(num_spins, big_arr):
    filled_arr = big_arr.copy()
    for i in range(num_spins):
        filled_arr[i] = episode_spin_with_bankroll()
    return filled_arr

def episode_spin():
    winnings_arr = []
    episode_winnings = 0
    attempts = 0
    while episode_winnings < 80 and attempts < 1000:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(0.5)
            winnings_arr.append(episode_winnings)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            attempts = attempts + 1
    #fill remaining with highest value
    while attempts < 1000:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr


def episode_spin_with_bankroll():
    winnings_arr = []
    episode_winnings = 0
    attempts = 0
    bankroll_limit = -256

    # smaller bankroll doesn't make it
    # bankroll_limit = -25

    # high limit looks like unlimited
    # bankroll_limit = -999999999999999999999
    while episode_winnings < 80 and attempts < 1000:
        won = False
        bet_amount = 1
        if episode_winnings <= bankroll_limit:
            # print("bust")
            break
        while not won:
            won = get_spin_result(0.5)
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
    while attempts < 1000:
        winnings_arr.append(episode_winnings)
        attempts = attempts + 1
    return winnings_arr


if __name__ == "__main__":
    test_code()
